from socket import socket
from select import select

server = socket()
server.bind(('192.168.19.81', 5000))

server.listen()

while True:
    client, addr = server.accept()   #cold
    print('accept connect to ', addr)

    while True:
        client.send(b'hello client')
        print(1)
        message = client.recv(1)      #cold
        print(message)
        print(2)
        if message == b'q':
            client.close()
            break



from select import select
from socket import socket

server = socket()
server.bind(('192.168.19.81', 5000))
server.listen()

to_monitor = [server]

while True:
    ready_to_ready, ready_to_write, _ = select(to_monitor, to_monitor, [])

    for sock in ready_to_ready:
        if sock is server:
            client, addr = sock.accept()  # not cold
            to_monitor.append(client)
            print('accept connect to ', addr)
        else:
            try:
                message = sock.recv(12)  # not cold
            except:
                print('except with', sock)
                to_monitor.remove(sock)
                continue

            print(message)
            if message == b'q':
                sock.send(b'poka')
                sock.close()
                print('remove')
                to_monitor.remove(sock)
                ready_to_ready.remove(sock)