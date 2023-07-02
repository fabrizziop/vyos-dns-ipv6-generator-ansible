import os
from pytodns_cfg import *
import ipaddress
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir() if (isfile(join(os.getcwd(), f)) and f[-5:] == ".conf")]
print(onlyfiles)


fzone = []
rzone = []

for router_name_file in onlyfiles:
    with open(router_name_file) as file:
        lines = [line.rstrip() for line in file]
    #processing lines
    lines = [line for line in lines if line.find("set interfaces") >=0]
    lines = [line for line in lines if line.find("address") >=0]
    lines = [line for line in lines if line.find(prefix_sel) >=0]
    router_name = router_name_file[:-5]
    for line in lines:
        nline = ""
        interface = ""
        address = ""
        valid = True
        if line[:15] == "set interfaces ":
            nline = line[15:]
            apos = nline.find("address")
            nline2 = nline[:apos]
            address = nline.split("'")[1]
            if nline2[:8] == "ethernet":
                interface = nline2[9:-1]
            elif nline2[:9] == "wireguard":
                interface = nline2[10:-1]
            elif nline2[:6] == "bridge":
                interface = nline2[7:-1]
            elif nline2[:5] == "dummy":
                interface = nline2[6:-1]
            elif nline2[:6] == "tunnel":
                interface = nline2[7:-1]
            else:
                valid = False
        else:
            valid = False
        if valid == True:
            address = address.split("/")[0]
            fzone.append(interface+"."+router_name+"    IN AAAA    "+address)
            rzone.append(str(ipaddress.ip_address(address).reverse_pointer)+".    IN PTR "+interface+"."+router_name+"."+fqdn)

print("----FORWARD ZONE----")
for line in fzone:
    print(line)
print("----FORWARD ZONE----")

print("----REVERSE ZONE----")
for line in rzone:
    print(line)
print("----REVERSE ZONE----")
