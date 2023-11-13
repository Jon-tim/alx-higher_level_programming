#!/usr/bin/node

const argLength = process.argv.length;

if (argLength < 3) {
  console.log(0);
} else {
  const sorted = process.argv.slice(2).sort();
  console.log(sorted[sorted.length - 2]);
}
