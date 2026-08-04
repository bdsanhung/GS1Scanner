from pathlib import Path


# Application
APP_NAME = "GS1 Scanner"
APP_VERSION = "1.0.0"


# Directory
BASE_DIR = Path(__file__).resolve().parent.parent

RESOURCE_DIR = BASE_DIR / "resources"

IMAGE_DIR = RESOURCE_DIR / "images"

SOUND_DIR = RESOURCE_DIR / "sounds"


# Default resources
DEFAULT_IMAGE = IMAGE_DIR / "no-image.png"

SUCCESS_SOUND = SOUND_DIR / "ok.mp3"

ERROR_SOUND = SOUND_DIR / "ng.mp3"


# GS1 Separator
GS1_GROUP_SEPARATOR = "\x1D"


# GS1 Application Identifiers

AI_GTIN = "01"

AI_PRODUCTION_DATE = "11"

AI_EXPIRATION_DATE = "17"

AI_BATCH = "10"

AI_SERIAL = "21"


# Scanner

DEFAULT_CAMERA_INDEX = 0

DEFAULT_SCAN_INTERVAL = 200


# History

MAX_HISTORY_RECORDS = 10000