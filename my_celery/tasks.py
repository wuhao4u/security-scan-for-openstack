from __future__ import absolute_import
from my_celery.celery import app
import time
import subprocess
import vminspectNEU
import time

@app.task
def vminspect_scan(image_path, redis_addr):
    #print("#########################################################")
    print("perform security scanning on " + image_path)

    subprocess.run(["sudo", "python3",
        "/home/ubuntu/Security-Scan-for-OpenStack/vminspectNEU/inspector.py", "vulnscan",
        redis_addr, image_path, "-c", "30"])
    #with vminspectNEU.VulnScanner(image_path, redis_addr) as vulnscanner:
    #    res = [r._asdict() for r in vulnscanner.scan(10)]
    #    print(res)
