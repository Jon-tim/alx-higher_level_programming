#!/usr/bin/node

const req = require('request');
const movieId = process.argv[2];

const URL = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

req.get(URL, function (response, body) {
  const results = JSON.parse(body.body);
  const charactersApiList = results.characters;
  charactersApiList.forEach(character => {
    req.get(character, function (response, body) {
      const data = JSON.parse(body.body);
      console.log(data.name);
    });
  });
});
