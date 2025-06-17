from scapy.all import sniff

def packet_callback(packet):
    print("========== Packet Captured ==========")
    print(f"Source IP: {packet[0][1].src if packet.haslayer('IP') else 'N/A'}")
    print(f"Destination IP: {packet[0][1].dst if packet.haslayer('IP') else 'N/A'}")
    print(f"Protocol: {packet.proto if hasattr(packet, 'proto') else 'N/A'}")
    print(f"Payload: {bytes(packet.payload)}")
    print("=====================================")

print("Starting Packet Capture...")
sniff(prn=packet_callback, count=10)
