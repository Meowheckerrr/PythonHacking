import subprocess
import sys

# commands
cmd = "nmap -sC -sV -PN -A -T4 " + sys.argv[1]

print("script is running. Author:meowhecker")

# new process
p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# retrive the result
stdout, stderr = p.communicate()

# output
print(stdout.decode())
print(stderr.decode())






