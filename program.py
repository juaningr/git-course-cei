import sys

sys.path.append("./git-course-submodule/")

from program_s import call_this

my_list = [21, 45, 39, 11]

for index, val in enumerate(my_list):
    print(index, call_this(val))
