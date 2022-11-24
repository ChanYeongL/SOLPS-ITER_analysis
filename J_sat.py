import numpy as np



import Mesh_data_integrated
import b2fplasmf

e = 1.60217663*(10**(-19))
charge = []
charge.append(0)
charge.append(e*1)
charge.append(0)
charge.append(e*1)
charge.append(e*2)
charge.append(e*3)
charge.append(e*4)
charge.append(e*5)
charge.append(e*6)
charge.append(0)
charge.append(e*1)
charge.append(e*2)
charge.append(e*3)
charge.append(e*4)
charge.append(e*5)
charge.append(e*6)
charge.append(e*7)
charge.append(e*8)
charge.append(e*9)
charge.append(e*10)
charge.append(e*12)
charge.append(e*12)
charge.append(e*13)
charge.append(e*14)
charge.append(e*15)
charge.append(e*16)
charge.append(e*17)
charge.append(e*18)


def flux(file_location, n):
    facing_data= Mesh_data_integrated.facing_data("%s/b2fgmtry" %file_location)
    fna = b2fplasmf.data("%s/b2fplasmf" %file_location,"fna", n)
    bb = b2fplasmf.data("%s/b2fplasmf" %file_location,"bb", n)
    qc = b2fplasmf.data("%s/b2fplasmf" %file_location,"qc", n)
    J1 = np.zeros([n, 2, 38, 98])
    J = np.zeros([n, 2, 38, 98])
    geo_eff = (bb[3,1:,96]/bb[0,1:,96])/qc[1:,96]

    for i in range(n):
        J1[i, :, :, :] = fna[i,:,:,:]*charge[i]

    J = (np.sum(J1,axis=0)[0,1:,96]*geo_eff)/(10000*facing_data[0,1:,96])
    
    return J
    
    
    