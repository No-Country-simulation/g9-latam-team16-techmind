# Etapa 1: construir el Frontend
FROM node:24-alpine AS build

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build


# Etapa 2: servir el Frontend con Nginx
FROM nginx:alpine

ENV NGINX_ENVSUBST_FILTER="^BACKEND_URL$"

COPY nginx.conf /etc/nginx/templates/default.conf.template

COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]