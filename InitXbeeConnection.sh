#!/bin/sh
sudo ls -l /dev | grep ttyUSB > dev
python XBeeDetector.py
python XBnetInit.py
