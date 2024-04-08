#!/usr/bin/node

let ans = 1;
function factorial (a) {
  const num = parseInt(a);
  if (isNaN(num)) {
    console.log(1);
    return;
  }
  if (num === 0) {
    console.log(ans);
    return;
  }
  ans *= a;
  factorial(a - 1);
}
factorial(process.argv[2]);
