import os
import sys
import time
from time import sleep
import requests
from os import system



try:
	request = requests.get("https://www.google.com/search?q=zspoof.com", timeout=3)
except (requests.ConnectionError, requests.Timeout) as exception:
    print("[!] Oops, It looks like you have no Internet [!]")
    sys.exit()

import requests

R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'

def hprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8.0 / 100)

logo = """


\033[1;32m  _________  ____   ___   ___  _____ 
\033[1;32m|__  / ___||  _ \ / _ \ / _ \|  ___|
\033[1;32m  / /\___ \| |_) | | | | | | | |_   
\033[1;32m / /_ ___) |  __/| |_| | |_| |  _|  
\033[1;32m/____|____/|_|    \___/ \___/|_|   


\033[1;36m [\033[1;37m+\033[1;36m]\033[1;32m DEVELOPED BY ZSPOOF.COM \033[1;31m(\033[1;33m ZSPOOF \033[1;31m)

\033[1;36m [\033[1;37m+\033[1;36m]\033[1;32m MADE IN \033[1;31m(\033[1;33mNEPAL\033[1;31m)
"""
system("clear")
print (logo)
hprint(G + ' Starting Spoofy for Sending Emails ...')
sleep(2)
print ("")
license = input(G + " Enter License Key" + C + " --> " + Y)
print ("")
username = input(G + " Enter Username" + C + " --> " + Y)
print ("")
caller_id  = input(G + " Enter New Caller ID" + C + " --> " + Y)
print("")

files = {
    'license': (None, license),
    'username': (None, username),
    'caller_id': (None, caller_id),
    'submit': (None, "submit"),
}
response = requests.post('https://call.zspoof.com', files=files)
hprint(C + ' Changing Caller ID of  ' + username + ' ...')
print("")
print(G + " " + response.text + "Callerid Changed")
print("")

