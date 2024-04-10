#!/bin/bash

output_dir="/tmp/ExtractedInfo"
mkdir -p $output_dir
logfile="$output_dir/extraction.log"
password="YOUR_PASSPHRASE"

write_output() {
    command=$1
    filename=$2
    if $command > "$output_dir/$filename" 2>&1; then
        echo "Successfully executed: $command" >> "$logfile"
    else
        echo "Failed to execute: $command" >> "$logfile"
    fi
}

tput civis

if [ -f /etc/os-release ]; then
    . /etc/os-release
    if [ -n "$ID" ]; then
        distro="$ID"
        read -p "Install additional dependencies for proper extraction? (y/n): " install_dependencies
        if [ "$install_dependencies" == "y" ]; then
            echo "Installing Dependencies." > "$logfile"
            (while :; do for c in / - \\ \|; do printf "\e[1;33m\r[$c] Installing Dependencies...\e[0m"; sleep .1; done; done) &
            case "$distro" in
                "ubuntu" | "debian" | "linuxmint" | "elementary")
                    sudo apt-get update &> /dev/null
                    sudo apt-get install -y util-linux net-tools zip unzip &> /dev/null
                    ;;
                "centos" | "rhel" | "fedora")
                    sudo yum update &> /dev/null
                    sudo yum install -y util-linux net-tools zip unzip &> /dev/null
                    ;;
                "opensuse")
                    sudo zypper refresh &> /dev/null
                    sudo zypper install -y util-linux net-tools zip unzip &> /dev/null
                    ;;
                *)
                    exit 1
                    ;;
            esac
        elif [ "$install_dependencies" == "n" ]; then
            echo "Skipping Dependency Installation." > "$logfile"
        else
            echo "Invalid input. Please enter 'y' or 'n'."
            exit 1
        fi
    else
        echo "Unable to determine distribution." >> "$logfile"
        exit 1
    fi
else
    echo "Unable to determine distribution." >> "$logfile"
    exit 1
fi

if [ "$install_dependencies" == "y" ]; then
  echo "Successfully Installed Dependencies." >> "$logfile"
  { printf "\e[1;32m\r[+] Successfully Installed Dependencies.\e[0m"; kill $! && wait $!; } 2>/dev/null
else
  { printf "\e[1;32m\r[+] Skipped Installing Dependencies.\e[0m"; kill $! && wait $!; } 2>/dev/null
fi

printf "\n\n"

(while :; do for c in / - \\ \|; do printf "\e[1;33m\r[$c] Extracting Data...\e[0m"; sleep .1; done; done) &
echo "Forensic data extraction started at $(date)" >> "$logfile"

# System Information Extraction
write_output "uptime -p" "system_uptime.txt"
write_output "uptime -s" "system_startup_time.txt"
write_output "date" "current_system_date.txt"
write_output "date +%s" "current_unix_timestamp.txt"
write_output "env" "system_environment_variables.txt"
write_output "lsmod" "system_modules.txt"
write_output "lsof" "open_files.txt"
write_output "cat /etc/passwd" "system_users.txt"
write_output "cat /etc/group" "system_groups.txt"
write_output "cat /proc/cpuinfo" "system_cpuinfo.txt"
write_output "cat /etc/sudoers" "system_sudoers_file.txt"
write_output "cat /etc/fstab" "system_filesystem_table.txt"
write_output "ps aux" "running_processes.txt"

if command -v hwclock &>/dev/null; then
    write_output "hwclock -r" "hardware_clock_readout.txt"
else
    echo "hwclock command not found" >> "$logfile"
fi

# Operating System Installation Date
write_output "df -P /" "root_filesystem_info.txt"
write_output "ls -l /var/log/installer" "os_installer_log.txt"
filesystem_name=$(df / | awk 'NR==2 {print $1}')
write_output "tune2fs -l $filesystem_name" "root_partition_filesystem_details.txt" # Check for correct root partition

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
write_output "cat /var/log/syslog" "system_syslog.txt"
write_output "cat /var/log/auth.log" "system_auth_logs.txt"
write_output "ls -lah /var/log/" "var_log_directory_listing.txt"
write_output "last" "last_logged_on_users.txt"

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

{ printf "\e[1;32m\r[+] Successfully Extracted Data.\e[0m"; kill $! && wait $!; } 2>/dev/null
printf "\n\n"

echo "Forensic data extraction completed at $(date)" >> "$logfile"

(while :; do for c in / - \\ \|; do printf "\e[1;33m\r[$c] Hashing Executable Files...\e[0m"; sleep .1; done; done) &

echo "Started Hashing Executable Files." >> "$logfile"
find / -type f -xdev -executable -not \( -path '/proc/*' -o -path '/sys/*' \) -exec md5sum {} \; 2>/dev/null > "$output_dir/executables_MD5_hashes.txt"

{ printf "\e[1;32m\r[+] Successfully Hashed Executable Files.\e[0m"; kill $! && wait $!; } 2>/dev/null
printf "\n\n"

echo "Successfully Completed Hashing Executable Files." >> "$logfile"

(while :; do for c in / - \\ \|; do printf "\e[1;33m\r[$c] Dumping Memory...\e[0m"; sleep .1; done; done) &

echo "Started Dumping Memory." >> "$logfile"
sudo ./avml memory.dmp
sudo mv memory.dmp $output_dir

{ printf "\e[1;32m\r[+] Successfully Dumped Memory.\e[0m"; kill $! && wait $!; } 2>/dev/null
printf "\n\n"

echo "Successfully Completed Dumping Memory." >> "$logfile"

(while :; do for c in / - \\ \|; do printf "\e[1;33m\r[$c] Encrypting & Compressing Data...\e[0m"; sleep .1; done; done) &

echo "Started Encrypting & Compressing Data." >> "$logfile"
host_name=$(hostname)
$(cd $output_dir && zip -P $password -m "$output_dir/$host_name.zip" *.txt &> /dev/null)

{ printf "\e[1;32m\r[+] Successfully Encrypted & Compressed Data.\e[0m"; kill $! && wait $!; } 2>/dev/null
printf "\n\n"

echo "Successfully Encrypted & Compressed Data." >> "$logfile"

echo "Data extraction complete. Check the $output_dir directory for output." >> "$logfile"
printf "\e[1;32m[+] Data extraction complete. Check the $output_dir directory for output.\e[0m"
printf "\n"

tput cnorm
