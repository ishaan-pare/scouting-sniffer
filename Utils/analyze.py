from Utils import global_constants
from Utils import process

#it return True only
def __Check__():
    print("Port Scan Detector Started Successfully :)")
    a = True
    while(a):
        if(process.__TCPpacketFreq__(global_constants.TIME,global_constants.T4) > global_constants.THRESHOLD):
            return True

