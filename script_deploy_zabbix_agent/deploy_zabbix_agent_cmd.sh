#!/bin/bash
#
# Edited by suosuoli.cn on 2020.03.06
#

HOSTS="$1"
DEPLOY_TAR="zabbix_agent_deploy.tar.gz"
ZABBIX_COMPILE_SCRIPT="compile_install_zabbix.sh"
CMD1="cd /usr/local/src && tar -xf zabbix_agent_deploy.tar.gz"
CMD2="bash /usr/local/src/compile_install_zabbix.sh"


rpm -q expect &> /dev/null || yum -y install expect

if [[ ! -f /root/.ssh/id_rsa ]]; then
    ssh-keygen -P "" -f "/root/.ssh/id_rsa"
fi

userpwd="stevenux"
while read ipaddr;do
expect <<EOF
set timeout 100
spawn ssh-copy-id $ipaddr
expect {
"yes/no" {send "yes\n"; exp_continue}
"password" {send "$userpwd\n"}
}
spawn scp ${DEPLOY_TAR} ${ipaddr}:/usr/local/src 
spawn ssh "${ipaddr}" "${CMD1}"
spawn ssh "${ipaddr}" "${CMD2}"
expect eof
EOF
done < ${HOSTS}
