from bot import Bot

SERVER = ("", 6667)
IDENT = ("", "")
CHANNEL = ("", "")

LOGFILE = ""

if IDENT[0] != "" and LOGFILE != "":
    bot = Bot(SERVER, IDENT, CHANNEL, LOGFILE)
    bot.loop()
else:
    print "Please configure."
