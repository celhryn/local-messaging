# Créé par BAPTISTE.PUAUD, le 03/03/2022 en Python 3.7
import socket
from threading import Thread

def Send(socket):
    while True :
        msg = input("=> ")
        msg = msg.encode('utf-8')
        socket.send(msg)
def Reception(socket):
    while True:
        requete_server = socket.recv(500)
        requete_server = requete_server.decode('utf-8')
        print("=> ",servername,"--> ",requete_server)




Host = '192.168.1.16'
Port = 6390

clientname = input("Nom d'utilisateur : ")
clientname = clientname.encode('utf-8')

servcol = '\33[91m'
colres = '\33[0m'

#socket
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket.connect((Host,Port))
servername = socket.recv(20)
servername = servername.decode('utf-8')
socket.send(clientname)

envoi = Thread(target=Send,args=[socket])
reception = Thread(target=Reception,args=[socket])
envoi.start()
reception.start()

