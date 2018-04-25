# Copyright (c) 2016-2017, Matteo Cafasso
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.

# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.

# 3. Neither the name of the copyright holder nor the names of its contributors
# may be used to endorse or promote products derived from this software without
# specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,
# OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT
# OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import json
import time
import os


def store_scan_results(arguments, results):
    # file output specific code
    #outputDict = {}
    workloadStartIndex = arguments.disk.find('/workload')
    INPUT_FILE_NAME = arguments.disk.replace("/", "_")
    timestr = time.strftime("%Y%m%d-%H%M%S")
    if workloadStartIndex != -1:
        workloadString = arguments.disk[workloadStartIndex:]
        splitlist = workloadString[1:].split('/')
        WORKLOAD_METADATA = splitlist[0]
        SNAPSHOT_METADATA = splitlist[1]
        VM_ID_METADATA = splitlist[2]
        VM_RES_ID_METADATA = splitlist[3]
        INPUT_FILE_NAME = "vm_" + splitlist[4]
        # prepare dict to be written to file
        #outputDict["workload_id"] = WORKLOAD_METADATA.split("workload_")[1]
        #outputDict["snapshot_id"] = SNAPSHOT_METADATA.split("snapshot_")[1]
        #outputDict["vm_id"] = VM_ID_METADATA.split("vm_id_")[1]
        #outputDict["vm_res_id"] = VM_RES_ID_METADATA.split("vm_res_id_")[1]
        #outputDict["scanned_file"] = INPUT_FILE_NAME

        # find path of snapshot__ folder
        snapshotPath = arguments.disk[:arguments.disk.find("/vm_id")]
    else:
        # else scan was called from outside trilio folder structure, so
        # scans folder is created in current directory
        snapshotPath = os.getcwd()

    # create /scans folder inside snapshot directory if not there
    outFilePath = snapshotPath + "/scans/"
    if not os.path.exists(outFilePath):
        try:
            os.makedirs(outFilePath)
        except OSError as err:
            raise err
    outFilePath = outFilePath + INPUT_FILE_NAME + "_" + timestr

    if results is not None:
        # embed json results in dict
        #resultDict  = {"results": results}
        #outputDict.update(resultDict)
        print("############save scanning result to: " + outFilePath + "#############")
        with open(outFilePath, 'w+') as outfile:
            #outfile.write(json.dumps(outputDict, indent=4))
            outfile.write(results)
