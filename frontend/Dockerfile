FROM node:12.19.0-alpine
WORKDIR /app/frontend
COPY package.json /app/frontend
RUN yarn install
EXPOSE 8080
CMD yarn serve