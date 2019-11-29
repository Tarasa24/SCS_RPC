from colorama import Fore, ansi, init
from time import sleep
from modules import telemetry

init(autoreset=True)
telemetry.update()
closest = telemetry.getClosestCity()


while True:
  print(ansi.clear_screen())
  telemetry.update()

  print(Fore.CYAN + "SDK: " + Fore.RESET + telemetry.sdkVersion())
  print(Fore.CYAN + "Game: " + Fore.RESET + telemetry.gameVersion())
  print(Fore.CYAN + "Truck manufacturer: " + Fore.RESET + telemetry.getVehicle())
  print(Fore.CYAN + "Truck fullname: " + Fore.RESET + telemetry.getVehicleFull())
  print(Fore.CYAN + "Speed k/mh: " + Fore.RESET + telemetry.getSpeed()[0])
  print(Fore.CYAN + "Speed mph: " + Fore.RESET + telemetry.getSpeed()[1])
  print(Fore.CYAN + "Status t/km: " + Fore.RESET + telemetry.getStatus()[0])
  print(Fore.CYAN + "Status t/mil: " + Fore.RESET + telemetry.getStatus()[1])
  print(Fore.CYAN + "Closest city: " + Fore.RESET + closest)

  sleep(1)
  closest = telemetry.getClosestCity()