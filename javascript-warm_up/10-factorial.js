#!/usr/bin/node
function factorial (n) {
  if (process.argv.length === 2) return 1;
  const mem = [];
  if (n === 0 || n === 1) { return 1; }
  if (mem[n] > 0) { return mem[n]; }
  mem[n] = factorial(n - 1) * n;
  return mem[n];
}

console.log(factorial(process.argv[2]));
