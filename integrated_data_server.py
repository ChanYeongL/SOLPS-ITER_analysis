from genericpath import isdir
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pickle
import os, sys
import fort44_reader



output_dir = input("./data_Heating_Geo_sput")


	
fname_list =[]
fpath_list=[]



fname_list.append("b2fplasmf_31642_14500")
fpath_list.append("/home/chanyeong/solps-iter/runs/Ar_3e19_31642_014500/3MW_Ar_31642_14500/b2fplasmf")




data_list = list()

data_list.append("fht")
data_list.append("fhi")
data_list.append("fhe")
data_list.append("fne")
data_list.append("fni")
data_list.append("rqrad")
data_list.append("na")
data_list.append("ne")
data_list.append("ti")
data_list.append("te")

data_list.append("rrana")
data_list.append("rrahi")
data_list.append("rcxhi")
data_list.append("rsana")
data_list.append("rsahi")
#data_list.append("po")

#data_list.append("fmo")
data_list.append("ua")
data_list.append("na")
data_list.append("fna")
#data_list.append("fch")

data_list.append("bb")
data_list.append("vol")



nx = 96
ny = 36
ns = 28

def find_ni(fname):
    with open(fname) as f:
        line = f.readlines()
        print(line)
    return line


for data_ran in range(len(fname_list)):
	dum_name = fname_list[data_ran]

	fname =  "./%s" %fname_list[data_ran]


	with open(fpath_list[data_ran],'r') as f:
		line = f.readlines()    
	a=type(line)
	k = len(line)
	data_array = np.array(line)
	full_length = np.size(data_array)

	for var_ran in range(len(data_list)):
		data_name = data_list[var_ran]
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
		print(selected_data_merged_deleted)
		ns_nx_ny = str(ns*(nx+2)*(ny+2))
		ns_nx_ny2 = str(ns*(nx+2)*(ny+2)*2)
		print(check_length[2])
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

		np.save("./%s/%s_%s" %(output_dir,data_name,dum_name), selected_data_final)
		
		print("%s_%s was saved" %(data_name,dum_name))

        #selected_data_final = selected_data_merged_deleted.reshape(ns, ny+2,nx+2)

        #print(selected_data_final[0,:,3])

        #selected_data_final[0,:,96]

        #map_plot = plt.pcolormesh(selected_data_final[1,:,:])
        #plt.savefig(data_name)
        #plt.title(data_name)
        #plt.colorbar()
        #plt.show()

		x_axis = np.linspace(1,98,98)
		y_axis = np.linspace(1,38,38)
			






