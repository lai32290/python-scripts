#!/usr/bin/python

import sys
import os
import shutil

class File():
    def __init__(self, path, name):
        self.name = name
        filepath = "%s/%s" % (path, name)
        self.date = os.path.getmtime(filepath);

path = sys.argv[1]

count = 1
files = []
for filename in os.listdir(path):
    files = files + [File(path, filename)]

files = sorted(files, key=lambda file: file.date)

for index, file in enumerate(files):
    newName = "%02d- %s" % (index + 1, file.name)
    shutil.move(file.name, newName)
