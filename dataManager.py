from paste import Paste
import json
import arrow
from os import listdir

def ser(o):
    if isinstance(o, arrow.Arrow):
        return o.for_json()
    else:
        return json.dumps(o.__dict__, default=ser, indent=4)

class DataManager:
    def saveToFile(p: Paste, filename:str):
        f = open("pastes/{}.json".format(filename), 'w')
        json_data = json.dumps(p.__dict__, default=ser, indent=4)
        f.write(json_data)
        f.close()

    def get_existing_pastes():
        return [l.removesuffix('.json') for l in listdir('./pastes')]
    
    def saveToDB():
        pass
