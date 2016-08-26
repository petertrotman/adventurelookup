FROM node

RUN mkdir /code
COPY package.json /code/

WORKDIR /code
RUN npm install

COPY . /code

EXPOSE 80

COPY cmd.sh /
CMD ["/cmd.sh"]
