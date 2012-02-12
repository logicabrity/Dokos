from bot import Bot

SERVER = ("", 6667)
IDENT = ("", "")
CHANNEL = ("", "")

bot = Bot(SERVER, IDENT, CHANNEL)
bot.loop()
