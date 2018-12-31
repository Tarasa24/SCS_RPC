<center>
<img align="left" src="https://cdn.discordapp.com/app-assets/529016610137309184/529052463643230211.png">
<h1>SCS Discord Rich Presence</h1>
Euro Truck simulator 2 & American Truck simulator
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
This project is simple discord rich presence for SCS games ETS2 and ATS (possibly more in the future).

Here is quick preview:

![cmd_view](https://i.imgur.com/bgJTTS2.png) ![Discord Rich Presence](https://i.imgur.com/nyazDBN.png)
	
## Technologies
Project is created with:
* [python-discord-rpc](https://github.com/suclearnub/python-discord-rpc) - outdated, yet still functional
* [ETS2 Log to Coordinates](https://github.com/Koenvh1/ETS2-City-Coordinate-Retriever) - cities.json
* [ETS2 Telemetry Web Server 3.2.5](https://github.com/Funbit/ets2-telemetry-server) - api

## Requirements and Setup
Until is this project **entirely written in python and not converted to exe**, python itself and dependencies must be **installed manually**.

[Python](https://www.python.org/) 🐍
```
$ cd ../SCS_RPC
$ pip install -r requirements.txt
```

## Execution
Simply run **run_me.bat**

## Contributing
Take a look at [example api json](https://github.com/Tarasa24/scs_rpc/blob/master/server/Ets2TestTelemetry.json). If you have any nice idea how to utilize this data even more, hit me up on discord: **Tarasa24**#1761

.

###### Acknowledgement
I am not related to the company **SCS software s.r.o.** in any sense. This project is non-profit and open source. This project represents funbase both of SCS software and Discord.
Any problems relating use of company name and/or their logo, will be resolved asap. I don't really want deal with **any** legal disputes regarding this project. Thank you for understanding.