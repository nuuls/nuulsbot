
class Pyramid:


    def __init__(self):
        super().__init__()

        self.data = []
        self.going_down = False

    def on_pubmsg(self, user, message, channel, steal=True):
       # if source.username == 'twitchnotify':
         #   return

        #try:
        if steal:
            curlen = 2
        else:
            curlen = 1
        if True:
            msg_parts = message.split(' ')
            if len(self.data) > 0:
                cur_len = len(msg_parts)
                last_len = len(self.data[-1])
                pyramid_thing = self.data[-1][0]
                len_diff = cur_len - last_len
                if abs(len_diff) == 1:
                    good = True

                    # Make sure the pyramid consists of the same item over and over again
                    for x in msg_parts:
                        if not x == pyramid_thing:
                            good = False
                            break

                    if good:
                        self.data.append(msg_parts)
                        if len_diff > 0:
                            if self.going_down:
                                self.data = []
                                self.going_down = False
                        elif len_diff < 0:
                            self.going_down = True
                            if cur_len == curlen:
                                # A pyramid was finished
                                if "." in pyramid_thing:
                                    return
                                elif steal:
                                    self.bot.say(pyramid_thing)
                                    print("stole pyramid")
                                peak_length = 0
                                for x in self.data:
                                    if len(x) > peak_length:
                                        peak_length = len(x)

                                arguments = {
                                    'emote': pyramid_thing,
                                    'width': peak_length
                                }

                                if peak_length > 2:
                                    self.bot.say("{user} has finished a {width}-width {thing} pyramid Kappa //".format(user=user, width=peak_length, thing=pyramid_thing), channel=channel)
                                    pass
                                self.data = []
                                self.going_down = False
                    else:
                        self.data = []
                        self.going_down = False
                else:
                    self.data = []
                    self.going_down = False

            if len(msg_parts) == 1 and len(self.data) == 0:
                self.data.append(msg_parts)
        #except:
           # print("didnt work ")
