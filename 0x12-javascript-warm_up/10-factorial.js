#!/usr/bin/node

const firstArgument = Number(process.argv[2]);

function factorial (firstArgument) {
  if (isNaN(firstArgument) || firstArgument < 0) {
    return (1);
  } else if (firstArgument === 0 || firstArgument === 1) {
    return (1);
  } else {
    return (firstArgument * factorial(firstArgument - 1));
  }
}

console.log(factorial(firstArgument));
