#!/usr/bin/node
const { argv } = require("node:process");

if (argv[2] && !isNaN(Number(argv[2]))) {
	console.log(`My number: ${Math.floor(Number(argv[2]))}`);
} else {
	console.log("No argument");
}
