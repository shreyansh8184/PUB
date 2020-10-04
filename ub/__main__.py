import sys
from ub import app, LOGGER
from pyrogram import idle

from ub.bot import instructions
if len(sys.argv) not in (1, 3, 4):
    quit(1)
else:
    app.start()
    LOGGER.info("Your bot is now online.")
    idle()
