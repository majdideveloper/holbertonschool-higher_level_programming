#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request(url, function (error, response, body) {
  if (!error) {
    const listChara = JSON.parse(body).characters;

    listChara.map((urlcara) => {
      request(urlcara, function (error, response, body) {
        if (error) console.error('error:', error);
        else console.log(JSON.parse(body).name);
      });
    });
  }
});