#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let nb = 0;
  for (let index = 0; index < list.length; index++) {
    if (list[index] === searchElement) {
      nb++;
    }
  }
  return nb;
};
