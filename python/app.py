from pypresence import Presence
import telemetry
import processes
from time import time, sleep
import sys
from colorama import Fore, ansi, init

init(autoreset=True)

class base:
    game = "  "
    km_mil = 0
    vehicle_list = ["daf", "iveco", "man", "mercedes-benz",
                    "renault", "scania", "volvo", "peterbilt", "kenworth"]
    start_time = int(time())


def client_id():
    print(ansi.clear_screen())
    if processes.is_running("eurotrucks2.exe"):
        base.game = "ets2"
        base.km_mil = 0
        return '529016610137309184'

    elif processes.is_running("amtrucks.exe"):
        base.game = "ats"
        base.km_mil = 1
        return '529069002874421249'
    else:
        print(Fore.RED + "Sim is not running ")
        input("Press any key when ready...\n")
        return client_id()


RPC = Presence(client_id())
RPC.connect()

telemetry.update()
while True:
    print(ansi.clear_screen())
    print("RPC pipe: " + Fore.GREEN + "connected")
    print("SDK: " + Fore.GREEN + "loaded v" + telemetry.sdkVersion())
    print("Game: " + Fore.GREEN + "ready v" + telemetry.gameVersion())
    print(20 * "=")

    vehicle = telemetry.getVehicle()
    if vehicle not in base.vehicle_list:
        vehicle = "unknown"

    activity = {
        "details": telemetry.getStatus()[base.km_mil],
        "state": telemetry.getClosestCity(),
        "start": base.start_time,
        "assets": {
            "small_text": "{} | {}".format(telemetry.getVehicleFull(), telemetry.getSpeed()[base.km_mil]),
            "small_image": vehicle,
            "large_image": base.game
        }
    }
    RPC.update(details=activity["details"],
               state=activity["state"],
               start=activity["start"],
               small_text=activity["assets"]["small_text"],
               small_image=activity["assets"]["small_image"],
               large_image=activity["assets"]["large_image"])
    print(activity["details"])
    print(activity["assets"]["small_text"])
    print(activity["state"])

    sleep(15)  # Can only update rich presence every 15 seconds
    telemetry.update()
