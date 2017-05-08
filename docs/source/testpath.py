import sys
import os
import glob

#path = os.path.relpath("/Code",os.path.abspath("."))

path1 = os.path.abspath("../../Code")

print os.listdir(path1)

print os.path.exists(path1)