#!/usr/bin/env node
const len = process.argv.length;
if (len <= 3) {
  console.log(0);
} else {
  let max = Number.MIN_VALUE;
  let secondBiggest = Number.MIN_VALUE;
  for (let i = 2; i < len; i++) {
    if (process.argv[i] > max) {
      max = process.argv[i];
    }
  }
  for (let j = 2; j < len; j++) {
    if (max !== process.argv[j] && secondBiggest < max && process.argv[j] > secondBiggest) {
      secondBiggest = process.argv[j];
    }
  }

  console.log(secondBiggest);
}
