const coap = require('coap')
const server = coap.createServer()

server.listen(() => {
    const req = coap.request('coap://localhost/temp')
  
    req.on('response', (res) => {
      res.pipe(process.stdout)
      res.on('end', () => {
        process.exit(0)
      })
    })
  
    req.end()
  })
