## add a modeule from the parent folder

import os, sys

p = os.path.abspath('..') # add parent absolute path
sys.path.insert(1, p)
print(p)

import <module_name>
