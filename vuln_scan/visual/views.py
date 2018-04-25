# Create your views here.
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
import json
import os

ROOT_DIR = "/mnt/bigdisk"
# ROOT_DIR = "/Users/HappyMole/Desktop"


def index(request):
    return HttpResponse("Hello, world. You're at the visual index.")


def workload(request, workload_id):
    workload_dir = os.path.join(ROOT_DIR, workload_id)
    snapshot_ids = [p for p in os.listdir(workload_dir) if os.path.isdir(os.path.join(workload_dir, p))]
    res_dict = dict()
    for snapshot_id in snapshot_ids:
        snapshot_dir = os.path.join(workload_dir, snapshot_id)
        scan_res_dir = os.path.join(snapshot_dir, "scans")
        if os.path.exists(scan_res_dir) and len(os.listdir(scan_res_dir)) != 0:
            res_dict[snapshot_id] = [snapshot_id + "/" + p for p in os.listdir(scan_res_dir)]

    return render(request, "visual/workload.html", {"data": res_dict})


def detail(request, workload_id, snapshot_id, vm_id):
    with open(os.path.join(ROOT_DIR, workload_id, snapshot_id, "scans", vm_id)) as file:
        data = file.read()
        json_obj_list = json.loads(data)

        severity_summary = {
            "HIGH": 0,
            "MEDIUM": 0,
            "LOW": 0,
            "UNKNOWN": 0
        }
        scan_results = list()
        vuln_count = dict()
        for json_obj in json_obj_list:
            app_name = json_obj["name"]
            app_version = json_obj["version"]
            vuln_list = json_obj["vulnerabilities"]
            vuln_count[app_name] = len(vuln_list)

            app_scan_results = []
            for vuln in vuln_list:
                published_date = vuln["publishedDate"]
                last_modified_date = vuln["lastModifiedDate"]
                cve_id = vuln["cve"]["CVE_data_meta"]["ID"]
                desc = ""
                for desc_data in vuln["cve"]["description"]["description_data"]:
                    if desc_data["lang"] == "en":
                        desc = desc_data["value"]
                metric = vuln["impact"]["baseMetricV2"]
                vector = ""
                if "cvssV2" in metric:
                    vector = metric["cvssV2"]["accessVector"]
                severity = metric["severity"]
                severity_score = -1
                if severity == "HIGH" or severity == "MEDIUM" or severity == "LOW":
                    severity_summary[severity] += 1
                    if severity == "HIGH":
                        severity_score = 3
                    elif severity == "MEDIUM":
                        severity_score = 2
                    else:
                        severity_score = 1
                else:
                    severity_summary["UNKNOWN"] += 1

                exploitability_score = metric["exploitabilityScore"]
                impact_score = metric["impactScore"]

                scan_res = {
                    "app_name": app_name,
                    "app_version": app_version,
                    "cve_id": cve_id,
                    "description": desc,
                    "vector": vector,
                    "published_date": published_date,
                    "last_modified_date": last_modified_date,
                    "severity": severity,
                    "exploitability_score": exploitability_score,
                    "impact_score": impact_score,
                    "severity_score": severity_score
                }

                app_scan_results.append(scan_res)
            app_scan_results = sorted(app_scan_results, key=lambda r: r["severity_score"], reverse=True)
            app_scan_results[0]["is_first"] = True
            scan_results += app_scan_results

    return render(request, "visual/scan_report.html",
                  {"scan_results": scan_results,
                   "severity_summary": severity_summary,
                   "vuln_count": vuln_count})
