"""
    Utility Module
    
    Task    -   Processed the data obtain by tcpStat() function in mon module 
                and calculate the frequancy of packet recived by formula
                frequency = (recieved packet at time t0 - recived packet at time (t0+t))/2

    module contains     -   TCPpacketFreq(t,s)
                            *this will take 2 variables t which is time by which we want to 
                            calculate number of packet recived during that time period and 
                            string s which is either TCPipv4 or TCPipv6
                            this will return the number of packet recieved using TCP
                            for specified s i.e. either TCPipv4 or TCPipv6

                        -   PlotLiveGraph()
                            *todos part (this should draw the live graph)

                        -   PrintFreqToFile()
                            *todos part (this should print Freq of packets in file given like csv, txt, excel etc...)
                        
                        -   PrintPacketsCountToFile()
                            *todos part (this should print number of packets in file given like csv, txt, excel etc...)
                        
                        -   StdevPacketCounts()
                            *todo part (this should calculate standard deviation of packet counts in file given like csv, txt, excel etc...)
                        
                        -   StdevPacketFreqCounts()
                            *todo part (this should calculate standard deviation of packet frequency
                            counts in file given like csv, txt, excel etc...)

                         -  VarPacketCounts()
                            *todo part (this should calculate Variance of packet counts in file given like csv, txt, excel etc...)
                        
                        -   VarPacketFreqCounts()
                            *todo part (this should calculate Variance of packet frequency
                            counts in file given like csv, txt, excel etc...)
"""

from Utils import monitor
import time 

#this will return the number of packet recieved (using TCP)
def __TCPpacketFreq__(t,s):
    initial = monitor.__tcpStat__()[s]
    time.sleep(t)

    final = monitor.__tcpStat__()[s]

    return(final-initial)/t


# todo part starts from here

# def PlotLiveGraph():
#     pass

#def PrintFreqToFile():
#   pass

#def PrintPacketsCountToFile():
#   pass

#def StdevPacketCounts():
#   pass

#def StdevPacketFreqCounts():
#   pass

#def VarPacketCounts():
#   pass

#def VarPacketFreqCounts():
#   pass








