# implementing 3-tier structure: Hall --> Room --> Clients; 
# 14-Jun-2013

import select, socket, sys, pdb
from pychat_util import Hall, Room, Player
import pychat_util
import pygame
from time import sleep
from random import random

READ_BUFFER = 4096

host = sys.argv[1] if len(sys.argv) >= 2 else ''
listen_sock = pychat_util.create_socket((host, pychat_util.PORT))

hall = Hall()
connection_list = []
connection_list.append(listen_sock)

pygame.mixer.pre_init(channels = 9)
pygame.mixer.init(channels = 9)

zero = pygame.mixer.Sound("/Users/EricLemmon/Google Drive/PhD/Learning to Code/Toy1/Samples/0.wav")
one = pygame.mixer.Sound("/Users/EricLemmon/Google Drive/PhD/Learning to Code/Toy1/Samples/1.wav")
two = pygame.mixer.Sound("/Users/EricLemmon/Google Drive/PhD/Learning to Code/Toy1/Samples/2.wav")
three = pygame.mixer.Sound("/Users/EricLemmon/Google Drive/PhD/Learning to Code/Toy1/Samples/3.wav")
four = pygame.mixer.Sound("/Users/EricLemmon/Google Drive/PhD/Learning to Code/Toy1/Samples/4.wav")
five = pygame.mixer.Sound("/Users/EricLemmon/Google Drive/PhD/Learning to Code/Toy1/Samples/5.wav")
six = pygame.mixer.Sound("/Users/EricLemmon/Google Drive/PhD/Learning to Code/Toy1/Samples/6.wav")
seven = pygame.mixer.Sound("/Users/EricLemmon/Google Drive/PhD/Learning to Code/Toy1/Samples/7.wav")
eight = pygame.mixer.Sound("/Users/EricLemmon/Google Drive/PhD/Learning to Code/Toy1/Samples/8.wav")
nine = pygame.mixer.Sound("/Users/EricLemmon/Google Drive/PhD/Learning to Code/Toy1/Samples/9.wav")
ten = pygame.mixer.Sound("/Users/EricLemmon/Google Drive/PhD/Learning to Code/Toy1/Samples/10.wav")
eleven = pygame.mixer.Sound("/Users/EricLemmon/Google Drive/PhD/Learning to Code/Toy1/Samples/11.wav")

edone = pygame.mixer.Sound("/Users/EricLemmon/Google Drive/PhD/Learning to Code/Toy1/Samples/E1.wav")
edtwo = pygame.mixer.Sound("/Users/EricLemmon/Google Drive/PhD/Learning to Code/Toy1/Samples/E2.wav")
edthree = pygame.mixer.Sound("/Users/EricLemmon/Google Drive/PhD/Learning to Code/Toy1/Samples/E3.wav")
edfour = pygame.mixer.Sound("/Users/EricLemmon/Google Drive/PhD/Learning to Code/Toy1/Samples/E4.wav")
ednine = pygame.mixer.Sound("/Users/EricLemmon/Google Drive/PhD/Learning to Code/Toy1/Samples/E9.wav")
ednine.set_volume(.5)

playerEnter = pygame.mixer.Sound("/Users/EricLemmon/Google Drive/PhD/Learning to Code/Toy1/Samples/dooropen.wav")
playerLeave = pygame.mixer.Sound("/Users/EricLemmon/Google Drive/PhD/Learning to Code/Toy1/Samples/doorslam.wav")

pcsdict1 = {
    0: zero,
    1: one,
    2: two,
    3: three,
    4: four,
    5: five,
    6: six,
    7: seven,
    8: eight,
    9: nine,
    10: ten,
    11: eleven,
    }

pcsdict2 = {
    0: zero,
    1: edone,
    2: edtwo,
    3: edthree,
    4: edfour,
    5: five,
    6: six,
    7: seven,
    8: eight,
    9: ednine,
    10: ten,
    11: eleven,
    }

chanCount = 0

def SoundGen(pcs):
    global chanCount
    if chanCount == 8:
        chanCount = 0
        for i in pcs:
            a = ord(i) % 12
            pygame.mixer.find_channel().play(pcsdict2[a])
            sleep(random()/5)
    else:
        chanCount += 1
        for i in pcs:
            a = ord(i) % 12
            pygame.mixer.find_channel().play(pcsdict1[a])
            sleep(random()/5)



while True:
    # Player.fileno()
    read_players, write_players, error_sockets = select.select(connection_list, [], [])
    for player in read_players:
        if player is listen_sock: # new connection, player is a socket
            new_socket, add = player.accept()
            new_player = Player(new_socket)
            connection_list.append(new_player)
            hall.welcome_new(new_player)
            playerEnter.play()

        else: # new message
            msg = player.socket.recv(READ_BUFFER)
            pcs = [s for s in msg.decode()]
        
            if msg:
                msg = msg.decode().lower()
                hall.handle_msg(player, msg)
                try:
                    SoundGen(pcs)
                except:
                    continue

            else:
                player.socket.close()
                connection_list.remove(player)

    for sock in error_sockets: # close error sockets
        sock.close()
        connection_list.remove(sock)
        playerLeave.play()
