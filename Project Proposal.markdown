# Security Scan for OpenStack Project Proposal
### Clara De Paolis, Dilip Makwana, Hao Wu, Chi Zhang

## I. Background/Motivation
OpenStack is an open-source software platform for deploying and managing cloud environments. More than 500 companies[1] are involved in sponsoring and developing OpenStack. OpenStack provides APIs to its various components, but it also provides a dashboard for cloud administrators to easily see and manage the status of their environments. The API for one component of OpenStack, Cinder, allows for building a pipeline for saving volume snapshots of VMs. However, during this backup process the VM must be taken offline, which interferes with applications[2].

Trilio Data provides business assurance platform for IT organizations and cloud service providers deploying application workloads in the cloud. Trilio provides native backup services for OpenStack environments. Importantly, these backups are performed without interrupting running workloads[2]. In order to meet the needs of reliable recovery on complex environment such as Financial, Healthcare, and many other secure-sensitive services, the company intends to provide a better security scanning solution on the backup files. 

Our team will design and develop an intuitive web service for clients to perform security scans, vulnerability checks towards their backup files. We hope through a deeper integration with current security scanning technologies and Tilio’s current backup service, we will offer a simple, fast and reliable security solution to protect clients’ invaluable data.

## II. Goals
1. Develop a service to perform security scan on the backup image files. It will be integrated into Trilio Data System as a plugin. \
a. Specifically scan for QCOW2 format\
b. Based on existing scanning tools
    * ~~Libguestfs, for load VM images~~ (we have decided not to load VM images)
    * VMInspect, inspecting VM disk images

2. Perform security scan on the images using common security tools\
a. CVE-Search\
A tool to import Common Vulnerabilities and Exposures into a MongoDB for searching and processing CVEs <br/>
b. ~~**Nessus** & Open VAS\
Vulnerability scanners for live servers<br/>~~
c. Bandit\
Static analyzer for Python code

3. Minimum Viable Product\
a. Scan the snapshots for security purposes and prepare reports to show the clients the vulnerabilities\
b. Ideally, showing scanning results using data visualization technologies in the web form

## III. Evaluation
1. Minimum acceptance criteria is to build the service which identifies the vulnerabilities with given snapshots.\
a. Support scanning on one QCOW2 format snapshot\
b. Scanning using at least one Common Vulnerabilities and Exposures (CVE) database for our scanning reference\
c. Show the client scanning results with texts and other stats

2. Stretch goals:\
a. Support scanning on multiple snapshots simultaneously\
b. Use multiple CVE databases for scanning references\
c. Having a user-friendly front-end page for displaying results and better user interactions.

## IV. Solution Concept
Key Components:
1. Users
2. OpenStack dashboard - dashboard to configure OpenStack 
3. **Trilio Service/Plugin** - plugin of the service we are building  (responsibility of our project)
4. Cloud VM Snapshot - backup image file taken by Trilio from the client
5. Vulnerability Databases (e.g., NVD) - Database to be access by service for Vulnerabilities
6. Scanning tools
7. Data Visualization Tools - e.g. D3.js

![alt text](https://github.com/BU-NU-CLOUD-SP18/Security-Scan-for-OpenStack/blob/master/Architecture%20for%20Trilio%20Service.png "Hover text")
Figure 1: 
Trilio’s service regarding an OpenStack environment [3]

![alt text](https://github.com/BU-NU-CLOUD-SP18/Security-Scan-for-OpenStack/blob/master/Architecture%20for%20Security%20Scan.jpg "Hover text")
Figure 2: 
Our solution will be presented as a web application, which will interact with Trilio’s existing functions through RESTful API. The scanning process can be either on-demand or event-driven: users can choose to run scanning on specific images after backup is done, and scannings will also be run automatically when there are new backups. *And since there might be thousands of images once the backup is done, scaling must be considered in our solution. We are plannig to use RabbitMQ for task distribution and Containers for horizontal scaling. (under discussion)*

**Functionalities of Security Scan Service**:
1. Showing the detectable files in the snapshot\
a. Size\
b. Path\
c. Sha1\
d. Type
2. Identify known malwares in the snapshot
3. Query 3rd party services to check the eligibility of a file in the snapshot
    - E.g., VirusTotal
4. Scan applications using 3rd party CVE databases
5. Showing event logs in the snapshot
    - Also find possible vulnerabilities in the logs

## V. Timeline
Sprint 1: 19 Jan 2018-02 Feb 2018
1. Work on Initial project proposal.
2. Identify Service goals/requirements.
3. Research related security scanning technologies, libraries and tools.

Sprint 2: 02 Feb 2018-09 Feb 2018
1. Setup a proof of concept environment on Mass Open Cloud
2. Access snapshots provided by Trilio and understand how to work with the POC environment
3. Design a Restful API standard based on Trilio’s 

Sprint 3: 09 Feb 2018-23 Feb 2018
1. Scan snapshots to understand cloud environment when snapshot was taken
2. Aggregate collected scanning results from different vulnerability scanning software

Sprint 4: 23 Feb 2018-16 Mar 2018
1. Evaluate different vulnerability scanners that were tested in previous sprint

Sprint 5: 16 Mar 2018-30 Mar 2018
1. Implement and test RESTful API designed in sprint 2

Sprint 6: 30 Mar 2018-13 Apr 2018
1. Generate a user friendly report based on the scanning result using data visualization tools
2. Present the reports to the clients (Trilio) and gain feedback from clients

Sprint 7: 13 Apr 2018-20 Apr 2018
1. Improvement based on feedback received.


### References:
[1] https://www.openstack.org/foundation/companies/  
[2] “OpenStack Backup and Recovery Business Assurance Platform White Paper,” 2016. https://www.trilio.io/whitepaper/  
[3] Figure 1. Data Protection & Backup as a Service for OpenStack clouds - TrilioVault. (n.d.). Retrieved January 29, 2018, from https://www.trilio.io/triliovault/
