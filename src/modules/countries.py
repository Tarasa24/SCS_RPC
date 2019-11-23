import json
from modules import processes


world_db = None
with open('dbs/states/world.json', 'r') as f:
    world_db = json.load(f)

us_db = None
with open('dbs/states/us.json', 'r') as f:
    us_db = json.load(f)


def ISOcode(country):
    country = country.replace("_", " ")
    if processes.is_running("eurotrucks2.exe"):
        for e in world_db:
            db_name = e.get("name").lower() 
            if country == db_name or country in db_name:
                return e.get("alpha")
        else:
            return "??"
    elif processes.is_running("amtrucks.exe"):
        for e in us_db:
            db_name = e.get("name").lower() 
            if country == db_name or country in db_name:
                return e.get("alpha")
        else:
            return "??"
