#!/usr/bin/node

const request = require('request');
const util = require('util');
const movieId = process.argv[2];

const URL = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

const getAsync = util.promisify(request.get);

async function fetchCharacterNames () {
  const response = await getAsync(URL);
  const results = JSON.parse(response.body);
  const charactersApiList = results.characters;

  const charNames = await Promise.all(charactersApiList.map(async (character) => {
    const charResponse = await getAsync(character);
    const data = JSON.parse(charResponse.body);
    return data.name;
  }));

  charNames.forEach(name => console.log(name));
}

fetchCharacterNames();
