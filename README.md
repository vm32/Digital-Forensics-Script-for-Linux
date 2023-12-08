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
   sudo apt-get install util-linux  # For Debian/Ubuntu
   sudo yum install util-linux  # For CentOS/RHEL
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

## Linux Distribution Compatibility

The advanced digital forensics Bash script is designed to be compatible with most major Linux distributions. Below is a breakdown of compatibility across different types of distributions:

### Debian-based distributions (e.g., Ubuntu, Linux Mint)
- Utilizes `apt` for listing installed packages, which is specific to Debian-based systems.
- Most other commands (like `ifconfig`, `netstat`, `lspci`, `lshw`, `dmidecode`) are generally available or can be easily installed.

### Red Hat-based distributions (e.g., Fedora, CentOS, RHEL)
- Includes `rpm -qa` for listing installed RPM packages, catering to Red Hat-based systems.
- Other commands are typically available, but installation of certain tools might be necessary if they are not present by default.

### Arch Linux and derivatives (e.g., Manjaro)
- The script does not include a specific command for `pacman`, but this can be added (`write_output "pacman -Q" "pacman_installed_packages.txt"`).
- Other commands should function as expected, assuming necessary tools are installed.

### Other distributions
- Compatibility depends on the availability of specific tools and commands used in the script.
- Modifications may be needed based on the distribution's package management system and available utilities.

### Additional Notes
- The script uses traditional networking tools like `ifconfig` and `netstat`. Some newer distributions might prefer `ip` and `ss`, requiring modifications to those commands.
- Root access is generally required for many of the script's operations.
- It is recommended to test the script in a controlled environment on your specific distribution to ensure compatibility and make any necessary adjustments.

In summary, while the script should work on most major Linux distributions with minimal modifications, slight adjustments may be required for specific distributions, particularly those not based on Debian or Red Hat.
