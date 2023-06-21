import os
cmds_path = 'temp'
count = 0
file_list = os.listdir(cmds_path)


for file_name in file_list:
    if os.path.isfile(os.path.join(cmds_path, file_name)) and file_name.endswith('.py'):
        os.remove(f"temp/{file_name}")