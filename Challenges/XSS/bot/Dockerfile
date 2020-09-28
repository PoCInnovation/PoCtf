FROM buildkite/puppeteer:latest
WORKDIR /app

COPY package.json .

RUN npm install

COPY bot.js .

CMD npm start
