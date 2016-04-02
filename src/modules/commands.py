import random
import time
import json

from threading import Thread

from src.modules.eightball import ball
from settings import ADMIN, BANPHRASES, CHANNEL
from src.modules.myd import myd
from src.modules.created import created, accage
from src.modules.pyramid import Pyramid
from src.modules.chatters import *


class Commands():
    def __init__(self):
        self.pyramid = Pyramid()
        self.pyramid_on = False

    with open("src/modules/simplecom.json", "r") as simplecoms:
        coms = json.load(simplecoms)
        print("coms loaded")

    def addcom(self, trigger, response):
        try:
            self.coms[trigger.lower()] = response
            with open("src/modules/simplecom.json", "w") as simplecoms:
                json.dump(self.coms, simplecoms)
            print("command added")

        except:
            pass

    def delcom(self, trigger):
        try:
            del self.coms[trigger]
            with open("src/modules/simplecom.json", "w") as simplecoms:
                json.dump(self.coms, simplecoms)

        except:
            print("didnt work")

    def checkCom(self, user, msg, channel=CHANNEL[0]):

        if msg.startswith("!"):

            if user == ADMIN:

                """if "!eval " in msg.lower():
                    try:
                        eval(msg.split(" ", 1)[1])
                    except:
                        self.bot.whisper(user, "didnt work")

                if "!join" in msg.lower():
                    try:
                        temp = msg.split(" ")
                        self.bot.join(temp[1])
                    except:
                        print("could not join channel")

                if "!part" in msg.lower():
                    try:
                        temp = msg.split(" ")
                        self.bot.part(temp[1])
                    except:
                        print("could not leave channel")

                if "!say " in msg.lower():
                    tempmsg = msg.replace("!say ", "")
                    self.bot.say(tempmsg, channel=channel)

                if "!send" in msg.lower():
                    tempmsg = msg.replace("!send ", "")
                    try:
                        self.bot.send_raw(self.bot.mains, tempmsg)
                    except:
                        self.bot.whisper(user, "didnt work")

                if "!whisper " in msg.lower():
                    tempmsg = msg.replace("!whisper ", "")
                    test = tempmsg.split(" ", 1)
                    target_user = test[0]
                    print("target user: " + target_user)

                    msg = test[1]
                    print("msg: " + msg)
                    self.bot.whisper(target_user, msg)

                if "!on" in msg.lower():
                    self.bot.on = True
                    self.bot.whisper(user, "on")

                if "!off" in msg.lower():
                    self.bot.on = False
                    self.bot.whisper(user, "off")"""

                if "!status" in msg.lower():
                    uptime = time.time() - self.bot.uptime
                    uptime = time.strftime('%H:%M:%S', time.gmtime(uptime))
                    self.bot.say("nuulsbot has been online for {uptime} FeelsGoodMan".format(uptime=uptime), channel=channel)


            if "!circle " in msg.lower():
                pasta = "ᅚᅚᅚᅚᅚᅚᅚᅚᅚᅚᅚᅚᅚᅚᅚᅚᅚᅚᅚᅚᅚᅚ ᅚᅚᅚᅚᅚᅚᅚᅚᅚ Keepo ᅚ Keepo ᅚᅚ ᅚᅚᅚᅚᅚᅚᅚ Keepo ᅚᅚᅚᅚᅚ Keepo ᅚᅚᅚᅚ ᅚᅚᅚᅚᅚᅚ Keepo ᅚᅚ KaRappa ᅚᅚ Keepo ᅚᅚ ᅚᅚᅚᅚᅚᅚᅚ Keepo ᅚᅚᅚᅚᅚ Keepo ᅚᅚᅚᅚ ᅚᅚᅚᅚᅚᅚᅚᅚᅚ Keepo ᅚ Keepo"
                try:
                    if "." in msg:
                        emote = "HotPokket"
                        emote2 = "BabyRage"
                    else:
                        tempmsg = msg.split(" ")
                        emote = tempmsg[1]
                        emote2 = tempmsg[2]
                    tempmsg = pasta.replace("Keepo", emote)
                    tempmsg = tempmsg.replace("KaRappa", emote2)
                    self.bot.say(tempmsg, channel=channel)
                except:
                    print("circle didnt work")

            """if "!hangman " in msg.lower() and user == ADMIN:
                self.hangman = Hangman()
                word = msg.split(" ")
                self.hangman.word = word[1]
                self.hangman.word_list = list(self.hangman.word)
                self.hangman.word_guessed = len(self.hangman.word) * "_"
                print(self.hangman.word_guessed)
                self.bot.say("a game of hangman has started, guess with !h and a single letter PogChamp", channel=channel)

            if "!h " in msg.lower():
                guess = msg.split(" ")
                self.hangman.hangman(user, guess[1])"""

            if "!8ball " in msg.lower():
                tempmsg = user + ", " + ball(msg)
                self.bot.say(tempmsg, channel=channel)

            if "!addcom " in msg.lower() and user == ADMIN:
                try:
                    tempmsg = msg.replace("!addcom ", "")
                    tempmsg = tempmsg.split(" ", 1)
                    trigger = tempmsg[0]
                    response = tempmsg[1]
                    Commands.addcom(self, trigger.lower(), response)
                    self.bot.whisper(user, "command " + trigger + " has been added KKona")
                except:
                    pass

            if "!delcom " in msg.lower() and user == ADMIN:
                try:
                    tempmsg = msg.split(" ", 1)
                    trigger = tempmsg[1]
                    Commands.delcom(self, trigger.lower())
                    self.bot.whisper(user, "command %s has been removed" % (trigger))
                except:
                    pass

            if "!delcomall" in msg.lower() and user == ADMIN:
                try:
                    with open("simplecom.json", "w") as simplecoms:
                        json.dump({}, simplecoms)
                    print("deleted all commands")

                except:
                    pass

            if "!chatters " in msg.lower():
                chann = msg.split(" ")[1]
                if "." in chann:
                    return
                chatters = "0"
                viewers = "offline"

                try:
                    chatters = chatter(chann)
                except Exception as e:
                    print(e)
                try:
                    viewers = viewer(chann)
                except Exception as e:
                    print(e)
                self.bot.say("current channel info for %s: chatters: %s viewers: %s pajaHop" %(chann, str(chatters), str(viewers)), channel=channel)
            if "!viewers " in msg.lower():
                try:
                    chann = msg.split(" ")[1]
                    self.bot.say(str(viewer(chann)))
                except Exception as e:
                    print(e)

            if "!myd" in msg.lower():
                self.bot.say(user + "'s dick is " + myd(), channel=channel)

            if "!created" in msg.lower():
                self.bot.say(created(user, msg), channel=channel)

            if "!accage" in msg.lower():
                try:
                    self.bot.say(accage(user, msg), channel=channel)
                except:
                    pass

            if "!rateme" in msg.lower():
                a = random.randint(1, 10)
                pool = {1:"(puke)", 2:"DansGame", 3:"EleGiggle", 4:"4Head", 5:":)", 6:"FeelsGoodMan", 7:"SeemsGood", 8:"PogChamp", 9:"nymnWink", 10:"Kappa"}

                self.bot.say(("I rate {user} {a} out of 10 {emote}".format(user=user, a=a, emote=pool[a])), channel=channel)

            if "pyramid" in msg.lower() and user == ADMIN:
                if "steal" in msg.lower():
                    self.pyramid_on = True
                    self.steal = True
                    self.bot.whisper(user, "stealing pyramids on Keepo")

                if "off" in msg.lower():
                    self.pyramid_on = False
                    self.bot.say("no longer stealing pyramids Keepo", channel=channel)

                if "display" in msg.lower():
                    self.pyramid_on = True
                    self.steal = False
                    self.bot.whisper(user, "now displaying pyramids in %s" % channel)

        msgtemp = msg.lower().split(" ")

        for key in self.coms:
            if key == msgtemp[0]:
                reply = self.coms[key.lower()]
                self.bot.say(reply, channel=channel)


        if self.pyramid_on:
            self.pyramid.on_pubmsg(user, msg, channel, self.steal)
