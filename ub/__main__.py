import sys
from ub import app, LOGGER


if len(sys.argv) not in (1, 3, 4):
    quit(1)
else:
    app.run()
    LOGGER.info("Your bot is now online.")
