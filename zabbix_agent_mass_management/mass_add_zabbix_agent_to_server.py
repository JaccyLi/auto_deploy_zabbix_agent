import json
import requests

# 更改下面三个参数
server_ip = "192.168.100.17"
user = "Admin"
password = "zabbix"

# 要添加的主机列表
agent_list = ["192.168.100.12",
              "192.168.100.20",
              "192.168.100.22",
              "192.168.100.24"]

base_url = 'http://' + server_ip + '/zabbix/api_jsonrpc.php'
post_header = {'Content-Type': 'application/json'}

post_data_login = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": user,
        "password": password
    },
    "id": 1
}

login = requests.post(base_url, data=json.dumps(post_data_login), headers=post_header)
return_token = json.loads(login.text)
token_value = return_token['result']

# 添加主机
for ip in agent_list:
    post_data_add_host = {
        "jsonrpc": "2.0",
        "method": "host.create",
        "params": {
            "host": "redis-server-" + ip,
            "interfaces": [
                {
                    "type": 1,
                    "main": 1,
                    "useip": 1,
                    "ip": ip,
                    "dns": "",
                    "port": "10050"
                }
            ],
            "groups": [
                {
                    "groupid": "15"
                }
            ],
            "templates": [
                {
                    "templateid": "10270"
                }
            ],
        },
        "auth": token_value,
        "id": 1
    }
    return_data = requests.post(base_url, data=json.dumps(post_data_add_host), headers=post_header)
    print(json.dumps(json.loads(return_data.text),
                     sort_keys=True,
                     indent=4,
                     separators=(',', ': ')
                     )
          )
