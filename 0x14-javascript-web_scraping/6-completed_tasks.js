#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  let users = JSON.parse(body);
  let result = {};
  for (let i in users) {
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
