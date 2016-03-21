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
        try:
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
        except:
            pass

def accage(user, message):

    try:
        message = message.split(" ")
        user_from_msg = message[1]
        url = "https://apis.rtainc.co/twitchbot/created?user=" + user_from_msg
        req = urllib.request.Request(url)
        print(req)
        opener = urllib.request.build_opener()
        f = opener.open(req).read()
        print(f)
        data = f.decode("utf-8")
        #data = json.loads((f))
        #print(data)

        return "{user} was created {data} ago Keepo".format(user=user_from_msg, data=data)

    except:
        try:
            url = "https://apis.rtainc.co/twitchbot/created?user=" + user
            req = urllib.request.Request(url)
            opener = urllib.request.build_opener()
            f = opener.open(req).read()
            data = f.decode("utf-8")
            return "{user} was created {data} ago Keepo".format(user=user, data=data)
        except:
            pass