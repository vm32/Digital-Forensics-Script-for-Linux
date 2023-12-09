#!/bin/bash

output_dir="/tmp/ExtractedInfo"
mkdir -p "$output_dir/hash"
logfile="$output_dir/forensics_log.txt"

write_output() {
    command=$1
    filename=$2
    if $command > "$output_dir/$filename" 2>&1; then
        echo "Successfully executed: $command" >> "$logfile"
    else
        echo "Failed to execute: $command" >> "$logfile"
    fi
}

echo "Forensic data extraction started at $(date)" > "$logfile"

# System Information Extraction
write_output "uptime -p" "system_uptime.txt"
write_output "uptime -s" "system_startup_time.txt"
write_output "date" "current_system_date.txt"
write_output "date +%s" "current_unix_timestamp.txt"

if command -v hwclock &>/dev/null; then
    write_output "hwclock -r" "hardware_clock_readout.txt"
else
    echo "hwclock command not found" >> "$logfile"
fi

# Operating System Installation Date
write_output "df -P /" "root_filesystem_info.txt"
write_output "ls -l /var/log/installer" "os_installer_log.txt"
write_output "tune2fs -l /dev/sda1" "root_partition_filesystem_details.txt" # Check for correct root partition

# Network Information
write_output "ifconfig" "network_configuration.txt"
write_output "ip addr" "ip_address_info.txt"
write_output "netstat -i" "network_interfaces.txt"

# Installed Programs
write_output "dpkg -l" "dpkg_installed_packages.txt" # Replaced 'apt' with 'dpkg -l'
write_output "rpm -qa" "rpm_installed_packages.txt"

# Hardware Information
write_output "lspci" "pci_device_list.txt"
write_output "lshw -short" "hardware_summary_report.txt"
write_output "dmidecode" "dmi_bios_info.txt"

# System Logs and Usage
write_output "journalctl" "system_journal_logs.txt"
write_output "ls -lah /var/log/" "var_log_directory_listing.txt"

for user_home in /home/*; do
    username=$(basename "$user_home")
    
    if [ -f "$user_home/.bash_history" ]; then
        write_output "cat $user_home/.bash_history" "bash_command_history_$username.txt"
    else
        echo "No .bash_history for $username" >> "$output_dir/bash_command_history_$username.txt"
    fi
    
    if [ -f "$user_home/.zsh_history" ]; then
        write_output "cat $user_home/.zsh_history" "zsh_command_history_$username.txt"
    else
        echo "No .zsh_history for $username" >> "$output_dir/zsh_command_history_$username.txt"
    fi
    
    write_output "cat $user_home/.local/share/recently-used.xbel" "recently_used_files_$username.txt"
done

if crontab -l &>/dev/null; then
    write_output "crontab -l" "scheduled_cron_jobs_root.txt"
else
    echo "No crontab for root" >> "$output_dir/scheduled_cron_jobs_root.txt"
fi

tar -czf "$output_dir/user_data.tar.gz" -C "$output_dir" ./*.txt --remove-files

echo "Data extraction complete. Check the $output_dir directory for output." >> "$logfile"
echo "Forensic data extraction completed at $(date)" >> "$logfile"

echo "Data extraction complete. Check the $output_dir directory for output."
