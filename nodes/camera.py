import os
import nemu
import subprocess
import time
import hyperparameters
from util import get_ip

class Camera():
    def __init__(self, id=0, X=None):
        self.node = nemu.Node(forward_X11=X)
        self.interface = nemu.NodeInterface(self.node)
        self.id = id
    
    def connect(self, wifi_ap):
        wifi_ap.connect(self)
        self.ip = get_ip(wifi_ap.id, self.id + 2) # id 1 is reserved for wifi AP
        self.interface.add_v4_address(address=self.ip, prefix_len=hyperparameters.prefix_len)
        self.node.add_route(prefix=wifi_ap.prefix, prefix_len=hyperparameters.prefix_len, nexthop=wifi_ap.ip)
