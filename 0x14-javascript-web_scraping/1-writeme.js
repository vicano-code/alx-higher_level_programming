#!/usr/bin/node

const filePath = process.argv[2];
const text = process.argv[3];
const fs = require('fs');
fs.writeFile(filePath, text, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
