# !/usr/bin/python3
# -*- coding:utf-8 -*-
import socket
import threading


def client_send(tcpSock):
    while True:
        try:
            sendInfo = input('')
            tcpSock.send(sendInfo.encode('utf-8'))
        except:
            pass


def client_recv(tcpSock):
    while True:
        try:
            recvInfo = tcpSock.recv(1024)
            print('\r>> %s\r\n<< ' % recvInfo.decode('utf-8'), end = '')
        except:
            pass


def main():
    serverIp=input('请输入要连接的ip: ')
    serverPort=int(input('请输入要使用的端口: '))

    tcpSock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        tcpSock.connect((serverIp, serverPort))
    except:
        print('ERROR: Cannot connect. ')
        return

    th_send=threading.Thread(target = client_send, args = (tcpSock, ))
    th_recv=threading.Thread(target = client_recv, args = (tcpSock, ))

    th_send.start()
    th_recv.start()

    th_send.join()
    th_recv.join()


if __name__ == '__main__':
    main()
