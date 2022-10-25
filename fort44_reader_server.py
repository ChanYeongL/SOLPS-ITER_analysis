import numpy as np


def eir(dir):
    with open("%s/fort.44" %(dir),'r') as f:
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

def eir_spec(dir):
    with open("%s/fort.44" %(dir),'r') as f:
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
    neu_rad_array = []
    mol_rad_array = []
    ion_rad_array = []
    for j in range(start_neu+1,full_length):
        if "*eirene" in data_array[j]:
            break;
        else:
            damn_array= np.array(data_array[j].split())
            total_neu_rad += np.sum(damn_array.astype(np.float64))
            neu_rad_array = np.append(neu_rad_array,damn_array.astype(np.float64))      
                  
    for j in range(start_mol+1,full_length):
        if "*eirene" in data_array[j]:
            break;
        else:
            damn_array = np.array(data_array[j].split())
            total_mol_rad += np.sum(damn_array.astype(np.float64))
            mol_rad_array = np.append(mol_rad_array,damn_array.astype(np.float64))


    for j in range(start_ion+1,full_length):
#        ion_to_data = np.zeros([38,2])
        
        if "*eirene" in data_array[j]:
            break;
        else:
            damn_array = np.array(data_array[j].split())
            #print(damn_array.astype(np.float64))
            total_ion_rad += np.sum(damn_array.astype(np.float64))
            
            ion_rad_array = np.append(ion_rad_array,damn_array.astype(np.float64))
            
    #print(np.shape(impor_arr))
    neu_rad_array  = neu_rad_array.reshape(3, 36,96)
    mol_rad_array  = mol_rad_array.reshape(36,96)
    ion_rad_array  = ion_rad_array.reshape(36,96)
    
    po_nul = np.zeros([2,96])
    ra_nul = np.zeros([38,2])

    po_nul_neu = np.zeros([3, 2 ,96])
    ra_nul_neu = np.zeros([3, 38, 2])
    
    neu_rad_array = np.concatenate([po_nul_neu, neu_rad_array], axis = 1)
    neu_rad_array = np.concatenate([ra_nul_neu, neu_rad_array], axis = 2)
    
    mol_rad_array = np.vstack([po_nul, mol_rad_array])
    mol_rad_array = np.hstack([ra_nul, mol_rad_array])
    
    ion_rad_array = np.vstack([po_nul, ion_rad_array])
    ion_rad_array = np.hstack([ra_nul, ion_rad_array])
    #print(np.shape(ion_rad_array))
    return neu_rad_array,mol_rad_array,ion_rad_array
#print(np.shape(ion_rad_array))




