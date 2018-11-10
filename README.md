# TcpChatRoom
A TCP socket communication chat room. 
一个简单socket通信的的实例：C/S架构的多人聊天室，用python实现

## 原理简介
  通信方式为TCP/IP的原理。


## 使用方式
  ### 服务器
    在服务器上运行server.py
    服务器监听端口为2101，如要修改，可以修改tcpPort来修改服务器监听端口。
  
  ### 客户机
    在客户机上运行client.py
    先输入服务器的ip地址，再输入服务器监听的端口，即可进入聊天室。
    当有人进入聊天室和离开聊天室时都有交互信息广播到所有已连接用户。
