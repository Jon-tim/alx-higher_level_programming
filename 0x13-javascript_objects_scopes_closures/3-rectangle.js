#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let output = '';
    for (let index = 0; index < this.height; index++) {
      output = '';
      for (let index = 0; index < this.width; index++) {
        output += 'X';
      }
      console.log(output);
    }
  }
}

module.exports = Rectangle;
