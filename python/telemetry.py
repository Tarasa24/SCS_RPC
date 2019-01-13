import ets2sdk
import closest_city
import processes
from us import us
import pycountry

data = ets2sdk.ets2sdkclient()


def update():
    data.update()


def getVehicle():
    return "{} {}".format(data.truckMake, data.truckModel)


def getVehicleID():
    return data.truckMakeId


def getClosestCity():
    def ISOcode(country):
        if processes.is_running("eurotrucks2.exe"):
            for e in list(pycountry.countries):
                if country in e.name.lower():
                    return e.alpha_2
        elif processes.is_running("amtrucks.exe"):
            return us.get(country.title())
    coord = (data.coordinateX, data.coordinateZ)
    querry = closest_city.ccQuerry(coord)
    city = querry["realName"]
    code = ISOcode(querry["country"])
    return "Close to {} ({})".format(city, code)


def getSpeed():
    data.update()
    speedkmh = round(data.speed * 3.6)
    speedmph = round(speedkmh * 0.62)
    return ["{} km/h".format(speedkmh), "{} mph".format(speedmph)]


def getStatus():
    def getDistance(data):
        distancekm = round(data.routeDistance / 1000)
        distancemil = round(distancekm * 0.62)
        return [str(distancekm), str(distancemil)]
    name = data.trailerName
    weight = round(data.trailerMass / 1000)
    if name is not "":
        return ["{} ({}t) | {} km".format(name, weight, getDistance(data)[0]), "{} ({}t) | {} mil".format(name, weight, getDistance(data)[1])]
    else:
        return ["Freeroaming...", "Freeroaming..."]
