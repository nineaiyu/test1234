FROM nineaiyu/xadmin-client-base:20241113_091144 AS stage-build

COPY . .
RUN pnpm build

FROM nginx:stable-alpine as production-stage

COPY --from=stage-build /app/dist /usr/share/nginx/html
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
