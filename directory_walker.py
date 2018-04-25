#!/usr/bin/python

import os
import sys

start_dir = "."
if len(sys.argv) > 1:
    start_dir = sys.argv[1]

# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk(start_dir):
    path = root.split(os.sep)
    print((len(path) - 1) * '---', os.path.basename(root))
    for file in files:
        print(len(path) * '---', file)
