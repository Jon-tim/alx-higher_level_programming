#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const address = process.argv[2];
const file = process.argv[3];

request.get(address, function (response, body) {
  fs.writeFile(file, body.body, 'utf-8', err => {
    if (err) {
      console.error(err);
    }
  });
});
