from scipy import spatial
import json
import telemetry

def chooseJson(game):
    if game == "ETS2":
        with open('cities/ETS2_cities.json', encoding='utf-8') as x:
            data = json.load(x)
            cities = []
            for e in data["citiesList"]:
                cities.append((float(e["x"]),float(e["z"])))
            return (cities,data)
    elif game == "ATS":
        with open('cities/ATS_cities.json', encoding='utf-8') as y:
            data = json.load(y)
            cities = []
            for e in data["citiesList"]:
                cities.append((float(e["x"]),float(e["z"])))
            return (cities,data)

def ccQuerry(coord, game):
    cities = chooseJson(game)[0]
    data = chooseJson(game)[1]
    tree = spatial.KDTree(cities)
    q = tree.query([coord])
    index = q[1][0]
    return data["citiesList"][index]