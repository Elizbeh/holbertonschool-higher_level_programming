#!/usr/bin/node
const numb = parseInt(process.argv[2]);
function factorial (n) {
  if (isNaN(n) || n <= 0) {
    return 1;
  } else {
    return (n * factorial(n - 1));
  }
}
console.log(factorial(numb));
