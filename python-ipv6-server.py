import socket,SocketServer,CGIHTTPServer
SocketServer.TCPServer.address_family=socket.AF_INET6
print("hello world")
CGIHTTPServer.test()
