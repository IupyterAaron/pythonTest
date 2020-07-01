# coding=utf-8
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)  # 创建UDP socket
serverSocket.bind(('', serverPort))  # 绑定socket 到本地端口 12000
print("The server is ready to receive")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)  # UDP socket 读取 message, 获得(client IP and port)
    modifiedMessage = message.decode().upper()  # 打包大写的字符串
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
