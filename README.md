# ${1:Project Name}

A variation of Turing Test that has been adapted as
a demonstration to show the power of modern chat-bots.
The game is written in Python


## Requirements 
    SpotABot requires the chatterbotapi.py which can be [found here on github](https://github.com/pierredavidbelanger/chatter-bot-api)
    But the API library comes with installation.


System:
A chat-server allows two humans to talk to each other.
When game.py is run, the player who ran it will be
randomly assigned to talk to a chat bot, or a human.

When assigned to a chat-bot, the player will communicate with
a cleverbot within the player script.

When assigned to a human, the two players communicate to each other 
through the chat-server

## Use
There are two human players. One acts as the judge, the second acts as a player.

### Server
One of the players runs a server as follows:

    $ python server.py

This prints out a public IP Address, which should be shared with the second player.

### Judge
The Human who wants to play the judge runs:

    $ python judge.py (host IP Address) (9009)
This script will either set up a connection to the server to chat with the Contestant, or it will setup 
a bot. The judge chats with both over the command line.

When the judge feels as though a decision as been made, they must press '^D', and then submit a guess: 'Human', or 'Robot'
The result of the guess is then shown on the screen
### Human Player
The Human who wants to play as the Human runs:
    $ python player.py (host_IP_Address) (9009)

## Rules
The Judge is programmed to try to guess the identity of the mystery contestant
The Human Player can do whatever they want, as agreed by the two players. For example
the Human Player can try their best to convince the Judge that they are a Human, or they
can try to act like a chatbot!

 
