from modules import scs2sdk
from modules import closest_city
from modules import processes
from modules.countries import ISOcode

data = scs2sdk.scssdkclient()


def update():
    data.update()


def gameVersion():
    return "{}.{}".format(str(data.ets2_version_major), str(data.ets2_version_minor))


def sdkVersion():
    return str(data.ets2_telemetry_plugin_revision)


def getVehicleFull():
    return "{} {}".format(data.truckMake, data.truckModel)


def getVehicle():
    return data.truckMake.lower()


def getClosestCity():
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
    if name == "":
        name = "Empty"
    weight = data.trailerMass // 1000
    return ["{} ({}t) | {} km".format(name, weight, getDistance(data)[0]), "{} ({}t) | {} mil".format(name, weight, getDistance(data)[1])]
