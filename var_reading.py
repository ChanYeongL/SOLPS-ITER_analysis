import numpy as np






data_list = list()

def data_picking(iwant, loc):
    data_list.append(iwant)
    fname_list = list()
    fname_list.append(loc) 

    nx = 96
    ny = 36
    ns = 20

    for date_ran in range(len(fname_list)):
        dum_name = fname_list[date_ran]
        fname = "%s" %dum_name
        with open(fname,'r') as f:
            line = f.readlines()    
        a=type(line)
        k = len(line)
        data_array = np.array(line)
        full_length = np.size(data_array)
        

            
        for var_ran in range(len(data_list)):
            data_name = data_list[var_ran]

            print(line[2])
            mesh = line[2].split()

            print(line[2])

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

            #np.save("./%s_%s" %(data_name,dum_name), selected_data_final)
            #print("./%s_%s" %(data_name,fname))

            return(selected_data_final)
            #selected_data_final = selected_data_merged_deleted.reshape(ns, ny+2,nx+2)
