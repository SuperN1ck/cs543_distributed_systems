# cs543_distributed_systems
Repository for group project in CS543 - Distributed Systems @ KAIST, Spring 2019


## Setup
### Pip
Create a virtual environment
```
$ virtualenv -p /usr/bin/python3 env
```
Activate it
```
$ source env/bin/activate
```
First make sure `pip` is up-to-date by upgrading it
```
$ pip install --upgrade pip
```
Then install all requierements requiered for this project
```
$ pip install -r requirements.txt
```

### Setting Up ns-3
Follow the [official tutorial](https://www.nsnam.org/docs/tutorial/singlehtml/index.html#downloading-ns-3-using-git).
This will take some time to download and install the package.

First download the package
```
git clone https://gitlab.com/nsnam/ns-3-allinone.git
cd ns-3-allinone
python download.py
```
Then build it
```
./build.py --enable-examples --enable-tests --enable-sudo
```
Tests (timely) can be run by
```
cd ns-3-dev
./test.py
```
An example can be run by
```
cd ns-3-dev
./waf --run hello-simulator
```
Or to run a python example located in `ns-3-allinone/ns-3-dev/examples/tutorial/` execute
```
./waf --pyrun examples/tutorial/first.py
```
An example using [taps](https://www.nsnam.org/wiki/HOWTO_make_ns-3_interact_with_the_real_world) can be found here
```
./waf --pyrun ../../tap-wifi-virtual-machine.py
```
There is a bug in the code, you have to manually change [line 57](https://www.nsnam.org/doxygen/tap-wifi-virtual-machine_8py_source.html#l00057) to
```
wifiMac = ns.wifi.WifiMacHelper()
```
## Execution
To execute run following in the `ns-3-allinone/ns-3-dev/`-directory
```
./waf --pyrun ../../main.py
```


Check this tomorrow:
https://askubuntu.com/questions/765526/how-to-install-gtk2-0
