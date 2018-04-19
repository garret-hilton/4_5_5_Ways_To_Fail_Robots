
#!/usr/bin/python3           # This is server.py file
import socket
import time
from threading import Thread
import netifaces as ni

class Server():
    def __init__(self):
        self.msg = 'Test'+"\r\n"
        self.change = 0
        self.name = "name"
        self.data = "none"
        self.lastData = ""
        self.lastMsg = ""
        self.sendFlag = 0
        self.host = "10.200.0.160"
        self.ip = ""
        self.get_ip_address()
        self.queue = ""
        self.queueFlag = 0;



    def get_ip_address(self):
        ipArray = ni.interfaces()

        print(ipArray)
        ni.ifaddresses('wlp1s0')
        self.ip = ni.ifaddresses('wlp1s0')[ni.AF_INET][0]['addr']
        print (self.ip)  # should print "192.168.100.37"

    def startServer(self):
        print("Starting Server")
        threadServerListen = Thread(target = self.startSend, args = ( ))
        threadServerListen.start()
        threadServerRec = Thread(target = self.startRec, args = ( ))
        threadServerRec.start()

    def getMessage(self):
        while True:
            #if self.data != self.lastData:
            #    print("Data: ")
            #    print(self.data)
            #    self.lastData = self.data
            self.name = input("Enter a meassage to Send\n")
            self.sendFlag = 1

            time.sleep(1)

    def stt(self):
        self.name = ("SST")
        self.sendFlag = 1

    def tts(self, message):
        self.name = message
        self.sendFlag = 1

    def startSend(self):
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = "10.200.0.160"
        port = 9997

        serversocket.bind((self.ip, port))
        serversocket.listen(5)
        #clientsocket,addr = serversocket.accept()
        #self.msg = self.name + "\r\n"
        #clientsocket.send(self.msg.encode('ascii'))

        while True:
            if self.sendFlag == 1:
                clientsocket,addr = serversocket.accept()
                self.msg = self.name + "\r\n"
                clientsocket.send(self.msg.encode('ascii'))
                self.sendFlag = 0;

    def startRec(self):
        serversocket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = "10.200.0.160"
        port = 9996
        serversocket2.bind((self.ip, port))
        serversocket2.listen(5)
        while True:
            clientsocket,addr = serversocket2.accept()
            self.data = clientsocket.recv(1024).decode("ascii")
            if self.data != "":
                print (self.data)
                self.parseMessage(self.data)

    def parseMessage(self, message):
        value = message.split(" ")
        loop = len(value)
        messageSet = 0;
        if value[0] == 'move':
            if value[1] == 'forward':
                self.queue = ('For/Back :1, T :'+value[2]+',S :6700')
                messageSet = 1;
            if value[1] == 'backward':
                self.queue = ('For/Back :1, T :'+value[2]+',S :5300')
                messageSet = 1;
            if value[1] == 'backwards':
                self.queue = ('For/Back :1, T :'+value[2]+',S :5300')
                messageSet = 1;
        if value[0] == 'turn':
            if value[1] == 'left':
                self.queue = ('Turn Robot :2, T :'+value[2]+',S :6700')
                messageSet = 1;
            if value[1] == 'right':
                self.queue = ('Turn Robot :2, T :'+value[2]+',S :5300')
                messageSet = 1;
            if value[1] == 'head':
                if value[2] == 'left':
                    self.queue = ('Turn Head :3, T :'+value[3]+',S :4000')
                    messageSet = 1;
                if value[2] == 'left':
                    self.queue = ('Turn Head :3, T :'+value[3]+',S :8000')
                    messageSet = 1;
        if value[0] == 'twist':
            if value[1] == 'body':
                if value[2] == 'left':
                    self.queue = ('Turn Body :0, T :'+value[3]+',S :4000')
                    messageSet = 1;
                if value[2] == 'right':
                    self.queue = ('Turn Body :0, T :'+value[3]+',S :4000')
                    messageSet = 1;
                if value[2] == 'write':
                    self.queue = ('Turn Body :0, T :'+value[3]+',S :4000')
                    messageSet = 1;
        if value[0] == 'tilt':
            if value[1] == 'head':
                if value[2] == 'up':
                    self.queue = ('Tilt Head :4, T :'+value[3]+',S :4000')
                    messageSet = 1;
                if value[2] == 'down':
                    self.queue = ('Tilt Head :4, T :'+value[3]+',S :4000')
                    messageSet = 1;
        if value[0] == 'robot':
            if value[1] == 'start':
                self.queue = 'start'
                messageSet = 1;

        print(self.queue)
        if messageSet == 1:
            print(self.queue)
            self.queueFlag = 1;
        messageSet = 0;

    def setQueueFlag(self):
        self.queueFlag = 0;

    def getQueue(self):
        if(self.queueFlag == 1):
            return self.queue
        else:
            return "no"

def __main__():
    Server()
    #print("Here")

__main__()
