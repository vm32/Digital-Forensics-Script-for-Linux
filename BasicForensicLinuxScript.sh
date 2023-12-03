#!/bin/bash

# Define the output directory
output_dir="/tmp/ExtractedInfo"
mkdir -p "$output_dir/hash"

# Assign execution permissions to the forensic script, if needed
# chmod +x /path/to/BasicForensicLinuxScript.sh

# Function to write command output to a file in the output directory
write_output() {
    command=$1
    filename=$2
    $command > "$output_dir/$filename"
}

# System Information Extraction
write_output "uptime -p" "days_On.txt"
write_output "uptime -s" "start_time.txt"
write_output "date" "current_date.txt"
write_output "date +%s" "current_timestamp.txt"
write_output "hwclock -r" "hardware_clock.txt"

# Operating System Installation Date
write_output "df -P /" "root_fs_info.txt"
write_output "ls -l /var/log/installer" "installer_log.txt"
write_output "tune2fs -l /dev/sda1" "filesystem_info.txt" # Assuming /dev/sda1 is the root partition

# Network Information
write_output "ifconfig" "network_info.txt"
write_output "ip addr" "ip_addresses.txt"
write_output "netstat -i" "net_interfaces.txt"

# Installed Programs
write_output "rpm -qa" "installed_packages_rpm.txt"
write_output "apt list --installed" "installed_packages_apt.txt"

# Hardware Information
write_output "lspci" "pci_devices.txt"
write_output "lshw -short" "hardware_summary.txt"
write_output "dmidecode" "dmi_info.txt"

# System Logs and Usage
write_output "journalctl" "system_journal.txt"
write_output "ls -lah /var/log/" "var_log_listing.txt"

# User Specific Data
for user_home in /home/*; do
    username=$(basename "$user_home")
    write_output "cat $user_home/.local/share/recently-used.xbel" "recently_used_$username.txt"
    write_output "cat $user_home/.bash_history" "bash_history_$username.txt"
done

# Compress User Data
tar -czf "$output_dir/user_data.tar.gz" -C "$output_dir" ./*.txt --remove-files

# Cleanup and Final Messages
echo "Data extraction complete. Check the $output_dir directory for output."
