#!/usr/bin/node

const dict = require('./101-data').dict;

const dictKeys = new Set(Object.values(dict).sort());

const newDict = function (params) {
  const newDictionary = {};

  params.forEach((element) => {
    newDictionary[element] = Object.keys(dict).filter(item => dict[item] === element);
  });

  return newDictionary;
};

console.log(newDict(dictKeys));
