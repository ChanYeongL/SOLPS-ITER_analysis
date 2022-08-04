import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pickle
import os, sys
import paramiko
import getpass

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

#delete = "rm ./b2fplasmf_trial.txt"

puff = "noNe_sep"

ws_name = input("Choose workstation(e.g ws4) ")

ID = input("Insert I.D : ")

pw = getpass.getpass("Insert Password : ")

mkdir_bool = input("would you make another directory?(y/n) ")

if mkdir_bool == "y":
	output_dir = input("Insert a name of the new output directory : ")
	os.mkdir(output_dir)
elif mkdir_bool == "n":
	output_dir = input("Choose a output directory : ")

else:
	print("Invalid input")
	sys.exit(0)
	

if ws_name=='ws1':
	ssh.connect("143.248.98.209",username="%s" %ID,password="%s" %pw)
	print('ws1 connected.')
elif ws_name=='ws2':
	ssh.connect("143.248.99.155",username="%s" %ID,password="%s" %pw)
	print('ws2 connected.')
elif ws_name=='ws3':
	ssh.connect("143.248.98.247",username="%s" %ID,password="%s"%pw)
	print('ssh ws3 connected.')
elif ws_name=='ws4':
	ssh.connect("143.248.99.71",username="%s" %ID,password="%s" %pw)
	print('ssh ws4 connected.')
elif ws_name=='ws5':
	ssh.connect("143.248.101.40",username="%s" %ID,password="%s" %pw)
	print('ssh ws5 connected.')

sftp = ssh.open_sftp()


#ws4
if ws_name=='ws4':
	fname_list = list()
	fpath_list = list()
	fname_list.append("b2fplasmf_SAS_8MW_%s" %puff)
	fpath_list.append("/home/chanyeong/solps-iter/runs/SAS_Ne_0_Heating/2_5MW_SAS")
#	fname_list.append("b2fplasmf_SAS_8MW_%s" %puff)
#	fpath_list.append("/home/chanyeong/solps-iter/runs/SAS_Ne_0_Heating/8MW_SAS")
#	fname_list.append("b2fplasmf_SAS_16MW_%s" %puff)
#	fpath_list.append("/home/chanyeong/solps-iter/runs/SAS_Ne_0_Heating/16MW_SAS")
#	fname_list.append("b2fplasmf_SAS_32MW_%s" %puff)
#	fpath_list.append("/home/chanyeong/solps-iter/runs/SAS_Ne_0_Heating/32MW_SAS")
#	fname_list.append("b2fplasmf_co_KDEMO_%s" %puff)
#	fpath_list.append("/home/chanyeong/solps-iter/runs/conventionalgeo_no_neon/KDEMO_Heating")

#fname_list.append("b2fstate_al_3e7P_%s" %puff)

#	fname_list.append("b2fplasmf_co_8MW_%s" %puff)
#	fpath_list.append("/home/chanyeong/solps-iter/runs/Con_Ne_0_Heating/8MW_Con")
#	fname_list.append("b2fplasmf_co_16MW_%s" %puff)
#	fpath_list.append("/home/chanyeong/solps-iter/runs/Con_Ne_0_Heating/16MW_Con")
#	fname_list.append("b2fplasmf_co_32MW_%s" %puff)
#	fpath_list.append("/home/chanyeong/solps-iter/runs/Con_Ne_0_Heating/32MW_Con")

#	fname_list.append("b2fplasmf_SAS_32MW_Ne_zero")
#	fpath_list.append("/home/chanyeong/solps-iter/runs/SAS_Ne_zero/32MW_Heating/b2fplasmf")

#	fname_list.append("b2fplasmf_co_32MW_Ne_zero")
#	fpath_list.append("/home/chanyeong/solps-iter/runs/con_Ne_zero/32MW_Heating/b2fplasmf")

#	fname_list.append("b2fplasmf_co_32MW_Ne_3e19")
#	fpath_list.append("/home/chanyeong/solps-iter/runs/con_Ne_3e19/32MW_Heating/b2fplasmf")


#	fname_list.append("b2fplasmf_new_mesh_al_Ne_zero")
#	fpath_list.append("/home/chanyeong/solps-iter/runs/SAS_Ne_zero/Baseline_KSTAR")

#	fname_list.append("b2fplasmf_co_Ne_zero")
#	fpath_list.append("/home/chanyeong/solps-iter/runs/conventionalgeo_no_neon/Baseline_KSTAR")

#	fname_list.append("b2fplasmf_co_32MW_Ne_3e19")
#	fpath_list.append("/home/chanyeong/solps-iter/runs/con_Ne_3e19/32MW_Heating/b2fplasmf")



#Arbirary name
#fname_list.append("b2fplasmf_al_1.6e7_3e16")
#fpath_list.append("/home/chanyeong/solps-iter/runs/altergeo_sput_neon/1.6e7Heating/b2fplasmf")
#fname_list.append("b2fplasmf_co_1.6e7_3e16")
#fpath_list.append("/home/chanyeong/solps-iter/runs/conventionalgeo_sput_neon/1.6e7Heating/b2fplasmf")
#fname_list.append("b2fplasmf_co_1.6e7_3e19")
#fpath_list.append("/home/chanyeong/solps-iter/runs/conventionalgeo_Ne_3e19/1.6e17Heating/b2fplasmf")

#densi_list = list()
#densi_list.append("na")
#densi_list.append("ne")

	#ws3
elif ws_name=='ws3':
	fname_list.append("b2fplasmf_co_KSTAR_%s" %puff)
	fpath_list.append("home/chanyeong/solps-iter/runs/convgeo_Ne_3e16/Baseline_KSTAR/b2fplasmf")

data_list = list()
data_list.append("fht")
data_list.append("fhi")
data_list.append("fhe")
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
data_list.append("po")


nx = 96
ny = 36
ns = 20

def find_ni(fname):
    with open(fname) as f:
        line = f.readlines()
        print(line)
    return line


for data_ran in range(len(fname_list)):
	dum_name = fname_list[data_ran]
#	file = "scp chanyeong@143.248.99.71:/%s ./b2fplasmf_trial.txt" %fpath_list[data_ran] #ws4

	fname =  "./%s.txt" %fname_list[data_ran]
	file = sftp.get('%s/b2fplasmf' %fpath_list[data_ran], './%s' %fname)
	sftp.get('/%s/fort.44'%fpath_list[data_ran], './%s/fort44_%s' %(output_dir, fname_list[data_ran]))

#	file = "scp chanyeong@143.248.98.247:/%s ./b2fplasmf_trial.txt" %fpath_list[data_ran] #ws3

#	os.system(file)
#fname =  fname_list[data_ran]

	with open(fname,'r') as f:
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
                    #print(dum3)
				elif j+1>len(dum):
					continue



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


		if check_length[2] == '3724':
			selected_data_final = selected_data_merged_deleted.reshape(ny+2,nx+2)
		elif check_length[2]== '7448':
			selected_data_final = selected_data_merged_deleted.reshape(2, ny+2,nx+2)
		else:
			selected_data_final = selected_data_merged_deleted.reshape(ns, ny+2,nx+2)

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
			
	delete = "rm %s" %fname
	os.system(delete)
ssh.close()






