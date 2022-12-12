#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = `${process.argv[2]}`;
const file = process.argv[3];

request(url, function (error, response, body) {
  if (error) console.error('error:', error);
  const data = body;
  fs.writeFile(process.argv[3], data, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
    }
  });
});
