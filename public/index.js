const sio = io({
  transportOptions : {
    polling : {
      extraHeaders: {
        'X-username':window.location.hash.substring(1)
      }
    }
  }
}
);

sio.on('connect', () => {
  console.log('connected');
  // Client asking something from server here. To sum things
  // Client could ask this incase a button was pushed event as well.
  // Something like, when client clicks send, find the room that client
  // belongs to in server through the SID. Or just send Room ID directly from
  // frontend.. Now  server will emit 
  // that message to everyone in that room. 
  sio.emit('sum', {numbers: [1, 2]}, (result) => {
    console.log(result);
  });
}); 

sio.on('disconnect', () => {
  console.log('disconnected');
});

sio.on('mult', (data, cb) => {
  const result = data.numbers[0] * data.numbers[1];
  cb(result);
});

sio.on('client_count', (count) => {
  console.log('In total, There are ' + count + ' connected clients.');
});

sio.on('room_count', (count) => {
  console.log('There are ' + count + ' connected clients in Room ');
});