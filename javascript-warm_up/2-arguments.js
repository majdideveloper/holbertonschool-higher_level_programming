#!/usr/bin/node
const process = require('process');
const argNum = process.argv.length;
if (argNum === 0) {
  console.log('No argument');
} else if (argNum === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
