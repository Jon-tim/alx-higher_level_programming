#!/usr/bin/node

exports.esrever = function (list) {
  const outputArray = [];

  for (let index = list.length - 1; index > -1; index--) {
    outputArray.push(list[index]);
  }
  return outputArray;
};
