#!/usr/bin/node
const request = require('request');
const fs = require('fs');

// Get the URL and file path from the command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Call the URL and save the response in the given file
request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    fs.writeFile(filePath, body, 'utf8', function (err) {
      if (err) {
        console.error(err);
      } else {
        console.log('Saved to file:', filePath);
      }
    });
  }
});
