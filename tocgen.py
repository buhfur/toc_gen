#!/usr/bin/env python3 

# Script that generates a Table Of Contents with links to other pages for a Markdown file 
import sys
import os
from pathlib import Path
USAGE = 'Usage : main.py [ABS_PARENT_DIR] file.md'

PATH = Path(sys.argv[1])
FILE = sys.argv[2]


if not os.path.isabs(PATH):
    print("ERROR: path provided is not Absolute path")
    exit(1)

if not os.path.isfile(FILE):
    print(os.system(f'file {FILE}'))
    exit(1)


count = 0
template_list = []
for x in os.listdir(PATH):
    MD_PATH_TEMPLATE=f'{PATH.parts[-1]}/{x}'
    stripped_ext = x[:-3]
    final_str = stripped_ext[0].upper() + stripped_ext[1:]
    count+=1
    template = f'{count}. [{final_str}]({MD_PATH_TEMPLATE})'
    template_list.append(template)

with open(FILE, 'a') as f : 
    for x in template_list:
        f.write(''.join(x)+"\n")
    

# Display the results of the TOC 

with open(FILE,'r') as f:
    print(f.read())

