const { WebSocketServer } = require('ws')
const {createServer} = require('http')

const wss = new WebSocketServer({port:8080});

wss.on('connection', (ws)=> {
  ws.on('message', (data)=> {
    console.log(data);
  });

  ws.send('something');
});
