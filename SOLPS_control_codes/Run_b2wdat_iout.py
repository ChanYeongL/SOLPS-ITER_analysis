import os, sys
import subprocess
from datetime import datetime

current_dir = os.getcwd()
text_file_path = './b2mn.dat'
new_text_content = ''

time = datetime.now()

switch = 0
position_return = 0

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


new_text_content2 = ''
with open(text_file_path,'r') as f:
	lines = f.readlines()
	for i, l in enumerate(lines):
		if l.find('b2wdat_iout') !=-1:
			new_string2 = "'b2wdat_iout'	'4'"
			switch =1
			position_return = l
		else:
			new_string2 = l.strip()
		if new_string2:
			new_text_content2 += new_string2 + '\n'
		else:
			new_text_content2 += '\n'

with open(text_file_path,'w') as f:
    f.write(new_text_content2)

k=open(text_file_path,'a')
if switch ==0:
	k.write("'b2wdat_iout'	'4'")
	print('there was no b2wdat_iout, so added')
else:
	print("b2wdat_iout already setted.")
k.close()
subprocess.run(["b2run", "b2mn", "< input.dat >" ,"run.log", "&"])

g = open("/home/chanyeong/solps-iter/ex_log.txt", "a")
g.write("I execute b2run for b2wdat data in %s at %s \n" %(current_dir, time))
g.close()
