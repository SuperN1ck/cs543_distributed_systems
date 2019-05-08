import os
import nemu
import subprocess
import time
import hyperparameters
from util import get_ip

class WifiAP:
    def __init__(self, id=0, X=None):
        self.node = nemu.Node(forward_X11=X)
        self.id = id

        self.switch = nemu.Switch(
            bandwidth=hyperparameters.max_bandwidth,
            delay=hyperparameters.delay,  
            delay_jitter=hyperparameters.delay_jitter,
            delay_correlation=hyperparameters.delay_correlation,
            loss=hyperparameters.loss)

        self.interface = nemu.NodeInterface(self.node)
        self.ip = get_ip(self.id, 1) # id 1 is reserved for wifi AP
        self.prefix = get_ip(self.id, 0)
        self.interface.add_v4_address(address=self.ip, prefix_len=hyperparameters.prefix_len)
        self.switch.connect(self.interface)

        self.cameras = []

        self.interface.up = True
        self.switch.up = True
    
    def connect(self, camera):
        self.cameras.append(camera)
        self.switch.connect(camera.interface)


