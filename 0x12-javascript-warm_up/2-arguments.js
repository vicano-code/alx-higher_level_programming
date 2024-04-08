#!/usr/bin/node

// const { argv } = require('node:process');
const argSize = process.argv.length;
if (argSize < 3) {
  console.log('No argument');
} else if (argSize === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
