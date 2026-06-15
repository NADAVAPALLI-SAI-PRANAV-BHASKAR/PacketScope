from flask import Flask, render_template
from collections import Counter

app = Flask(__name__)

@app.route("/")
def home():
    try:
        with open("packets.txt", "r") as file:
            packets = file.readlines()
    except FileNotFoundError:
        return "packets.txt not found"

    source_ips = []
    destination_ips = []
    protocols = []

    for line in packets:
        parts = line.strip().split(",")

        if len(parts) != 3:
            continue

        source_ips.append(parts[0])
        destination_ips.append(parts[1])
        protocols.append(parts[2].upper())

    return render_template(
        "index.html",
        total_packets=len(protocols),
        protocols=Counter(protocols),
        source_ips=Counter(source_ips).most_common(5),
        destination_ips=Counter(destination_ips).most_common(5)
    )

if __name__ == "__main__":
    app.run()
