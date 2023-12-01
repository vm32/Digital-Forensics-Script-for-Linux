#!/bin/bash
output_dir="/tmp/ExtractedInfo/"
mkdir /tmp/ExtractedInfo/
mkdir /tmp/ExtractedInfo/hash/
#Permissions to folder and extraction script
chmod -R +x /tmp/BasicForensicLinuxScript.sh
#Days the server has been on
uptime -p > /tmp/ExtractedInfo/days_On0.txt
uptime -s > /tmp/ExtractedInfo/days_On01.txt
#Date of extraction
date > /tmp/ExtractedInfo/fechaextraccion0.txt
date +%s > /tmp/ExtractedInfo/fechaextraccion00.txt
hwclock -r > /tmp/ExtractedInfo/hwfechaextraccion000.txt
#Operating System Installation Date
df -P / > /tmp/ExtractedInfo/date_so0.txt
ls -l /var/log/installer > /tmp/ExtractedInfo/install0.txt
ls -lah /var/log/installer > /tmp/ExtractedInfo/install00.txt
tune2fs -l > /tmp/ExtractedInfo/date_so00.txt
ls -lct /etc | tail -1 | awk '{print $6, $7, $8}' > /tmp/ExtractedInfo/date_so010.txt
#IP Addresses and Network Interfaces 
ifconfig > /tmp/ExtractedInfo/ifconfig_0.txt
ifconfig -a > /tmp/ExtractedInfo/ifconfig_0.txt
ip addr > /tmp/ExtractedInfo/ifconfig_1.txt
cat /etc/sysconfig/network > /tmp/ExtractedInfo/networkcong0.txt
cat /etc/sysconfig/network-scripts/ifcfg-interface-name > /tmp/ExtractedInfo/networkcong001.txt
ip link show > /tmp/ExtractedInfo/networkcong002.txt
netstat -i > /tmp/ExtractedInfo/net_interfaces0.txt
#Programs installed in the operating system
rpm -qa > /tmp/ExtractedInfo/packages.txt
rpm -Va > /tmp/ExtractedInfo/packages02.txt
yum list installed > /tmp/ExtractedInfo/packages02.txt
apt list --installed > /tmp/ExtractedInfo/packages03.txt
apt list --upgradeable > /tmp/ExtractedInfo/packages04.txt
dpkg --list > /tmp/ExtractedInfo/packages05.txt
#Hardware and serial information 
lspci > /tmp/ExtractedInfo/pci001.txt
lscpu > /tmp/ExtractedInfo/cpu0.txt
lshw -short > /tmp/ExtractedInfo/hwinfo0.txt
hwinfo --short > /tmp/ExtractedInfo/hwinfo001.txt
dmidecode > /tmp/ExtractedInfo/hwinfo002.txt
mount | column -t > /tmp/ExtractedInfo/hwmounts0.txt
cat /proc/cpuinfo > /tmp/ExtractedInfo/cpu00.txt
cat /proc/meminfo > /tmp/ExtractedInfo/meminfo_0.txt
cat /proc/version > /tmp/ExtractedInfo/versions0.txt
#Weight of the /var/log folder and each file in the /var/log/ folder
ls -lah /var/log/ > /tmp/ExtractedInfo/varlog_listing0.txt
ls -la /var/log/ > /tmp/ExtractedInfo/varlog_listing00.txt
stat /var/log/*.* > /tmp/ExtractedInfo/varlog_dates0.txt
#File and directory enumeration in temporary folders
ls -lah /tmp/ > /tmp/ExtractedInfo/temp_list0.txt
ls -lah /var/tmp/ > /tmp/ExtractedInfo/temp_list00.txt
#File and directory enumeration in binary folder
ls -lah /usr/bin/ > /tmp/ExtractedInfo/binusr_tree0.txt
ls -lah /bin/ > /tmp/ExtractedInfo/bin_tree0.txt
ls -lah /bin/ > /tmp/ExtractedInfo/bin0.txt
# Journal Data
journalctl > /tmp/ExtractedInfo/journal_data.txt
#USB History 
cat /var/log/kern.log | grep usb > /tmp/ExtractedInfo/USBHistory-1.txt
cat /var/log/syslog | grep usb > /tmp/ExtractedInfo/USBHistory-2.txt
# Recent History
for user_home in /home/*; do
    usb_history_file="$user_home/.local/share/recently-used.xbel"

    if [ -f "$usb_history_file" ]; then
        cp "$usb_history_file" "$output_dir/usb_history_$user_home.txt"
    fi
done
# File Recent History
for user_home in /home/*; do
    recent_history_file="$user_home/.recently-used.xbel"

    if [ -f "$recent_history_file" ]; then
        cp "$recent_history_file" "$output_dir/recent_history_$user_home.txt"
    fi
done
# Wi-Fi History
cat /etc/NetworkManager/system-connections/* > /tmp/ExtractedInfo/wifi_connectionHistory.txt
nmcli con show > /tmp/ExtractedInfo/wifi_connectionHistory-2.txt
nmcli -f TYPE,TIMESTAMP,NAME con show > /tmp/ExtractedInfo/wifi_connectionTime.txt
#tree -df / > /tmp/ExtractedInfo/treefiles0.txt
#System user enumeration
users > /tmp/ExtractedInfo/users.txt
#Last server logins
lastlog > /tmp/ExtractedInfo/lastlog0.txt
last > /tmp/ExtractedInfo/last0.txt
last -Faiwx > /tmp/ExtractedInfo/last01.txt
lastb > /tmp/ExtractedInfo/lastb0.txt
#Who is logged in to the server
who > /tmp/ExtractedInfo/who0.txt
w > /tmp/ExtractedInfo/w0.txt
#Ports on the server listening
netstat -lntp > /tmp/ExtractedInfo/netstat0.txt
#Open Connections
netstat -oanp > /tmp/ExtractedInfo/netstat00.txt
netstat -oanp | grep ESTAB > /tmp/ExtractedInfo/netstat000.txt
netstat -anp > /tmp/ExtractedInfo/netstatanp0.txt
lsof -i > /tmp/ExtractedInfo/connection0.txt
lsof -V > /tmp/ExtractedInfo/OpenFiles.txt
netstat -lntp > /tmp/ExtractedInfo/netstat.txt
#Host Resolutions - Local DNS
cat /etc/hosts > /tmp/ExtractedInfo/hosts0.txt
#List of DNS servers
cat /etc/resolv.conf > /tmp/ExtractedInfo/resolv0.txt
#Open processes in the system and their execution paths
ps aux > /tmp/ExtractedInfo/psaux0.txt
ps -fea > /tmp/ExtractedInfo/top0.txt
ls -lah /etc/init.d/ > /tmp/ExtractedInfo/initetc0.txt
ps -ej > /tmp/ExtractedInfo/psaux00.txt
ps -auxwe > /tmp/ExtractedInfo/psaux_paths0.txt
ps -l > /tmp/ExtractedInfo/process_list0.txt
pstree -Aup > /tmp/ExtractedInfo/pstree0.txt
tree -df /etc/init.d/ > /tmp/ExtractedInfo/initetc00.txt
#History of commands executed by the active user
history > /tmp/ExtractedInfo/history0.txt
#History of commands executed by all system users 
grep -e "$pattern" /home/*/.bash_history > /tmp/ExtractedInfo/AllHistoryCommands.txt
getent passwd | cut -d : -f 6 | sed 's:$:/.bash_history:' | xargs -d '\n' grep -s -H -e "$pattern" > /tmp/ExtractedInfo/AllHistoryCommands.txt
cat /root/.bash_history > /tmp/ExtractedInfo/historyroot00.txt
#List of users created in the system
cat /etc/passwd > /tmp/ExtractedInfo/users0.txt
#System group list
cat /etc/group > /tmp/ExtractedInfo/groups.txt
#Processes running as jobs
jobs > /tmp/ExtractedInfo/jobs0.txt
#Known SSH hosts 
cat ~/.ssh/known_hosts > /tmp/ExtractedInfo/knownhosts0.txt
#ARP table visualization
arp -a > /tmp/ExtractedInfo/arp0.txt
arp -v > /tmp/ExtractedInfo/arp00.txt
#List of connected USB devices
lsusb > /tmp/ExtractedInfo/lsusb0.txt
lsblk > /tmp/ExtractedInfo/lsblk0.txt
#List of modules loaded by the Kernel
dmesg > /tmp/ExtractedInfo/dmesg0.txt
dmesg | grep -i promisc > /tmp/ExtractedInfo/dmesg02.txt
#List of disks and system partitions
fdisk -l > /tmp/ExtractedInfo/fdisk0.txt
df -h > /tmp/ExtractedInfo/dfdisk0.txt
#Default gateway
netstat -rn > /tmp/ExtractedInfo/netstat0000.txt
#routing table 
route -n > /tmp/ExtractedInfo/route0.txt
ip route list > /tmp/ExtractedInfo/route_list0.txt
insmod > /tmp/ExtractedInfo/insmod0.txt
#List of modules loaded by the Kernel
lsmod > /tmp/ExtractedInfo/lsmod0.txt
#List of top10 processes with high memory consumption
ps auxf | sort -nr -k 4 | head -10 > /tmp/ExtractedInfo/tophighprocess0.txt
#System memory status  
vmstat > /tmp/ExtractedInfo/virtualmem0.txt
free -m > /tmp/ExtractedInfo/freemem00.txt
#Kernel and operating system version 
uname -ra > /tmp/ExtractedInfo/kernelversion0.txt
uname -srv > /tmp/ExtractedInfo/kernelversion00.txt
cat /proc/version > /tmp/ExtractedInfo/osversion.txt
cat /etc/redhat-release > /tmp/ExtractedInfo/osversion00.txt
#operating system and hostname information
hostnamectl > /tmp/ExtractedInfo/hostname0.txt
#List of running system services
systemctl list-units --type=service > /tmp/ExtractedInfo/systemctl0.txt
systemctl list-units –type=service –state=active > /tmp/ExtractedInfo/systemctl00.txt
systemctl list-units --type=service --state=running > /tmp/ExtractedInfo/systemctl000.txt
systemctl list-units --type=service > /tmp/ExtractedInfo/systemctl0.txt
service --status-all > /tmp/ExtractedInfo/daemons0.txt
systemctl list-units --type service > /tmp/ExtractedInfo/daemons01.txt
systemctl list-units --type mount > /tmp/ExtractedInfo/daemons02.txt
#extraction of system profiles - customize according to user's folder
cat /etc/profile > /tmp/ExtractedInfo/profile00.txt
cat /root/.bash_profile > /tmp/ExtractedInfo/bashprofile0.txt
cat /root/.bash_login > /tmp/ExtractedInfo/bashlogin0.txt 
cat /root/.profile > /tmp/ExtractedInfo/rootprofile.txt
cat /root/.bashrc > /tmp/ExtractedInfo/bashrcroot0.txt
cat /root/.bash_logout > /tmp/ExtractedInfo/bashlogoutroot0.txt
#List of users in the privileged sudoers file
cat /etc/sudoers > /tmp/ExtractedInfo/sudoers0.txt
#List of tasks scheduled in the system
crontab -l > /tmp/ExtractedInfo/crontab000.txt
#List of network interfaces - customize according to the operating system
cat /etc/network/interfaces > /tmp/ExtractedInfo/interfaces0.txt
#Search for executables and scripts
find / -name \*.bin > /tmp/ExtractedInfo/Executablefinder-BIN.txt
find / -name \*.exe > /tmp/ExtractedInfo/Executablefinder-EXE.txt
find / -name \*.sh > /tmp/ExtractedInfo/Executablefinder-SH.txt
find / -name \*.py > /tmp/ExtractedInfo/Executablefinder-PY.txt
find / -name \*.pl > /tmp/ExtractedInfo/Executablefinder-pl.txt
find / -name \*.csh > /tmp/ExtractedInfo/Executablefinder-csh.txt
find / -name \*.ksh > /tmp/ExtractedInfo/Executablefinder-ksh.txt
find / -name \*.tcsh > /tmp/ExtractedInfo/Executablefinder-tcsh.txt
find / -name \*.zsh > /tmp/ExtractedInfo/Executablefinder-zsh.txt
find / -name \*.rb > /tmp/ExtractedInfo/Executablefinder-rb.txt
find / -name \*.awk > /tmp/ExtractedInfo/Executablefinder-awk.txt
find / -name \*.ps1 > /tmp/ExtractedInfo/Executablefinder-ps1.txt
find / -name \*.js > /tmp/ExtractedInfo/Executablefinder-js.txt
find / -name \*.php > /tmp/ExtractedInfo/Executablefinder-php.txt
find / -name \*.vbs > /tmp/ExtractedInfo/Executablefinder-vbs.txt
find / -name \*.bat > /tmp/ExtractedInfo/Executablefinder-bat.txt
find / -name \*.cmd > /tmp/ExtractedInfo/Executablefinder-cmd.txt
#Search for files or links redirected to dev-null
lsof -w /dev/null > /tmp/ExtractedInfo/redireccion_null0.txt
find /var/log -type f -printf "%P,%A+,%T+,%C+,%u,%g,%M,%s\n" > /tmp/ExtractedInfo/VarLogTimeline.txt

