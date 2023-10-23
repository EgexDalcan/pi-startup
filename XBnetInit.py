import os
import subprocess
import time
import XBeeReboot

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
  XBeeReboot(port1)
  p1 = subprocess.Popen(["sudo", "xbnet", port1, "tun"])

if(port2 != "none"):
  XBeeReboot(port1)
  p2 = subprocess.Popen(["sudo", "xbnet", port2, "tun"])
  
time.sleep(10)

if(port1 != "none"):
  try:
    subprocess.run(["sudo", "ifconfig", "xbnet0", ip1, "up"])
  except:
    subprocess.run(["sudo", "reboot"])

if(port2 != "none"):
  try:
    subprocess.run(["sudo", "ifconfig", "xbnet1", ip2, "up"])
  except:
    subprocess.run(["sudo", "reboot"])

fport.close()
fip.close()