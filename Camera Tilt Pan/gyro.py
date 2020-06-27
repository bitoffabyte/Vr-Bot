import socket, traceback
host = ''
port = 5555
n = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
n.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
n.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
n.bind((host, port))
while 1:
    try:
        message, address = n.recvfrom(8192)
        print (message)
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()
    