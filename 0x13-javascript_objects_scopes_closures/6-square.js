#!/usr/bin/node

const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  charPrint (c) {
    const printChar = c || 'X';
    let output = '';
    for (let index = 0; index < this.height; index++) {
      output = '';
      for (let index = 0; index < this.width; index++) {
        output += printChar;
      }
      console.log(output);
    }
  }
}

module.exports = Square;
