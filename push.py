import subprocess
import sys 

cmd = "git add . && git commit -m " + sys.argv[1] + "&& git push " 


# new process
p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# retrive the result
stdout, stderr = p.communicate()

# output
print(stdout.decode())
print(stderr.decode())


