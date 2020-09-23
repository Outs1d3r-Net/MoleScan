#!/usr/bin/env python3

import platform
import socket
import time
import os

#===> COLOR TABLE
#Purple = \033[95m
#Red    = \033[91m
#Blue   = \033[94m
#Green  = \033[92m
#White  = \033[0m
#WhiteB = \033[1m

#===> VARIALES
startTime = time.time() # COUNTER TIME
s = socket.socket()     # CREATE SOCKET
oPP = []                # List for open ports
ir = 70                 # Initial Range port
cr = ir                 # Current Range port
fr = 140              # Final Range port

iP = input('Set the Target>>> ') # Get the target

## GET PLATFORM
if 'Win' in platform.system():
    cTs = 'cls'
else:
    cTs = 'clear'

#===> FUNCTIONS
def Banner():
    print('\033[1m{*}==>\t\t[*] MOLE SCAN [*]')
    print('\033[1m{*}==>\t\t(Simple tcp scan running python.)')
    print('\033[1m{*}==>\t\tCreate: https://github.com/Outs1d3r-NET/MoleScan\n')
    print('\033[95m Runing the scan in target:','\033[91m',iP)
    global oPP
    print("\033[94m Ports Open:","\033[92m",' '.join(oPP))

def c_s(): # CLOSE AND CREATE SOCKET
    global s
    s.close()
    s = socket.socket()


#===> START
while cr != fr:

    conn = s.connect_ex((iP, cr))

    if (conn == 0):
        oPP.append(str(cr))
        cr += 1
        c_s()

    else:
        os.system(cTs) # clear The screen
        Banner()
        print('\033[0m Scanning port number:',str(cr))
        cr += 1

#===> END
os.system(cTs)
print('\033[1m{*}==>\t\t[*] MOLE SCAN [*]')
print('\033[1m{*}==>\t\t(Simple tcp scan running python.)')
print('\033[1m{*}==>\t\tCreate: https://github.com/Outs1d3r-NET/MoleScan\n')
print("\033[92m\t{*} End the scan ! {*}")
print("\033[95m\tTarget IP = ","\033[91m",iP)
print("\033[94m\tOpen Ports = ","\033[92m",' '.join(oPP))
print('\033[0m\tTime taken = ', time.time() - startTime),"\n"
