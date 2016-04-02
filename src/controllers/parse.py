def parse(line):
    data = {}
    line = line.split(";", 7)
    data["user"] = line[7].split(":", 2)[1].split("!")[0]
    data["emotes"] = line[2][7:]

    if "1" in line[3]:
        data["mod"] = True
    else:
        data["mod"] = False

    if "1" in line[5]:
        data["sub"] = True
    else:
        data["sub"] = False

    data["channel"] = line[7].split("#")[1][:line[7].split("#")[1].find(" ")]

    data["msg"] = line[7].split(":", 2)[2]

    return data
