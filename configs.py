# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("5441410", "0"))
	API_HASH = os.environ.get("a1a4fe7d23328f419d98a58339fd9980")
	BOT_TOKEN = os.environ.get("5195991252:AAE5dY1PhDIKfHRXXDxLY8iyF8mLjmzGDYI")
	BOT_USERNAME = os.environ.get("PS_FilesStore_Bot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001734801300"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1451257129"))
	DATABASE_URL = os.environ.get("mongodb+srv://User:User@cluster0.ry8oo.mongodb.net/cluster0?retryWrites=true&w=majority")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "0")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", False))
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

🧑🏻‍💻 **Developer:** @SushanthMachineni

👥 **Support Group:** [Linux Repositories](https://t.me/PokeSensei)

📢 **Updates Channel:** [Discovery Projects](https://t.me/PokeSensei)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @SushanthMachineni

Developer is Super Noob.

	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Permanent **File Store Bot**.

Hello I Will Files Of PokeSensei! Check **About Bot** Button.
"""
