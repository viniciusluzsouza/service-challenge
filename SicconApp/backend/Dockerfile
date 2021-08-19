FROM node:13.12.0-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install --silent
COPY . .
CMD ["node", "index.js"]
