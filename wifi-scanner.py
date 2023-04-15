import scapy.all as scapy

request = scapy.ARP()

request.pdst = '192.168.0.1/24'
broadcast = scapy.Ether()

broadcast.dst = 'ff:ff:ff:ff:ff:ff'

request_broadcast = broadcast / request
clients = scapy.srp(request_broadcast, timeout=10, verbose=1)
for element in clients:
    # print(element.psrc + "      " + element.hwsrc)
    element.show()
