#!/usr/bin/node

const fs = require('fs').promises;

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const readFile = (filePath) => {
  return fs.readFile(filePath, 'utf-8');
};

const writeFile = (filePath, data) => {
  return fs.writeFile(filePath, data);
};

readFile(fileA)
  .then((textOne) => {
    return readFile(fileB).then((textTwo) => {
      const text = textOne + '\n' + textTwo + '\n';

      return writeFile(fileC, text);
    });
  })
  .catch((err) => {
    console.error(err);
  });
