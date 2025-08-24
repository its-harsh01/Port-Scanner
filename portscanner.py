import socket
import sys

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"[+] Port {port} is open")
        sock.close()
    except Exception as e:
        print(f"[-] Error scanning port {port}: {e}")

def scan_host(host, start_port, end_port):
    print(f"Scanning host {host} from port {start_port} to {end_port}...")
    for port in range(start_port, end_port + 1):
        scan_port(host, port)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python portscanner.py <host> <start_port> <end_port>")
        sys.exit(1)
    
    target_host = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])

    scan_host(target_host, start_port, end_port)
