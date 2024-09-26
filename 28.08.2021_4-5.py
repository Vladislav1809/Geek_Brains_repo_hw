import os
import json


files = []
for r, d, f in os.walk('./'):
    for file in f:
        file_path = os.path.join(r, file)
        files.append((file_path.split('.')[-1], os.stat(file_path).st_size))
max_size = max(files, key=lambda x:x[1])[1]


i = 1
final_dict = {}
for _ in range(len(str(max_size))):
    i *= 10
    final_dict[i] = (0, [])

for file in files:
    num, exit_list = final_dict[10 ** len(str(file[1]))]
    exit_list.append(file[0])
    exit_list = list(set(exit_list))
    final_dict[10 ** len(str(file[1]))] = (num + 1, exit_list)


print(final_dict)


with open(os.path.basename(os.getcwd()) + '_summary.json', 'w') as f_out:
    json.dump(final_dict, f_out)


