#!/usr/bin/node

const request = require('request');
const url = `${process.argv[2]}`;

request(url, function (error, response, body) {
  if (error) console.error('error:', error);
  const datas = JSON.parse(body).results;

  let num = 0;
  for (const data of datas) {
    data.characters.map((cara) => {
      if (cara.endsWith('/18/')) num++;
      return num;
    }
    );
  }
  console.log(num);
  return num;
});
