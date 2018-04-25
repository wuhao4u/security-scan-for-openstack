import argparse
import sys
import os
from trilio_file_util import *
import vminspectNEU
# using python-magic library, not filemagic
import magic
import my_celery

def scan_workload(root_path, redis_addr):
    wdb = None
    sdb = None
    ddb = None
    scan_res_dir = os.path.join(root_path, "scan-res")

    image_files = []
    for cur_path, dirs, files in os.walk(root_path):
        for filename in files:
            if is_snapshot_db(cur_path, filename):
                sdb = SnapshotDB(cur_path, filename)
                # create a scanning result folder in the same dir
                if not os.path.exists(scan_res_dir):
                    os.makedirs(scan_res_dir)
            elif is_workload_db(cur_path, filename):
                wdb = WorkloadDB(cur_path, filename)
            elif is_qcow_image(cur_path, filename):
                # TODO: do the scanning
                
                img_path = cur_path + os.sep + filename
                print("Found image: ", img_path)
                image_files.append(img_path)

    my_celery.run_tasks.run(image_files, redis_addr)


def scan_image(img_path, redis_addr):
    my_celery.run_tasks.run([img_path], redis_addr)
    

def main():
    parser = argparse.ArgumentParser(description="Perform security scan for qcow3 images.")
    parser.add_argument("workloadpath", type=str, help="a path string to the workload directory.")
    parser.add_argument("redisaddr", type=str, help="the ip and port of the redis server that saves the cve data, in the format of ip:port. If the port is not provided, it will be the default value 6379")
    parsed_args = parser.parse_args()

    if os.path.isfile(parsed_args.workloadpath):
        scan_image(parsed_args.workloadpath, parsed_args.redisaddr)
    else:
        scan_workload(parsed_args.workloadpath, parsed_args.redisaddr)

if __name__ == "__main__":
    main()
