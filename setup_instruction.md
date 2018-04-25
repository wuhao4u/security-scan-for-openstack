**Master**:
1. install redis\
https://medium.com/@petehouston/install-and-config-redis-server-on-ubuntu-linux-16-04-3c59729e12cc
2. install RabbitMQ\
https://www.rabbitmq.com/install-debian.html\
"Using Bintray Apt Repository"
> Note we'll need to add `127.0.0.1 localhost` in the `/etc/hosts` file
3. install pip3, Django, celery
```
sudo apt --assume-yes install python3-pip
pip3 install celery
pip3 install Django
```
4. update `/etc/rc.local` file to run NFS server, RabbitMQ, Django at the system startup
5. change celery configuration, and check out code base

**Worker**:
1. check out code base
2. Run the `install.sh` script to install everything on one VM.

**Other setups**:
1. set up NFS\
https://www.digitalocean.com/community/tutorials/how-to-set-up-an-nfs-mount-on-ubuntu-16-04#step-2-%E2%80%94-creating-the-share-directories-on-the-host
2. start up celery\
can use the script files in `control_script` to simply control all workers 
3. update `/etc/rc.local` file to run NFS client, celery worker at the system startup
4. create snapshot backup for the worker, and fork multiple
