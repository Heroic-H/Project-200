import socket
from threading import Thread
nickname=input("enter your nickname: ")
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_address="127.0.0.1"
port=8000
client.connect((ip_address,port))
print("connected with server")
def recieve():
    while True:
        try:
            message=client.recv(2048).decode("utf-8")
            if message=="NICKNAME":
                client.send(nickname.encode("utf-8"))
            else:
                print(message)
        except:
            print("an error occured")
            client.close()
            break
def write():
    while True:
        message="{}: {}".format(nickname,input(""))
        client.send(message.encode("utf-8"))
recieveThread=Thread(target=recieve)
recieveThread.start()
writeThread=Thread(target=write)
writeThread.start()