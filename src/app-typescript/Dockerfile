FROM node:16-alpine AS build

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

# Nginx para servir os arquivos estáticos
FROM nginx:alpine

# Copiar os arquivos de configuração customizado do Nginx
COPY ./nginx.conf /etc/nginx/conf.d/default.conf

# Copia os arquivos do build para o diretório do Nginx
COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 82

CMD ["nginx", "-g", "daemon off;"]
