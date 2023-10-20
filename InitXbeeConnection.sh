#!/bin/sh
sudo ls -l /dev | grep ttyUSB > dev.txt
python XBeeDetector.py
python XBnetInit.py
