from genericpath import isdir
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pickle
import os, sys
import paramiko
import getpass
import fort44_reader


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

#delete = "rm ./b2fplasmf_trial.txt"


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


#puff = "Ne_0" #Neon puff zero
#puff = "Ne_3e19" #Neon puff 3e19
#puff = "Ne_0_sep_density"


#ws4
if ws_name=='ws4':
	fname_list = list()
	fpath_list = list()
#new g file section
#	fname_list.append("b2fplasmf_SAS_new_gfile_8MW_%s" %puff)
#	fpath_list.append("/home/chanyeong/solps-iter/runs/SAS_another_gfile/8MW_SAS_New_gfile")	
 
 #2022 08 07 now, new-mesh is standard
 #SAS - Heating
#	fname_list.append("b2fplasmf_SAS_2_5MW_%s" %puff)
#	fpath_list.append("/home/chanyeong/solps-iter/runs/SAS_Ne_0_Heating/2_5MW_SAS")
	# fname_list.append("b2fplasmf_SAS_8MW_Ne_0")#%s" %puff)
	# fpath_list.append("/home/chanyeong/solps-iter/runs/SAS_Ne_0_Heating/8MW_SAS")
	# fname_list.append("b2fplasmf_SAS_16MW_Ne_0")#%s" %puff)
	# fpath_list.append("/home/chanyeong/solps-iter/runs/SAS_Ne_0_Heating/16MW_SAS")
	# fname_list.append("b2fplasmf_SAS_32MW_Ne_0")#%s" %puff)
	# fpath_list.append("/home/chanyeong/solps-iter/runs/SAS_Ne_0_Heating/32MW_SAS")


	# fname_list.append("b2fplasmf_SAS_8MW_Ne_3e19")# %puff)
	# fpath_list.append("/home/chanyeong/solps-iter/runs/SAS_Ne_e19_Heating/8MW_SAS_Ne19")
	# fname_list.append("b2fplasmf_SAS_8MW_Ne_3e19")# %puff)
	# fpath_list.append("/home/chanyeong/solps-iter/runs/SAS_Ne_e19_Heating/8MW_SAS_Ne19")
	# fname_list.append("b2fplasmf_SAS_32MW_Ne_3e19")# %puff)
	# fpath_list.append("/home/chanyeong/solps-iter/runs/SAS_Ne_e19_Heating/32MW_SAS_Ne19")


#SAS - another g file
#	fname_list.append("b2fplasmf_SAS_2_5MW_%s" %puff)
#	fpath_list.append("/home/chanyeong/solps-iter/runs/SAS_Ne_0_Heating/2_5MW_SAS")
	# fname_list.append("b2fplasmf_SAS_new_g_8MW_%s" %puff)
	# fpath_list.append("/home/chanyeong/solps-iter/runs/SAS_another_gfile/8MW_SAS_New_gfile")
	# # fname_list.append("b2fplasmf_SAS_new_g_16MW_%s" %puff)
	# # fpath_list.append("/home/chanyeong/solps-iter/runs/SAS_another_gfile/16MW_SAS_New_gfile")
	# fname_list.append("b2fplasmf_SAS_new_g_32MW_%s" %puff)
	# fpath_list.append("/home/chanyeong/solps-iter/runs/SAS_another_gfile/32MW_SAS_New_gfile")


#SAS - sep density
	#puff = "sep_density"
#	fname_list.append("b2fplasmf_SAS_8MW_1e18_%s" %puff)
#	fpath_list.append("/home/chanyeong/solps-iter/runs/SAS_Ne_0_8MW_sep_density/1e18_SAS_8MW")
#	fname_list.append("b2fplasmf_SAS_8MW_05e19_%s" %puff)
#	fpath_list.append("/home/chanyeong/solps-iter/runs/SAS_Ne_0_8MW_sep_density/0_5e19_SAS_8MW")
#	fname_list.append("b2fplasmf_SAS_8MW_1e19_%s" %puff)
#	fpath_list.append("/home/chanyeong/solps-iter/runs/SAS_Ne_0_8MW_sep_density/1e19_SAS_8MW")
#	fname_list.append("b2fplasmf_SAS_8MW_2e19_%s" %puff)
#	fpath_list.append("/home/chanyeong/solps-iter/runs/SAS_Ne_0_8MW_sep_density/2e19_SAS_8MW")
#	fname_list.append("b2fplasmf_SAS_8MW_3e19_%s" %puff)
#	fpath_list.append("/home/chanyeong/solps-iter/runs/SAS_Ne_0_8MW_sep_density/3e19_SAS_8MW")
#	fname_list.append("b2fplasmf_SAS_8MW_4e19_%s" %puff)
#	fpath_list.append("/home/chanyeong/solps-iter/runs/SAS_Ne_0_8MW_sep_density/4e19_SAS_8MW")
#	fname_list.append("b2fplasmf_SAS_8MW_5e19_%s" %puff)
#	fpath_list.append("/home/chanyeong/solps-iter/runs/SAS_Ne_0_8MW_sep_density/5e19_SAS_8MW") 
 
