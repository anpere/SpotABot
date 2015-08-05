from chatterbotapi import ChatterBotFactory, ChatterBotType
import random, sys, socket, select
import server
factory = ChatterBotFactory()

print "Time to guess if you can indentify a bot\n"

choices = {"Robot":0,"Human":1}
person = random.randint(0,1)
if person == 0:
    bot1 = factory.create(ChatterBotType.CLEVERBOT)
    bot1session = bot1.create_session()
    s = raw_input("[Me] ")
if person == 1:
    host = sys.argv[1]
    port = int(sys.argv[2])
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(None)

    try:
        s.connect((host,port))
    except:
        print "unable to connect"


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
#        print 'connected to remote host. You can start sending messages'
        try:
            msg = raw_input("[Me] ")
        except KeyboardInterrupt:
            decision = raw_input("Tell me your guess\n")
            result = 'Correct' if (person==choices[decision]) else "Wrong!"
            print result
            sys.exit(0)
        msg+='\n'
        s.send(msg)
        print "[Mystery] ",
        data = s.recv(4096)
        sys.stdout.write(data)
        sys.stdout.flush()


