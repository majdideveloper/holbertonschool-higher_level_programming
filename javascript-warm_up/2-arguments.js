#!/usr/bin/node
const process = require('process');
const argNum = process.argv.length;
if (argNum === 2) {
  console.log('No argument');
} else if (argNum === 3) {
  console.log('Argument found');
} else if (argNum > 3) {
  console.log('Arguments found');
}
