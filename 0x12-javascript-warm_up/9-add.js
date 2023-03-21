#!/usr/bin/node

let total = 0;
function add (a, b) {
  total = Number(a) + Number(b);
  console.log(total);
}
add(process.argv[2], process.argv[3]);
