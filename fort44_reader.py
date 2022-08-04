import numpy as np

def fuck():
    return 21

def eir(dir, spec):
    with open("%s/fort44_b2fplasmf_%s" %(dir, spec),'r') as f:
        line = f.readlines()
        #line_1 = line.split()
    data_array = np.array(line)
    full_length = np.size(data_array)
    #raw_data = np.empty((1,5))
    #emolrad = np
    for i in range(full_length):
        switch = data_array[i]
        if "eneutrad" in switch:
            start_neu = i
        elif "emolrad" in switch:
            start_mol = i
        elif "eionrad" in switch:
            start_ion = i
            
    total_neu_rad=0
    total_mol_rad=0
    total_ion_rad=0

    for j in range(start_neu+1,full_length):
        if "*eirene" in data_array[j]:
            break;
        else:
            damn_array = np.array(data_array[j].split())
            total_neu_rad += np.sum(damn_array.astype(np.float64))
            
    for j in range(start_mol+1,full_length):
        if "*eirene" in data_array[j]:
            break;
        else:
            damn_array = np.array(data_array[j].split())
            total_mol_rad += np.sum(damn_array.astype(np.float64))

    for j in range(start_ion+1,full_length):
        if "*eirene" in data_array[j]:
            break;
        else:
            damn_array = np.array(data_array[j].split())
            total_ion_rad += np.sum(damn_array.astype(np.float64))
    return total_neu_rad,total_mol_rad,total_ion_rad
