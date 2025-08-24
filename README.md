# py-portscanner

A fast, simple **TCP port scanner** in Python with optional banner grabbing. Great for learning networking and showcasing security tooling on your GitHub.

## Features
- Scan single hosts or CIDR ranges
- Port ranges and lists (e.g., `1-1024,80,443`)
- Threaded scanning for speed
- Optional banner grab
- Save results to **JSON** or **CSV**
- Pure standard library (no external deps)

## Quick start
```bash
python3 portscanner.py -t scanme.nmap.org --common
python3 portscanner.py -t 192.168.1.0/24 -p 1-1024 -T 300 -b -O results.json
python3 portscanner.py -t example.com -p 80,443,8080 -b -o csv -O results.csv
