import json
import urllib.request


def created(user, message):

    try:
        message = message.split(" ")
        user_from_msg = message[1]
        url = "https://api.twitch.tv/kraken/users/" + user_from_msg
        req = urllib.request.Request(url)
        opener = urllib.request.build_opener()
        f = opener.open(req).read()
        data = json.loads((f).decode("utf-8"))
        date = data.get("created_at")
        date = date.split("T", 1)
        date = date[0]
        date = date.split("-")
        day = date[2]
        month = date[1]
        year = date[0]
        date = day + "." + month + "." + year
        return user_from_msg + " was created on: " + date

    except:

        url = "https://api.twitch.tv/kraken/users/" + user + ".json"
        req = urllib.request.Request(url)
        opener = urllib.request.build_opener()
        f = opener.open(req).read()
        data = json.loads((f).decode("utf-8"))
        date = data.get("created_at")
        date = date.split("T", 1)
        date = date[0]
        date = date.split("-")
        day = date[2]
        month = date[1]
        year = date[0]
        date = day + "." + month + "." + year
        return user + " was created on: " + date
