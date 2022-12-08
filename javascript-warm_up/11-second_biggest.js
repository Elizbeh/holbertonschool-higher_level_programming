#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  const numb = [];
  for (let i = 2; i < process.argv.length; i++) {
    numb.push(parseInt(process.argv[i]));
  }

  numb.sort((a, b) => a - b);
  console.log(numb[numb.length - 2]);
}
