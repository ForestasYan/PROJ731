# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 14:45:22 2020

@author: forestas yan
"""
cara_separateurs = [".", ",", " ", "\n", "!", "?",":", '"', "(", ")", ";", "-", "`", "<", ">"]
majuscules = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


import socket, sys
from threading import Thread
import threading


def compte_mots(texte, dico):

    dernier_sep = -1
    for maj in majuscules:
        texte = texte.replace(maj, maj.lower())
        
    for k in range(len(texte)):
        if texte[k] in cara_separateurs:
            if dernier_sep + 1 < k:
                mot = texte[dernier_sep+1:k]

                try:
                    dico[mot] += 1
                except:
                    dico[mot] = 1
            dernier_sep = k

def fusion_dicos(dicos):
    dico_final = {}
    for dico in dicos:
        for key in dico.keys():
            try:
                dico_final[key] += dico[key]
            except:
                dico_final[key] = dico[key]
    return dico_final
            



socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    socket_client.bind(('127.0.0.1', 1))

    
except socket.error:
    print("La liaison du socket à l'adresse choisie a échoué.")
    sys.exit()


while True:
    
    print ("Serveur prêt, en attente de requètes ...")
    socket_client.listen(5)
    
    connexion, adresse = socket_client.accept()
    print ("Client connecté, adresse IP %s, port %s" % (adresse[0], adresse[1]))
    print(adresse)
    
    
    msg_client = connexion.recv(1024)
    print("j'ai reçu")
    msg_client = str(msg_client)
    msg_client = msg_client[2:-1]

    
    textes = []
    dernier_txt = 0
    for k in range(len(msg_client)-3):
        if msg_client[k:k+4] == ".txt":
            textes.append(msg_client[dernier_txt:k+4])
            dernier_txt = k+5
    
    threads = []
    dicos = []
    
    
    for k in range(len(textes)):
        dicos.append({})
        with open(textes[k], 'r') as f:
            texte = f.read()
            
        threads.append(Thread(target=compte_mots, args=(texte, dicos[k],)))
        
    for thread in threads:    
        thread.start()
    for thread in threads:       
        thread.join()
        
    
    dico = fusion_dicos(dicos)
    dico = sorted(dico.items(), key=lambda t: t[1])
    
    with open("nombre_mot.txt", 'w') as f:
        for mot in dico:
            f.write(mot[0] + " " + str(mot[1]) + "\n")
    
    connexion.send(b"nombre_mot.txt")
    
