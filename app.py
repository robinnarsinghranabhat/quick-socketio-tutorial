import socketio
import random

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': './public/'
})
client_count = 0
room_count_a = 0
room_count_b = 0


def task(sid):
    sio.sleep(5)
    result = sio.call('mult', {'numbers': [3, 4]}, to=sid)
    print(result)


@sio.event
def connect(sid, environ):
    """
    As new clients Join in, We notify total uses to everyone.
    We also notify clients about know total clients in their room. But not about 
    other rooms.
    """
    global client_count, room_count_a, room_count_b
    client_count += 1
    print(sid, 'connected')
    sio.start_background_task(task, sid)
    sio.emit('client_count', client_count)
    if random.random() > 0.5:
        sio.enter_room(sid, 'a')
        room_count_a += 1
        sio.emit('room_count', room_count_a, to='a')
    else:
        sio.enter_room(sid, 'b')
        room_count_b += 1
        sio.emit('room_count', room_count_b, to='b')    


@sio.event
def disconnect(sid):
    global client_count, room_count_a, room_count_b
    client_count -= 1
    print(sid, 'disconnected')
    sio.emit('client_count', client_count)
    if 'a' in sio.rooms(sid):
        room_count_a -= 1
        sio.emit('room_count', room_count_a, to='a')
    elif 'b' in sio.rooms(sid):
        room_count_b -= 1
        sio.emit('room_count', room_count_b, to='b')


@sio.event
def sum(sid, data):
    result = data['numbers'][0] + data['numbers'][1]
    return {'result': result}
