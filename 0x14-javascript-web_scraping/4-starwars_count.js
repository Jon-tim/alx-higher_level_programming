#!/usr/bin/node

const request = require('request');
const address = process.argv[2];
const targetID = '18';

request.get(address, function (response, body) {
  const result = JSON.parse(body.body).results;
  const wedgeAntillesPresent = result.filter(film =>
    film.characters.some(character => character.includes(targetID))
  );
  console.log(wedgeAntillesPresent.length);
});
