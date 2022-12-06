#!/usr/bin/node
function add (a, b) {
  if (isNaN(1) || isNaN(b)) {
    return NaN;
  } else {
    return (Number(a) + Number(b));
  }
}
module.exports = { add };
