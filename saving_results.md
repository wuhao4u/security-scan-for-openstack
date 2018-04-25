## Storing output on shared drive (NFS) inside snapshot directory
If the file to be scanned was stored at 
Path-> /mnt/store/workload_52395c9b-e7a9-4e0c-a4a2-4578d105bff1/snapshot_1a04bb46-de77-4511-909f-2eacaf562592/vm_id_56e22431-d49c-41d3-8fa9-7846a9ea1e1b/vm_res_id_dc9a1d3f-3c68-492f-9da1-7ae161af648a_vda/195f6d48-fa65-4895-b48e-af203b82836c

Then the above result of scan in json formatted output file will be stored at /mnt/store/workload_52395c9b-e7a9-4e0c-a4a2-4578d105bff1/snapshot_1a04bb46-de77-4511-909f-2eacaf562592.

***Thus result of each scan is stored inside workload_abc/snapshot_xyz/scans folder.***

And each such file is store with this name convention : **inputFileName_YYYYMMDD-HHMMSS**

example for above path it will be something like 195f6d48-fa65-4895-b48e-af203b82836c_20180330-024343
