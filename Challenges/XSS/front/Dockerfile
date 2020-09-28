FROM node:alpine
WORKDIR /app

COPY package.json .

RUN npm install

COPY index.js .
COPY form.html .
COPY schema.sqlite .

CMD npm start
