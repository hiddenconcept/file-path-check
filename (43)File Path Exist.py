import os.path

print(os.path.isfile('__file__'))
print(os.path.isdir('__file__.txt'))
print(os.path.islink('__file__.py'))
print(os.path.isfile('(43)File Path Exist.py'))
print(os.path.isfile('(43)File Path Exist.txt'))