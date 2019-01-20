<center>
<img align="left" src="https://cdn.discordapp.com/app-assets/529016610137309184/529052463643230211.png">
<h1>SCS Discord Rich Presence</h1>
Euro Truck Simulator 2 & American Truck Simulator
</center>
</br>


___
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Requirements and Setup](#requirements-and-setup)
* [Execution](#execution)
* [Contributing](#contributing)

## General info
This project is simple discord rich presence for SCS software games ETS2 and ATS (possibly more in the future 🤞).

Project is bound on json files in folder *cities*. Don't move individual executables / python scripts from respective folders.

Here is quick preview:

![cmd_view](https://i.imgur.com/bgJTTS2.png) ![Discord Rich Presence](https://i.imgur.com/nyazDBN.png)
![cmd_view ATS](https://i.imgur.com/hpABirQ.png) ![Discord Rich Presence ATS](https://i.imgur.com/em4T5Th.png)

## Technologies
Project is created with:
* <a href="https://github.com/suclearnub/python-discord-rpc" target="_blank">python-discord-rpc</a>
* <a href="https://github.com/Koenvh1/ETS2-City-Coordinate-Retriever" target="_blank">ETS2 Log to Coordinates</a>
* <a href="https://github.com/nlhans/ets2-sdk-plugin" target="_blank">SDK plugin</a>
* <a href="https://github.com/jurkov/ets2-sdk-python-plugin" target="_blank">SDK python client</a>
* <a href="https://github.com/pyinstaller/pyinstaller" target="_blank">PyInstaller</a>

## Requirements and Setup
You need to download <a href="https://github.com/nlhans/ets2-sdk-plugin/releases" target="_blank">latest release</a> of SDK plugin and put .dll to the folder as described below.

```
..\steamapps\common\<desired simualtor>\bin\win_x64\plugins
or
..\steamapps\common\<desired simualtor>\bin\win_x86\plugins
```
___
**Only if you are planning to run python scrip**, you will need: Python itself and dependencies.

[Python](https://www.python.org/) 🐍
```
$ cd ../SCS_RPC/python
$ pip install -r _requirements.txt
```

## Execution
Simply run **SCS_RPC.exe**

Alternatively run **py.bat** when using Python (batch file is used because of working directory)

## Contributing
Take a look at <a href="https://github.com/Funbit/ets2-telemetry-server/blob/master/server/Ets2TestTelemetry.json" target="_blank">example json</a>. If you have any idea how to nicely utilize this data even more, hit me up on discord: **Tarasa24**#1761

.

###### Acknowledgement
I am not related to the company **SCS software s.r.o.** in any sense. This project is non-profit and open source. This project represents funbase both of SCS software and Discord.
Any problems relating use of company name and/or their logo, will be resolved asap. I don't really want deal with **any** legal disputes regarding this project. Thank you for understanding.
