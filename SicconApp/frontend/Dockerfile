FROM node:13.12.0-alpine
RUN mkdir /app
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY package*.json ./
RUN npm install --silent
COPY . .
#TODO: deploy with nginx
CMD ["npm", "start"]
