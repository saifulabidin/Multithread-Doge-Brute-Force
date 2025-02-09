"""
DogeCoin Multithread Brute Force (For Testing & Security)
Author: Saiful Abidin
Disclaimer: This tool is for educational and security testing purposes only.
"""

import threading
import hashlib
import random
import string
import configparser

# Baca config.ini
config = configparser.ConfigParser()
config.read('config.ini')

# Ambil nilai dari config
threads = int(config['GENERAL']['threads'])
log_level = config['GENERAL']['log_level']
wallet_address = config['TARGET']['wallet_address']
key_length = int(config['BRUTE_FORCE']['key_length'])
max_attempts = int(config['BRUTE_FORCE']['max_attempts'])
rpc_url = config['API']['rpc_url']
timeout = int(config['API']['timeout'])

# Cetak untuk debug
print(f"Threads: {threads}, Log Level: {log_level}")
print(f"Target Wallet: {wallet_address}")
print(f"Key Length: {key_length}, Max Attempts: {max_attempts}")
print(f"RPC URL: {rpc_url}, Timeout: {timeout}")

def generate_random_private_key():
    """Generate a random private key"""
    return ''.join(random.choices(string.hexdigits, k=64))

def check_wallet(private_key):
    """Simulate checking if the private key corresponds to a valid wallet"""
    hashed = hashlib.sha256(private_key.encode()).hexdigest()
    print(f"Checked: {private_key} -> {hashed[:10]}...")
    
    # Simulate finding a match
    if hashed.endswith("0000"):  # Example condition
        print(f"[!] Valid wallet found! Private Key: {private_key}")
        exit(0)

def brute_force_worker():
    while True:
        private_key = generate_random_private_key()
        check_wallet(private_key)

if __name__ == "__main__":
    THREADS = 10  # Number of threads
    print(f"Starting {THREADS} threads for brute force testing...")
    
    for _ in range(THREADS):
        t = threading.Thread(target=brute_force_worker, daemon=True)
        t.start()
    
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Exiting...")
