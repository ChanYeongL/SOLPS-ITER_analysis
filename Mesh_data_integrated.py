import numpy as np




def is_valid_float(element: str) -> bool:
    try:
        float(element)
        return True
    except ValueError:
        return False
    
def check_float(element):
    partition = element.partition('.')
    
    if element.isdigit():
      newelement = float(element)
      print('string is valid')

    elif (partition[0].isdigit() and partition[1] == '.' and partition[2].isdigit()) or (partition[0] == '' and partition[1] == '.' and partition[2].isdigit()) or (partition[0].isdigit() and partition[1] == '.' and partition[2] == ''):
            newelement = float(element)
            #print(newelement)
            #print("String is also valid !")
    else:
        print("string is not valid !")
# def is_valid_string(element):
#     if element.isdigit():
#         print("String is valid")
#     else:
#         print("String is not valid")

def get_distance(first_point, second_point):
   
    x_range = x_center_data[first_point[1],first_point[0]]-x_center_data[second_point[1],second_point[0]]
    y_range = y_center_data[first_point[1],first_point[0]]-y_center_data[second_point[1],second_point[0]]
    
    result = (x_range**2 + y_range**2)**(1/2)
    
    return result
#fname_or = "_co"
fname_or = "_ng"


#fname = "./b2fgmtry_ng"


#def find_ni(fname):
#    with open(fname) as f:
#        line = f.readlines()
#        print(line)
#    return line

