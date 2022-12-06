#!/usr/bin/node
const len = process.argv.length;
if (len <= 3) {
  console.log(0);
} else {
  let max = Number.MIN_VALUE;
  let secondBiggest = Number.MIN_VALUE;
  for (let i = 2; i < len; i++) {
    if (process.argv[i] > max) {
      max = parseInt(process.argv[i]);
    }
  }
  for (let j = 2; j < len; j++) {
    if (secondBiggest < process.argv[j] && process.argv[j] < max) {
      secondBiggest = parseInt(process.argv[j]);
    }
  }

  console.log(secondBiggest);
}
