import fs from 'fs';

import('./data.js')
    .then((module) => {
        const data = JSON.stringify(module.default);
        fs.writeFile('data.json', data, 'utf8', (err) => {
            if (err) {
                console.error('Error writing file:', err);
                return;
            }
            console.log('JSON file generated successfully.');
        });
    })
    .catch((err) => {
        console.error('Error importing module:', err);
    });