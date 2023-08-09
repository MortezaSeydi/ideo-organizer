import pathlib
import shutil
from pathlib import Path

# input must be an absoloute path
# entering the input path
input_ = input("Give me the path:")
current_path = Path(input_)
files = []
f = [files.append(item) for item in current_path.iterdir()]
filtered = []
for file in files:
     if (file.suffix in {'.mp4','.avi','.flv','.mov'}) == True:
            filtered.append(file)
            
# determining number of current video
a = 0
numbers = []
for item in files:
    if 'video number' in str(item):
        numbers.append(int(str(item)[-1]))
        a = max_ = max(numbers) + 1
    else:
        a = 0

# renaming and creating folder for videos        
for file in filtered:
    videoname = 'video number' + str(a)
    Path.mkdir(current_path / videoname, exist_ok=True)
    dest =str(Path(current_path / videoname))
    shutil.move(str(file), dest)
    a += 1

print('file orgnization finished...')
        