def grid_data(fname):
    
    with open(fname,'r') as f:
        line = f.readlines()
        #line_1 = line.split()

    a=type(line)
    k = len(line)
    data_array = np.array(line)
    full_length = np.size(data_array)
    k1 = np.zeros(k)


    mesh = line[2].split()
    nx = int(mesh[0])
    ny = int(mesh[1])
    #ns = int(mesh[2])
    x_name = 'crx'
    y_name = 'cry'
    data_name ='gs'


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
        if x_name in line[ch]:
            x_start = ch+1
            break;
        else:
            continue

    for ch in range(full_length):
        if y_name in line[ch]:
            y_start = ch+1
            break;
        else:
            continue
        
    for ch2 in range(x_start+1,full_length):
        try:
            check_cf = line[ch2].split()
            check_er = float(check_cf[0])
        except ValueError as m:
            x_end = ch2-1
            break;
        
    for ch2 in range(y_start+1,full_length):
        try:
            check_cf = line[ch2].split()
            check_er = float(check_cf[0])
        except ValueError as m:
            y_end = ch2-1
            break;
            
        


    #print(line[position_end])
    x_check_length = line[x_start-1].split()
    x_tot_len =int(x_check_length[2])


    y_check_length = line[y_start-1].split()
    y_tot_len =int(y_check_length[2])


    x_selected_length = x_end-x_start
    x_selected_data = np.zeros((x_selected_length+1,6))

    for i in range(x_start,x_end+1):
        dum = line[i].split()
        #print(line[i])
        dum2 = len(dum)
        for j in range(dum2):
            dum3 = dum[j]
            x_selected_data[i-x_start,j] = dum3    

    y_selected_length = y_end-y_start
    y_selected_data = np.zeros((y_selected_length+1,6))

    for i in range(y_start,y_end+1):
        dum = line[i].split()
        #print(line[i])
        dum2 = len(dum)
        for j in range(dum2):
            dum3 = dum[j]
            y_selected_data[i-y_start,j] = dum3    
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

    x_numerical_len = np.shape(x_selected_data)[0]*np.shape(x_selected_data)[1]

    y_numerical_len = np.shape(y_selected_data)[0]*np.shape(y_selected_data)[1]



    np.shape(x_selected_data)
    x_selected_data_merged = x_selected_data.reshape(x_numerical_len,1)
    x_selected_data_merged_deleted = x_selected_data_merged[:x_tot_len,0]

    np.shape(y_selected_data)
    y_selected_data_merged = y_selected_data.reshape(y_numerical_len,1)
    y_selected_data_merged_deleted = y_selected_data_merged[:y_tot_len,0]


    x_selected_data_final =x_selected_data_merged_deleted.reshape(4, ny+2,nx+2)
    y_selected_data_final =y_selected_data_merged_deleted.reshape(4, ny+2,nx+2)

    x_center_data = x_selected_data_final.sum(axis = 0)/4
    y_center_data = y_selected_data_final.sum(axis = 0)/4
    x_tot_len1 = int(x_tot_len/4)
    y_tot_len1 = int(y_tot_len/4)


    x_center_data_final = x_center_data.reshape(x_tot_len1,1)
    y_center_data_final = y_center_data.reshape(y_tot_len1,1)


    x_corner_data = x_selected_data_final[1,:,:]
    y_corner_data = y_selected_data_final[1,:,:]
    al_x_center_data_final = x_corner_data.reshape(x_tot_len1,1)
    al_y_center_data_final = y_corner_data.reshape(y_tot_len1,1)



    x_center_data_final_fl = np.squeeze(x_center_data_final)
    y_center_data_final_fl = np.squeeze(y_center_data_final)



    selected_mesh_final = np.concatenate((x_center_data_final,y_center_data_final),axis=1)



    def mesh_center():
        return(selected_mesh_final)

    def mesh_x():
        return(x_selected_data_final)

    def mesh_y():
        return(y_selected_data_final)

    ny = 36
    nx = 96
    

    inte_mesh = selected_mesh_final
    inte_mesh_x = x_selected_data_final
    inte_mesh_y = y_selected_data_final

    def distance_center(first_point, second_point):
        x_range = x_co_meshinfo[first_point[1],first_point[0]]-x_co_meshinfo[second_point[1],second_point[0]]
        y_range = y_co_meshinfo[first_point[1],first_point[0]]-y_co_meshinfo[second_point[1],second_point[0]]
        result = (x_range**2 + y_range**2)**(1/2)
        return result

    def distance_point(first_point, second_point):
        x_range = inte_mesh_x[first_point[2],first_point[1],first_point[0]]-inte_mesh_x[second_point[2],second_point[1],second_point[0]]
        y_range = inte_mesh_y[first_point[2],first_point[1],first_point[0]]-inte_mesh_y[second_point[2],second_point[1],second_point[0]]
        result = (x_range**2 + y_range**2)**(1/2)
        return result

    def total_pressure(ne,te,na,ti):
        pr = ne[:,:]*te[:,:] + na[1,:,:]*ti[:,:] +np.sum(na[2:9,:,:]*ti[:,:],axis = 0)+np.sum(na[9:,:,:]*ti[:,:],axis = 0)
        return pr

    def neutral_pressure(na,ti):
        pr = na[0,:,:]*ti[:,:]+ na[0,:,:]*ti[:,:]+ na[2,:,:]*ti[:,:]+na[2,:,:]*ti[:,:]+na[9,:,:]*ti[:,:]
        return pr
        

    dumx_inte_meshinfo =inte_mesh[:,0]
    dumy_inte_meshinfo =inte_mesh[:,1]
    x_co_meshinfo = dumx_inte_meshinfo.reshape(ny+2,nx+2)
    y_co_meshinfo = dumy_inte_meshinfo.reshape(ny+2,nx+2)


    #po_dumx_meshinfo = convmesh[:,0]
    #po_dumy_meshinfo = convmesh[:,1]
    #po_x_meshinfo = dumx_meshinfo.reshape(4,ny+2,nx+2)
    #po_y_meshinfo = dumy_meshinfo.reshape(4,ny+2,nx+2)
    inte_sep_out_target = np.zeros(2)
    inte_sep_out_target[0] = inte_mesh_x[1,18,96]
    inte_sep_out_target[1] = inte_mesh_y[1,18,96]
    inte_mesh_x_cen = np.sum(inte_mesh_x, axis = 0)/4
    inte_mesh_y_cen = np.sum(inte_mesh_y, axis = 0)/4

    X_point = []

    inte_sep_out_target_dist = np.zeros(ny+2)
    inte_sep_in_target_dist = np.zeros(ny+2)     
    inte_sep_out_midplane_dist = np.zeros(ny+2)
    inte_sep_in_midplane_dist = np.zeros(ny+2)
    conv_Xpt_dist = np.zeros(20)


    for i in range(ny+2):
        inte_sep_out_midplane_dist[i] = distance_point([52,i,1],[52,18,1])
        inte_sep_in_midplane_dist[i]  = distance_point([29,i,1],[29,18,1])
        inte_sep_out_target_dist[i] = distance_point([96,i,1],[96,18,1])
        inte_sep_in_target_dist[i] = distance_point([1,i,1],[1,18,1])



        if i<18:
            inte_sep_out_midplane_dist[i] = -inte_sep_out_midplane_dist[i]
            inte_sep_in_midplane_dist[i]  = -inte_sep_in_midplane_dist[i]
            inte_sep_out_target_dist[i] = -inte_sep_out_target_dist[i]
            inte_sep_in_target_dist[i] = -inte_sep_in_target_dist[i]



    for i in range(20):
        conv_Xpt_dist[i] = distance_center([78,18],[78+i,18])

#    print("Included data(in order) : inner target distance, outer targer distance, ")
    return inte_sep_in_target_dist,inte_sep_out_target_dist, selected_mesh_final



