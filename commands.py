from bot import Bot
from eightball import ball
import time
from threading import Thread
import json
from settings import ADMINS, BANPHRASES
from myd import myd
from created import created
import random
from pyramid import Pyramid
bot = Bot()
#bot.start()




class Commands():
    pyramid = Pyramid()
    pyramid_on = False

    waittime = 30
    indungeon = {}
    with open("simplecom.json", "r") as simplecoms:
        coms = json.load(simplecoms)
        print("coms loaded")

    def addcom(self, trigger, response):
        try:
            self.coms[trigger.lower()] = response
            with open("simplecom.json", "w") as simplecoms:
                json.dump(self.coms, simplecoms)
            print("command added")
            bot.say("command " + trigger + " has been added KKona")
        except:
            pass

    def delcom(self, trigger):
        try:
            del self.coms[trigger]
            with open("simplecom.json", "w") as simplecoms:
                json.dump(self.coms, simplecoms)
        except:
            print("didnt work")

    def checkCom(self, user, msg):

        """if "!dungeon" in msg.lower():
            dungeon = Dungeon(user)
            print(self.indungeon)
            if "level" in msg:
                print(user)
                bot.say(user + " is on level: " + str(dungeon.getLevel()))

            if "enter" in msg:
                try:
                    if not self.indungeon[user]:
                        self.indungeon[user] = True
                        print(self.indungeon)
                        Thread(target=Commands().dungeonwait, args=(user, )).start()

                except:
                    self.indungeon[user] = True
                    print(self.indungeon)
                    Thread(target=Commands().dungeonwait, args=(user, )).start()"""

        if msg.startswith("!"):

            if "!say " in msg.lower() and user in ADMINS:
                tempmsg = msg.replace("!say ", "")
                bot.say(tempmsg)

            if "!send" in msg.lower() and user in ADMINS:
                tempmsg = msg.replace("!send ", "")
                try:
                    bot.send_raw(bot.mains, tempmsg)
                except:
                    bot.whisper(user, "didnt work")

            if "!whisper " in msg.lower() and user in ADMINS:
                tempmsg = msg.replace("!whisper ", "")
                test = tempmsg.split(" ", 1)
                target_user = test[0]
                print("target user: " + target_user)

                msg = test[1]
                print("msg: " + msg)
                bot.whisper(target_user, msg)

            if "!on" in msg and user in ADMINS:
                bot.on = True
                bot.whisper(user, "on")

            if "!off" in msg and user in ADMINS:
                bot.on = False
                bot.whisper(user, "off")

            if "!status" in msg.lower() and user in ADMINS:
                uptime = time.time() - bot.uptime
                uptime = time.strftime('%H:%M:%S', time.gmtime(uptime))
                bot.say("nuulsbot has been online for {uptime} FeelsGoodMan".format(uptime=uptime))

            #if "!join " in msg.lower() and user in ADMINS:


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
                    bot.say(tempmsg)
                except:
                    print("circle didnt work")

            """if "!hangman " in msg.lower() and user in ADMINS:
                self.hangman = Hangman()
                word = msg.split(" ")
                self.hangman.word = word[1]
                for _ in word:
                    self.hangman.word_guessed.append("_")
                bot.say("a game of hangman has started, guess with !h and a single letter PogChamp")"""

            """if "!h " in msg.lower():
                guess = msg.split(" ")
                self.hangman.hangman(user, guess[1])"""

            if "!8ball " in msg.lower():
                tempmsg = user + ", " + ball(msg)
                bot.say(tempmsg)

            if "!addcom " in msg.lower() and user in ADMINS:
                try:
                    tempmsg = msg.replace("!addcom ", "")
                    tempmsg = tempmsg.split(" ", 1)
                    trigger = tempmsg[0]
                    response = tempmsg[1]
                    Commands.addcom(self, trigger.lower(), response)
                except:
                    pass

            if "!delcom " in msg.lower() and user in ADMINS:
                try:
                    tempmsg = msg.split(" ", 1)
                    trigger = tempmsg[1]
                    Commands.delcom(self, trigger.lower())
                except:
                    pass

            if "!delcomall" in msg.lower() and user in ADMINS:
                try:
                    with open("simplecom.json", "w") as simplecoms:
                        json.dump({}, simplecoms)
                    print("deleted all commands")

                except:
                    pass

            if "!myd" in msg.lower():
                bot.say(user + "'s dick is " + myd())

            if "!created" in msg.lower():
                bot.say(created(user, msg))

            if "!rate" in msg.lower():
                a = random.randint(1, 10)
                pool = {1:"(puke)", 2:"DansGame", 3:"EleGiggle", 4:"4Head", 5:":)", 6:"FeelsGoodMan", 7:"SeemsGood", 8:"PogChamp", 9:"nymnWink", 10:"Kappa"}

                if "!rateme" in msg.lower():
                    bot.say(("I rate {user} {a} out of 10 {emote}".format(user=user, a=a, emote=pool[a])))

                else:
                    lowermsg = msg.lower()
                    for item in BANPHRASES:
                        if item in lowermsg:
                            return False
                    if "pajlada" in lowermsg:
                        msg = lowermsg.replace("pajlada", "paj-lada")

                    try:
                        tempmsg = msg.split(" ")
                        target = tempmsg.pop(1)
                        bot.say("I rate {target} {a} out of 10 {emote}".format(target=target, a=a, emote=pool[a]))
                    except:
                        bot.say(("I rate {user} {a} out of 10 {emote}".format(user=user, a=a, emote=pool[a])))



            if "pyramid" in msg.lower() and user in ADMINS:
                if "steal" in msg.lower():
                    self.pyramid_on = True
                    self.steal = True
                    bot.whisper(user, "stealing pyramids on Keepo")

                if "off" in msg.lower():
                    self.pyramid_on = False
                    bot.say("no longer stealing pyramids Keepo")

                if "display" in msg.lower():
                    self.pyramid_on = True
                    self.steal = False
                    bot.whisper(user, "now displaying pyramids")

        msgtemp = msg.lower().split(" ")

        for key in self.coms:
            if key == msgtemp[0]:
                reply = self.coms[key.lower()]
                bot.say(reply)


        if self.pyramid_on:
            self.pyramid.on_pubmsg(user, msg, self.steal)





        #except:
           # print("something went wrong")