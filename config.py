from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "d7fbe2036e9ed2a1468fad5a5584a255")
      API_ID = int(getenv("API_ID", 22420997))
      AS_COPY = True if getenv("AS_COPY", True) == "True" else False
      BOT_TOKEN = getenv("BOT_TOKEN", "7490926656:AAHG-oUUzGPony9xfyApSI0EbbymhneDU1k")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "").replace("\n", " ").split(' '))
