import os
import shutil
cmds_path = 'config'
count = 0
for path in os.listdir(cmds_path):
    if os.path.isfile(os.path.join(cmds_path, path)):
        count += 1
print("Found", count, "configuration files")
file_list = os.listdir(cmds_path)


for file_name in file_list:
    if os.path.isfile(os.path.join(cmds_path, file_name)):
        new_file_name = os.path.splitext(file_name)[0] + ".py"
        source_file_path = os.path.join(cmds_path, file_name)
        destination_file_path = os.path.join('temp', new_file_name)
        shutil.copy2(source_file_path, destination_file_path)
        
        print(f"Loaded {file_name}")