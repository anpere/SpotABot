# Player, connects to server run by game.

import sys
import socket
import select

def chat_client():
    if(len(sys.argv)<3):
        print 'expected a hostname and port'
        sys.exit()
    host = sys.argv[1]
    port = int(sys.argv[2])

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(2)

    # connect to remote host
    try:
        s.connect((host,port))
    except:
        print "unable to connect"
        sys.exit()
    print "able to connect. please wait to get confirmation that you are playing"

if __name__ == "__main__":

    sys.exit(chat_client())
