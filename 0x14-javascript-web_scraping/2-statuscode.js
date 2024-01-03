#!/usr/bin/node

const request = require('request');
const address = process.argv[2];

request.get(address).on('response', function (response) {
  console.log('code:', response.statusCode);
});
