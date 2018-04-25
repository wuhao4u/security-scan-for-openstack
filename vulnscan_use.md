# Using vminspect vulnscan

## Overview
Code from [vminspect](https://github.com/noxdafox/vminspect) has been forked and modified for use in this project.  vminspect uses libguestfs to read disk images in qcow2 format and find applications installed in that system. The function vulnscan provided by vminspect searched a vulnerability database to check for vulnerabilities in installed applications.

The original code for vminspect's function vulnscan made calls to a remote vulnerability service API to and for each vulnerability that was found, it reported the CVE ID number and a text description of the vulnerability.  

Here, we use the datafeed from the [NVD CVE database](https://nvd.nist.gov/vuln/data-feeds) instead. If the data exists locally, it can be loaded into the vulnscan function. If not, or if the files need to be updated, the feed is downloaded, the files unzipped, and then loaded.


## Use
To scan the disk image `image.qcow2` for vulnerabilities using the vulnerability database in `/path/to/local/cveDB/`:  
`python inspector.py vulnscan /path/to/local/cveDB/ image.qcow2`  

or, to download the datafeed from NVD and then scan the same image:       
`python inspector.py vulnscan -r /path/to/save/cveDB/ image.qcow2`   
    
The flag `-r` is used to download (or update) the NVD CVE database from the remote feed 

## Output
We output in json format a list of all the installed application, their version, and the associated vulnerabilities. This is similar to the original vminspect vulnscan, except the structure of the vulnerabilities field is different and includes more information. In particular, for each vulnerability we include all the information from the NVD CVE database for the corresponding CVE entry. Below is an example of the output. Some fields are collapsed for compactness. For all the fields available, refer to the [NVD CVE feed json schema](https://csrc.nist.gov/schema/nvd/feed/0.1/nvd_cve_feed_json_0.1_beta.schema). 


	[
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