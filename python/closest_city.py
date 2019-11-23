import processes
from scipy import spatial
import json


cities_ets2 = None
with open('dbs/cities/cities_ets2.json', encoding='utf-8') as x:
    cities_ets2 = json.load(x)

cities_ats = None
with open('dbs/cities/cities_ats.json', encoding='utf-8') as y:
    cities_ats = json.load(y)

def chooseJson():
    if processes.is_running("eurotrucks2.exe"):
        cities = []
        for e in cities_ets2["citiesList"]:
            cities.append((float(e["x"]), float(e["z"])))
        return (cities, cities_ets2)
    elif processes.is_running("amtrucks.exe"):
        cities = []
        for e in cities_ats["citiesList"]:
            cities.append((float(e["x"]), float(e["z"])))
        return (cities, cities_ats)


def ccQuerry(coord):
    cities = chooseJson()[0]
    data = chooseJson()[1]
    tree = spatial.KDTree(cities)
    q = tree.query([coord])
    index = q[1][0]
    return data["citiesList"][index]
