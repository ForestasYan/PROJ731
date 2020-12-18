# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 14:33:51 2020

@author: forestas yan
"""

#-*- coding: utf-8 -*-


import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mySocket.connect(('127.0.0.1', 1))

mySocket.send(b"Les_miserables.txt alice.txt Shakespeare1.txt Shakespeare2.txt")

msg_recu = mySocket.recv(1024)
msg_recu = str(msg_recu)
msg_recu = msg_recu[2:-1]
print("le nombre de mots se trouve dans: " + msg_recu)

print("Fermeture de la connexion")
mySocket.close()