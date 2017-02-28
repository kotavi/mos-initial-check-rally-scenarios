# mos-initial-check-rally-scenarios

#### How to update yaml files with all scenarios

python combine_files.py <path_to_folder> <name_of_file>.yaml

Example:

python combine_files.py cinder/ cinder_scenarios.yaml

Steps:
1. deletes file cinder_scenarios.yaml if it exists
2. from cinder/ folder collects all the yaml files to the list
3. writes data from all files to temp.file
4. removes lines with '---' except the first one and writes it to sys.argv[2] file
5. deletes temp.file file



