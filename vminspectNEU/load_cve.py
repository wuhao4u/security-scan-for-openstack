import os
import os.path
import zipfile
import json
import requests
import re
import errno
import redis
from collections import defaultdict


def dl_remote(local_path):
    if not os.path.exists(local_path):
        try:
            os.makedirs(local_path)
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
    r = requests.get('https://nvd.nist.gov/vuln/data-feeds#JSON_FEED')
    for filename in re.findall("nvdcve-1.0-.*\.json\.zip", r.text):
        r_file = requests.get("https://static.nvd.nist.gov/feeds/json/cve/1.0/" + filename, stream=True)
        with open(local_path + filename, 'wb+') as f:
            for chunk in r_file:
                f.write(chunk)
        archive = zipfile.ZipFile(local_path + filename, 'r')
        archive.extractall(local_path)
        archive.close()
        os.remove(local_path + filename)


def load_local(cvepath):
    files = [f for f in os.listdir(cvepath) if os.path.isfile(os.path.join(cvepath, f))]
    files.sort()

    cve_dict = defaultdict(list)
    for file in files:
        jsonfile = open(cvepath + "/" + file)
        file_dict = json.loads(jsonfile.read())
        for k, v in file_dict.items():
            cve_dict[k] += v
        jsonfile.close()
    return cve_dict


def save_cve_to_redis(cve_dict):
    # save the cve into database 0
    r = redis.StrictRedis(host='128.31.25.222', port=6379, db=0)
    cve_feed = cve_dict['CVE_Items']
    for cve in cve_feed:
        cve_id = cve['cve']["CVE_data_meta"]["ID"]
        r.set(cve_id, json.dumps(cve))


def save_app_cve_map_to_redis(cve_dict):
    # save the mapping into database 1
    r = redis.StrictRedis(host='128.31.25.222', port=6379, db=1)
    cve_feed = cve_dict['CVE_Items']
    for cve in cve_feed:
        cve_id = cve['cve']["CVE_data_meta"]["ID"]
        vendor_list = cve['cve']['affects']['vendor']['vendor_data']
        for vendor in vendor_list:
            for product in vendor['product']['product_data']:
                product_name = product['product_name'].lower()
                r.sadd(product_name, cve_id)


if __name__ == '__main__':
    dl_remote('/mnt/bigdisk/cve_db')
    print("finished downloading cve database")
    cve_dict = load_local('/mnt/bigdisk/cve_db')
    save_cve_to_redis(cve_dict)
    print("finished saving cve")
    save_app_cve_map_to_redis(cve_dict)
    print("finished saving app cve mapping")
