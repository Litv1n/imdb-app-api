import os

try:
    os.system('cmd /k "docker ps"')
except:
    print('could not execute command')
