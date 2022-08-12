
from ast import Import
from email.policy import strict
from imaplib import Int2AP
import ipaddress
from string import octdigits
from sys import prefix, set_asyncgen_hooks
from telnetlib import IP
from tkinter import FALSE, TRUE


#User enters IP Address
def Main():
        def do_something():

            X1 = input("Enter IP4V Address/CIDR: ")
            print("")

            print("Broadcast Address: ", (ipaddress.IPv4Network(X1, strict=FALSE).broadcast_address))
            print("  Network Address: ", (ipaddress.IPv4Network(X1, strict=FALSE).network_address))
            print("        Host Mask: ", (ipaddress.IPv4Network(X1, strict=FALSE).hostmask))
            print("         Net Mask: ", (ipaddress.IPv4Network(X1, strict=FALSE).netmask))
            print("           Prefix: ", (ipaddress.IPv4Network(X1, strict=FALSE).prefixlen))
            print("           Binary: ", (bin(int(ipaddress.IPv4Address(X1, strict=FALSE.broadcast_address)))[2:]))
    
        try:
            do_something()
        except Exception:
          pass
repeat = input("Would you like to run again? ")
if repeat == "y":
    Main()
else:
    print("Bye!")
    exit()



