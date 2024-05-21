#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
request.get(url, function (err, response) {
  if (err) {
    console.log(err);
    return;
  }
  console.log('code: ' + response.statusCode);
});
