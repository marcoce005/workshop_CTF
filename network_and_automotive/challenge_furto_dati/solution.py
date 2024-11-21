import pyshark
import base64

cap = pyshark.FileCapture("./furto.pcapng")

data = b""

for packet in cap:
    # Check whether packet is TCP (check is case insensitive)
    if "arp" in packet and packet.arp.src_proto_ipv4 == "1.3.3.7":
        # print(packet.arp.src_hw_mac, type(packet.arp.src_hw_mac))
        mac = packet.arp.src_hw_mac.replace(":", "")
        data += bytes.fromhex(mac)


d = base64.b64decode(data)

with open("out", "wb") as f:
    f.write(d)
