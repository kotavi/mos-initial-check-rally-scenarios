# mos-initial-check-rally-scenarios

#### How to create yaml files with all scenarios

python combine_files.py --path `<path_to_folder>` --filename `<name_of_file>.yaml`

Example 1. Here we create cinder_scenarios.yaml with all scenarios from cinder/ folder:

`python combine_files.py --path cinder/ --filename cinder_scenarios.yaml`

Example 2. Here we create all_scenarios.yaml with all scenarios from all folder:

`python combine_files.py --filename all_scenarios.yaml`

Steps:

1. deletes file cinder_scenarios.yaml if it exists
2. from cinder/ folder collects all the yaml files to the list
3. writes data from all files to temp.file
4. removes lines with '---' except the first one and writes it to sys.argv[2] file
5. deletes temp.file file



