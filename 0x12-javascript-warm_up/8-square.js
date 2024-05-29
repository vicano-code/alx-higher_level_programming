#!/usr/bin/node

const x = parseInt(process.argv[2]);
if (isNaN(x)) {
  console.log('Missing size');
}
for (let i = 0; i < x; i++) {
  let str = '';
  for (let j = 0; j < x; j++) {
    str += 'X';
  }
  console.log(str);
}
