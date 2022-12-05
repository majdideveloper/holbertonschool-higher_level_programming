#!/usr/bin/node
const process = require('process');
const argNum = process.argv.length;
if (argNum === 1) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
