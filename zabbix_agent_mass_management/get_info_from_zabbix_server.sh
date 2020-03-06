#!/bin/bash
# a example for to interact with zabbix server
# Edited by suosuoli.cn on 2020.03.06
#

# modify the three params to use
USER="Admin"
PASS="zabbix"
ZABBIX_SERVER_IP="192.168.100.17"

TOKEN=$(curl -s -X POST -H 'Content-Type:application/json' -d '{
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {"user": "'${USER}'",
               "password": "'${PASS}'"
              },
    "id": 1
}' http://"${ZABBIX_SERVER_IP}"/zabbix/api_jsonrpc.php | python3 -m json.tool | grep "result" | \
	awk -F"\"" '{print $4}')

curl -s -X POST -H 'Content-Type:application/json' -d '{
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": ["host"]
    },
    "auth": "'${TOKEN}'",
    "id": 1
}' http://"${ZABBIX_SERVER_IP}"/zabbix/api_jsonrpc.php | python3 -m json.tool

