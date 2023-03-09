import os

# From a shell you can do things
# See environment variables with env
# echo $"env variable"

print("HOME: " + os.environ.get("HOME", ""))
print("SHELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT", ""))

# Set a variable "export FRUIT=pineapple"

# Command line arguments
# ping 192.168.0.1 -l

import sys
print(sys.argv)

# Where is python installed?
import os
print(os.path.dirname(sys.executable))

# argv script
#! usr/bin/env python3

# Exit status is the value returned by a program to the shell.

# subprocess module allows you to use system commands like 'ping' and 'dir', sometimes this is useful.
import subprocess
# print(subprocess.run(['date'], shell=True))

# Capture the output of a subprocess command.
result = subprocess.run(["ping", "8.8.8.8"], shell=True, capture_output=True)
print(result)
print(result.returncode)
print(result.stdout)

# Clearly the best output
print(result.stdout.decode())

# https://docs.python.org/3/library/subprocess.html

# logfile = sys.arg[1]
# when you call the script from cmd, the logfile will be the arg passed
# ./script.py logfile.txt

# Useful when counting occurances of things
dictionary = {"farts": 3}
print(dictionary["farts"])
dictionary["farts"] = dictionary.get('farts', 0) + 1
print(dictionary["farts"])

#### all function ####
# Checks if all items in a list are True
myylist = [True, True, True]
x = all(myylist)
print(x)



# Week 4 Excersice script

#!/usr/bin/env python3
import sys
import os
import re

# def error_search(log_file):
  error = input("What is the error? ")
  returned_errors = []
  with open(log_file, mode='r',encoding='UTF-8') as file:
    for log in  file.readlines():
      error_patterns = ["error"]
      for i in range(len(error.split(' '))):
        error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
      if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
        returned_errors.append(log)
    file.close()
  return returned_errors
  
# def file_output(returned_errors):
  with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:
    for error in returned_errors:
      file.write(error)
    file.close()
# if __name__ == "__main__":
  log_file = sys.argv[1]
  returned_errors = error_search(log_file)
  file_output(returned_errors)
  sys.exit(0)
