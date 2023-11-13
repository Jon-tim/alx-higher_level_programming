#!/usr/bin/node

const firstArgument = process.argv[2];

if (!firstArgument) {
  console.log('Missing number of occurrences');
} else {
  for (let index = 0; index < Number(firstArgument); index++) {
    console.log('C is fun');
  }
}
