from chatterbotapi import ChatterBotFactory, ChatterBotType
import random, sys, socket, select
import server
factory = ChatterBotFactory()

s = raw_input("Time to guess if you can Identify a bot: \n[Me] ")
choices = {"Robot":0,"Human":1}
person = random.randint(0,1)
if person == 0:
    bot1 = factory.create(ChatterBotType.CLEVERBOT)
    bot1session = bot1.create_session()


while (1):

    if person == 0:
        s = bot1session.think(s);
        print '[mystery] ' + s
        try:
            s = raw_input("[Me] ")
        except KeyboardInterrupt:
            decision = raw_input("Tell me your guess\n")
            result = 'Correct' if (person==choices[decision]) else "Wrong!"
            print result
            sys.exit(0) 
    else:
        host = sys.argv[1]
        port = int(sys.argv[2])
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)

        # connect to remote host
        try:
            s.connect((host,port))
        except:
            print "unable to connect"
            #TODO: perhaps close  the socket

#        print 'connected to remote host. You can start sending messages'
        sys.stdout.write('[Me] '); sys.stdout.flush()

        while 1: 
            socket_list = [sys.stdin,s]
            # Get the list sockets which are readable
            ready_to_read,ready_to_write,in_error = select.select(socket_list , [], [])
             
            for sock in ready_to_read:             
                if sock == s:
                    # incoming message from remote server, s
                    data = sock.recv(4096)
                    if not data :
                        print '\nDisconnected from chat server'
                        sys.exit()
                    else :
                        #print data
                        sys.stdout.write(data)
                        sys.stdout.flush()     
                
                else :
                    # user entered a message
                    try:
                        msg = raw_input("[Me]")
                        s.send(msg)
                        sys.stdout.flush() 
                    except KeyboardInterrupt:
                        decision = raw_input("Tell me your guess\n")
                        result = 'Correct' if (person==choices[decision]) else "Wrong!"
                        print result
                        sys.exit(0) 
        

