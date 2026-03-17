import nmap

def scan_network(subnet):
    nm = nmap.PortScanner()

    print(f"Scanning network {subnet}... (this may take a few minutes)")

    # Run a scan with OS detection (-O) and service version (-sV)
    # You need to run your Python script with sudo for OS detection to work
    nm.scan(hosts=subnet, arguments='-O -sV -T4')

    devices = []

    for host in nm.all_hosts():
        if nm[host].state() == "up":
            ip = host
            mac = nm[host]['addresses'].get('mac', 'Unknown')
            vendor = nm[host]['vendor'].get(mac, 'Unknown') if mac != 'Unknown' else 'Unknown'

            # Try to get OS info
            osmatches = nm[host].get('osmatch', [])
            if osmatches:
                os_name = osmatches[0]['name']
                os_accuracy = osmatches[0]['accuracy']
                os_info = f"{os_name} (Accuracy: {os_accuracy}%)"
            else:
                os_info = "Unknown"

            devices.append({
                'IP': ip,
                'MAC': mac,
                'Model': vendor,
                'OS': os_info
            })

    # Print devices in readable format
    if devices:
        print(f"\nFound {len(devices)} devices:\n")
        for d in devices:
            print(f"IP: {d['IP']}")
            print(f"MAC: {d['MAC']}")
            print(f"Model: {d['Model']}")
            print(f"OS: {d['OS']}")
            print('-' * 40)
    else:
        print("No devices found.")

# Example usage:
if __name__ == "__main__":
    # Replace with your subnet; for your network it would be:
    scan_network('10.255.0.0/24')
