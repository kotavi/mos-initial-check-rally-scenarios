#!/usr/bin/python

import argparse
import glob
import os

parser = argparse.ArgumentParser()
parser.add_argument('--path', help='path to .yaml files, if specified then scenarios will be combined '
                                   'only for the specific component (e.g. nova)')
parser.add_argument('--filename', help='name of a new file where all scenarios will be stored')

args = parser.parse_args()
path = args.path
file_name = args.filename

# remove file if exists
if os.path.isfile(file_name):
    print(os.path.isfile(file_name))
    os.system('rm ' + file_name)

# check path
if path is not None:
    files = glob.glob(path + '*.yaml')
else:
    files = glob.glob("*/" + '*.yaml')

# write scenarios to a temporary file
temp_file = open('temp.file', 'w')
for afile in files:
    data = open(afile).read()
    temp_file.write(data)
    temp_file.write('\n\n')
temp_file.close()

# rewrite data to another file and remove lines with '---'
all_yaml_scenarios_file = open(file_name, 'w')
if os.access('temp.file', os.R_OK):
    with open('temp.file', 'r') as fn:
        # to leave the first '---' from deleting
        first_line = fn.readline()
        all_yaml_scenarios_file.write(first_line)
        for line in fn:
            if '---' not in line:
                all_yaml_scenarios_file.write(line)

all_yaml_scenarios_file.close()
os.system('rm temp.file')
