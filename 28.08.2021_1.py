import os

pattern = {'my_progect': ['settings', 'mainapp', 'adminapp', 'athoapp']}
for root, folders in pattern.items():
    if os.path.exists(root):
        print(root, 'exists')
    else:
        for folder in folders:
            dir = os.path.join(root, folder)
            os.makedirs(dir)
