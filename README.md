# auto_deploy_zabbix_agent

Using script deploy zabbix agent and ansible deploy zabbix agent.

## 使用脚本自动化部署多个zabbix agent主机

使用脚本时，查看一下`compile_install_zabbix.sh`，以便自定义安装目录等

```bash
root@ubuntu-suosuoli-node1:/usr/local/src/auto_deploy_zabbix_agent/script_deploy_zabbix_agent# tar -tf zabbix_agent_deploy.tar.gz 
./compile_install_zabbix.sh  # 查看一下这个文件
./zabbix-4.0.15.tar.gz
./zabbix_agentd.conf
./zabbix_agentd.conf.d/
./zabbix_agentd.conf.d/get_memcache_status.sh
./zabbix_agentd.conf.d/get_nginx_status.sh
./zabbix_agentd.conf.d/get_redis_status.sh
./zabbix_agentd.conf.d/get_tcp_status.sh
./zabbix_agentd.conf.d/customizedParams.conf
./zabbix-agent.service
```

## 使用ansible自动化部署多个zabbix agent主机

使用ansible部署时，在`/etc/ansible/hosts`添加要部署的主机列表即可，
下列两个文件放在同一个目录，执行`ansible-playbook zabbix_agent deploy_zabbix_agent.yaml`
就可以自动部署，前提是需要部署的主机于ansible主控制机使用key已经可以通讯。

```bash
-rw-r--r-- 1 root root      404 Mar  6 00:32 deploy_zabbix_agent.yaml
-rw-r--r-- 1 root root 17089145 Mar  5 22:06 zabbix_agent_deploy.tar.gz
```
