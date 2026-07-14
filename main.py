import os

print("=== Ping Sweeper ===")
print("Scanning 192.168.1.1 - 192.168.1.10...\n")

for ping in range(1, 11):
    ip = f"192.168.1.{ping}"

    result = os.system(f"ping -c 1 -w 1 {ip} > /dev/null 2>&1")

    if result == 0:
        print(f"[+] Device Active: {ip}")
    else:
        print(f"[-] No Response: {ip}")

print("\nScan completed.")
