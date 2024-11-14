# Supermicro IPMI License Key Generator

## Description

This Python script calculates an IPMI license key based on a given MAC address using HMAC-SHA1. The license key is returned in 4-character blocks. It is designed to generate a license key for Supermicro IPMI based on the system's MAC address.

The implementation mimics the functionality of a Perl script but is written in Python for easier use and management.

## Usage

```bash
supermicro-activation.py <MAC Address>
```

For example:

```bash
./supermicro-activation.py 01:23:45:67:89:AB
```

The script requires a MAC address in the format `XX:XX:XX:XX:XX:XX` and will validate that the input matches this format before proceeding. The MAC should consist of six pairs of hexadecimal characters (letters `a-f` or `A-F` and numbers `0-9`) separated by colons (`:`).

### Output

The license key is generated as a sequence of hexadecimal characters, formatted as 4-character blocks and printed to the terminal.

### Example Output

```
a1b2 c3d4 e5f6 g7h8 i9j0 klmn
```

## Requirements

- Python 3.x
- No external libraries required (uses Python's standard library modules like `hmac`, `hashlib`, and `sys`).

## Installation

1. Clone this repository:

```bash
git clone https://github.com/cwilliams001/Supermicro-activation.git
```

2. Make the script executable:

```bash
chmod +x supermicro-activation.py
```

3. Run the script using Python 3:

```bash
./supermicro-activation.py <MAC Address>
```