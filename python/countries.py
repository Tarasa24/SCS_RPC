import json
import processes


world_db = None
with open('dbs/states/world.json', 'r') as f:
    world_db = json.load(f)

us_db = None
with open('dbs/states/us.json', 'r') as f:
    us_db = json.load(f)


def ISOcode(country):
    if processes.is_running("eurotrucks2.exe"):
        for e in world_db:
            if country == e.get("name").lower() or country in e.get("name").lower():
                return e.get("alpha")
        else:
            return "??"
    elif processes.is_running("amtrucks.exe"):
        for e in us_db:
            if country == e.get("name").lower() or country in e.get("name").lower():
                return e.get("alpha")
        else:
            return "??"
