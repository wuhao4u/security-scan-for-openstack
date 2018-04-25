import os
import json
import magic

class WorkloadDB:
    '''Trilio Workload Info'''
    display_name = ""
    host = ""
    workload_id = ""
    project_id = ""
    updated_at = ""
    user_id = ""

    def __init__(self, path_to_dir, filename):
        with open(path_to_dir + os.sep + filename) as json_data:
            wj = json.load(json_data)
            self.display_name = (wj["display_name"])
            self.host = (wj["host"])
            self.workload_id = (wj["id"])
            self.project_id = (wj["project_id"])
            self.updated_at = (wj["updated_at"])
            self.user_id = (wj["user_id"])

class SnapshotDB:
    '''Trilio Snapshot Info'''
    host = ""
    sid = ""

    def __init__(self, path_to_dir, filename):
        with open(path_to_dir + os.sep + filename) as json_data:
            sj = json.load(json_data)
#            print(json.dumps(sj, indent=4, sort_keys=True))
            self.sid = (sj["host"])
            self.sid = (sj["id"])

def is_workload_db(path_to_dir, filename):
    magic_desc = magic.from_file(path_to_dir + os.sep + filename)
    if magic_desc[:10] == "ASCII text" and filename == "workload_db":
        return True
    else:
        return False

def is_snapshot_db(path_to_dir, filename):
    magic_desc = magic.from_file(path_to_dir + os.sep + filename)
    if magic_desc[:10] == "ASCII text" and filename == "snapshot_db":
        return True
    else:
        return False

def is_resources_db(path_to_dir, filename):
    magic_desc = magic.from_file(path_to_dir + os.sep + filename)
    if magic_desc[:10] == "ASCII text" and filename == "resources_db":
        return True
    else:
        return False

def is_qcow_image(path_to_dir, filename):
    magic_desc = magic.from_file(path_to_dir + os.sep + filename)
    if magic_desc[:9] == "QEMU QCOW":
        return True
    else:
        return False



