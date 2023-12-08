# Digital Forensics Script for Linux

This repository contains an advanced Bash script designed for conducting digital forensics on Linux systems. The script automates the collection of a wide range of system and user data, making it a valuable tool for IT professionals, system administrators, and digital forensic investigators.

## Features

- **System Information**: Collects basic system information including uptime, startup time, and hardware clock readouts.
- **Operating System Details**: Extract information about the operating system installation, including installer logs and file system details.
- **Network Information**: Gathers network configuration, IP addresses, and network interface details.
- **Installed Programs**: Lists all installed packages using both `rpm` and `apt`.
- **Hardware Information**: Retrieves detailed information about PCI devices, hardware summaries, and BIOS data.
- **System Logs**: Captures system journal logs and the contents of the `/var/log` directory.
- **User Data**: Extracts user-specific data like recently used files and bash command history.
- **Memory Dump**: Performs a memory dump for detailed analysis.
- **Process Information**: Captures information about current running processes.
- **User Login History**: Records user login history and scheduled tasks.
- **Secure Output Handling**: Compresses and encrypts the gathered data for security.

## Usage

1. **Set Permissions**: Ensure the script is executable:
   ```bash
   chmod +x DFLinux.sh
   sudo ./DFLinux.sh
   ```
   Output: Check the specified output directory for the collected data.

## Requirements
- The script is intended for use on Linux systems.
- Please make sure you have the necessary permissions to execute the script and access system files.
- Required tools: dump, gpg, netstat, ifconfig, lshw, dmidecode, etc., should be installed.

## Security and Privacy
- The script compresses and encrypts the output data. Replace `YOUR_PASSPHRASE` in the script with a secure passphrase of your choice. Ensure you handle and store the collected data responsibly, adhering to relevant laws and regulations.
