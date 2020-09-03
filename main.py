# -*- coding: utf-8 -*-
"""
@author: Ishaan Trivedi
"""

import os
from time import sleep, strftime, localtime
from sys import exit
import SendMessageFunction


with open("OPERATION.txt", "r") as dev:
    line = dev.readlines()
    global IP_ADRESS
    IP_ADRESS = line[3].rstrip("\n")
    global DEV_NAME
    DEV_NAME = line[1].rstrip("\n")
    global RECIPIENT
    RECIPIENT = line[6].rstrip("\n")

discon_count = 0

with open("STATUS.txt", "r") as stat:
    data = stat.read()
    if "LEFT HOME" in data:
        print("Not At Home")
        response = os.popen(f"ping {IP_ADRESS} -w 20").read()
        if not "Received = 0" in response:
            print(f"{DEV_NAME} Connected")
            ti = strftime("%H:%M", localtime())
            with open("STATUS.txt", "w") as stat:
                stat.write(f"BACK HOME at {ti}")
            SendMessageFunction.initialize()

            SendMessageFunction.SendMessage(RECIPIENT, f"Back Home at {ti}")

            SendMessageFunction.exit()
            exit(0)
        else:
            exit(1)


for i in range(0, 20):

    response = os.popen(f"ping {IP_ADRESS} -w 20").read()
    if "Received = 0" in response:
        print(f"{DEV_NAME} Not Connected")
        discon_count = discon_count + 1
        
        if discon_count > 3:
            print("LEFT HOME")
            ti = strftime("%H:%M", localtime())
            with open("STATUS.txt", "w") as stat:
                stat.write(f"LEFT HOME at {ti}")
            SendMessageFunction.initialize()

            SendMessageFunction.SendMessage(RECIPIENT, f"Left Home at {ti}")

            SendMessageFunction.exit()
            exit(0)

    else:
        print(f"{DEV_NAME} Connected")
        discon_count = 0

with open("STATUS.txt", "w") as stat:
    stat.write("AT HOME")

exit()
