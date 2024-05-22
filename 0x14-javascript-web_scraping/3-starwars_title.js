#!/usr/bin/node

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
const request = require('request');
request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
    return;
  }
  if (response.statusCode === 200) {
    body = JSON.parse(body);
    console.log(body.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
