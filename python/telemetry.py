import urllib.request
import json
import closest_city
import us
import pycountry
import sys
import os


def load():
    try:
        with urllib.request.urlopen("http://localhost:25555/api/ets2/telemetry") as url:
            data = json.loads(url.read().decode())
        return data
    except urllib.error.URLError as e:
        os.system('cls')
        print("Ets2Telemetry.exe is not running")

def getGameName():
    data = load()
    return data["game"]["gameName"]


def getVehicle(i=0):
    data = load()
    if i == 0:
        return "{} {}".format(data["truck"]["make"], data["truck"]["model"])
    else:
        return data["truck"]["id"]


def getClosestCity():
    def ISOcode(country):
        if getGameName() == "ETS2":
            for e in list(pycountry.countries):
                if country in e.name.lower():
                    return e.alpha_2
        elif getGameName() == "ATS":
            return us.states.lookup(country).abbr

    data = load()
    coord = (data["truck"]["placement"]["x"], data["truck"]["placement"]["z"])
    querry = closest_city.ccQuerry(coord, getGameName())
    city = querry["realName"]
    code = ISOcode(querry["country"])
    return "Close to {} ({})".format(city, code)


def getSpeed():
    data = load()
    speed = round(data["truck"]["speed"])
    return "{} km/h".format(speed)


def getStatus():
    def getDistance(data):
        distance = round(data["navigation"]["estimatedDistance"] / 1000)
        return "{}km".format(distance)

    data = load()
    name = data["trailer"]["name"]
    weight = round(data["trailer"]["mass"] / 1000)
    if data["game"]["connected"] == False:
        return "Loading up the game..."
    elif data["game"]["paused"]:
        return "Paused..."
    elif name is not "":
        return "{} ({}t) | {}".format(name, weight, getDistance(data))
    else:
        return "Freeroaming..."
