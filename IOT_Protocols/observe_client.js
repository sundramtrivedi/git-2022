const coap = require('coap') // or coap
const req = coap.request({
    observe: true
})

req.on('response', (res) => {
    res.pipe(process.stdout)
})

req.end()
