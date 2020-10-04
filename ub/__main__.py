import sys
from ub import app, LOGGER


if len(sys.argv) not in (1, 3, 4):
    quit(1)
else:
    LOGGER.info("Your bot is now online.")
    app.run()