#SAS - another version
	# fname_list.append("b2fplasmf_Ex_SAS_8MW_%s" %puff)
	# fpath_list.append("/home/chanyeong/solps-iter/runs/Exp_ne_zero/EX_8MW_Heating")
	# fname_list.append("b2fplasmf_Ex_SAS_16MW_%s" %puff)
	# fpath_list.append("/home/chanyeong/solps-iter/runs/Exp_ne_zero/16MW_ESAS_Heating")
	# fname_list.append("b2fplasmf_Ex_SAS_20MW_%s" %puff)
	# fpath_list.append("/home/chanyeong/solps-iter/runs/Exp_ne_zero/20MW_Heating_ESAS")
	# fname_list.append("b2fplasmf_Ex_SAS_32MW_%s" %puff)
	# fpath_list.append("/home/chanyeong/solps-iter/runs/Exp_ne_zero/32MW_Heating")
 
 
#SAS - another version with impurities
	# fname_list.append("b2fplasmf_Ex_SAS_8MW_%s" %puff)
	# fpath_list.append("/home/chanyeong/solps-iter/runs//Exp_ne_3e19/8MW_ESAS_Heating")
	# fname_list.append("b2fplasmf_Ex_SAS_16MW_%s" %puff)
	# fpath_list.append("/home/chanyeong/solps-iter/runs//Exp_ne_3e19/16MW_ESAS_Heating")
	# fname_list.append("b2fplasmf_Ex_SAS_32MW_%s" %puff)
	# fpath_list.append("/home/chanyeong/solps-iter/runs/Exp_ne_3e19/32MW_ESAS_Heating")

#SAS -  another version with different magnetic geometry
#	fname_list.append("b2fplasmf_Ex_SAS_8MW_Ng_%s" %puff)
#	fpath_list.append("/home/chanyeong/solps-iter/runs/Exp_another_g/8MW_ESAS_Ne0")
#	fname_list.append("b2fplasmf_Ex_SAS_16MW_Ng_%s" %puff)
#	fpath_list.append("/home/chanyeong/solps-iter/runs/Exp_ne_zero/EX_8MW_Heating")
#	fname_list.append("b2fplasmf_Ex_SAS_32MW_Ng_%s" %puff)
#	fpath_list.append("/home/chanyeong/solps-iter/runs/Exp_another_g/32MW_ESAS_Ne0_anotherG")

#SAS -  another version with reversed angle geometry
	# fname_list.append("b2fplasmf_SAS_v1_8MW_Ne_0")# %s" %puff)
	# fpath_list.append("/home/chanyeong/solps-iter/runs/SAS_Ne_0_ver1_1/8MW_SAS_Ne_0_v1_1")
	# # fname_list.append("b2fplasmf_Ex_SAS_16MW_Ng_%s" %puff)
	# # fpath_list.append("/home/chanyeong/solps-iter/runs/Exp_ne_zero/EX_8MW_Heating")
	# fname_list.append("b2fplasmf_SAS_v1_32MW_Ne_0")#%s" %puff)
	# fpath_list.append("/home/chanyeong/solps-iter/runs/SAS_Ne_0_ver1_1/32MW_SAS_Ne_0_v1_1")


#Con - sep density
	#puff = "sep_density"
#	fname_list.append("b2fplasmf_co_8MW_1e19_%s" %puff)
#	fpath_list.append("/home/chanyeong/solps-iter/runs/Con_Ne_0_8MW_sep_density/1e19Con")
#	fname_list.append("b2fplasmf_co_8MW_2e19_%s" %puff)
#	fpath_list.append("/home/chanyeong/solps-iter/runs/Con_Ne_0_8MW_sep_density/2e19Con")
#	fname_list.append("b2fplasmf_co_8MW_3e19_%s" %puff)
#	fpath_list.append("/home/chanyeong/solps-iter/runs/Con_Ne_0_8MW_sep_density/3e19Con")
#	fname_list.append("b2fplasmf_co_8MW_4e19_%s" %puff)
#	fpath_list.append("/home/chanyeong/solps-iter/runs/Con_Ne_0_8MW_sep_density/4e19Con")
#	fname_list.append("b2fplasmf_co_8MW_5e19_%s" %puff)
#	fpath_list.append("/home/chanyeong/solps-iter/runs/Con_Ne_0_8MW_sep_density/5e19Con") 
 
