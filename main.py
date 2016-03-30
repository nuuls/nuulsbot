import time
import sys

from threading import Thread

from src.controllers.irc import Irc
from settings import CHANNEL, GROUPHOST, GROUPPORT, ADMIN
from src.modules.commands import Commands

class Main:

    def __init__(self):
        self.bot = Irc()
        self.q = self.bot.q
        self.whisperq = self.bot.whisperq
        self.bot.conn(anon=True)
        self.bot.conn()
        self.bot.whisperconn = self.bot.conn(HOST=GROUPHOST, PORT=GROUPPORT, whisper=True)
        Thread(target=self.bot.ratelimit).start()
        self.commands = Commands()
        self.commands.bot = self.bot
        time.sleep(1)
        for chan in CHANNEL:
            self.bot.join(chan)


    def main(self):
        bot = self.bot
        while True:
            line = self.bot.q.get()
            try:
                user = line["user"]
                msg = line["msg"]
                channel = line["channel"]
                print("%s # %s : %s" % (channel, user, msg))

            except:
                pass
            if user == ADMIN:
                try:
                    if "!say " in msg:
                        self.bot.say(msg.replace("!say ", ""), channel=channel)
                    if "!eval " in msg:
                        eval(msg.replace("!eval ", ""))
                    if "!exec " in msg:
                        exec(msg.replace("!exec ", ""))
                except Exception as e:
                    print(e)
            if not bot.silent[channel]:
                try:
                    self.commands.checkCom(user, msg, channel)
                except Exception as e:
                    print(e)


    def whisper(self):
        bot = self.bot
        while True:
            line = bot.whisperq.get()
            #try:
            print(line)

            #except:
                #print("didnt work")

    def spam(self, emote, count, channel=CHANNEL[0]):
        for x in range(1, count):
            self.bot.say(emote + " " + str(x), channel=channel)


Main = Main()
Thread(target=Main.main).start()
Thread(target=Main.whisper).start()
