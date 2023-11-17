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

  rotate () {
    [this.height, this.width] = [this.width, this.height];
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
