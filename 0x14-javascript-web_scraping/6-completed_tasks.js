#!/usr/bin/node

const request = require('request');
const API = process.argv[2];

request.get(API, function (response, body) {
  const result = JSON.parse(body.body);
  const data = {};
  for (let i = 1; i <= 10; i++) {
    let doneTask = 0;
    for (let j = 0; j < result.length; j++) {
      if (Number(result[j].userId) === i && result[j].completed) {
        doneTask += 1;
      }
    }
    if (doneTask > 0) data[i] = doneTask;
  }
  console.log(data);
});
