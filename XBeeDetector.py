from digi.xbee.devices import XBeeDevice
import os

Lines = []
#The ports of the XBees (This is the things we want from this script)
xbeePort1 = ""
xbeePort2 = ""
port1 = "none"
port2 = "none"
with open("dev.txt", "r+") as devList:
  Lines = devList.readlines()
lineNo = 0

#Finding the ports with XBees attached
#XBee1
for line in Lines:
  port1 = "/dev/tty" + line.split("tty")[1].strip()
  try:
    xbee1 = XBeeDevice(port1,9600)
    xbee1.open(force_settings=True)
    print("XBee1 found!")
    for i in range(0,lineNo):
      Lines.remove(Lines[i])
    break
  except:
    lineNo+=1
  print("Failed to find XBee1")
  port1 = 'none'
#XBee2
for line in Lines:
  port2 = "/dev/tty" + line.split("tty")[1].strip()
  try:
    xbee2=XBeeDevice(port2,9600)
    xbee2.open(force_settings=True)
    print("XBee2 found!")
    break
  except:
    pass
  print("Failed to find XBee2")
  port2 = 'none'
#deleting the port list file
try:
  os.remove("dev.txt")
except:
  pass

#The Mac Adresses of the XBees
with open("MacAdresses.txt", "r") as adressList:
  adresses = adressList.readlines()
xbeeMac1 = adresses[0].strip()
xbeeMac2 = adresses[1].strip()

#Checking which are the XBees we want and putting them in a file
try:
  f = open("PortList.txt", "x")
except:
  os.remove("PortList.txt")
  f = open("PortList.txt", "x")

if(port1 == "none"):
  print("Could not find XBee1")
  f.write("none\n")
elif(str(xbee1.get_64bit_addr()) == xbeeMac1):
  xbeePort1 = port1
  print(xbeePort1)
  f.write(xbeePort1 + '\n')
elif(str(xbee1.get_64bit_addr()) == xbeeMac2):
  xbeePort2 = port1
  print(xbeePort2)
  f.write(xbeePort2 + '\n')
else:
  print('Could not find matching MAC address for XBee1.')
  f.write("none\n")
  if(port1 != 'none'):
    print('An XBee found on: ' + port1 + ' with MAC address: ' + str(xbee1.get_64bit_addr()))

if(port2 == "none"):
  print("Could not find XBee2")
  f.write("none\n")
elif((str(xbee2.get_64bit_addr()) == xbeeMac1) & (xbeePort1 != port1)):
  xbeePort2 = port2
  print(xbeePort2)
  f.write(xbeePort2 + '\n')
elif((str(xbee2.get_64bit_addr()) == xbeeMac2) & (xbeePort1 != port2)):
  xbeePort1 = port2
  print(xbeePort1)
  f.write(xbeePort1 + '\n')
else:
  print('Could not find matching MAC address for XBee2.')
  f.write("none\n")
  if(port2 != 'none'):
    print('An XBee found on: ' + port2 + ' with MAC address: ' + str(xbee2.get_64bit_addr()))

if(port1 != "none"):
  xbee1.close()
if(port2 != "none"):
  xbee2.close()
f.close()
