# Storing the results of viminspect scan 

*refer vulnscan_use.md for usage instruction of vminspect.*



#### Storing output on shared drive (NFS) inside snapshot directory

Results obtained after scanning each cow image file are stored inside scans/ folder under the snapshot to which the qcow image was read from.

ie. workload_abc/snapshot_xyz/scans folder.



One sample example.



If the file to be scanned was stored at path on NFS drive /mnt/store/workload_52395c9b-e7a9-4e0c-a4a2-4578d105bff1/snapshot_1a04bb46-de77-4511-909f-2eacaf562592/vm_id_56e22431-d49c-41d3-8fa9-7846a9ea1e1b/vm_res_id_dc9a1d3f-3c68-492f-9da1-7ae161af648a_vda/195f6d48-fa65-4895-b48e-af203b82836c



Then the result of scan in json formatted output file will be stored at /mnt/store/workload_52395c9b-e7a9-4e0c-a4a2-4578d105bff1/snapshot_1a04bb46-de77-4511-909f-2eacaf562592.



And each such file is store with this name convention : **inputFileName_YYYYMMDD-HHMMSS** .

For above path it will be something like 195f6d48-fa65-4895-b48e-af203b82836c_20180330-024343

```json
{
	"workload_id" : "52395c9b-e7a9-4e0c-a4a2-4578d105bff1",
	"snapshot_id" : "1a04bb46-de77-4511-909f-2eacaf562592",
	"vm_id" : "56e22431-d49c-41d3-8fa9-7846a9ea1e1b",
	"vm_res_id" : "dc9a1d3f-3c68-492f-9da1-7ae161af648a_vda",
	"results" : [
    	{
			name :  "apt",
			version :  "1.2.24",
			vulnerabilities : [
				{
					configurations : {
						CVE_data_version :  "4.0",
						nodes : [ ... ]
					},
					impact : {
						baseMetricV2 : { ... },
						baseMetricV3 : { ... }
					},
					lastModifiedDate :  "2017-12-20T20:44Z",
					publishedDate :  "2017-12-05T16:29Z",
					cve : {
						data_format :  "MITRE",
						CVE_data_meta : {
							ASSIGNER :  "cve@mitre.org",
							ID :  "CVE-2016-1252"
						},
						data_version :  "4.0",
						problemtype : { ... },
						description : {
							description_data : [
							{
								lang :  "en",
								value :  "The apt package in Debian jessie before 1.0.9.8.4, in Debian unstable before 1.4~beta2, in Ubuntu 14.04 LTS before 1.0.1ubuntu2.17, in Ubuntu 16.04 LTS before 1.2.15ubuntu0.2, and in Ubuntu 16.10 before 1.3.2ubuntu0.1 allows man-in-the-middle attackers to bypass a repository-signing protection mechanism by leveraging improper error handling when validating InRelease file signatures."
							}
							]
						},
						data_type :  "CVE",
						references : { ... },
						affects : { ... }
					}
				}
			]
		},	
        {...},
    	{...}
    ]
}    
```

