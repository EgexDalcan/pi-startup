from digi.xbee.devices import XBeeDevice
import os

Lines = []
#The ports of the XBees (This is the things we want from this script)
xbeePort1 = ""
xbeePort2 = ""
port1 = "none"
port2 = "none"
with open("dev", "r+") as devList:
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
  os.remove("dev")
except:
  pass

#The Mac Addresses of the XBees
with open("MacAddresses", "r") as addressList:
  addresses = addressList.readlines()
xbeeMac1 = addresses[0].strip()
xbeeMac2 = addresses[1].strip()

#Checking which are the XBees we want and putting them in a file
try:
  f = open("PortList", "x")
except:
  os.remove("PortList")
  f = open("PortList", "x")

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

#If no MacAddress is specified in MacAddresses but devices are still found, just pu them in the order you found them.
if((xbeeMac1 == "none" and xbeeMac2 == "none") and (port1 != "none" or port2 != "none")):
  print("No MacAddresses specified, but found XBee devices, putting XBee devices in random order.")
  if(port1 != 'none'):
    print('An XBee found on: ' + port1 + ' with MAC address: ' + str(xbee1.get_64bit_addr()))
  if(port2 != 'none'):
    print('An XBee found on: ' + port2 + ' with MAC address: ' + str(xbee2.get_64bit_addr()))
  if(port1 == port2):
    port2 = "none"
  xbeePort1 = port1
  xbeePort2 = port2
  f.truncate(0)
  f.seek(0)
  f.write(xbeePort1 + '\n')
  f.write(xbeePort2 + '\n')

if(port1 != "none"):
  xbee1.close()
if(port2 != "none"):
  xbee2.close()
f.close()
