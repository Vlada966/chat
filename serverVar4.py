import socket

sock = socket.socket()
sock.bind(('', 10254))
sock.listen(1)
conn, addr = sock.accept()

print('connected:', addr)

while True:
    data = conn.recv(1024)
    jour = open('Log.txt', 'a')
    jour.write('Клиент отправил:' + str(data.decode('utf-8')) + '     ' + 'Количество байт:' + str(len(data)) + '\n')
    jour.close()
    if len(data.decode('utf-8')) > 20:
        st = data.decode('utf-8')
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
        print('Вам написали:', data.decode('utf-8'))
    data2 = str(input('Введите ответ: '))
    if len(data2) == 0:
        data2 = ' '
    print("Вы написали: ", data2)
    jour = open('Log.txt', 'a')
    jour.write('Сервер отправил:' + data2 + '     ' + 'Количество байт:' + str(len(data2.encode('utf-8')) + 1) + '\n')
    jour.close()
    conn.send(data2.encode('utf-8'))
