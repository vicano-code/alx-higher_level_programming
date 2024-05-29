#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const users = JSON.parse(body);
  const result = {};
  for (const i in users) {
    if (users[i].completed) {
      if (result[users[i].userId] === undefined) {
        result[users[i].userId] = 1;
      } else {
        result[users[i].userId] += 1;
      }
    }
  }
  console.log(result);
});
