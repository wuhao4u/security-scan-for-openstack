# Security Scan for OpenStack
### Team Trilio
###### - This is the repo for the course _[CS 6620 Cloud Computing 18Sp](https://okrieg.github.io/EC500/index-spring-2018.html)_.

#### Project Description:
Security scans are integral process of any Commercial account, specifically the Financial Services industry. Security teams can either scan end-point devices or target data repositories. Trilio is a native OpenStack Cloud data protection software technology, that creates a snapshot of the production environment, making it easy to restore an entire workload/environment with a single click. Trilio exposes these snapshots to 3rd party applications so that organizations can use the solution for Security, BC/DR, and other solutions.

_[Read More About The Project](https://docs.google.com/document/d/1LkbUpa9Y5I7E5Jl6rSxW-cwVX2mcfOEAt8WZmHtdACQ/edit?usp=sharing)_

_[See our project proposal here](https://github.com/BU-NU-CLOUD-SP18/Security-Scan-for-OpenStack/blob/master/Project%20Proposal.markdown)_

#### Overview
This project is a tool to scan these backups for vulnerabilities in installed applications using a vulnerability database.

* We have built on an existing tool, [vminspect](https://github.com/noxdafox/vminspect) to read the VM backup images and find installed applications and search the vulnerability database
    - Our modified code uses instead a local copy of the NVD CVE datafeed as the vulnerability database and provides for each vulnerability its full entry in the database. This yields much more information on each vulnerability
    - See [vulnscan_use.md](vulnscan_use.md) for more details
* Our tool schedules running these scans on all VM images in a workload using [Celery](https://github.com/celery/celery/) and [RabbitMQ](https://github.com/rabbitmq)
* Scanning results are augmented with metadata about the image that was scanned and saved to the workload directory. 
    - See [saving_results.md](saving_results.md) for more details

#### Using this code
##### Setting up environment and dependencies
[setup_instruction.md](setup_instruction.md)
##### Running code
Once the environement is set up, run the vulnerability scanner   
on each worker VM: `celery worker -l info -A my_celery.tasks --concurrency=3`  
on the master VM: `python securityscan.py [workload_path] [redis_DB_IP]`  

##### Using results
Scan results are saved to corresponding snapshot directory in NFS. 
Results can also be browsed visually using the visualization front-end. ANd example is shown here:

![front end example](https://raw.githubusercontent.com/BU-NU-CLOUD-SP18/Security-Scan-for-OpenStack/master/front_end.JPG?token=ASiuI1hOdu8uFG13yAHwOO2XJydhNDrdks5a6Lc6wA%3D%3D)

### System Diagram
<img src="https://raw.githubusercontent.com/BU-NU-CLOUD-SP18/Security-Scan-for-OpenStack/master/CC_sys_diagram.png?token=ASiuI0WRRmK-SjEksujWKvhTdE7SsBt6ks5a6Ld1wA%3D%3D" width="600">


### Collaborators
* [claradepaolis](https://github.com/claradepaolis) - **Clara De Paolis Kaluza**  &lt;depaoliskaluza.m at husky.neu.edu&gt;

* [dilip7](https://github.com/dilip7) - **Dilip Makwana**  &lt;makwana.d at husky.neu.edu&gt;

* [wuhao4u](https://github.com/wuhao4u) - **Hao Wu**  &lt;wu.hao2 at husky.neu.edu&gt;

* [Chi Zhang](https://github.com/Fredy-Z) - **Chi Zhang**  &lt;zhang.chi12 at husky.neu.edu&gt;

