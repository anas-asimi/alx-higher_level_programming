#!/usr/bin/node
const { argv } = require("node:process");

function add(a, b) {
	return a + b;
}

console.log(add(Math.floor(Number(argv[2])), Math.floor(Number(argv[3]))));
