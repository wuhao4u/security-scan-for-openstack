#!/bin/bash

while read worker_ip
do
    echo "ssh to ${worker_ip} ..."
    scp -i ~/.ssh/id_rsa worker.sh ubuntu@${worker_ip}:/home/ubuntu/Security-Scan-for-OpenStack > /dev/null 2>&1
    echo "start celery ..."
    ssh -i ~/.ssh/id_rsa ubuntu@${worker_ip} "screen -d -m sh /home/ubuntu/Security-Scan-for-OpenStack/worker.sh" < /dev/null
    #ssh -i ~/.ssh/id_rsa ubuntu@${worker_ip} "cd /home/ubuntu/Security-Scan-for-OpenStack/ && rm -r test111111" </dev/null
done<worker_list
