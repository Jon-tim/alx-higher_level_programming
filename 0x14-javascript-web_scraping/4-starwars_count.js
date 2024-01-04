#!/usr/bin/node

const request = require('request');
const address = process.argv[2];

request.get(address, function (response, body) {
  const result = JSON.parse(body.body).results;
  const wedgeAntillesPresent = result.filter(film =>
    film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
  );

  console.log(wedgeAntillesPresent.length);
});
