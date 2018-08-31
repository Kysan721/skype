import socket
import os
import cv2
import base64
import time

def takeGoodLuminosityPic():
    rt, frame = cam.read()
    for k in range(0,30):
        rt, frame = cam.read()  #poru que la camera s'adapte a la luminosité ambiante
    return frame


def takePicture():
    cam = cv2.VideoCapture(0)
    rt, frame = cam.read()
    cam.release()
    
    retval, buffer = cv2.imencode('.jpg', frame)         #on converti l'image récuperer en jpg
    text_jpg = base64.b64encode(buffer)      #et on la converti elle meme en base 64
    
    return text_jpg         #ouais on aurai pu return direct avant mais osef c'est plus comprehensible étant donné que le nom de la fonctoin correspond pas a ce qu'elle fait vue que je suis un fucking retarded
    
    


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((socket.gethostbyname('127.0.0.1'), 7009))
print("Connected to senpai")

while True:
    try:
        client.send(takePicture())
        print("picutre sended")
    catch ex:
        print "error"
