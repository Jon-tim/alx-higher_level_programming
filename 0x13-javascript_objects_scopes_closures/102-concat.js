#!/usr/bin/node

const fs = require('fs');

fs.readFile('fileA', 'utf-8', (firstErr, firstData) => {
  if (firstErr) {
    console.error(firstErr);
    return;
  }
  const textOne = firstData;

  fs.readFile('fileB', 'utf-8', (secondErr, secondData) => {
    if (secondErr) {
      console.error(secondErr);
      return;
    }
    const textTwo = secondData;

    const textThree = textOne + '\n' + textTwo + '\n';

    fs.writeFile('fileC', textThree, (err) => {
      if (err) {
        console.error(err);
      }
    });
  });
});
