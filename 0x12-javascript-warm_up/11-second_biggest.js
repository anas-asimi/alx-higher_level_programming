#!/usr/bin/node
const { argv } = process;

if (argv.length < 4) {
  console.log(0);
} else {
  console.log(
    argv
      .map((n) => Math.floor(Number(n)))
      .sort()
      .reverse()[1 + 2] // 2 is the number of default in args
  );
}
