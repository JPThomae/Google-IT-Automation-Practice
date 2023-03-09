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



