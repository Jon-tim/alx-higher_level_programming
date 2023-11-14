#!/usr/bin/node

const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

fs.readFile(fileA, 'utf-8', (firstErr, firstData) => {
  if (firstErr) {
    console.error(firstErr);
    return;
  }
  const textOne = firstData;

  fs.readFile(fileB, 'utf-8', (secondErr, secondData) => {
    if (secondErr) {
      console.error(secondErr);
      return;
    }
    const textTwo = secondData;

    const textThree = textOne + '\n' + textTwo + '\n';

    fs.writeFile(fileC, textThree, (err) => {
      if (err) {
        console.error(err);
      }
    });
  });
});
