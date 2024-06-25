import os

API_ID = API_ID = API ID :- 7395573126


API_HASH = os.environ.get("API_HASH", "AAHaNPYjSgLa-7ndbhY66KL8NpKhp4wWc8Q")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7395573126:AAHaNPYjSgLa-7ndbhY66KL8NpKhp4wWc8Q")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 7395573126) )

LOG = -1002070057679

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5987970971").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


