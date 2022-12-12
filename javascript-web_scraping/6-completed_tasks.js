#!/usr/bin/node

const request = require('request');
const url = `${process.argv[2]}`;

request(url, function (error, response, body) {
  if (error) console.error('error:', error);
  const tasks = JSON.parse(body);
  const dick = {};
  for (const task of tasks) {
    if (task.userId in dick) {
      if (task.completed === true) dick[`${task.userId}`] += 1;
    } else {
      dick[`${task.userId}`] = 0;
    }
  }
  console.log(dick);
});
