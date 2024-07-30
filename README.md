# pi-startup
Scripts for the startup of the raspberrypis in the field.
These scripts will be used by the raspberrypis connected to the different stations to initialize
their settings. This will ensure they will have;
a) Proper connection with their XBee Radios.
b) Proper connection with their respective central station XBees and the internet through central VPN over XBnet.
  1) This will be done by IP addresses assigned to the tunneling XBnet devices.
  2) IP routing to ensure internet connection.
To use, add the MacAdresses of the wired XBees and add the IPs for the interfaces. If MacAddresses are replaced with "none" in the config files the script will use every XBee it finds and will assign them randomly.
