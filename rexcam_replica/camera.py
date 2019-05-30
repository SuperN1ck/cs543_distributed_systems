import argparse

class Camera():

    def __init__(self, id, ip_address, ip_address_wifi_ap):          
        self.id = id
        self.ip_address = ip_address
        self.ip_address_wifi_ap = ip_address_wifi_ap

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run a Camera')
    parser.add_argument('id', type=int, help='id of the camera')
    parser.add_argument('ip', help='IP of the Camera')
    parser.add_argument('wifi_ap_ip', help='IP of the Wifi-AP')

    args = parser.parse_args()
    

