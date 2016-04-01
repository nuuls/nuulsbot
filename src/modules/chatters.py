import urllib.request
import json

def chatter(channel):
    url = "http://tmi.twitch.tv/group/user/%s" % channel
    req = urllib.request.Request(url)
    opener = urllib.request.build_opener()
    f = opener.open(req).read()
    data = json.loads((f).decode("utf-8"))

    chatter_count = data["chatter_count"]
    return chatter_count


def viewer(channel):
    url = "https://api.twitch.tv/kraken/streams/%s" % channel
    req = urllib.request.Request(url)
    opener = urllib.request.build_opener()
    f = opener.open(req).read()
    data = json.loads((f).decode("utf-8"))

    viewers = data.get("stream").get("viewers")
    return viewers
