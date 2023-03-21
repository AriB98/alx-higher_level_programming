#!/usr/bin/node

const squareInput = Number(process.argv[2]);

if (Number.isNaN(squareInput)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < squareInput; i++) {
    let row = '';
    for (let j = 0; j < squareInput; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
