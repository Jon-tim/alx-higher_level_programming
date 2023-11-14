#!/usr/bin/node
const argv = process.argv;
const fs = require('fs');
const fileA = argv[2];
const fileB = argv[3];
const fileC = argv[4];

const fileReader = (file) => {
  return new Promise((resolve, reject) => {
    fs.readFile(file, 'utf8', (err, data) => {
      if (err) {
        reject(err);
      } else {
        resolve(data);
      }
    });
  });
};

const promises = [fileA, fileB].map(fileReader);

Promise.all(promises)
  .then((resolve) => {
    const text = resolve.join('');
    fs.writeFile(fileC, text, (err) => {
      if (err) throw err;
    });
  })
  .catch((err) => console.log(err));
