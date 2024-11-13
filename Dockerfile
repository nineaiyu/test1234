FROM nineaiyu/test1234-base:20241113_121253

WORKDIR /data/xadmin-server/

RUN addgroup --system --gid 1001 nginx \
    && adduser --system --disabled-login --ingroup nginx --no-create-home --home /nonexistent --gecos "nginx user" --shell /bin/false --uid 1001 nginx

USER 1001

ENTRYPOINT ["/bin/bash", "entrypoint.sh"]

EXPOSE 8896

STOPSIGNAL SIGQUIT

CMD ["start", "all"]
