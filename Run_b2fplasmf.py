import os, sys
import subprocess
from datetime import datetime

current_dir = os.getcwd()

text_file_path = './b2mn.dat'
new_text_content = ''
time=datetime.now()

with open(text_file_path,'r') as f:
	lines = f.readlines()
	for i, l in enumerate(lines):
		if i == 6:
			new_string = "'b2mndr_ntim'   '1'"
		else:
			new_string = l.strip()
		if new_string:
			new_text_content += new_string + '\n'
		else:
			new_text_content += '\n'
																		                   

with open(text_file_path,'w') as f:
    f.write(new_text_content)

subprocess.run(["b2run", " ","b2uf"])

f = open("/home/chanyeong/solps-iter/ex_log.txt", "a")
f.write("I formatted %s at %s \n" %(current_dir, time))