def mesh_data(fname):
    
    with open(fname,'r') as f:
        line = f.readlines()
        #line_1 = line.split()

    a=type(line)
    k = len(line)
    data_array = np.array(line)
    full_length = np.size(data_array)
    k1 = np.zeros(k)


    mesh = line[2].split()
    nx = int(mesh[0])
    ny = int(mesh[1])
    #ns = int(mesh[2])
    x_name = 'crx'
    y_name = 'cry'
    data_name ='gs'


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
        if x_name in line[ch]:
            x_start = ch+1
            break;
        else:
            continue

    for ch in range(full_length):
        if y_name in line[ch]:
            y_start = ch+1
            break;
        else:
            continue
        
    for ch2 in range(x_start+1,full_length):
        try:
            check_cf = line[ch2].split()
            check_er = float(check_cf[0])
        except ValueError as m:
            x_end = ch2-1
            break;
        
    for ch2 in range(y_start+1,full_length):
        try:
            check_cf = line[ch2].split()
            check_er = float(check_cf[0])
        except ValueError as m:
            y_end = ch2-1
            break;
            
        


    #print(line[position_end])
    x_check_length = line[x_start-1].split()
    x_tot_len =int(x_check_length[2])


    y_check_length = line[y_start-1].split()
    y_tot_len =int(y_check_length[2])


    x_selected_length = x_end-x_start
    x_selected_data = np.zeros((x_selected_length+1,6))

    for i in range(x_start,x_end+1):
        dum = line[i].split()
        #print(line[i])
        dum2 = len(dum)
        for j in range(dum2):
            dum3 = dum[j]
            x_selected_data[i-x_start,j] = dum3    

    y_selected_length = y_end-y_start
    y_selected_data = np.zeros((y_selected_length+1,6))

    for i in range(y_start,y_end+1):
        dum = line[i].split()
        #print(line[i])
        dum2 = len(dum)
        for j in range(dum2):
            dum3 = dum[j]
            y_selected_data[i-y_start,j] = dum3    
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

    x_numerical_len = np.shape(x_selected_data)[0]*np.shape(x_selected_data)[1]

    y_numerical_len = np.shape(y_selected_data)[0]*np.shape(y_selected_data)[1]



    np.shape(x_selected_data)
    x_selected_data_merged = x_selected_data.reshape(x_numerical_len,1)
    x_selected_data_merged_deleted = x_selected_data_merged[:x_tot_len,0]

    np.shape(y_selected_data)
    y_selected_data_merged = y_selected_data.reshape(y_numerical_len,1)
    y_selected_data_merged_deleted = y_selected_data_merged[:y_tot_len,0]


    x_selected_data_final =x_selected_data_merged_deleted.reshape(4, ny+2,nx+2)
    y_selected_data_final =y_selected_data_merged_deleted.reshape(4, ny+2,nx+2)

    x_center_data = x_selected_data_final.sum(axis = 0)/4
    y_center_data = y_selected_data_final.sum(axis = 0)/4
    x_tot_len1 = int(x_tot_len/4)
    y_tot_len1 = int(y_tot_len/4)


    x_center_data_final = x_center_data.reshape(x_tot_len1,1)
    y_center_data_final = y_center_data.reshape(y_tot_len1,1)


    x_corner_data = x_selected_data_final[1,:,:]
    y_corner_data = y_selected_data_final[1,:,:]
    al_x_center_data_final = x_corner_data.reshape(x_tot_len1,1)
    al_y_center_data_final = y_corner_data.reshape(y_tot_len1,1)



    x_center_data_final_fl = np.squeeze(x_center_data_final)
    y_center_data_final_fl = np.squeeze(y_center_data_final)



    selected_mesh_final = np.concatenate((x_center_data_final,y_center_data_final),axis=1)



    def mesh_center():
        return(selected_mesh_final)

    def mesh_x():
        return(x_selected_data_final)

    def mesh_y():
        return(y_selected_data_final)

    ny = 36
    nx = 96
#    print("Included data(in order) : inner target distance, outer targer distance, ")
    return selected_mesh_final





def facing_data(fname):
    with open(fname,'r') as f:
        line = f.readlines()

    a=type(line)
    k = len(line)
    data_array = np.array(line)
    full_length = np.size(data_array)
    k1 = np.zeros(k)

    mesh = line[2].split()
    nx = 96
    ny = 36
    ns = 3
    data_name = 'gs'
    
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
            position_start = ch+1
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
    # print("first line", position_start)
    # print("first line", line[position_start])
    # print("last line", position_end)
    # print("last line", line[position_end])


    #print(line[position_end])
    check_length = line[position_start-1].split()
    tot_len =int(check_length[2])

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

    check_length = line[position_start-1].split()
    tot_len =int(check_length[2])



    selected_length = position_end-position_start
    selected_data = np.zeros((selected_length+1,6))

    for i in range(position_start, position_end+1):
        dum = line[i].split()
        #print(line[i])
        dum2 = len(dum)
        for j in range(dum2):
            dum3 = dum[j]
            selected_data[i-position_start,j] = dum3    

    numerical_len = np.shape(selected_data)[0]*np.shape(selected_data)[1]  
    selected_data_merged = selected_data.reshape(numerical_len,1)
    selected_data_merged_deleted = selected_data_merged[:tot_len,0]
    
    selected_data_final = selected_data_merged_deleted.reshape(3,ny+2,nx+2)
    
    return selected_data_final