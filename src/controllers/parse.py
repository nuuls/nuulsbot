class Parse:

    def __init__(self, line):
        line = line.split(";", 7)
        self.user = line[7].split(":", 2)[1].split("!")[0]
        self.emotes = line[2][7:]

        if "1" in line[3]:
            self.mod = True
        else:
            self.mod = False

        if "1" in line[5]:
            self.sub = True
        else:
            self.sub = False

        self.channel = line[7].split("#")[1][:line[7].split("#")[1].find(" ")]

        self.msg = line[7].split(":", 2)[2]
        if self.msg.startswith("\x01ACTION "):
            self.msg = self.msg.replace("\x01ACTION ", "")
            if self.msg.endswith("\x01"):
                self.msg = self.msg.replace("\x01", "")
                self.me = True
        else:
            self.me = False
