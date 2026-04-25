const fs = require('fs');
const https = require('https');

const files = ['arch.mmd', 'pipeline.mmd', 'analysis.mmd'];

async function generateDiagram(filename) {
    const content = fs.readFileSync(filename, 'utf8');
    const base64 = Buffer.from(content).toString('base64');
    const url = `https://mermaid.ink/img/${base64}?bgColor=white`;
    const output = `fig_${filename.replace('.mmd', '.png')}`;
    
    console.log(`Generating ${output} from ${filename}...`);
    
    return new Promise((resolve, reject) => {
        https.get(url, (res) => {
            if (res.statusCode !== 200) {
                console.error(`Failed to generate ${output}: ${res.statusCode}`);
                resolve();
                return;
            }
            const file = fs.createWriteStream(output);
            res.pipe(file);
            file.on('finish', () => {
                file.close();
                console.log(`Successfully saved ${output}`);
                resolve();
            });
        }).on('error', (err) => {
            console.error(`Error generating ${output}: ${err.message}`);
            resolve();
        });
    });
}

async function run() {
    for (const file of files) {
        await generateDiagram(file);
    }
}

run();
