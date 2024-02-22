from scapy.all import *

settings = {
    "src": "127.0.0.1",
    "dst": "8.8.8.8"
}

def build_layers():
    return Ether() / IP(src=settings["src"], dst=settings["dst"]) / UDP(dport=53) / DNS(rd=1)

def set_payload(packet, data):
    dns_layer = DNSQR(qname=data.encode('utf-8'))
    packet[DNS] /= dns_layer
    return packet

def send_dns_command(command):
    query = DNSQR(qname=command, qtype="A")  # Use A type for simplicity, adjust as needed
    dns_packet = Ether() / IP(src=settings["src"], dst=settings["dst"]) / UDP(dport=53) / DNS(rd=1, qd=query)
    sendp(dns_packet)

data = "command.yourdomain.com"  # Replace "yourdomain.com" with your actual domain

# Create DNS packet
dns_packet = build_layers()

# Set DNS payload
dns_packet = set_payload(dns_packet, data)

# Optional: Print the modified packet
dns_packet.show()

# Send the command via DNS
send_dns_command(data)
