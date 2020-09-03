# -*- coding: utf-8 -*-
"""
@author: Ishaan Trivedi
"""


import os
from time import sleep
from sys import exit

with open("DEVICE.txt", "r") as dev:
    line = dev.readlines()
    IP_ADRESS = line[4]
    DEV_NAME = line[2]

discon_count = 0

with open("STATUS.txt", "r") as stat:
    data = stat.read()
    if "LEFT HOME" in data:
        print("Not At Home")
        exit(1)


for i in range(0, 20):

    response = os.popen(f"ping {IP_ADRESS} -w 20").read()
    if "Received = 0" in response:
        print(f"{IP_ADRESS} Not Connected")
        discon_count = discon_count + 1
        
        if discon_count > 3:
            print("LEFT HOME")
            with open("STATUS.txt", "w") as stat:
                stat.write("LEFT HOME")
            #Call potential WhatApp functions here
            exit(0)

    else:
        print(f"{IP_ADRESS} Connected")
        discon_count = 0

with open("STATUS.txt", "w") as stat:
    stat.write("AT HOME")


# CONDUCTING TESTS
#       - All loops work fine
#       - Buffer of 4 failed pings (of 4 packages each, 20 ms timeout) before device declared as left Home
# Performance Times
#       - Best case shortest time
#           - called after left home. Immediate exit
#       - Regular case shortest time
#           - called with sceduler after it has already left
#           - 0:20 minutes
#       - Worst case shortest time
#           - pinging all 20 times
#           - 1:03 minutes
#
