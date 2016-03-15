import socket
import time

from queue import Queue
from threading import Thread

from settings import HOST, PORT, IDENT, PASS, WHISPERPORT, WHISPERHOST, CHANNEL


class Bot():
    mains = socket.socket()
    secs = socket.socket()
    ws = socket.socket()

    def __init__(self):
        self.last_msg_sent = time.time()
        self.uptime = time.time()
        self.on = True

    def conn(self, s=socket.socket(), HOST=HOST, PORT=PORT):
        #s = socket.socket()
        s.connect((HOST, PORT))
        s.send(("PASS " + PASS + "\r\n").encode("utf-8"))
        s.send(("NICK " + IDENT + "\r\n").encode("utf-8"))
        print("connected")
        return s

    def join(self, s, channel):
        s.send(("JOIN #" + channel + "\r\n").encode("utf-8"))
        print("joined " + channel)

    def send_raw(self, s, msg):
        s.send((msg + "\r\n").encode("utf-8"))
        print("sent: " + msg)

    def say(self, msg, channel=CHANNEL):
        if self.on:
            if self.last_msg_sent + 1.2 < time.time():

                if self.last_msg_sent + 5 > time.time():
                    self.sock = self.secs
                else:
                    self.sock = self.mains
                if msg.startswith("."):
                    space = ""
                else:
                    space = ". "
                #try:
                msgTemp = "PRIVMSG #" + channel + " :" + space + msg
                self.sock.send((msgTemp + "\r\n").encode("utf-8"))
                try:
                    print("sent: " + msg)
                except:
                    print("message sent but could not print")
                self.last_msg_sent = time.time()
                #except:
                #    print("disconnected, trying again")
                #    time.sleep(2)
                #    self.say(msg)

    def whisper(self, user, msg):
        msgTemp = "PRIVMSG #jtv :/w " + user + " " + msg
        self.send_raw(self.ws, msgTemp)

    def pong(self, s):
        need_to_pong = True
        readbuffer = ""
        while need_to_pong:

            try:
                readbuffer = readbuffer + (s.recv(1024)).decode("utf-8")
                temp = readbuffer.split("\r\n")
                readbuffer = temp.pop()

                for line in temp:
                    if line.startswith("PING"):
                        print(line)
                        self.send_raw(s, line.replace("PING", "PONG"))
                        print("ponged")
            except:
                print("no longer ponging")
                need_to_pong = False

    def start(self):
        self.mains = self.conn(self.mains)
        self.secs = self.conn(self.secs)
        self.ws = self.conn(self.ws, HOST=WHISPERHOST, PORT=WHISPERPORT)

        Thread(target=self.pong, args=(self.mains,)).start()
        Thread(target=self.pong, args=(self.secs,)).start()
        Thread(target=self.pong, args=(self.ws,)).start()







