#!/usr/bin/node

let id = process.argv[2];
let url = 'https://swapi-api.alx-tools.com/api/films/' + id;
const request = require('request');
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
    return;
  }
  if (response.statusCode === 200) {
    let characters = JSON.parse(body).characters;
    for (let i in characters) {
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