# Another User Traces Create a folder to store the extracted information
mkdir /tmp/ExtractedInfo/user_traces

# Get a list of all users on the system
cut -d: -f1 /etc/passwd > /tmp/ExtractedInfo/user_traces/user_list.txt

# Iterate through each user and extract their traces
while read -r user; do
    # Create a folder for the user
    mkdir "/tmp/ExtractedInfo/user_traces/$user"

    # Extract the user's command history
    cp "/home/$user/.bash_history" "/tmp/ExtractedInfo/user_traces/$user/command_history.txt"

    # Extract the user's SSH history
    cp "/home/$user/.ssh/known_hosts" "/tmp/ExtractedInfo/user_traces/$user/ssh_history.txt"

    # Extract the user's login history
    last -n 100 "$user" > "/tmp/ExtractedInfo/user_traces/$user/login_history.txt"

    # Extract the users active processes
    ps -u "$user" > "/tmp/ExtractedInfo/user_traces/$user/active_processes.txt"

    # Extract the user's open network connections
    netstat -antp | grep "$user" > "/tmp/ExtractedInfo/user_traces/$user/network_connections.txt"

    # Extract the user's file access history
    find "/home/$user" -type f -exec stat {} \; > "/tmp/ExtractedInfo/user_traces/$user/file_access_history.txt"

