import json
from paste import Paste

class DataManager:
    def saveToFile(p: Paste, filename:str):
        f = open("pastes/{}".format(filename), 'w')
        f.write(json.dumps(p.__dict__))
        f.close()

    
    def saveToDB():
        pass