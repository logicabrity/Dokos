from bot import Bot

SERVER = ("", 6667)
IDENT = ("", "")
CHANNEL = ("", "")

LOGGING_DIR = ""

if IDENT[0] != "":
    bot = Bot(SERVER, IDENT, CHANNEL, LOGGING_DIR)
    bot.loop()
else:
    print "Please configure."