done < "/tmp/ExtractedInfo/user_traces/user_list.txt"

# Compress the user traces folder
tar -czvf /tmp/ExtractedInfo/user_traces.tar.gz -C /tmp/ExtractedInfo/user_traces .

# Cleanup: Remove the temporary folder
rm -rf /tmp/ExtractedInfo/user_traces

#Internet History
# Create a folder to store the extracted information
mkdir /tmp/internet_traces

# Get a list of all users on the system
cut -d: -f1 /etc/passwd > /tmp/internet_traces/user_list.txt

# Iterate through each user and extract their internet history, traces, and DNS cache
while read -r user; do
    # Create a folder for the user
    mkdir "/tmp/internet_traces/$user"

    # Extract Chrome history
    cp "/home/$user/.config/google-chrome/Default/History" "/tmp/internet_traces/$user/chrome_history"

    # Extract Firefox history
    cp "/home/$user/.mozilla/firefox/*.default-release/places.sqlite" "/tmp/internet_traces/$user/firefox_history.sqlite"

    # Extract Chrome bookmarks
    cp "/home/$user/.config/google-chrome/Default/Bookmarks" "/tmp/internet_traces/$user/chrome_bookmarks"

    # Extract Firefox bookmarks
    cp "/home/$user/.mozilla/firefox/*.default-release/bookmarkbackups" "/tmp/internet_traces/$user/firefox_bookmarks"

    # Extract Chrome cookies
    cp "/home/$user/.config/google-chrome/Default/Cookies" "/tmp/internet_traces/$user/chrome_cookies"

    # Extract Firefox cookies
    cp "/home/$user/.mozilla/firefox/*.default-release/cookies.sqlite" "/tmp/internet_traces/$user/firefox_cookies.sqlite"
	
	# Extract the user's download history
    ls -liah /home/$user/Downloads > /tmp/internet_traces/$user/download_history/user_downloads.txt

    # Extract DNS cache
    cp "/home/$user/.config/google-chrome/Default/Network\ Action\ Predictor" "/tmp/internet_traces/$user/chrome_dns_cache"
    cp "/home/$user/.mozilla/firefox/*.default-release/Network\ Cache" "/tmp/internet_traces/$user/firefox_dns_cache"
	cp "/home/$user/.cache/mozilla/firefox/*.default-release/cache2/entries/*" "/tmp/internet_traces/$user/dns_cache_entries/"
	
