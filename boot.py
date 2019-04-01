# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

#from iterate import iterative_lights
#iterative_lights()

#from scroll import scroll
#scroll("TIM")

from waves import waves
waves()

#from iterate import iterative_lights
#iterative_lights()
