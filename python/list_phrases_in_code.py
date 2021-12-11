#!/usr/bin/python3

import os
import sys
import subprocess

folder = sys.argv[2]

with open(sys.argv[1], 'r') as input_file:
    while True:
        line = input_file.readline()
        if not line:
            break
        stripped = line.strip()
        if (len(stripped) == 0):
            continue
        grep_command = ['grep', '-r', stripped, folder]
        ret = subprocess.run(grep_command, capture_output=True)
        if ret.returncode == 0:
            print(stripped)




