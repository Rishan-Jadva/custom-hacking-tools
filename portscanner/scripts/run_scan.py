# CLI interface, calls everything else
"""
Parse CLI input (target IP/range, port range, scan type)
Resolve hostname/IP
discovery.py to find live hosts
for each live host;
use tcp or udp scanner to scan ports
use response parser to interpret open/close/filtered fields
use service detect for banner grabbing
write results to reports/
"""
