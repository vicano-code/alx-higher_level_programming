#!/usr/bin/node

let filePath = process.argv[2];
let text = process.argv[3];
const fs = require('fs');
fs.writeFile(filePath, text, 'utf-8', (err) => {
  if (err) {
    console.log(error);
  }
});
