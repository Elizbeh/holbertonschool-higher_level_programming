#!/usr/bin/node
const numb = parseInt(process.argv[2]);

if (process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < numb; i++) {
  console.log('C is fun');
}
