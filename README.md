# IP-Address Security Scanner
Sequentially pinging 255 addresses via the Windows CLI takes ~5 minutes on my machine. I created this quick Python script to parallelize the address pinging, resulting in a runtime of ~10 seconds.

I created this mock version in Python with the goal to transpose it to the C `socketAPI` to run scripts on my ESP32 when my phone's IP address logs on to the network. Additionally, this script can be used to ensure that only valid devices are connected to a network at a given time.

## USAGE
DEFAULT_GATEWAY is hardcoded in `network_scanner.py`. Run `ipconfig` to find your DEFAULT_GATEWAY and change to suit your needs.

Run via `python3 network_scanner.py`

# DO NOT USE FOR MALICIOUS INTENT
