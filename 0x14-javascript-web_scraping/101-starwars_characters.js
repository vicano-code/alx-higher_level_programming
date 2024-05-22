#!/usr/bin/node

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
const request = require('request');
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
    return;
  }
  if (response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    for (const i in characters) {
      request(characters[i], function (err, response, body) {
        if (err) {
	  console.log(err);
        }
        if (response.statusCode === 200) {
	  console.log(JSON.parse(body).name);
        }
      });
    }
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
