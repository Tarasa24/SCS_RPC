import processes
from scipy import spatial
import json


def chooseJson():
    if processes.is_running("eurotrucks2.exe"):
        with open('dbs/cities/cities_ets2.json', encoding='utf-8') as x:
            data = json.load(x)
            cities = []
            for e in data["citiesList"]:
                cities.append((float(e["x"]), float(e["z"])))
            return (cities, data)
    elif processes.is_running("amtrucks.exe"):
        with open('dbs/cities/cities_ats.json', encoding='utf-8') as y:
            data = json.load(y)
            cities = []
            for e in data["citiesList"]:
                cities.append((float(e["x"]), float(e["z"])))
            return (cities, data)


def ccQuerry(coord):
    cities = chooseJson()[0]
    data = chooseJson()[1]
    tree = spatial.KDTree(cities)
    q = tree.query([coord])
    index = q[1][0]
    return data["citiesList"][index]
