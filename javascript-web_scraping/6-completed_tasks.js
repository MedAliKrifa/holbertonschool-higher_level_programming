#!/usr/bin/node
const request = require('request');
const endpoint = 'https://jsonplaceholder.typicode.com/todos';

request(endpoint, function (error, response, body) {
    if (!error && response.statusCode === 200) {
        const data = JSON.parse(body);

        const counts = data.reduce((counts, todo) => {
            if (todo.completed) {
                counts[todo.userId] = (counts[todo.userId] || 0) + 1;
            }
            return counts;
        }, {});

        for (const userId in counts) {
            console.log(`{'${userId}': ${counts[userId]},}`);
        }
    }
});
