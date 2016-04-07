import time
import sys

from threading import Thread

from src.controllers.irc import Irc
from settings import CHANNEL, ADMIN
from src.modules.commands import Commands

class Main:

    def __init__(self):
        self.bot = Irc()
        self.q = self.bot.q
        self.whisperq = self.bot.whisperq
        self.bot.conn(anon=True)
        self.bot.conn()
        Thread(target=self.bot.ratelimit).start()
        self.commands = {}
        self.bot.commands = self.commands
        self.bot.bot = self.bot

        time.sleep(1)
        for chan in CHANNEL:
            self.bot.join(chan)
            self.commands[chan] = Commands()
            self.commands[chan].bot = self.bot
            self.commands[chan].pyramid.bot = self.bot

    def main(self):
        bot = self.bot
        while True:
            source = self.bot.q.get()
            try:
                user = source.user
                msg = source.msg
                channel = source.channel
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
                    self.commands[channel].checkCom(user, msg, channel)
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
