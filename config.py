import os

API_ID = API_ID = 25038096

API_HASH = os.environ.get("API_HASH", "098112aae38be62db58363267a061b59")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7301491923:AAFrQjxhpSJ39i4jiMyGOX0brx0vF42JCdE")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 7208237246))

LOG = -1002106094933

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1833865556").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)

