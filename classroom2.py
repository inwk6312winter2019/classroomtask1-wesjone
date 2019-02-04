import random
import sys
class ipaddr():
    def __init__(self,ip = [192*168*0*1], nm=[0,0,0,0]):
        self.ip = ip
        self.nm = nm
        def_str_(self):
        ipformat = ""
        for ips in self.ip:
            ipformat = ipfprmat + str(ips) + "."

            return("This is internet address is : " + ipformat)
myip = ipaddr([192,168,1,1],[255,255,255,0])
addip = ipaddr([2,1,1,1])
result = myip + addip
print(myip)
print(result)
