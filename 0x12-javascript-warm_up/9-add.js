#!/usr/bin/node

const firstArgument = Number(process.argv[2]);
const secondArgument = Number(process.argv[3]);

let result;

function add (a, b) {
  result = a + b;
  console.log(result);
}

add(firstArgument, secondArgument);
