'''
Module      :   hardware
Description :   Abstraction layer to hardwares. Makes use of GPIO on the pi and provides a meaningful semantic. There should
                not be any business logic here. An example class would be NotificationLED and a method could be blink() which
                internally uses GPIO calls to turn on and turn off the LED after a second. There must not be any GPIO calls
                directly made outside of this library, instead other parts of the code can make use of the classes here to
                operate the hardware.
Author : Hari and Kanika
'''
