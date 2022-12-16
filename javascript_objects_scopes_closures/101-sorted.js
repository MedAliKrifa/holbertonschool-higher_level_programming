#!/usr/bin/node

const dict = require('./101-data.js').dict;
const newDict = {};

Object.entries(dict).forEach(([userId, occurrences]) => {
  if (!newDict[occurrences]) {
    newDict[occurrences] = [userId];
  } else {
    newDict[occurrences].push(userId);
  }
});

console.log(newDict);
