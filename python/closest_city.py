import processes
from scipy import spatial
import json
import os

def names(d):
    names_list = []
    for e in d["citiesList"]:
        names_list.append(e.get("realName"))
    return names_list


cities_ets2 = None
with open('dbs/cities/cities_ets2.json', encoding='utf-8') as x:
    cities_ets2 = json.load(x)
    names_ets2 = names(cities_ets2)

    for filename in os.listdir('dbs/cities/usr_ets2'):
        if filename[-5:] == ".json":
            with open('dbs/cities/usr_ets2/' + filename, encoding='utf-8') as z:
                data = json.load(z)
                for e in data["citiesList"]:
                    if e.get("realName") in names_ets2:
                        cities_ets2["citiesList"][names_ets2.index(e.get("realName"))] = e
                    else:
                        cities_ets2["citiesList"].append(e)

cities_ats = None
with open('dbs/cities/cities_ats.json', encoding='utf-8') as y:
    cities_ats = json.load(y)
    names_ats = names(cities_ats)

    for filename in os.listdir('dbs/cities/usr_ats'):
        if filename[-5:] == ".json":
            with open('dbs/cities/usr_ats/' + filename, encoding='utf-8') as z:
                data = json.load(z)
                for e in data["citiesList"]:
                    if e.get("realName") in names_ats:
                        cities_ats["citiesList"][names_ats.index(e.get("realName"))] = e
                    else:
                        cities_ats["citiesList"].append(e)

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
