# Créé par BAPTISTE.PUAUD, le 03/03/2022 en Python 3.7
import socket
from threading import Thread

def Send(client):
    while True:
        msg = input("=> ")
        msg = msg.encode('utf-8')
        client.send(msg)
def Reception(client):
    while True :
        requete_client = client.recv(500)
        requete_client = requete_client.decode('utf-8')
        print("=> ",clientname,"--> ",requete_client)
        if not requete_client :
            print('CONNEXION PERDUE')
            break




Host = '192.168.1.16'
Port = 6390

servername = input("Nom d'utilisateur : ")
servername = servername.encode('utf-8')

servcol = '\33[32m'
colres = '\33[0m'

#socket
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket.bind((Host,Port))
socket.listen(1)

#récupérer le client
client, ip = socket.accept()
print("Le client d'ip",ip,"s'est connecté")
client.send(servername)
clientname = client.recv(20)
clientname = clientname.decode('utf-8')

envoi = Thread(target=Send,args=[client])
reception = Thread(target=Reception,args=[client])

envoi.start()
reception.start()
reception.join()

client.close()
socket.close()    #fermeture du port pour sécurité
