import os, sys
import subprocess
from datetime import datetime

run_name = input("insert name of run : ")
print(run_name)
core_num = int(input("insert number of core : "))

current_dir = os.getcwd()
text_file_path = './b2mn.dat'
new_text_content = ''

time = datetime.now()

with open(text_file_path,'r+', encoding = "utf-8") as f:
	lines = f.readlines()
	for i, l in enumerate(lines):
		if i == 6:
			new_string = "'b2mndr_ntim'   '1000000'"
		else:
			new_string = l.strip()
		if new_string:
			new_text_content += new_string + '\n'
		else:
			new_text_content += '\n'

with open(text_file_path,'w') as f:
    f.write(new_text_content)

#subprocess.run(["kstarsubmit", "-j", "%s"%run_name ,"-m", "--np %i" %core_num])

#f = open("/home/chanyeong/solps-iter/ex_log.txt", "a")
#f.write("I execute %s in %s at %s \n" %(run_name, current_dir, time))
