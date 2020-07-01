# coding=utf-8
from socket import *

serverName = '127.0.0.1'  # 可以是IP,也可以是主机名，若是主机名，会自动调用DNS解析
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)  # 创建UDP socket#AF_INET表示IPv4协议，datagram表示数据块传输，即UDP
message = input('Input lowercase sentence:')
address=(serverName,serverPort)
clientSocket.sendto(message.encode(),address)  # 编码并打包IP端口; 放到socket里
# 端口进行打包，（自动把本地ip端口也打包了）
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)  # 读取返回的消息
# 后面是缓存大小，只读取前2k字节的内容
print(modifiedMessage.decode())  # 在屏幕上打印
clientSocket.close()  # 关闭 socket