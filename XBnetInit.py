import os
import subprocess
import time

try:
  fport = open("PortList.txt", "r")
  os.remove("PortList.txt")
except:
  raise Exception("PortList.txt not found or failed to open. Probably problem in XBeeDetector.py")
 
try:
  fip = open("IPList.txt", "r")
except:
  raise Exception("IPList.txt not found or failed to open.")

port1 = fport.readline().strip()
port2 = fport.readline().strip()
ip1 = fip.readline().strip()
ip2 = fip.readline().strip()

if(port1 != "none"):
  p1 = subprocess.Popen(["xbnet", port1, "tun"])

if(port2 != "none"):
  p2 = subprocess.Popen(["xbnet", port2, "tun"])
  
time.sleep(10)

if(port1 != "none"):
  subprocess.run(["sudo", "ifconfig", "xbnet0", ip1, "up"])

if(port2 != "none"):
  subprocess.run(["sudo", "ifconfig", "xbnet1", ip2, "up"])

fport.close()
fip.close()