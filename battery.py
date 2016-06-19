from objc_util import *
from time import sleep
from datetime import datetime
import requests
from speech import say
import sound
import os
import urllib

urlprefix = "http://example.com/battery"

UIDevice = ObjCClass("UIDevice")
UIDevice.currentDevice().setBatteryMonitoringEnabled(True)

if not os.path.exists("10silence.mp3"):
    urllib.request.urlretrieve(urlprefix + "10silence.mp3", "10silence.mp3")
player = sound.Player("10silence.mp3")
player.number_of_loops = -1
player.play()

while True:
    req = requests.request("GET", urlprefix +str(UIDevice.currentDevice().identifierForVendor().UUIDString()) + "/" +
  (datetime.now().isoformat()) + "/" + str(UIDevice.currentDevice().batteryLevel()))
    sleep(5)

player.stop()
