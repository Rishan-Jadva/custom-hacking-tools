# TCP connect of SYN scan (socket or scapy)
import socket

def check_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        s.close()
        if result == 0:
            return "Open"
        else:
            return "Closed/Filtered"
    except socket.timeout:
        return "Filtered"
    except Exception as e:
        return f"Error: {e}"

def scan_tcp_ports(target, ports):
    results = {}

    for port in ports:
        status = check_port(target, port)
        results[port] = status
    
    return results