#!/usr/bin/node

const request = require('request');
const url = `${process.argv[2]}`;

request(url, function (error, response, body) {
  if (error) console.error('error:', error);
  const tasks = JSON.parse(body);
  const dick = {};
  for (const task of tasks) {
    if (task.completed && dick[task.userId] === undefined) {
       dick[`${task.userId}`] = 1;
    } else if(task.completed) {
      dick[`${task.userId}`] += 1;
    }
    
  }
  console.log(dick);
});
