#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let n = 0;
  for (let i = 0; i < list.length; i++) {
    list[i] === searchElement ? n++ : n += 0;
  }
  return n;
};
