import psutil
import os

def is_running(name):
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name'])
        except psutil.NoSuchProcess:
            pass
        else:
            if pinfo["name"] == name:
                return True
    return False

def run_process(path):
    os.startfile(os.getcwd() + path)
