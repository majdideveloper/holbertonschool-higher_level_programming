#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const id = 'https://swapi-api.hbtn.io/api/people/18/';
request(url, function (error, response, body) {
  if (error) console.error('error:', error);
  const datas = JSON.parse(body).results;

  let num = 0;
  for (const data of datas) {
    if (data.characters.includes(id)) {
      num++;
    }
  }
  console.log(num);
});
