# -*- coding: utf-8 -*-

import pyjokes
import time
from plyer import notification

while True:
    var = pyjokes.get_joke()
    print(var)
    notification.notify(title = "Here's a joke for U", message=var,
                        # displaying time
                        timeout=5,
                        app_icon = None)
    time.sleep(30) #Displays desktop notifications after every 30 seconds
    