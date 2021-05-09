from paste import Paste
import json
from os import listdir
from pathlib import Path


class DataManager:
    def saveToFile(p: Paste, filename: str):
        Path("./pastes").mkdir(exist_ok=True)
        f = open("./pastes/{}.json".format(filename), 'w')
        json_data = json.dumps(p.__dict__, default=str, indent=4)
        f.write(json_data)
        f.close()

    def get_existing_pastes():
        # should support db also
        try:
            return [fn.removesuffix('.json') for fn in listdir('./pastes')]
        except Exception:
            return []

    def saveToDB():
        pass
