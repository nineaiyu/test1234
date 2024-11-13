FROM nineaiyu/xadmin-client-base:2024 AS stage-build

COPY . .
RUN pnpm build

FROM nginx:stable-alpine as production-stage

COPY --from=stage-build /app/dist /usr/share/nginx/html
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
