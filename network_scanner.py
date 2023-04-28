"""
Quick multi-threading project (because sequentially pinging 255 addresses takes way too long) 
for network security purposes only. 
"""
import subprocess
import threading


DEFAULT_GATEWAY = "10.0.0.1"  # for my personal home network

def add_connected_ip_address(address: str, addresses: list, print_to_console=True):
    """Appends ADDRESS to ADDRESSES list if ADDRESS returns a positive ping request. """
    if print_to_console:
        print(f"Trying {address}")
    completed_process = subprocess.run(f"ping -n 1 {address}", capture_output=True)
    output = completed_process.stdout
    if ("TTL" in str(output)):
        addresses.append(address)


if __name__ == "__main__":
    addresses = list()

    threads = list()
    for i in range(256):
        address = DEFAULT_GATEWAY[:-1] + str(i)
        t = threading.Thread(target=add_connected_ip_address, args=(address, addresses), kwargs={"print_to_console": False})
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    addresses.sort(key=lambda a: a[-3])  # sort based on last 3 characters (don't feel like doing regex rn)
    for address in addresses:
        print(f"Found {address}")