#Conventional - Heating
#	fname_list.append("b2fplasmf_co_8MW_%s" %puff)
#	fpath_list.append("/home/chanyeong/solps-iter/runs/Con_Ne_0_Heating/8MW_Con")
#	fname_list.append("b2fplasmf_co_16MW_%s" %puff)
#	fpath_list.append("/home/chanyeong/solps-iter/runs/Con_Ne_0_Heating/16MW_Con")
#	fname_list.append("b2fplasmf_co_20MW_%s" %puff)
#	fpath_list.append("/home/chanyeong/solps-iter/runs/Con_Ne_0_Heating/20MW_Con_Ne0")
#	fname_list.append("b2fplasmf_co_24MW_%s" %puff)
#	fpath_list.append("/home/chanyeong/solps-iter/runs/Con_Ne_0_Heating/24MW_Con_Ne0")
#	fname_list.append("b2fplasmf_co_28MW_%s" %puff)
#	fpath_list.append("/home/chanyeong/solps-iter/runs/Con_Ne_0_Heating/28MW_Con_Ne0")
#	fname_list.append("b2fplasmf_co_32MW_%s" %puff)
#	fpath_list.append("/home/chanyeong/solps-iter/runs/Con_Ne_0_Heating/new_32MW_Con_Ne0")


#	fname_list.append("b2fplasmf_co_32MW_re_%s" %puff)
#	fpath_list.append("/home/chanyeong/solps-iter/runs/Con_Ne_0_Heating/new_32MW_Con_Ne0")



#Conventional - Heating(3e19)
#	fname_list.append("b2fplasmf_co_8MW_%s" %puff)
#	fpath_list.append("/home/chanyeong/solps-iter/runs/Con_Ne_e19_Heating/8MW_Con")
#	fname_list.append("b2fplasmf_co_16MW_%s" %puff)
#	fpath_list.append("/home/chanyeong/solps-iter/runs/Con_Ne_e19_Heating/16MW_Con")
#	fname_list.append("b2fplasmf_co_32MW_%s" %puff)
#	fpath_list.append("/home/chanyeong/solps-iter/runs/Con_Ne_e19_Heating/32MW_Con")


#Conventional - 22839 g file(Ne 0)
	fname_list.append("b2fplasmf_Con_22849_8MW_Ne_0")
	fpath_list.append("/home/chanyeong/solps-iter/runs/Con_22849_Ne0_Heating/8MW_Con_22849")
	# fname_list.append("b2fplasmf_SAS_new_g_16MW_%s" %puff)
	# fpath_list.append("/home/chanyeong/solps-iter/runs/SAS_another_gfile/16MW_SAS_New_gfile")
	fname_list.append("b2fplasmf_Con_22849_32MW_Ne_0")
	fpath_list.append("/home/chanyeong/solps-iter/runs/Con_22849_Ne0_Heating/32MW_Con_22849")



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
#elif ws_name=='ws3':
#	fname_list.append("b2fplasmf_co_KSTAR_%s" %puff)
#	fpath_list.append("home/chanyeong/solps-iter/runs/convgeo_Ne_3e16/Baseline_KSTAR/b2fplasmf")

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
	sftp.get('/%s/fort.44'%fpath_list[data_ran], '%s/fort44_%s' %(output_dir, fname_list[data_ran]))
	if os.path.isdir("/Volumes/Universal/Data_storage")==True:
		sftp.get('/%s/balance.nc'%fpath_list[data_ran], '/Volumes/Universal/Data_storage/balance_%s.nc' %fname_list[data_ran])
#	else:
#		continue
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


		if check_length[2] == '3724':
			selected_data_final = selected_data_merged_deleted.reshape(ny+2,nx+2)
		elif check_length[2]== '7448':
			selected_data_final = selected_data_merged_deleted.reshape(2, ny+2,nx+2)
		elif check_length[2] == '14896':
			selected_data_final = selected_data_merged_deleted.reshape(4, ny+2,nx+2)	
		elif check_length[2]== '74480':
			selected_data_final = selected_data_merged_deleted.reshape(ns, ny+2,nx+2)
		elif check_length[2]== '148960':
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
			
	delete = "rm %s" %fname
	os.system(delete)
ssh.close()






