#!/usr/bin/node

const firstArgument = process.argv[2];
const number = Number(firstArgument);

if (isNaN(number) || !firstArgument) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
