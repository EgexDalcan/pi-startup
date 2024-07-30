import os
import subprocess
import time
import XBeeReboot

try:
  fport = open("PortList", "r")
  os.remove("PortList")
except:
  raise Exception("PortList not found or failed to open. Probably problem in XBeeDetector.py")
 
try:
  fip = open("IPList", "r")
except:
  raise Exception("IPList not found or failed to open.")

port1 = fport.readline().strip()
port2 = fport.readline().strip()
ip1 = fip.readline().strip()
ip2 = fip.readline().strip()
if(port1 == port2):
  port2 = "none"

if(port1 != "none"):
  x = XBeeReboot.XBeeReboot(port1)
  x.reset()
  p1 = subprocess.Popen(["sudo", "xbnet", port1, "tun"])

if(port2 != "none"):
  y = XBeeReboot.XBeeReboot(port2)
  y.reset()
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