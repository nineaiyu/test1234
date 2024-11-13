FROM nineaiyu/test1234-base:20241113_092309 AS stage-build

COPY . .
RUN pnpm build

FROM nginx:1.24-bullseye
COPY --from=stage-build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
