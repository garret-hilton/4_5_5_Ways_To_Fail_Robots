
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
        self.queueFlag = 0
        global serverSocket
        global clientsocket

    def diconnect(self):
        clientsocket.close()
        serverSocket.close()

    def get_ip_address(self):
        ipArray = ni.interfaces()
        print(ipArray)
        ni.ifaddresses('wlp1s0')
        self.ip = ni.ifaddresses('wlp1s0')[ni.AF_INET][0]['addr']
        print (self.ip)  # should print "192.168.100.37"

    def startServer(self):
        global serverSocket
        print("Starting Server")
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = "10.200.0.160"
        port = 9996
        serverSocket.bind((self.ip, port))
        serverSocket.listen(5)
        threadServerRec = Thread(target = self.startRec, args = ())
        threadServerRec.start()

    def getMessage(self):
        while True:
            self.name = input("Enter a meassage to Send\n")
            self.sendFlag = 1

            time.sleep(1)

    def stt(self):
        self.name = ("SST")
        self.startSend()

    def tts(self, message):
        self.name = message
        self.startSend()

    def startSend(self):
        global clientsocket
        print('Sending Message :' + self.name)
        self.msg = self.name + "\r\n"
        clientsocket.send(self.msg.encode('ascii'))

    def startRec(self):
        global serverSocket
        global clientsocket
        while True:
            print('listening')
            clientsocket,addr = serverSocket.accept()
            print('Got a connection from %s' % str(addr))
            rec = Thread(target = self.receive, args = ())
            rec.start()


    def receive(self):
        global clientsocket
        while True:
            data = clientsocket.recv(1024)
            message = data.decode('ascii')
            print('Received: ' + message)
            self.parseMessage(message)

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
