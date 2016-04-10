import socket
import time

from threading import Thread
from queue import Queue

from src.controllers.parse import Parse
from settings import PASS, IDENT, HOST, PORT, CHANNEL
from src.modules.commands import Commands

class Irc:

    def __init__(self):
        self.msgs_sent_total = 0
        self.msgs_last_30secs = 0
        self.last_msg_sent = {}
        self.last_msg = 0
        self.mod = {}
        self.q = Queue()
        self.whisperq = Queue()
        self.connlist = {}
        self.connlist_read = []
        self.mod = {}
        self.silent = {}
        self.uptime = time.time()

    def send_raw(self, s, msg):
        s.send((msg + "\r\n").encode("utf-8"))
        self.msgs_sent_total += 1
        print("sent: " + msg)

    def conn(self, read=False, whisper=False):
        s = socket.socket()
        s.connect((HOST, PORT))
        if not read:
            s.send(("PASS " + PASS + "\r\n").encode("utf-8"))
            self.send_raw(s, "NICK " + IDENT)
            if not whisper:
                self.connlist[s] = 0
            Thread(target=self.listen, args=(s,)).start()
        else:
            #self.send_raw(s, "NICK " + "justinfan69")
            s.send(("PASS " + PASS + "\r\n").encode("utf-8"))
            self.send_raw(s, "NICK " + IDENT)
            Thread(target=self.listen, args=(s,), kwargs={"read": True}).start()
            self.send_raw(s, "CAP REQ :twitch.tv/tags")
            self.connlist_read.append(s)
        self.send_raw(s, "CAP REQ :twitch.tv/commands")
        print("connected")

        return s

    def join(self, channel, silent=False):
        self.send_raw(self.connlist_read[0], "JOIN #" + channel.lower())
        self.mod[channel] = False
        self.silent[channel] = silent
        self.bot.commands[channel] = Commands()
        self.bot.commands[channel] = Commands()
        self.bot.commands[channel].bot = self.bot
        self.bot.commands[channel].pyramid.bot = self.bot

    def part(self, channel):
        self.send_raw(self.connlist_read[0], "PART #" + channel)

    def say(self, msg, channel=CHANNEL[0]):
        if not channel in self.last_msg_sent:
            self.last_msg_sent[channel] = 1.0
        if not channel in self.mod:
            self.mod[channel] = False
        if self.mod[channel] or self.last_msg_sent[channel] + 1.2 < time.time():
            #sock = self.connlist[self.msgs_sent_total % len(self.connlist)]
            s = min(self.connlist, key=self.connlist.get)
            #print("used connection %s" % str(min(self.connlist, key=self.connlist.get)))
            if msg.startswith("."):
                space = ""
            else:
                space = ". "
            self.send_raw(s,"PRIVMSG #%s :%s%s" % (channel, space, msg))
            self.msgs_last_30secs += 1
            self.connlist[s] += 1
            self.last_msg_sent[channel] = time.time()
            self.last_msg = time.time()
            if self.msgs_last_30secs / len(self.connlist) > 15:
                self.conn()

    def whisper(self, user, msg):
        #self.say(".w %s %s" % (user, msg))
        self.send_raw(self.connlist_read[0], "PRIVMSG #nuuls :.w %s %s" % (user, msg))

    def listen(self, s, read=False):
        readbuffer = ""
        while True:
            readbuffer = readbuffer + (s.recv(4096)).decode("utf-8", errors="ignore")
            temp = readbuffer.split("\r\n")
            readbuffer = temp.pop()
            for line in temp:
                #print(line)
            #    try:
                if line.startswith("PING"):
                    print(line)
                    self.send_raw(s, line.replace("PING", "PONG"))
                elif read:
                    if "PRIVMSG" in line:
                        source = Parse(line)
                        if source.user == IDENT:
                            self.mod[source.channel] = source.mod
                        else:
                            self.q.put(source)

                    elif "WHISPER" in line:
                        data = {}
                        data["user"] = line.split(":", 2)[1].split("!", 1)[0]
                        data["message"] = line.split(":", 2)[2]
                        self.whisperq.put(data)
                    else:
                        print(line)
            #    except:
                #    pass

    def ratelimit(self):
        while True:
            if self.msgs_last_30secs > 0:
                self.msgs_last_30secs -= 1
                if self.last_msg + 30 < time.time():
                    for s in self.connlist:
                        self.connlist[s] = 0
            time.sleep(2)
