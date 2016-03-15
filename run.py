import time
import sys
import socket

from queue import Queue
from threading import Thread

from bot import Bot
from settings import ADMINS, CHANNEL, WHISPERHOST, WHISPERPORT
from commands import Commands


class Main():

    def __init__(self):

        self.bot = Bot()
        self.q = Queue()
        self.wq = Queue()
        self.rs = self.bot.conn()
        self.bot.start()
        self.bot.join(self.rs, CHANNEL)
        self.wr = socket.socket()
        self.wr = self.bot.conn(s=self.wr, HOST=WHISPERHOST, PORT=WHISPERPORT)
        self.checkCom = Commands().checkCom
        self.uptime = time.time()

    def listen(self):

        readbuffer = ""

        while True:
            readbuffer = readbuffer + (self.rs.recv(4096)).decode("utf-8", errors="ignore")
            temp = readbuffer.split("\r\n")
            readbuffer = temp.pop()

            for line in temp:
                self.q.put(line)

    def listen_whisper(self):

        readbuffer = ""
        self.bot.send_raw(self.wr, "CAP REQ :twitch.tv/commands")

        while True:
            readbuffer = readbuffer + (self.wr.recv(4096)).decode("utf-8", errors="ignore")
            temp = readbuffer.split("\r\n")
            readbuffer = temp.pop()

            for line in temp:
                self.wq.put(line)

    def getUser(self, line):
        seperate = line.split(":", 2)
        user = seperate[1].split("!", 1)[0]
        return user

    def getMessage(self, line):
        separate = line.split(":", 2)
        message = separate[2]
        return message

    def read(self):

        while True:
            line = self.q.get()

            if line.startswith("PING"):
                self.rs.send((line.replace("PING", "PONG") + "\r\n").encode("utf-8"))
                print(line)
                print("ponged rs")

            elif "PRIVMSG" in line:
                user = self.getUser(line)
                msg = self.getMessage(line)

                try:
                    print((user + ": " + msg).encode(sys.stdout.encoding, errors="ignore"))
                except:
                    pass

                self.checkCom(user, msg)

            else:
                print(line)

    def read_whisper(self):
        print("read whisper")
        while True:
            line = self.wq.get()

            if line.startswith("PING"):
                self.wr.send((line.replace("PING", "PONG") + "\r\n").encode("utf-8"))
                print(line)
                print("ponged ws")

            elif "WHISPER" in line:
                user = self.getUser(line)
                msg = self.getMessage(line)

                try:
                    print((user + ": " + msg).encode(sys.stdout.encoding, errors="ignore"))
                except:
                    pass

                if user in ADMINS:
                    self.checkCom(user, msg)
            else:
                print(line)

    def type(self):
        while True:
            self.bot.say(input())

def start():
    main = Main()
    Thread(target=main.listen).start()
    Thread(target=main.read).start()
    Thread(target=main.listen_whisper).start()
    Thread(target=main.read_whisper).start()
    Thread(target=main.type).start()

start()



