import rpc
from time import time, sleep
import telemetry
import os
import sys
import processes

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def client_id():
    os.system('cls')
    game = ""
    if processes.is_running("eurotrucks2.exe"):
        return '529016610137309184'

    elif processes.is_running("amtrucks.exe"):
        return '529069002874421249'
    else:
        input("{}Sim is not running.{} Press any key when ready...\n".format(bcolors.FAIL, bcolors.ENDC))
        return client_id()         

rpc_obj = rpc.DiscordIpcClient.for_platform(client_id())
start_time = int(time())

vehicle_list = ["daf", "iveco", "man", "mercedes", "renault", "scania", "volvo", "peterbilt", "kenworth"]
while True:
    os.system('cls')
    print("RPC pipe: {}connected!{}".format(bcolors.OKGREEN, bcolors.ENDC))
    print("Simulator: {}running...{}\n".format(bcolors.OKGREEN, bcolors.ENDC))

    vehicle = telemetry.getVehicle(1)
    if vehicle not in vehicle_list:
        vehicle = "unknown"

    activity = {
        "details": telemetry.getStatus(),
        "state": telemetry.getClosestCity(),
        "timestamps": {
            "start": start_time
        },
        "assets": {
            "small_text": "{} | {}".format(telemetry.getVehicle(), telemetry.getSpeed()),
            "small_image": telemetry.getVehicle(1),
            "large_image": telemetry.getGameName().lower()
        }
    }
    rpc_obj.set_activity(activity)
    print(activity["details"])
    print(activity["assets"]["small_text"])
    print(activity["state"])

    sleep(15)  # Can only update rich presence every 15 seconds
