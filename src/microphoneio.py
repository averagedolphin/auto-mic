from pyaudio import *

def initMicrophoneIo():
    pass

import pyaudio

def getaudiodevices():
    returnee = ""
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        returnee.append(p.get_device_info_by_index(i).get('name'))
    return returnee