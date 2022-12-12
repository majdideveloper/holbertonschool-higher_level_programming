#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  item = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      item += 1;
    }
  }
  return item;
};
