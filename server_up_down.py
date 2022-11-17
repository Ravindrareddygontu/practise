
import subprocess
import time
import os

def identifier():
 IP_ADDRESS = ["8.8.8.8"]
 t = 5
 while t>0:
    for ip in IP_ADDRESS:
      ping = subprocess.Popen(['ping',ip])
      status_change = False
      status = 0
      ping.wait()
      if ping.poll():
        status_change = True
        status = 1
      else: 
        status_change = True
        status= 0
      if status_change:
        if status ==1:
          print(ip," went down")
        else:
          print(ip, " came up")
##    time.sleep(1)
    t -= 1


identifier()
