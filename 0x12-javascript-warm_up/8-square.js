#!/usr/bin/node

const firstArgument = process.argv[2];
const number = Number(firstArgument);

let output = '';

if (isNaN(number) || !firstArgument) {
  console.log('Missing size');
} else {
  for (let index = 0; index < number; index++) {
    output = '';
    for (let index = 0; index < number; index++) {
      output += 'X';
    }
    console.log(output);
  }
}
