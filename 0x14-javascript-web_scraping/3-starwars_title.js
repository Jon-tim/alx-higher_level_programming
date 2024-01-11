#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

request.get(`https://swapi-api.alx-tools.com/api/films/${id}`, function (response, body) {
  const title = JSON.parse(body.body).title;
  console.log(title);
});
