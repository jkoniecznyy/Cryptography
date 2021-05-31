const path = require('path')

module.exports = {
    outputDir: path.resolve(__dirname, '../src/public'),
    devServer: {
        port: 8080,
        proxy: {
            '/api': {
                target: `http://localhost:5000/`
            }
        },
        watchOptions: {
            ignored: [/node_modules/, /public/],
        }
    }
}