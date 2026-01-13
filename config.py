import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8435607789:AAG4vKk1WqvfOeZ_nZnJGB3IzamLSWQE4lQ")

    APP_ID = int(os.environ.get("APP_ID", 8435607789))

    API_HASH = os.environ.get("API_HASH", "AAG4vKk1WqvfOeZ_nZnJGB3IzamLSWQE4lQ")

    AUDIO_THUMBNAIL = os.environ.get("AUDIO_THUMBNAIL", "")

    VIDEO_THUMBNAIL = os.environ.get("VIDEO_THUMBNAIL", "")
