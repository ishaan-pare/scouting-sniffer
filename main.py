from Utils import analyze
from cmdUtils.logo import logo
from cmdUtils.boot import Boot
from troubleshoot import msg

#booting up the application
Boot()

#displaying the logo
logo("logo1")

#starting the application
if(analyze.__Check__()):
    print("\n\t|-Oh no!\n")
    print("\t|-Sombody Just Scanned Your Computer :(\n\t|-Need urgent Actions\n")
    msg()