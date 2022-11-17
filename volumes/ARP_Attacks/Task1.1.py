#!/usr/bin/env python3
from scapy.all import *

E = Ether()
A = ARP()

A.op = 1 # 1 for ARP request; 2 for ARP reply

pkt = E/A
sendp(pkt)


# #!/usr/bin/python3
# from scapy.all import *

# E = Ether(dst='08:00:27:cd:2d:fd', src='08:00:27:b7:ba:af')
# A = ARP(hwsrc='08:00:27:b7:ba:af',psrc='10.0.2.9', 
# 	hwdst='08:00:27:cd:2d:fd', pdst='10.0.2.8')

# pkt = E/A
# pkt.show()
# sendp(pkt)