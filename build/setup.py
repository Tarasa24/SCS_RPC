import sys
from cx_Freeze import setup, Executable
import os


# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["psutil", "scipy.spatial", "scipy._distributor_init", "scipy.sparse.csgraph._validation"],
                     "excludes": ["scipy.spatial.cKDTree"],
                     "include_files": ["../src/modules", "../src/dbs", "../src/config.json"],
                     "build_exe": "out"}

app = Executable(
    script="../src/app.py",
    base=None,
    icon="scs_ico.ico",
    targetName="SCS_RPC.exe"
    )

status = Executable(
    script="../src/status.py",
    base=None,
    targetName="status.exe"
    )

setup(name="SCS_RPC",
      version="0.1",
      description="Unofficial Open-source Discord Rich Presence for ETS2 and ATS",
      options={"build_exe": build_exe_options},
      executables=[app, status])
