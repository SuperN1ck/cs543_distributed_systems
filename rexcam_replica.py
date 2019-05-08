import os
import nemu
import subprocess
import time

from nodes.wifi_ap import WifiAP
from nodes.camera import Camera

xterm = nemu.environ.find_bin("xterm")
X = "DISPLAY" in os.environ and xterm

ap = WifiAP(id=0) # ID
cam = Camera(id=0) # ID

cam.connect(ap)

'''
Camera 0: 10.0.0.1
Camera 1: 10.0.0.2
WifiAP 0: 10.0.0.0

Camera 2: 10.0.1.1
Camera 3: 10.0.1.2
WifiAP 1: 10.0.1.0
'''
