import random

def ball(message):

    a = random.randint(1, 10)
    message = message.lower()

    if message == "!8ball":

        return "You gotta ask something OMGScoots"

    if "?" not in message:
        return "where is the \"?\" OMGScoots"

    if ("ban" in message.lower() or "banned" in message.lower())  and (" nuulsbot" in message.lower() or " bot" in message.lower()):
        return " dont ban me BibleThump"

    #if "gay" in message and "nuuls" not in message:
     #   return "Yes KappaPride"

    if "gay" in message and "nuuls" in message:
        return "no OMGScoots"

    else:
        phrases = [
            'sure',
            'are you kidding?!',
            'yeah',
            'no',
            'i think so',
            'don\'t bet on it',
            'ja',
            'doubtful',
            'for sure',
            'forget about it',
            'nein',
            'maybe',
            'Kappa Keepo PogChamp',
            'sure',
            'i dont think so',
            'it is so',
            'leaning towards no',
            'look deep in your heart and you will see the answer',
            'most definitely',
            'most likely',
            'my sources say yes',
            'never',
            'nah m8',
            'might actually be yes',
            'no.',
            'none',
            'outlook good',
            'outlook not so good',
            'perhaps',
            'mayhaps',
            'that\'s a tough one',
            'idk kev',
            'don\'t ask that',
            'the answer to that isn\'t pretty',
            'the heavens point to yes',
            'who knows?',
            'without a doubt',
            'yesterday it would\'ve been a yes, but today it\'s a yep',
            'you will have to wait'
            ]

        emotes = [
            "Kappa",
            "Keepo",
            "xD",
            "KKona",
            "KappaWealth",
            "4Head",
            "EleGiggle",
            "nymnWink",
            "KappaCool",
            "BrokeBack",
            "OpieOP",
            "KappaRoss",
            "KappaPride",
            "FeelsBadMan",
            "FeelsGoodMan",
            "PogChamp",
            "VisLaud",
            "OhMyDog",
            "FrankerZ",
            "DatSheffy",
            "BabyRage",
            "VoHiYo",
            "haHAA",
            "FeelsBirthdayMan",
            "LUL"
            ]

    return "The magic 8ball says... " + random.choice(phrases) + " " + random.choice(emotes)
