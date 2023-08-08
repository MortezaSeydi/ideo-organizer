import pathlib
import shutil
from pathlib import Path

# input must be an absoloute path
input_ = input("Give me the path:")
current_path = Path(input_)
files = []
f = [files.append(item) for item in current_path.iterdir()]
filtered = []
for file in files:
     if file.suffix == '.mp4' or '.avi' or '.flv' or '.mov':
            filtered.append(file)
a = 1
numbers = []
for item in files:
    if 'video number' in str(item):
        numbers.append(int(str(item)[-1]))
        a = max_ = max(numbers) + 1

        
for file in filtered:
    
    videoname = 'video number' + str(a)
        
    Path.mkdir(current_path / videoname, exist_ok=True)
    dest =str(Path(current_path / videoname))
        
    shutil.move(str(file), dest)
    a += 1

print('file orgnization finished...')
        
        