done < "/tmp/internet_traces/user_list.txt"

# Compress the internet traces folder
tar -czvf /tmp/internet_traces.tar.gz -C /tmp/internet_traces .

# Cleanup: Remove the temporary folder
rm -rf /tmp/internet_traces

#Time stamps of extracted files
ls -liah /tmp/ExtractedInfo/*.txt > /tmp/ExtractedInfo/time_evidence0.txt
ls -lah /tmp/ExtractedInfo/*.txt > /tmp/ExtractedInfo/time_evidence00.txt
stat /tmp/ExtractedInfo/*.txt > /tmp/ExtractedInfo/time_evidence000.txt
ls -liah /tmp/ExtractedInfo/user_traces.tar.gz > /tmp/ExtractedInfo/time_evidence-user_traces-1.txt
stat /tmp/ExtractedInfo/user_traces.tar.gz > /tmp/ExtractedInfo/time_evidence-user_traces-2.txt

#Hash checksum calculation sha256 for integrity of each extracted file 
sha256sum /tmp/ExtractedInfo/*.txt > /tmp/ExtractedInfo/hash/hashes.txt
sha256sum /tmp/*.tar.gz > /tmp/ExtractedInfo/hash/hashes_compressed.txt
echo "--------------------------------------------------------------------------"
echo "The txt file with all the hashes has been saved to /tmp/ExtractedInfo/hash/hashes.txt"
echo "--------------------------------------------------------------------------"
echo -e "\e[1;31m!!!!!!!!!!!!!!!!!!Extraction Completed!!!!!!!!!!!!!!!!!!!\e[0m"
