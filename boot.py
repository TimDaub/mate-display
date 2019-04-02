import network
import json

from server import serve

def connect(name, pw, hostname):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        print("Setting hostname to", hostname)
        sta_if.config(dhcp_hostname=hostname)
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
    serve(params[0])
