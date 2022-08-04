import os, sys
import subprocess
from datetime import datetime

current_dir = os.getcwd()

time = datetime.now()

print("Finishing SOLPS-ITER run...")
subprocess.run(["touch","b2mn.exe.dir/.quit"])

f = open("/home/chanyeong/solps-iter/ex_log.txt", "a")

f.write("I finished run in %s at %s \n" %(current_dir, time))
