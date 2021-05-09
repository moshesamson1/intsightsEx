from paste import Paste
import json
import arrow
from os import listdir

class DataManager:
    def saveToFile(p: Paste, filename:str):
        f = open("pastes/{}.json".format(filename), 'w')
        json_data = json.dumps(p.__dict__, default=str, indent=4)
        f.write(json_data)
        f.close()

    def get_existing_pastes():
        return [l.removesuffix('.json') for l in listdir('./pastes')]
    
    def saveToDB():
        pass
