"""
    Utility Module
    
    Task    -   execute "netstat -s" command which gives all the network statistics 
                and piped the output of the command to the variables in the form of 
                lines
    module contains     -   execute()
                            *this execute powershell command and return the whole
                            output into the array of lines 

                        -   tcpStat()
                            *this will return a dictionary consist of TCPipv4 and
                            TCPipv6 recieved Packets
     
"""

import subprocess
from types import resolve_bases
from global_constants import POWERSHELL_CMD

#return output of powershell - POWERSHELL_CMD - command
def execute():
    process = subprocess.Popen(["powershell", POWERSHELL_CMD], stdout = subprocess.PIPE)
    result = process.communicate()[0].splitlines()

    return result

#return dictionary of tcp recieved packets for ipv4 and ipv6
def tcpStat():
    #
    result = execute()

    ipv4RecievedStat = result[88]
    ipv6RecievedStat = result[99]

    stat = {
        "TCPipv4": int(ipv4RecievedStat.split()[3]),
        "TCPipv6": int(ipv6RecievedStat.split()[3]),
    }
    return stat

#for testing purpose
print(tcpStat())