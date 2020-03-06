import json
import requests

# 更改下面三个参数
ip = "192.168.100.17"
user = "Admin"
password = "zabbix"

base_url = 'http://' + ip + '/zabbix/api_jsonrpc.php'
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

# 下面的JRPC请求内容最好放在另一个文件，以导入的方式使用
# 获取某个主机信息
post_data_get_host_info = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "filter": {
            "host": [
                "192.168.100.12"
            ]
        }
    },
    "auth": token_value,
    "id": 1
}

# 获取所有主机
post_data_get_all_hosts = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": ["host"]
    },
    "auth": token_value,
    "id": 1
}

# 获取所有用户信息
post_data_get_all_users = {
    "jsonrpc": "2.0",
    "method": "user.get",
    "params": {
        "output": ["extend"]
    },
    "auth": token_value,
    "id": 1
}

# 获取该主机所属的主机组
post_data_get_group = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": ["hostid"],
        "selectGroups": "extend",
        "filter": {
            "host": [
                "192.168.100.12"
            ]
        }
    },
    "auth": token_value,
    "id": 1
}

# 获取某ID主机关联的模板
post_data_get_tmplate = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": ["hostid"],
        "selectParentTemplates": [
            "templateid",
            "name"
        ],
        "hostids": "10277"
    },
    "id": 1,
    "auth": token_value
}

# 获取模板信息
post_data_get_tmplate_info = {
    "jsonrpc": "2.0",
    "method": "template.get",
    "params": {
        "output": "extend",
        "filter": {
            "host": [
                "Template-Percona-MySQL-stevenux-cus"
]
        }
    },
    "auth": token_value,
    "id": 1
}

post_list = [post_data_get_host_info,
             post_data_get_all_hosts,
             post_data_get_all_users,
             post_data_get_tmplate,
             post_data_get_tmplate_info,
             post_data_get_group]

for p in post_list:
    return_data = requests.post(base_url, data=json.dumps(p), headers=post_header)
    print(json.dumps(json.loads(return_data.text),
                     sort_keys=True,
                     indent=4,
                     separators=(',', ': ')
                     )
          )
