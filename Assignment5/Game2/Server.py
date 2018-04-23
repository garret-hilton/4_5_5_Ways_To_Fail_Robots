
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
        self.message = "null"
        global serverSocket
        global clientsocket

    def disconnect(self):
        global serverSocket
        global clientsocket
        clientsocket.close()
        serverSocket.close()

    def get_ip_address(self):
        ipArray = ni.interfaces()
        print(ipArray)
        ni.ifaddresses('wlan0')
        self.ip = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
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
            message = message.lower()
            print('Received: ' + message)
            self.parseMessage(message)

    def parseMessage(self, message):
        value = message.split(" ")
        loop = len(value)
        messageSet = 0;
        if value[0] == 'move':
            if len(value) != 1:
                if value[1] == 'north':
                    messageSet = 1;
                    self.message = 'north'
                if value[1] == 'south':
                    messageSet = 1;
                    self.message = 'south'
                if value[1] == 'west':
                    messageSet = 1;
                    self.message = 'west'
                if value[1] == 'east':
                    messageSet = 1;
                    self.message = 'east'
            else:
                self.message = message
                messageSet = 1
        elif value[0] == 'fight':
            self.message = 'fight'
            messageSet = 1;
        elif value[0] == 'run':
            self.message = 'run'
            messageSet = 1;
        elif value[0] == "":
            self.message = "null"
            messageSet = 1;
        else:
            self.message = message
            messageSet = 1;

        print("Message Parse :" + self.message)
        if messageSet == 1:
            print(self.queue)
            self.queueFlag = 1;
        messageSet = 0;

    def setQueueFlag(self):
        self.queueFlag = 0;

    def getQueue(self):
        while(self.queueFlag != 1):
            pass
        self.queueFlag = 0
        return self.message


def __main__():
    Server()
    #print("Here")
