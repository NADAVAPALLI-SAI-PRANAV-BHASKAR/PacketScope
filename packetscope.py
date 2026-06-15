from collections import Counter
from datetime import datetime
import os

print("=" * 50)
print("PacketScope - Network Packet Analyzer")
print("=" * 50)

try:
    packet_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "packets.txt"
    )

    with open(packet_path, "r") as file:
        packets = file.readlines()

except FileNotFoundError:
    print("packets.txt not found")
    input("\nPress Enter to exit...")
    exit()

source_ips = []
destination_ips = []
protocols = []

for line in packets:
    parts = line.strip().split(",")

    if len(parts) != 3:
        continue

    source_ip = parts[0]
    destination_ip = parts[1]
    protocol = parts[2].upper()

    source_ips.append(source_ip)
    destination_ips.append(destination_ip)
    protocols.append(protocol)

source_count = Counter(source_ips)
destination_count = Counter(destination_ips)
protocol_count = Counter(protocols)

print("\n===== PacketScope Analysis Report =====\n")

print(f"Total Packets: {len(protocols)}")

print("\nProtocols:")

for protocol, count in protocol_count.items():
    print(f"{protocol}: {count}")

print("\nTop Source IPs:")

for ip, count in source_count.most_common(5):
    print(
        f"{ip} - {count} "
        f"{'packet' if count == 1 else 'packets'}"
    )

print("\nTop Destination IPs:")

for ip, count in destination_count.most_common(5):
    print(
        f"{ip} - {count} "
        f"{'packet' if count == 1 else 'packets'}"
    )

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"report_{timestamp}.txt"

report_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    filename
)

with open(report_path, "w") as report:
    report.write("PacketScope Analysis Report\n")
    report.write("=" * 40 + "\n")

    report.write(
        f"Total Packets: {len(protocols)}\n\n"
    )

    report.write("Protocols:\n")

    for protocol, count in protocol_count.items():
        report.write(
            f"{protocol}: {count}\n"
        )

    report.write("\nTop Source IPs:\n")

    for ip, count in source_count.most_common(5):
        report.write(
            f"{ip} - {count} "
            f"{'packet' if count == 1 else 'packets'}\n"
        )

    report.write("\nTop Destination IPs:\n")

    for ip, count in destination_count.most_common(5):
        report.write(
            f"{ip} - {count} "
            f"{'packet' if count == 1 else 'packets'}\n"
        )

print(f"\nReport saved as {filename}")

input("\nPress Enter to exit...")
