import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

CONFIG_FILE = DATA_DIR / "config.json"



DEFAULT_CONFIG = {

    "application": {

        "name": "GS1 Scanner",

        "version": "1.0.0"

    },


    "camera": {

        "default_index": 0,

        "resolution": {

            "width": 1920,

            "height": 1080

        },

        "fps": 30

    },


    "scanner": {

        "scan_interval_ms": 200,

        "auto_scan": True

    },


    "sound": {

        "success": "ok.mp3",

        "failed": "ng.mp3"

    },


    "history": {

        "max_records": 10000

    },
    "roi": {

        "enabled": True,

        "width_ratio": 0.6,

        "height_ratio": 0.6

    }

}




def ensure_config():


    DATA_DIR.mkdir(

        parents=True,

        exist_ok=True

    )



    if not CONFIG_FILE.exists():

        save_config(
            DEFAULT_CONFIG
        )





def load_config():


    ensure_config()



    try:


        with open(

            CONFIG_FILE,

            "r",

            encoding="utf-8"

        ) as file:


            return json.load(
                file
            )



    except Exception:


        save_config(
            DEFAULT_CONFIG
        )


        return DEFAULT_CONFIG.copy()





def save_config(
    config: dict
):


    DATA_DIR.mkdir(

        parents=True,

        exist_ok=True

    )



    with open(

        CONFIG_FILE,

        "w",

        encoding="utf-8"

    ) as file:


        json.dump(

            config,

            file,

            ensure_ascii=False,

            indent=4

        )