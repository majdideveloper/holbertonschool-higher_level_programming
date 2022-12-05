#!/usr/bin/node
const res = parseInt(process.argv[2]);
if (String(res) === 'NaN') {
  console.log('Not a number');
} else {
  console.log('My number: ' + res);
}
