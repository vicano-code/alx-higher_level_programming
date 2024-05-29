#!/usr/bin/node

// returns the  reversed version of a list

exports.esrever = function (list) {
  const reversedList = [];
  for (let i = 0; i < list.length; i++) {
    reversedList.unshift(list[i]);
  }
  return reversedList;
};
