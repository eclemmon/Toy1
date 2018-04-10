# LOL Music Generator

import pygame
from time import sleep

pygame.mixer.init(channels = 8)


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

pcsdict = {
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

pcs = [zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven]

##for i in pcs:
##    i.play()
##    sleep(0.25)

while True:
    numbers = [s for s in input("Please input numbers: ")]

    print(numbers)

    for i in numbers:
        a = ord(i) % 12
        pcsdict[a].play()
        sleep(0.2)
    
