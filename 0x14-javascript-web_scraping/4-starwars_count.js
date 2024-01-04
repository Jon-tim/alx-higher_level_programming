#!/usr/bin/node

const request = require('request');
const address = process.argv[2];

request.get(address, function (response, body) {
  const result = JSON.parse(body.body).results;
  let wedgeAntillesPresent = 0;
  result.forEach(film =>
    film.characters.forEach(character => {
      if (character.endsWith('18/')) wedgeAntillesPresent += 1;
    }));
  console.log(wedgeAntillesPresent);
});
