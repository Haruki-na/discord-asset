import json

class statusVoiceBot:


    def statusSet(status):
        push = {
            "status": status
        }
        with open("status.json", "w") as status:
            json.dump(push, status, indent=4)
    
    def statusCheck():
        with open("status.json", encoding="utf-8") as set:
            load = set.read()
            loads = json.loads(load)
            status = loads['status']
        if status == True:
            return True
        else:
            return False