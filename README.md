# PacketScope - Network Packet Analyzer

PacketScope is a Python-based network packet analysis tool that processes packet data, analyzes network protocols, identifies communication patterns, and generates automated traffic analysis reports.

The project demonstrates TCP/IP networking fundamentals, protocol analysis, data processing, file handling, and network traffic monitoring concepts.

---

## Features

* Packet data parsing
* Protocol analysis (TCP, UDP, ICMP)
* Source IP address analysis
* Destination IP address analysis
* Network traffic statistics
* Timestamped report generation
* Input validation
* Automatic report storage

---

## Technologies Used

* Python
* TCP/IP Networking
* Protocol Analysis
* Data Processing
* File Handling

---

## Requirements

* Python 3.10.0 or higher

No external dependencies are required.

---

## Project Structure

```text
PacketScope/
│
├── packetscope.py
├── packets.txt
├── README.md
├── requirements.txt
└── report_YYYYMMDD_HHMMSS.txt
```

---

## How It Works

1. Reads packet data from a text file.
2. Extracts source IP addresses, destination IP addresses, and protocols.
3. Analyzes protocol distribution.
4. Identifies the most active source IP addresses.
5. Identifies the most common destination IP addresses.
6. Generates a timestamped network traffic report.

---

## Usage

Run the script:

```bash
py packetscope.py
```

or

```bash
python packetscope.py
```

---

## Sample Input

```text
192.168.1.10,8.8.8.8,TCP
192.168.1.10,1.1.1.1,UDP
10.0.0.5,8.8.8.8,TCP
172.16.0.8,8.8.8.8,ICMP
192.168.1.10,8.8.4.4,TCP
10.0.0.5,1.1.1.1,UDP
172.16.0.8,8.8.8.8,TCP
```

---

## Example Output

```text
==================================================
PacketScope - Network Packet Analyzer
==================================================

===== PacketScope Analysis Report =====

Total Packets: 7

Protocols:
TCP: 4
UDP: 2
ICMP: 1

Top Source IPs:
192.168.1.10 - 3 packets
10.0.0.5 - 2 packets
172.16.0.8 - 2 packets

Top Destination IPs:
8.8.8.8 - 4 packets
1.1.1.1 - 2 packets
8.8.4.4 - 1 packet

Report saved as report_20260615_061500.txt
```

---

## Sample Report

```text
PacketScope Analysis Report
========================================
Total Packets: 7

Protocols:
TCP: 4
UDP: 2
ICMP: 1

Top Source IPs:
192.168.1.10 - 3 packets
10.0.0.5 - 2 packets
172.16.0.8 - 2 packets

Top Destination IPs:
8.8.8.8 - 4 packets
1.1.1.1 - 2 packets
8.8.4.4 - 1 packet
```

---

## Skills Demonstrated

* TCP/IP Networking
* Network Traffic Analysis
* Protocol Analysis
* Packet Processing
* Data Processing
* File Handling
* Python Development

---

## Future Improvements

* Support for PCAP files
* Live packet capture
* Protocol filtering
* Traffic visualization
* Network anomaly detection

---

## Disclaimer

This project is intended for educational purposes and network analysis practice only.

---

Thank you
