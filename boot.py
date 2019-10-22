import json
import network
import _thread

from server import serve
from clear import main as clear

def connect(name, pw, hostname):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        #print("Setting hostname to", hostname)
        # NOTE: As this function seems to brick the boot, we now set the host
        # name manually in the fritz.box
        #sta_if.config(dhcp_hostname=hostname)
        sta_if.connect(name, pw)
        while not sta_if.isconnected():
            pass
    params = sta_if.ifconfig()
    print('network config:', params)
    return params

def load_config():
    with open('config.json') as json_file:
        return json.load(json_file)

def boot():
    config = load_config()
    params = connect(
        config["WIFI"]["name"],
        config["WIFI"]["pw"],
        config["hostname"]
    )

    clear("ffffff")
    _thread.start_new_thread(serve, (params[0], config["display"]))

boot()
