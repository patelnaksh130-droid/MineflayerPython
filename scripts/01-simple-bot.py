from javascript import require, On, Once, AsyncTask, once, off

# Import the javascript libraries
mineflayer = require("mineflayer")

# Create bot with basic parameters
bot = mineflayer.createBot(
    {"username": "simple-bot", "host": "beetlepro0024-FHWn.aternos.me:20026", "port": 20026, "version": "1.21.8", "hideErrors": False}
)

# Login event required for bot
@On(bot, "login")
def login(this):
    pass
