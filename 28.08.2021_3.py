import shutil
import os

dir = r'task_3'
if not os.path.exists(dir):
    os.mkdir(dir)


folder = r'my_project'
files = []


for r, d, f in os.walk(folder):
    for file in f:
        if '.html' in file:
            files.append(os.path.join(r, file))
for path in files:
    folder = os.path.join(dir, os.path.basename(os.path.dirname(path)))
    if not os.path.exists(folder):
        os.mkdir(folder)
    final_path = os.path.join(folder, os.path.basename(path))
    shutil.copy(path, final_path)
