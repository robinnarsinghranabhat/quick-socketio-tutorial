This is Copy from Migueul Grinberg's Quick Socket.IO 
Tutorial. I merely added some notes for myself.
https://github.com/miguelgrinberg/quick-socketio-tutorial
=====================================================

## User Session
socketio will keep track of user-information for each of the connected clients.


## SERVING THE APPLICATION
- ### Synchronous Server 
    - Deploying a socketio app requies a multithreaded web-server.
    - By default, "gunicorn --reload --threads 50  app:app" will not use a permanent-connection. But
    rather polling from client side to act sort of real-timey.
    - To use WebSockets(which is more real-timey than polling ! ), 
    We require an event-let worker. So, Do this
        - pip install eventlet
        - gunicorn -k eventlet -w 1 app:app
    Now, inspecting we can see that connection upgrades from polling to WebSocket Protocol. !

- ###  Asynchronous Server
   Now our view functions and every logic they use (external libraries) go into world of async-await.
    - "uvicorn async_app:app" 
    - We could also run the app with [ gunicorn + eventlet worker ] to support WebSockets.  

