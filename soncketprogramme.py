#!/usr/bin/python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.sina.com.cn', 80))
s.send('GET  / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')


