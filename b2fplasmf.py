from genericpath import isdir
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pickle
import os, sys
import fort44_reader










nx = 96
ny = 36

def find_ni(fname):
    with open(fname) as f:
        line = f.readlines()
        print(line)
    return line


def data(input_path,input_name,spec):
	dum_name = input_name
	ns = spec
	fname =  input_name


	with open(input_path,'r') as f:
		line = f.readlines()    
	a=type(line)
	k = len(line)
	data_array = np.array(line)
	full_length = np.size(data_array)

	data_name = input_name
#print(line[0])
#mesh = line[2].split()
#nx = int(mesh[0])
#ny = int(mesh[1])
#ns = int(mesh[2])

#		print(line[2])

	raw_data = np.empty((full_length,6))

#		for i in range(0, full_length):
#
#			dum = line[i].split()
#			dum2 = len(dum)
#
#			for j in range(6):
#				if j+1<=len(dum):
#					dum3 = dum[j]
#
#					try:
#						raw_data[i,j] = dum3
#					except ValueError as m:
#						raw_data[i,j] = 0
				#print(dum3)
#				elif j+1>len(dum):
#					continue



	for i in range(0, full_length):  
		dum = line[i].split()
		dum2 = len(dum)
		for j in range(6):
			if j+1<=len(dum):
				dum3 = dum[j]
				try:
					raw_data[i,j] = dum3
				except ValueError as m:
					raw_data[i,j] = 0
					#print(line[i])
					break;
			elif j+1>len(dum):
				continue

	check_array = np.empty((1,6))
	for ch in range(full_length):
		if data_name in line[ch]:
			if line[ch].split()[3]==data_name:
				position_start = ch+1
				break;
			else:
				continue
		else:
			continue

	for ch2 in range(position_start+1,full_length):
		try:
			check_cf = line[ch2].split()
			check_er = float(check_cf[0])
		except ValueError as m:
			position_end = ch2-1
	#        print(ch2)
			break;

	#print(line[position_end])
	check_length = line[position_start-1].split()
	tot_len =int(check_length[2])




	line[250193].split()[3] == data_name


	selected_length = position_end-position_start
	selected_data = np.zeros((selected_length+1,6))

	for i in range(position_start, position_end+1):
		dum = line[i].split()
		#print(line[i])
		dum2 = len(dum)
		for j in range(dum2):
			dum3 = dum[j]
			selected_data[i-position_start,j] = dum3    

	#    for j in range(6):
	#        if j+1<=len(dum):
	#            dum3 = dum[j]
	#            try:
	#                selected_data[i-position_start,j] = dum3
	#            except ValueError as m:
	#                selected_data[i-position_start,j] = 0.0
	#            #print(dum3)
	#        elif j+1>len(dum):
	#            continue



	numerical_len = np.shape(selected_data)[0]*np.shape(selected_data)[1]

	np.shape(selected_data)
	selected_data_merged = selected_data.reshape(numerical_len,1)
	selected_data_merged_deleted = selected_data_merged[:tot_len,0]
	#print(selected_data_merged_deleted)
	ns_nx_ny = str(ns*(nx+2)*(ny+2))
	ns_nx_ny2 = str(ns*(nx+2)*(ny+2)*2)
	#print(check_length[2])
	if check_length[2] == '3724':
		selected_data_final = selected_data_merged_deleted.reshape(ny+2,nx+2)
	elif check_length[2]== '7448':
		selected_data_final = selected_data_merged_deleted.reshape(2, ny+2,nx+2)
	elif check_length[2] == '14896':
		selected_data_final = selected_data_merged_deleted.reshape(4, ny+2,nx+2)	
	elif check_length[2]== ns_nx_ny:
		selected_data_final = selected_data_merged_deleted.reshape(ns, ny+2,nx+2)
	elif check_length[2]== ns_nx_ny2:
		selected_data_final = selected_data_merged_deleted.reshape(ns,2, ny+2,nx+2)

	return(selected_data_final)





