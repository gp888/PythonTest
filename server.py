import socket
import threading
import time

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)



#基于IPv4和TCP协议的Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#服务器可能有多块网卡，可以绑定到某一块网卡的IP地址上，也可以用0.0.0.0绑定到所有的网络地址

#还可以用127.0.0.1绑定到本机地址
#127.0.0.1是一个特殊的IP地址，表示本机地址
#客户端必须同时在本机运行才能连接

# 监听端口:
s.bind(('127.0.0.1', 9999))

#开始监听
s.listen(5) #参数指定等待连接的最大数量
print('Waiting for connection...')

#永久循环来接受来自客户端的连接
while True:
    # 接受一个新连接:
    sock, addr = s.accept() #等待并返回一个客户端的连接
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()