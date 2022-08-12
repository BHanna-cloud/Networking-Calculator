
from ast import Import
from email.policy import strict
from imaplib import Int2AP
import ipaddress
from string import octdigits
from sys import prefix, set_asyncgen_hooks
from telnetlib import IP
from tkinter import FALSE, TRUE

def Main():
            
    X1 = input("Enter IP4V Address/CIDR: ")
    X2 = ipaddress.IPv4Network(X1, strict=FALSE).network_address
    X3 = ipaddress.IPv4Network(X1, strict=FALSE).netmask
    print("")

    print("   Network Address: ", (ipaddress.IPv4Network(X1, strict=FALSE).network_address))
    print(" Broadcast Address: ", (ipaddress.IPv4Network(X1, strict=FALSE).broadcast_address))
    print("         Host Mask: ", (ipaddress.IPv4Network(X1, strict=FALSE).hostmask))
    print("          Net Mask: ", (ipaddress.IPv4Network(X1, strict=FALSE).netmask))
    print("            Prefix: ", (ipaddress.IPv4Network(X1, strict=FALSE).prefixlen))
    print("        IP Address: ", (ipaddress.IPv4Network(X1, strict=FALSE).exploded))

    print("         IS Global: ", (ipaddress.IPv4Network(X1, strict=FALSE).is_global))
    print("     IS Link Local: ", (ipaddress.IPv4Network(X1, strict=FALSE).is_link_local))
    print("       IS Loopback: ", (ipaddress.IPv4Network(X1, strict=FALSE).is_loopback))
    print("   Number of Hosts: ", (ipaddress.IPv4Network(X1, strict=FALSE).num_addresses))
    print("Net_Address Binary: ", (bin(int(X2)))[2:])
    print("    NetMask Binary: ", (bin(int(X3)))[2:])

    repeat = input("Would you like to run again? ")
    if repeat == "y":
        Main()
    else:
        print("Bye!")
        exit()

Main()