#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
    return;
  }
  if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const i in films) {
      const character = films[i].characters;
      for (const c in character) {
        if (character[c].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
