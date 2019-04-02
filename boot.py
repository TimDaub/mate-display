import network
import json

def connect(name, pw):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(name, pw)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

def load_config():
    with open('config.json') as json_file:
        return json.load(json_file)

def boot():
    config = load_config()
    connect(config["WIFI"]["name"], config["WIFI"]["pw"])

boot()
