import sys
from ub import app, LOGGER, TOKEN
from pyrogram import idle

from ub.bot import instructions

if len(sys.argv) not in (1, 3, 4):
    quit(1)
else:
    app.run_until_disconnected()
    LOGGER.info("Your bot is now online.")
    app.start(bot_token=TOKEN)
