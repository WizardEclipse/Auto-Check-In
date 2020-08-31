Auto "Left Home" Message Sender
====

Licensing Information: See License.txt
---

Program Overview
---
### Usage:

- Auto "Left Home" Message Sender records wether user is 'AT HOME', has 'LEFT HOME' and when, or is now 'BACK HOME'.
- The program proceeds to send a WhatsApp message to a reciever when the User leaves home and the time, and when they get back.

- Network Scanning is done by pinging an ipadress 20 times every 20 minutes.
- The WhatsApp sending is handled through the Selenium library

File List
---

```
.:

README.md
-Read me

STATUS.txt              
-Stores Status of Device, "AT HOME", "LEFT HOME", "BACK HOME" and time of instance

OPERATION.txt
-Sets up the Device Name, IP Adress and WhatsApp recipient

Automation.bat          
-batch file that runs main.py, enables Automation when used with the Windows Task Scheduler

net_con.py              
-Code for scanning the home network for an ip adress using the OS' ipconfig command

SendMessageFuntion.py   
-Code for sending a WhatsApp message, broken into the initialize, SendMessage, and exit functions. To be used one after another respectively in another python file

main.py                 
-Integrates the net_con.py and SendMessageFuntion.py files
```

```
/chromedriver_win32:

chromedriver.exe

/data

```

Setup
---
Requirements
- Made and tested for Windows OS. (Mac and Linux OS Support coming soon)
- [Selenium Webdriver](https://www.selenium.dev/)
- `pip install selenium`

Setting up
- Install Manually by Downloading source code
- Add Automation.bat file to Windows Task Scheduler, to repeat every (20 minutes reccomended)
- Carefully Edit the OPERATION.txt file, add the IP address of the device to be monitored, it's Name, and the WhatsApp recipient of the check-in Messages.




Known Bugs and Notes
---
1. On the first run of the program, WhatsApp web will require you to scan a QR code through your phone
2. The SendMessage function can sometimes timeout if theres an unstable internet connection, or the website takes too long. Feel free to optimise the wait times set by `time.sleep` in the SendMessageFunction as per your internet speed.

Roadmap
---
In the future, I hope to find alternate/optimised uses for the sode made for this project, including:
- A 'Smart-Home' system that uses Arduinos and the `net-con.py` code to turn on lights when the user enters their home.
- A WhatsApp module for business use, aimed at sending mass marketing messages by tweaking the `SendMessagefunction.py` code


Author
---
### Ishaan Trivedi

All other known bugs and fixes can be sent to ishaan.t14@gmail.com

Reported bugs/fixed will be submitted to correction.
