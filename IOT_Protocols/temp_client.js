const coap = require('coap')
const server = coap.createServer()

const req = coap.request('coap://localhost/temp')//url where server will send respone

  req.on('response', (res) => {
    res.pipe(process.stdout)
    res.on('end', () => {
      process.exit(0)
    })
  })

  req.end()