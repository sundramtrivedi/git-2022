const coap = require('coap')
const server = coap.createServer()

server.on('request', (req, res) => {
   let x=Math.random()
   res.end('temp is ' + x)
})

server.listen(() => {
  console.log("server started");
})
