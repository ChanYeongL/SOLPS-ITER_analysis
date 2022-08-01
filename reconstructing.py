import numpy


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
            print(newelement)
            print("String is also valid !")
    else:
        print("string is not valid !")
def is_valid_string(element):
    if element.isdigit():
        print("String is valid")
    else:
        print("String is not valid")
def get_distance(first_point, second_point):
   
    x_range = x_center_data[first_point[1],first_point[0]]-x_center_data[second_point[1],second_point[0]]
    y_range = y_center_data[first_point[1],first_point[0]]-y_center_data[second_point[1],second_point[0]]
    
    result = (x_range**2 + y_range**2)**(1/2)
    
    return result
#fname_or = "_co"
fname_or = "new_SAS"


fname = "./b2fgmtry"

#def find_ni(fname):
#    with open(fname) as f:
#        line = f.readlines()
#        print(line)
#    return line
    
with open(fname,'r') as f:
    line = f.readlines()
    #line_1 = line.split()

a=type(line)
k = len(line)
data_array = np.array(line)
full_length = np.size(data_array)
k1 = np.zeros(k)


print(line[2])
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
                print(line[i])
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
print("selected x" , x_selected_data)
print("selected x" , np.shape(x_selected_data))


print(x_selected_length)
print(np.shape(x_selected_data))
x_numerical_len = np.shape(x_selected_data)[0]*np.shape(x_selected_data)[1]

print("data len : ", x_numerical_len)
print("before end", line[x_end-1])
print("end", line[x_end])
print("next data", line[x_end+1])


print("start", raw_data[x_start+1,:])


print("selected y" , y_selected_data)
print("selected y" , np.shape(y_selected_data))


print(y_selected_length)
print(np.shape(y_selected_data))
y_numerical_len = np.shape(y_selected_data)[0]*np.shape(y_selected_data)[1]

print("data len : ", y_numerical_len)
print("before end", line[y_end-1])
print("end", line[y_end])
print("next data", line[y_end+1])


print("start", raw_data[y_start+1,:])


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




