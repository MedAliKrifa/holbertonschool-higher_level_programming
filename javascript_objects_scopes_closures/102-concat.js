#!/usr/bin/node
const fs = require('fs');

const firstSource = process.argv[2];
const secondSource = process.argv[3];
const destination = process.argv[4];

const firstData = fs.readFileSync(firstSource, 'utf-8');
const secondData = fs.readFileSync(secondSource, 'utf-8');

const result = firstData + secondData;
fs.writeFileSync(destination, result, 'utf-8');
