from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "")
      API_ID = int(getenv("API_ID", ""))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "")
      session_string = getenv("session_string", "")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002000077230:-1002083341321").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
