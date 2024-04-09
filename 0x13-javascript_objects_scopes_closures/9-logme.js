#!/usr/bin/node

// prints the number of arguments already printed and the new argument value

const itemList = [];
exports.logMe = function (item) {
  if (item !== undefined) {
    console.log(itemList.length + ': ' + item);
    itemList.push(item);
  }
};
