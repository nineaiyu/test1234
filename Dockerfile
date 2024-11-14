FROM nineaiyu/test1234-base:20241114_065801 AS stage-build
ARG VERSION

WORKDIR /data/xadmin-server

COPY . .

RUN echo > config.yml \
    && \
    if [ -n "${VERSION}" ]; then \
        sed -i "s@VERSION = .*@VERSION = '${VERSION}'@g" server/const.py; \
    fi

RUN set -ex \
    && export SECRET_KEY=$(head -c100 < /dev/urandom | base64 | tr -dc A-Za-z0-9 | head -c 48)

FROM python:3.12.7-slim

ENV LANG=en_US.UTF-8 \
    PATH=/data/py3/bin:$PATH

ARG APT_MIRROR=http://deb.debian.org

ARG DEPENDENCIES="                    \
        libmariadb-dev"

RUN set -ex \
    && sed -i "s@http://.*.debian.org@${APT_MIRROR}@g" /etc/apt/sources.list.d/debian.sources \
    && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && apt-get update > /dev/null \
    && apt-get -y install --no-install-recommends ${DEPENDENCIES} \
    && echo "no" | dpkg-reconfigure dash \
    && apt-get clean all \
    && rm -rf /var/lib/apt/lists/*

COPY --from=stage-build /data /data
COPY --from=stage-build /usr/local/bin /usr/local/bin

RUN addgroup --system --gid 1001 nginx \
    && adduser --system --disabled-login --ingroup nginx --no-create-home --home /nonexistent --gecos "nginx user" --shell /bin/false --uid 1001 nginx

WORKDIR /data/xadmin-server

VOLUME /data/xadmin-server/data

USER 1001

ENTRYPOINT ["/bin/bash", "entrypoint.sh"]

EXPOSE 8896

STOPSIGNAL SIGQUIT

CMD ["start", "all"]
