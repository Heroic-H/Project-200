import socket
from threading import Thread
import random
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",8001))
server.listen()
clientsList=[]
questions=[
    ["What day is Mario day?",[["a","May 16"],["b","March 10"],["c","September 16"],["d","February 31"]]],
    ["Which one of these cities is not a megacity?",[["a","Paris"],["b","New York"],["c","London"],["d","beijing"]]],
    ["How many days 1 year?",[["a","365 unless it is a leap year then 366"],["b",365.25],["c",365.256],["d",365.242]]]
]
answers=["b","c","c"]
def removeQuestion(index):
    questions.pop(index)
    answers.pop(index)
def clientThread(connection,address):
    score=0
    conn.send("welcome to this quiz game!".encode("utf-8"))
    conn.send("You will recieve a question. The answer to that question will be a,b,c or d".encode("utf-9"))
    conn.send("good luck!".encode("utf-8"))
    index,question,answer=getAnswer((conn))
    while True:
        try:
            message=conn.recv(2048).decode("utf-8")
            if message:
                if message.lower==answer:
                    score+=1
                    conn.send(f"Bravo! Your score is {score}".encode("utf-8"))
                else:
                    conn.send("Incorrect answer! Better luck next time!".encode("utf-8"))
                removeQuestion(index)
                index,question,answer=getAnswer(conn)
            else:
                remove(conn)
        except:
            continue
def getAnswer(conn):
    randomIndex=random .randint(0,len(questions)-1)
    randomQuestion=questions[randomIndex]
    randomAnswer=answers[randomIndex]
    conn.send(randomQuestion.encode("utf-8"))
    return randomIndex,randomQuestion,randomAnswer
while True:
    connection,adress=server.accept()
    clientsList.append(connection)
    newThread=Thread(target=clientThread,args=(connection,adress))
    newThread.start()