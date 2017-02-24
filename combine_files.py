"""
python combine_files.py cinder/ cinder_scenarios.yaml
1. deletes file cinder_scenarios.yaml if it exists
2. collects all the yaml files to the list
3. writes data from all files to temp.file
4. removes lines with '---' except the first one and writes it to sys.argv[2] file
5. deletes temp.file file

"""

import sys
import glob
import os

path = sys.argv[1]
file_name = sys.argv[2]

if os.path.isfile(file_name):
    print(os.path.isfile(file_name))
    os.system('rm ' + file_name)

files = glob.glob(path + '*.yaml')

temp_file = open('temp.file', 'w')

for afile in files:
    if 'task_arguments' in afile:
        continue
    else:
        data = open(afile).read()
        temp_file.write(data)
        temp_file.write('\n\n')
temp_file.close()

all_yaml_scenarios_file = open(file_name, 'w')

if os.access('temp.file', os.R_OK):
    with open('temp.file', 'r') as fn:
        # to leave the first '---' from deleting
        first_line = fn.readline()
        all_yaml_scenarios_file.write(first_line)
        for line in fn:
            if '---' not in line:
                all_yaml_scenarios_file.write(line)

fn.close()
all_yaml_scenarios_file.close()
os.system('rm temp.file')


if file_name == 'heat_scenarios.yaml':
    file_data = open(file_name).read()
    with open(file_name, 'w') as fn:
        fn.write('{% set image_name = image_name or "^cirros.*-disk$" %}\n')
        fn.write('{% set public_net = neutron_floating_network or "public" %}\n')
        fn.write(file_data)
    fn.close()


