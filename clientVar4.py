import socket

sock = socket.socket()
sock.connect(('localhost', 10254))

while True:
    data = str(input('Введите сообщение: '))
    if len(data) == 0:
        data = ' '
    print("Вы написали: ", data)
    sock.send(data.encode('utf-8'))
    data2 = sock.recv(1024)
    if len(data2.decode('utf-8')) > 20:
        st = data2.decode('utf-8')
        lst = list(st)
        empt = []
        st2 = ''
        for symb in lst:
            if len(empt) < 19:
                empt.append(symb)
                st2 += symb
            else:
                empt = []
                st2 += symb + '\n'
        print('Вам написали:\n' + st2)
    else:
        print('Вам написали:', data2.decode('utf-8'))
