# Digital Forensics Script for Linux

This repository contains an advanced Bash script designed for conducting digital forensics on Linux systems. The script automates the collection of a wide range of system and user data, making it a valuable tool for IT professionals, system administrators, and digital forensic investigators.

## Features

- **System Information**: Collects basic system information including uptime, startup time, hardware clock readouts, environment variables, and many more.
- **Operating System Details**: Extract information about the operating system installation, including installer logs and file system details.
- **Network Information**: Gathers network configuration, IP addresses, and network interface details.
- **Installed Programs**: Lists all installed packages using both `rpm` and `dpkg`.
- **Hardware Information**: Retrieves detailed information about PCI devices, hardware summaries, and BIOS data.
- **System Logs**: Captures system journal logs, authentication logs, syslog and the contents of the `/var/log` directory.
- **User Data**: Extracts user-specific data like recently used files and bash command history and zsh command history.
- **Memory Dump**: Performs a memory dump for detailed analysis.
- **Process Information**: Captures information about current running processes.
- **User Login History**: Records user login history and scheduled tasks.
- **Secure Output Handling**: Compresses and encrypts the gathered data for security.

## Usage

1. **Set Permissions**: Ensure the script is executable:
   ```bash
   git clone https://github.com/vm32/Digital-Forensics-Script-for-Linux
   cd Digital-Forensics-Script-for-Linux
   chmod +x DFLinux.sh avml
   sudo ./DFLinux.sh
   ```
   Output: Check the specified output directory for the collected data.

## Requirements
- The script is intended for use on Linux systems.
- Please make sure you have the necessary permissions to execute the script and access system files.
- The scripts requires certain additional packages for proper extraction. You will be asked for installing the additional dependencies on the execution of script.

## Security and Privacy
- The script compresses and encrypts the output data. Replace `YOUR_PASSPHRASE` in the script with a secure passphrase of your choice. Ensure you handle and store the collected data responsibly, adhering to relevant laws and regulations.

## Linux Distribution Compatibility

The advanced digital forensics Bash script is designed to be compatible with most major Linux distributions. Below is a breakdown of compatibility across different types of distributions:

### Debian-based distributions (e.g., Ubuntu, Linux Mint)
- Utilizes `dpkg` for listing installed packages, which is specific to Debian-based systems.

### Red Hat-based distributions (e.g., Fedora, CentOS, RHEL)
- Includes `rpm -qa` for listing installed RPM packages, catering to Red Hat-based systems.

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

# Output
You can see the results of this script in `/tmp/ExtractedInfo/` which will consists password protected data zip with memory dump and extraction log file. <br><br>
`/tmp` is a standard temporary directory in Linux, used for storing temporary files. It is chosen because it is generally writable by all users and is cleared on reboot, which suits temporary data storage.<br>

![DFIR](https://github.com/SanketBaraiya/Digital-Forensics-Script-for-Linux/assets/56958135/844806bf-8eec-49c4-8dd4-b5962cff1c22)

In summary, while the script should work on most major Linux distributions with minimal modifications, slight adjustments may be required for specific distributions, particularly those not based on Debian or Red Hat.
## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=vm32/Digital-Forensics-Script-for-Linux&type=Date)](https://star-history.com/#vm32/Digital-Forensics-Script-for-Linux&Date)
