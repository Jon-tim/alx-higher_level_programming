#!/usr/bin/node

const argLength = process.argv.length;

if (argLength < 3) {
  console.log(0);
} else {
  const sorted = process.argv.slice(2).map(Number).sort((a, b) => a - b);
  console.log(sorted[sorted.length - 2]);
}
