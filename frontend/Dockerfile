# Etapa 1: build do React
FROM node:20 AS builder

WORKDIR /app

COPY game-store/package.json game-store/package-lock.json* ./
RUN npm install

COPY game-store ./

RUN npm run build

FROM nginx:alpine

COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]