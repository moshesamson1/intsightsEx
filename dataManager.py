from paste import Paste
import json
import arrow

def ser(o):
    if isinstance(o, arrow.Arrow):
        print(o.__dict__)
        return o.for_json()
    else:
        return json.dumps(o.__dict__, default=ser, indent=4)

class DataManager:
    def saveToFile(p: Paste, filename:str):
        f = open("pastes/{}.json".format(filename), 'w')
        json_data = json.dumps(p.__dict__, default=ser, indent=4)
        f.write(json_data)
        f.close()

    
    def saveToDB():
        pass
    