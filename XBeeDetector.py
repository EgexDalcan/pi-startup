from digi.xbee.devices import XBeeDevice
from digi.xbee.models.mode import OperatingMode
from digi.xbee.packets.common import ATCommPacket
from subprocess import call
import os

Lines = []
call("createdevlist.sh", shell=True)
with open("dev.txt", "r+") as devList:
  Lines = devList.readlines()
lineNo = 1

#Finding the ports with XBees attached
#XBee1
for line in Lines:
  port1 = "tty" + line.split("tty")[1].strip()
  try:
    xbee1 = XBeeDevice(port1,9600)
    xbee1.open(force_settings=True)
    for i in range(0,lineNo):
      Lines.remove(Lines[i])
    break
  except:
    lineNo+=1
#XBee2
for line in Lines:
  port2 = line.split("tty")[1]
  try:
    xbee2=XBeeDevice(port2,9600)
    xbee2.open(force_settings=True)
    break
  except:
    pass
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

#The ports of the XBees (This is the things we want from this script)
xbeePort1 = ""
xbeePort2 = ""

#Checking which are the XBees we want
if(xbee1.get_64bit_addr() == xbeeMac1):
  xbeePort1 = port1
  xbeePort2 = port2
elif(xbee1.get_64bit_addr() == xbeeMac2):
  xbeePort2 = port1
  xbeePort1 = port2

#Preparing the packet that will make the XBees to go to AT mode
#xbee1
frameNo1 = xbee1.get_next_frame_id()
packet1 = ATCommPacket(frameNo1, "AP", parameter=bytearray([OperatingMode.AT_MODE.code]))
out1 = packet1.output(False)
#xbee2
frameNo2 = xbee2.get_next_frame_id()
packet2 = ATCommPacket(frameNo2, "AP", parameter=bytearray([OperatingMode.AT_MODE.code]))
out2 = packet2.output(False)

#Turning the XBees back to AT mode
#xbee1
xbee1.comm_iface.write_frame(out1)
xbee1.close()
#xbee2
xbee2.comm_iface.write_frame(out2)
xbee2.close()