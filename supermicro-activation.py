#!/usr/bin/env python3

import hmac
import hashlib
import sys
import re

# HMAC key (hex encoded)
hmac_key = "8544E3B47ECA58F9583043F8"

def calculate_key(data, key):
    """
    Calculate the HMAC-SHA1 and return the hex digest
    :param data: The data (in hex) to be hashed
    :param key: The secret key (in hex)
    :return: HMAC-SHA1 result (hex digest)
    """
    # Convert the hex strings to bytes
    data_bytes = bytes.fromhex(data)
    key_bytes = bytes.fromhex(key)
    
    # Create HMAC-SHA1 using the key
    hmac_hash = hmac.new(key_bytes, data_bytes, hashlib.sha1)
    
    # Return the result as a hex string
    return hmac_hash.hexdigest()

def main(mac):
    # Validate MAC address with regex
    if not re.match(r'^([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}$', mac):
        print(f"Invalid MAC address: {mac}")
        sys.exit(1)

    # Remove colons from MAC address
    mac = mac.replace(":", "")
    
    # Calculate HMAC-SHA1
    license_key = calculate_key(mac, hmac_key)
    
    # Take the first 24 characters of the key
    license_key = license_key[:24]
    
    # Print in 4-character blocks
    output = " ".join([license_key[i:i+4] for i in range(0, 24, 4)])
    print(output)

if __name__ == "__main__":
    # Check if a MAC address was given
    if len(sys.argv) != 2:
        print("Usage: supermicro-ipmi-key <MAC>")
        sys.exit(1)

    # Get the MAC address
    mac_address = sys.argv[1]
    
    # Run the main function
    main(mac_address)
