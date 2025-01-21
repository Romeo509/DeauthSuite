# **DeauthSuite (Jammer)**

**DeauthSuite** is a Python-based toolkit for wireless network monitoring and deauthentication attacks. The tool utilizes the Aircrack-ng suite to enable monitor mode, scan for networks, and perform deauthentication attacks. This tool is designed for **educational and testing purposes** only.

## **Key Features**

- **Start Monitor Mode**: Activate monitor mode on your wireless interface.
- **Scan for Networks**: Discover nearby wireless networks and their details.
- **Target a Network**: Focus on a specific network by its BSSID and channel.
- **Perform Deauthentication Attacks**: Disrupt wireless connections by sending deauthentication packets.
- **Stop Monitor Mode**: Deactivate monitor mode after performing necessary actions.

## **Installation**

### **Prerequisites**

- **Linux** or **WSL (Windows Subsystem for Linux)** on Windows.
- **Aircrack-ng** suite installed. (To install, use: `sudo apt-get install aircrack-ng`)

### **Install the Tool**

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/DeauthSuite.git
   ```

2.  Navigate to the project directory:
    ```bash
     cd DeauthSuite
    ```
3.  Make sure you have the necessary permissions to run network monitoring 
    commands.

 ## **Usage*
1. Run the script:
   ```bash
     python jammer.py
    ```
2. The tool will display a menu with the following options:
  - **Start Monitor Mode**: Turns on monitor mode on your wireless interface.
  - **Scan for Networks**: Scans for nearby networks.
  - **Target a Network**: Focuses on a specific network for further attacks.
  - **Perform Deauthentication Attack:** Performs a deauthentication attack on 
   the targeted network and device (optional).
  - **Stop Monitor Mode**: Stops monitor mode.

## **Important Notes*
- **Monitor Mode**: Make sure your wireless network interface supports monitor mode (typically requires a compatible Wi-Fi adapter).
- **Deauthentication Attack**: This tool will send deauthentication packets to disconnect devices from the network. Be sure to use it only on networks you own or have explicit permission to test.
- **Responsibility**: This tool is for educational and penetration testing purposes only. Unauthorized use can result in legal consequences. Always seek permission before using this tool on any network.
