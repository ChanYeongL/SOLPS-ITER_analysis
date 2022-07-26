import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

import netCDF4

file_location = input("Insert location of balance.nc file : ")
nc_balance = netCDF4.Dataset(file_location)

fhi_32      = nc_balance['fhi_32'][:]
fhi_52      = nc_balance['fhi_52'][:]
fhi_cond    = nc_balance['fhi_cond'][:]
fhi_dia     = nc_balance['fhi_dia'][:]
fhi_ecrb    = nc_balance['fhi_ecrb'][:]
fhi_strange = nc_balance['fhi_strange'][:]
fhi_pschused= nc_balance['fhi_pschused'][:]
fhi_inert   = nc_balance['fhi_inert'][:]
fhi_vispar  = nc_balance['fhi_vispar'][:]
fhi_visper  = nc_balance['fhi_visper'][:]
fhi_visq    = nc_balance['fhi_visq'][:]
fhi_anml    = nc_balance['fhi_anml'][:]
fhi_kevis   = nc_balance['fhi_kevis'][:]

fhe_32      = nc_balance['fhe_32'][:]
fhe_52      = nc_balance['fhe_52'][:]
fhe_thermj   = nc_balance['fhe_thermj'][:]
fhe_cond    = nc_balance['fhe_cond'][:]
fhe_dia     = nc_balance['fhe_dia'][:]
fhe_ecrb    = nc_balance['fhe_ecrb'][:]
fhe_strange = nc_balance['fhe_strange'][:]
fhe_pschused= nc_balance['fhe_pschused'][:]
#fhe_vispar  = nc_balance['fhe_vispar'][:]
#fhe_visper  = nc_balance['fhe_visper'][:]
#fhe_visq    = nc_balance['fhe_visq'][:]
#fhe_anml    = nc_balance['fhe_anml'][:]
#fhe_kevis   = nc_balance['fhe_kevis'][:]

total_fhi =fhi_32+fhi_52+fhi_cond+fhi_dia+fhi_ecrb+fhi_strange+fhi_pschused+fhi_inert+fhi_vispar+fhi_visper+fhi_visq+fhi_anml+fhi_kevis
total_fhe =fhe_32+fhe_52+fhe_cond+fhe_dia+fhe_ecrb+fhe_strange+fhe_pschused+fhe_thermj

eirene_mc_eael_she_bal = nc_balance['eirene_mc_eael_she_bal'][:]
eirene_mc_emel_she_bal = nc_balance['eirene_mc_emel_she_bal'][:]
eirene_mc_eiel_she_bal = nc_balance['eirene_mc_eiel_she_bal'][:]
eirene_mc_epel_she_bal = nc_balance['eirene_mc_epel_she_bal'][:]

eirene_mc_eapl_shi_bal = nc_balance['eirene_mc_eapl_shi_bal'][:]
eirene_mc_empl_shi_bal = nc_balance['eirene_mc_empl_shi_bal'][:]
eirene_mc_eipl_shi_bal = nc_balance['eirene_mc_eipl_shi_bal'][:]
eirene_mc_eppl_shi_bal = nc_balance['eirene_mc_eppl_shi_bal'][:]




#watch out for the direction of the heat flux terms!
def heat_flux(valname):
    total_heat_loc = 1000000
    fht_local = valname

    heat_outer_diver = np.sum((fht_local[1,1:,96]))/total_heat_loc+ np.sum((fht_local[0,1:,96]))/total_heat_loc

    heat_inner_diver = np.sum((fht_local[1,1:,1]))/total_heat_loc+np.sum((fht_local[0,1:,1]))/total_heat_loc

    heat_PRF = (np.sum((fht_local[1,1,77:]))+np.sum((fht_local[1,1,:11])))/total_heat_loc

    sol_heat = (np.sum(fht_local[0,37,:])+np.sum(fht_local[1,37,:]))/total_heat_loc

    inner_heat = (np.sum((fht_local[0,0,11:77]))+np.sum((fht_local[1,0,11:77])))/total_heat_loc
    
    return -heat_outer_diver,heat_inner_diver,heat_PRF,-sol_heat,inner_heat

def eirene_sum():
    sum_eirene_mc_eael_she_bal = np.sum(eirene_mc_eael_she_bal)
    sum_eirene_mc_emel_she_bal = np.sum(eirene_mc_emel_she_bal)
    sum_eirene_mc_eiel_she_bal = np.sum(eirene_mc_eiel_she_bal)
    sum_eirene_mc_epel_she_bal = np.sum(eirene_mc_epel_she_bal)

    sum_eirene_mc_eapl_shi_bal = np.sum(eirene_mc_eapl_shi_bal)
    sum_eirene_mc_empl_shi_bal = np.sum(eirene_mc_empl_shi_bal)
    sum_eirene_mc_eipl_shi_bal = np.sum(eirene_mc_eipl_shi_bal)
    sum_eirene_mc_eppl_shi_bal = np.sum(eirene_mc_eppl_shi_bal)
    
    return (sum_eirene_mc_eael_she_bal+sum_eirene_mc_emel_she_bal+sum_eirene_mc_eiel_she_bal+sum_eirene_mc_epel_she_bal +sum_eirene_mc_eapl_shi_bal+sum_eirene_mc_eapl_shi_bal+sum_eirene_mc_eapl_shi_bal+sum_eirene_mc_eapl_shi_bal)/1000000

def other_source():
    heat_source= np.sum(nc_balance['b2srst_shi_bal'][:])+np.sum(nc_balance['b2srst_she_bal'][:])
    stel_terms = np.sum(nc_balance['b2stel_shi_ion_bal'][:])+np.sum(nc_balance['b2stel_she_bal'][:])
    
    joule = np.sum(nc_balance['b2sihs_joule_bal'][:])

    fraa  = np.sum(nc_balance['b2sihs_fraa_bal'][:])
    
    divue = np.sum(nc_balance['b2sihs_divue_bal'][:])
    
    visa  = np.sum(nc_balance['b2sihs_visa_bal'][:])
    return (heat_source+stel_terms+joule+fraa+divue+visa)/1000000

print(sum(heat_flux(total_fhe)))
print(sum(heat_flux(total_fhi)))

print('total internal energy "outward" = ',-(sum(heat_flux(total_fhe))+sum(heat_flux(total_fhi))+eirene_sum()+other_source()))

plt.title("Ion heat flux(+ sign means outward energy)")
x = [r'$P_{outer div}$',r'$P_{inner div}$',r'$P_{PFR}$',r'P_{SOL}',r'$P_{core}$']
plt.bar(x,heat_flux(-total_fhi))
plt.axhline(color = 'black',linewidth = 0.5)
plt.show()

plt.title("Electron heat flux(+ sign means outward energy)")
x = [r'$P_{outer div}$',r'$P_{inner div}$',r'$P_{PFR}$',r'P_{SOL}',r'$P_{core}$']
plt.bar(x,heat_flux(-total_fhe))
plt.axhline(color = 'black',linewidth = 0.5)
plt.show()

plt.title("Energy Balance(total input heat 2.5 MW)")
x = [r'$P_{ion}$',r'$P_{electron}$',r'$P_{eirene}$',r'P_{etc}']
y = [-sum(heat_flux(total_fhe)),-sum(heat_flux(total_fhi)),-eirene_sum(),-other_source()]
plt.bar(x,y)
plt.axhline(color = 'black',linewidth = 0.5)


plt.show()
