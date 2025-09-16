#!/usr/bin/env python3
"""
Enhanced Tello PCAP Analyzer
Parses .pcap/.pcapng files and adds basic performance metrics.
"""

import sys
import os
import pandas as pd
from scapy.all import rdpcap, UDP, IP

def classify_port(port):
    """Classify Tello port usage."""
    if port == 8889:
        return "CMD"     # Command & control
    elif port == 8890:
        return "STATE"   # Telemetry
    elif port == 11111:
        return "VIDEO"   # Video stream
    else:
        return "OTHER"

def parse_pcap(filename, max_payload_len=100):
    """Parse one pcap file into a list of dicts."""
    records = []
    try:
        packets = rdpcap(filename)
    except Exception as e:
        print(f"[!] Failed to read {filename}: {e}")
        return []

    last_time = None
    for i, pkt in enumerate(packets, start=1):
        if pkt.haslayer(UDP) and pkt.haslayer(IP):
            try:
                payload = bytes(pkt[UDP].payload)
                ts = float(pkt.time)
                delta = ts - last_time if last_time is not None else 0
                last_time = ts

                records.append({
                    "packet_index": i,
                    "time": ts,
                    "delta_time": delta,
                    "packet_rate": (1 / delta) if delta > 0 else None,
                    "src_ip": pkt[IP].src,
                    "dst_ip": pkt[IP].dst,
                    "sport": pkt[UDP].sport,
                    "dport": pkt[UDP].dport,
                    "port_role": classify_port(pkt[UDP].dport),
                    "length": len(payload),
                    "payload_hex": payload[:max_payload_len].hex()
                })
            except Exception:
                continue
    return records

def main(files):
    for f in files:
        print(f"[+] Parsing: {f}")
        rows = parse_pcap(f)
        if not rows:
            print(f"[!] No data parsed from {f}")
            continue

        df = pd.DataFrame(rows)

        # Rolling mean of payload size (window=10 packets)
        df["rolling_avg_len"] = df["length"].rolling(window=10, min_periods=1).mean()

        out_csv = os.path.splitext(f)[0] + "_parsed.csv"
        try:
            df.to_csv(out_csv, index=False)
            print(f"[+] Wrote CSV: {out_csv} ({len(df)} rows)")
        except Exception as e:
            print(f"[!] Failed to write CSV for {f}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 analyze_tello_captures.py file1.pcapng file2.cap ...")
        sys.exit(1)
    main(sys.argv[1:])
