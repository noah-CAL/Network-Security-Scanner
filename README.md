# Network-Scanner-Security-Tool
Sequentially pinging 255 addresses via the Windows CLI takes ~5 minutes on my machine. I created this quick Python script to parallelize the address pinging, resulting in a runtime of ~10 seconds.

## USAGE
DEFAULT_GATEWAY is hardcoded in `network_scanner.py`. Run `ipconfig` to find your DEFAULT_GATEWAY and change to suit your needs.

Run via `python3 network_scanner.py`
