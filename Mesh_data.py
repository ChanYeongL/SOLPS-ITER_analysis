from operator import ne
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy.special import rel_entr
import pickle
from mpl_toolkits.mplot3d import axes3d
from scipy.ndimage.filters import gaussian_filter
import seaborn as sns
import matplotlib.patches as patches
import pandas as pd
import netCDF4



ny = 36
nx = 96

co_mesh = np.load("./conv_geo_mesh_center.npy")
co_mesh_x = np.load("./conv_geo_mesh_x.npy")
co_mesh_y = np.load("./conv_geo_mesh_y.npy")

al_mesh = np.load("./al_geo_mesh_center.npy")
al_mesh_x = np.load("./al_geo_mesh_x.npy")
al_mesh_y = np.load("./al_geo_mesh_y.npy")

co_facing = np.load("./gs_b2fgmtry.npy")
al_facing = np.load("./gs_b2fgmtry_al.npy")


co_new_mesh = np.load("./new_mesh_co_geo_mesh_center.npy")
co_new_mesh_x = np.load("./new_mesh_co_geo_mesh_x.npy")
co_new_mesh_y = np.load("./new_mesh_co_geo_mesh_y.npy")
co_newmesh_facing = np.load("./gs_new_mesh_co.npy")


al_new_mesh = np.load("./new_mesh_al_geo_mesh_center.npy")
al_new_mesh_x = np.load("./new_mesh_al_geo_mesh_x.npy")
al_new_mesh_y = np.load("./new_mesh_al_geo_mesh_y.npy")
al_newmesh_facing = np.load("./gs_new_mesh_al.npy")


newSAS_mesh = np.load("./new_SAS_geo_mesh_center.npy")
newSAS_mesh_x = np.load("./new_SAS_geo_mesh_y.npy")
newSAS_mesh_y = np.load("./new_SAS_geo_mesh_y.npy")
newSAS_facing = np.load("./gs_new_SAS.npy")


v1SAS_mesh = np.load("./v1_SAS_geo_mesh_center.npy")
v1SAS_mesh_x = np.load("./v1_SAS_geo_mesh_y.npy")
v1SAS_mesh_y = np.load("./v1_SAS_geo_mesh_y.npy")
v1SAS_facing = np.load("./gs_SAS_v1.npy")




def co_distance_center(first_point, second_point):
    x_range = x_co_meshinfo[first_point[1],first_point[0]]-x_co_meshinfo[second_point[1],second_point[0]]
    y_range = y_co_meshinfo[first_point[1],first_point[0]]-y_co_meshinfo[second_point[1],second_point[0]]
    result = (x_range**2 + y_range**2)**(1/2)
    return result

def co_distance_point(first_point, second_point):
    x_range = co_mesh_x[first_point[2],first_point[1],first_point[0]]-co_mesh_x[second_point[2],second_point[1],second_point[0]]
    y_range = co_mesh_y[first_point[2],first_point[1],first_point[0]]-co_mesh_y[second_point[2],second_point[1],second_point[0]]
    result = (x_range**2 + y_range**2)**(1/2)
    return result

def al_distance_center(first_point, second_point):
    x_range = x_al_meshinfo[first_point[1],first_point[0]]-x_al_meshinfo[second_point[1],second_point[0]]
    y_range = y_al_meshinfo[first_point[1],first_point[0]]-y_al_meshinfo[second_point[1],second_point[0]]
    result = (x_range**2 + y_range**2)**(1/2)
    return result

def al_distance_point(first_point, second_point):
    x_range = al_mesh_x[first_point[2],first_point[1],first_point[0]]-al_mesh_x[second_point[2],second_point[1],second_point[0]]
    y_range = al_mesh_y[first_point[2],first_point[1],first_point[0]]-al_mesh_y[second_point[2],second_point[1],second_point[0]]
    result = (x_range**2 + y_range**2)**(1/2)
    return result

    #new geo files
def co_new_mesh_distance_center(first_point, second_point):
    x_range = x_co_new_meshinfo[first_point[1],first_point[0]]-x_co_new_meshinfo[second_point[1],second_point[0]]
    y_range = y_co_new_meshinfo[first_point[1],first_point[0]]-y_co_new_meshinfo[second_point[1],second_point[0]]
    result = (x_range**2 + y_range**2)**(1/2)
    return result
def co_new_mesh_distance_point(first_point, second_point):
    x_range = co_new_mesh_x[first_point[2],first_point[1],first_point[0]]-co_new_mesh_x[second_point[2],second_point[1],second_point[0]]
    y_range = co_new_mesh_y[first_point[2],first_point[1],first_point[0]]-co_new_mesh_y[second_point[2],second_point[1],second_point[0]]
    result = (x_range**2 + y_range**2)**(1/2)
    return result


def al_new_mesh_distance_center(first_point, second_point):
    x_range = x_al_new_meshinfo[first_point[1],first_point[0]]-x_al_new_meshinfo[second_point[1],second_point[0]]
    y_range = y_al_new_meshinfo[first_point[1],first_point[0]]-y_al_new_meshinfo[second_point[1],second_point[0]]
    result = (x_range**2 + y_range**2)**(1/2)
    return result

def al_new_mesh_distance_point(first_point, second_point):
    x_range = al_new_mesh_x[first_point[2],first_point[1],first_point[0]]-al_new_mesh_x[second_point[2],second_point[1],second_point[0]]
    y_range = al_new_mesh_y[first_point[2],first_point[1],first_point[0]]-al_new_mesh_y[second_point[2],second_point[1],second_point[0]]
    result = (x_range**2 + y_range**2)**(1/2)
    return result

def newSAS_distance_center(first_point, second_point):
    x_range = x_newSAS_meshinfo[first_point[1],first_point[0]]-x_newSAS_meshinfo[second_point[1],second_point[0]]
    y_range = y_newSAS_meshinfo[first_point[1],first_point[0]]-y_newSAS_meshinfo[second_point[1],second_point[0]]
    result = (x_range**2 + y_range**2)**(1/2)
    return result

def newSAS_distance_point(first_point, second_point):
    x_range = newSAS_mesh_x[first_point[2],first_point[1],first_point[0]]-newSAS_mesh_x[second_point[2],second_point[1],second_point[0]]
    y_range = newSAS_mesh_y[first_point[2],first_point[1],first_point[0]]-newSAS_mesh_y[second_point[2],second_point[1],second_point[0]]
    result = (x_range**2 + y_range**2)**(1/2)
    return result

def v1SAS_distance_center(first_point, second_point):
    x_range = x_v1SAS_meshinfo[first_point[1],first_point[0]]-x_v1SAS_meshinfo[second_point[1],second_point[0]]
    y_range = y_v1SAS_meshinfo[first_point[1],first_point[0]]-y_v1SAS_meshinfo[second_point[1],second_point[0]]
    result = (x_range**2 + y_range**2)**(1/2)
    return result

def v1SAS_distance_point(first_point, second_point):
    x_range = v1SAS_mesh_x[first_point[2],first_point[1],first_point[0]]-v1SAS_mesh_x[second_point[2],second_point[1],second_point[0]]
    y_range = v1SAS_mesh_y[first_point[2],first_point[1],first_point[0]]-v1SAS_mesh_y[second_point[2],second_point[1],second_point[0]]
    result = (x_range**2 + y_range**2)**(1/2)
    return result




def total_pressure(ne,te,na,ti):
    pr = ne[:,:]*te[:,:] + na[1,:,:]*ti[:,:] +np.sum(na[2:9,:,:]*ti[:,:],axis = 0)+np.sum(na[9:,:,:]*ti[:,:],axis = 0)
    return pr

def neutral_pressure(na,ti):
    pr = na[0,:,:]*ti[:,:]+ na[0,:,:]*ti[:,:]+ na[2,:,:]*ti[:,:]+na[2,:,:]*ti[:,:]+na[9,:,:]*ti[:,:]
    return pr
    

dumx_co_meshinfo = co_mesh[:,0]
dumy_co_meshinfo = co_mesh[:,1]
x_co_meshinfo = dumx_co_meshinfo.reshape(ny+2,nx+2)
y_co_meshinfo = dumy_co_meshinfo.reshape(ny+2,nx+2)

dumx_al_meshinfo = al_mesh[:,0]
dumy_al_meshinfo = al_mesh[:,1]
x_al_meshinfo = dumx_al_meshinfo.reshape(ny+2,nx+2)
y_al_meshinfo = dumy_al_meshinfo.reshape(ny+2,nx+2)

dumx_co_new_meshinfo = co_new_mesh[:,0]
dumy_co_new_meshinfo = co_new_mesh[:,1]
x_co_new_meshinfo = dumx_co_new_meshinfo.reshape(ny+2,nx+2)
y_co_new_meshinfo = dumy_co_new_meshinfo.reshape(ny+2,nx+2)

dumx_al_new_meshinfo = al_new_mesh[:,0]
dumy_al_new_meshinfo = al_new_mesh[:,1]
x_al_new_meshinfo = dumx_al_new_meshinfo.reshape(ny+2,nx+2)
y_al_new_meshinfo = dumy_al_new_meshinfo.reshape(ny+2,nx+2)

dumx_newSAS_meshinfo = newSAS_mesh[:,0]
dumy_newSAS_meshinfo = newSAS_mesh[:,1]
x_newSAS_meshinfo = dumx_newSAS_meshinfo.reshape(ny+2,nx+2)
y_newSAS_meshinfo = dumy_newSAS_meshinfo.reshape(ny+2,nx+2)

dumx_v1SAS_meshinfo = v1SAS_mesh[:,0]
dumy_v1SAS_meshinfo = v1SAS_mesh[:,1]
x_v1SAS_meshinfo = dumx_v1SAS_meshinfo.reshape(ny+2,nx+2)
y_v1SAS_meshinfo = dumy_v1SAS_meshinfo.reshape(ny+2,nx+2)


#po_dumx_meshinfo = convmesh[:,0]
#po_dumy_meshinfo = convmesh[:,1]
#po_x_meshinfo = dumx_meshinfo.reshape(4,ny+2,nx+2)
#po_y_meshinfo = dumy_meshinfo.reshape(4,ny+2,nx+2)
co_sep_out_target = np.zeros(2)
co_sep_out_target[0] = co_mesh_x[1,18,96]
co_sep_out_target[1] = co_mesh_y[1,18,96]
co_mesh_x_cen = np.sum(co_mesh_x, axis = 0)/4
co_mesh_y_cen = np.sum(co_mesh_y, axis = 0)/4

al_sep_out_target = np.zeros(2)
al_sep_out_target[0] = al_mesh_x[1,18,96]
al_sep_out_target[1] = al_mesh_y[1,18,96]
al_mesh_x_cen = np.sum(al_mesh_x, axis = 0)/4
al_mesh_y_cen = np.sum(al_mesh_y, axis = 0)/4

co_new_mesh_sep_out_target = np.zeros(2)
co_new_mesh_sep_out_target[0] = co_mesh_x[1,18,96]
co_new_mesh_sep_out_target[1] = co_mesh_y[1,18,96]
co_new_mesh_x_cen = np.sum(co_mesh_x, axis = 0)/4
co_new_mesh_y_cen = np.sum(co_mesh_y, axis = 0)/4

al_new_mesh_sep_out_target = np.zeros(2)
al_new_mesh_sep_out_target[0] = al_new_mesh_x[1,18,96]
al_new_mesh_sep_out_target[1] = al_new_mesh_y[1,18,96]
al_new_mesh_x_cen = np.sum(al_new_mesh_x, axis = 0)/4
al_new_mesh_y_cen = np.sum(al_new_mesh_y, axis = 0)/4

newSAS_sep_out_target = np.zeros(2)
newSAS_sep_out_target[0] = newSAS_mesh_x[1,18,96]
newSAS_sep_out_target[1] = newSAS_mesh_y[1,18,96]
newSAS_mesh_x_cen = np.sum(newSAS_mesh_x, axis = 0)/4
newSAS_mesh_y_cen = np.sum(newSAS_mesh_y, axis = 0)/4

v1SAS_sep_out_target = np.zeros(2)
v1SAS_sep_out_target[0] = v1SAS_mesh_x[1,18,96]
v1SAS_sep_out_target[1] = v1SAS_mesh_y[1,18,96]
v1SAS_mesh_x_cen = np.sum(v1SAS_mesh_x, axis = 0)/4
v1SAS_mesh_y_cen = np.sum(v1SAS_mesh_y, axis = 0)/4


X_point = []



co_sep_out_target_dist = np.zeros(ny+2)
co_sep_in_target_dist = np.zeros(ny+2)     
co_sep_out_midplane_dist = np.zeros(ny+2)
co_sep_in_midplane_dist = np.zeros(ny+2)

co_new_mesh_sep_out_midplane_dist = np.zeros(ny+2)
co_new_mesh_sep_in_midplane_dist = np.zeros(ny+2)
co_new_mesh_sep_out_target_dist = np.zeros(ny+2)
co_new_mesh_sep_in_target_dist = np.zeros(ny+2)

al_sep_out_midplane_dist = np.zeros(ny+2)
al_sep_in_midplane_dist = np.zeros(ny+2)
al_sep_out_target_dist = np.zeros(ny+2)
al_sep_in_target_dist = np.zeros(ny+2)


al_new_mesh_sep_out_midplane_dist = np.zeros(ny+2)
al_new_mesh_sep_in_midplane_dist = np.zeros(ny+2)
al_new_mesh_sep_out_target_dist = np.zeros(ny+2)
al_new_mesh_sep_in_target_dist = np.zeros(ny+2)

newSAS_sep_out_midplane_dist = np.zeros(ny+2)
newSAS_sep_in_midplane_dist = np.zeros(ny+2)
newSAS_sep_out_target_dist = np.zeros(ny+2)
newSAS_sep_in_target_dist = np.zeros(ny+2)

v1SAS_sep_out_midplane_dist = np.zeros(ny+2)
v1SAS_sep_in_midplane_dist = np.zeros(ny+2)
v1SAS_sep_out_target_dist = np.zeros(ny+2)
v1SAS_sep_in_target_dist = np.zeros(ny+2)

conv_Xpt_dist = np.zeros(20)
al_Xpt_dist = np.zeros(20)






# for i in range(ny+2):
#     co_sep_out_midplane_dist[i] = co_distance_point([52,i,1],[52,18,1])
#     co_sep_in_midplane_dist[i]  = co_distance_point([29,i,1],[29,18,1])
#     co_sep_out_target_dist[i] = co_distance_point([96,i,1],[96,18,1])
#     co_sep_in_target_dist[i] = co_distance_point([1,i,1],[1,18,1])


#     co_new_mesh_sep_out_midplane_dist[i] = co_new_mesh_distance_point([52,i,1],[52,18,1])
#     co_new_mesh_sep_in_midplane_dist[i]  = co_new_mesh_distance_point([29,i,1],[29,18,1])
#     co_new_mesh_sep_out_target_dist[i] = co_new_mesh_distance_point([96,i,1],[96,18,1])
#     co_new_mesh_sep_in_target_dist[i]  = co_new_mesh_distance_point([1,i,1],[1,18,1])

#     al_sep_out_midplane_dist[i] = al_distance_point([52,i,1],[52,18,1])
#     al_sep_in_midplane_dist[i]  = al_distance_point([29,i,1],[29,18,1])
#     al_sep_out_target_dist[i] = al_distance_point([96,i,1],[96,18,1])
#     al_sep_in_target_dist[i]  = al_distance_point([1,i,1],[1,18,1])


#     al_new_mesh_sep_out_midplane_dist[i] = al_new_mesh_distance_point([52,i,1],[52,18,1])
#     al_new_mesh_sep_in_midplane_dist[i]  = al_new_mesh_distance_point([29,i,1],[29,18,1])
#     al_new_mesh_sep_out_target_dist[i] = al_new_mesh_distance_point([96,i,1],[96,18,1])
#     al_new_mesh_sep_in_target_dist[i]  = al_new_mesh_distance_point([1,i,1],[1,18,1])
    

#     newSAS_sep_out_midplane_dist[i] = newSAS_distance_point([52,i,1],[52,18,1])
#     newSAS_sep_in_midplane_dist[i]  = newSAS_distance_point([29,i,1],[29,18,1])
#     newSAS_sep_out_target_dist[i] = newSAS_distance_point([96,i,1],[96,18,1])
#     newSAS_sep_in_target_dist[i]  = newSAS_distance_point([1,i,1],[1,18,1])
    
#     if i<18:
#         co_sep_out_midplane_dist[i] = -co_sep_out_midplane_dist[i]
#         co_sep_in_midplane_dist[i]  = -co_sep_in_midplane_dist[i]
#         co_sep_out_target_dist[i] = -co_sep_out_target_dist[i]
#         co_sep_in_target_dist[i] = -co_sep_in_target_dist[i]

#         co_new_mesh_sep_out_midplane_dist[i] = -co_new_mesh_sep_out_midplane_dist[i]
#         co_new_mesh_sep_in_midplane_dist[i]  = -co_new_mesh_sep_in_midplane_dist[i]
#         co_new_mesh_sep_out_target_dist[i] = -co_new_mesh_sep_out_target_dist[i]
#         co_new_mesh_sep_in_target_dist[i] = -co_new_mesh_sep_in_target_dist[i]

        
#         al_sep_out_midplane_dist[i] = -al_sep_out_midplane_dist[i]
#         al_sep_in_midplane_dist[i] = -al_sep_in_midplane_dist[i]
#         al_sep_out_target_dist[i] = -al_sep_out_target_dist[i]
#         al_sep_in_target_dist[i] = -al_sep_in_target_dist[i]
        
#         al_new_mesh_sep_out_midplane_dist[i] = -al_new_mesh_sep_out_midplane_dist[i]
#         al_new_mesh_sep_in_midplane_dist[i] = -al_new_mesh_sep_in_midplane_dist[i]
#         al_new_mesh_sep_out_target_dist[i] = -al_new_mesh_sep_out_target_dist[i]
#         al_new_mesh_sep_in_target_dist[i] = -al_new_mesh_sep_in_target_dist[i]

        
#         newSAS_sep_out_midplane_dist[i] = -newSAS_sep_out_midplane_dist[i]
#         newSAS_sep_in_midplane_dist[i] = -newSAS_sep_in_midplane_dist[i]
#         newSAS_sep_out_target_dist[i] = -newSAS_sep_out_target_dist[i]
#         newSAS_sep_in_target_dist[i] = -newSAS_sep_in_target_dist[i]
        
for i in range(1, ny+2):
    co_sep_out_midplane_dist[i] = co_distance_point([52,i-1,1],[52,i,1])
    co_sep_in_midplane_dist[i]  = co_distance_point([29,i-1,1],[29,i,1])
    co_sep_out_target_dist[i] = co_distance_point([96,i-1,1],[96,i,1])
    co_sep_in_target_dist[i] = co_distance_point([1,i-1,1],[1,i,1])


    co_new_mesh_sep_out_midplane_dist[i] = co_new_mesh_distance_point([52,i-1,1],[52,i,1])
    co_new_mesh_sep_in_midplane_dist[i]  = co_new_mesh_distance_point([29,i-1,1],[29,i,1])
    co_new_mesh_sep_out_target_dist[i] = co_new_mesh_distance_point([96,i-1,1],[96,i,1])
    co_new_mesh_sep_in_target_dist[i]  = co_new_mesh_distance_point([1,i-1,1],[1,i,1])

    al_sep_out_midplane_dist[i] = al_distance_point([52,i-1,1],[52,i,1])
    al_sep_in_midplane_dist[i]  = al_distance_point([29,i-1,1],[29,i,1])
    al_sep_out_target_dist[i] = al_distance_point([96,i-1,1],[96,i,1])
    al_sep_in_target_dist[i]  = al_distance_point([1,i-1,1],[1,i,1])


    al_new_mesh_sep_out_midplane_dist[i] = al_new_mesh_distance_point([52,i-1,1],[52,i,1])
    al_new_mesh_sep_in_midplane_dist[i]  = al_new_mesh_distance_point([29,i-1,1],[29,i,1])
    al_new_mesh_sep_out_target_dist[i] = al_new_mesh_distance_point([96,i-1,1],[96,i,1])
    al_new_mesh_sep_in_target_dist[i]  = al_new_mesh_distance_point([1,i-1,1],[1,i,1])
    

    # newSAS_sep_out_midplane_dist[i] = newSAS_distance_point([52,i-1,1],[52,i,1])
    # newSAS_sep_in_midplane_dist[i]  = newSAS_distance_point([29,i-1,1],[29,i,1])
    # newSAS_sep_out_target_dist[i] = newSAS_distance_point([96,i-1,1],[96,i,1])
    # newSAS_sep_in_target_dist[i]  = newSAS_distance_point([1,i-1,1],[1,i,1])
    newSAS_sep_out_midplane_dist[i] = newSAS_distance_center([52,i-1,1],[52,i,1])
    newSAS_sep_in_midplane_dist[i]  = newSAS_distance_center([29,i-1,1],[29,i,1])
    newSAS_sep_out_target_dist[i] = newSAS_distance_center([96,i-1,1],[96,i,1])
    newSAS_sep_in_target_dist[i]  = newSAS_distance_center([1,i-1,1],[1,i,1])

    v1SAS_sep_out_midplane_dist[i] = v1SAS_distance_center([52,i-1,1],[52,i,1])
    v1SAS_sep_in_midplane_dist[i]  = v1SAS_distance_center([29,i-1,1],[29,i,1])
    v1SAS_sep_out_target_dist[i] = v1SAS_distance_center([96,i-1,1],[96,i,1])
    v1SAS_sep_in_target_dist[i]  = v1SAS_distance_center([1,i-1,1],[1,i,1])


co_sep_out_midplane_dist = np.cumsum(co_sep_out_midplane_dist)
co_sep_in_midplane_dist  = np.cumsum(co_sep_in_midplane_dist)
co_sep_out_target_dist   = np.cumsum(co_sep_out_target_dist)
co_sep_in_target_dist    = np.cumsum(co_sep_in_target_dist)

co_new_mesh_sep_out_midplane_dist= np.cumsum(co_new_mesh_sep_out_midplane_dist)
co_new_mesh_sep_in_midplane_dist  = np.cumsum(co_new_mesh_sep_in_midplane_dist)
co_new_mesh_sep_out_target_dist   = np.cumsum(co_new_mesh_sep_out_target_dist)
co_new_mesh_sep_in_target_dist    = np.cumsum(co_new_mesh_sep_in_target_dist)

    
al_sep_out_midplane_dist = np.cumsum(al_sep_out_midplane_dist)
al_sep_in_midplane_dist  = np.cumsum(al_sep_in_midplane_dist)
al_sep_out_target_dist   = np.cumsum(al_sep_out_target_dist)
al_sep_in_target_dist    = np.cumsum(al_sep_in_target_dist)
    
al_new_mesh_sep_out_midplane_dist = np.cumsum(al_new_mesh_sep_out_midplane_dist)
al_new_mesh_sep_in_midplane_dist  = np.cumsum(al_new_mesh_sep_in_midplane_dist)
al_new_mesh_sep_out_target_dist   = np.cumsum(al_new_mesh_sep_out_target_dist)
al_new_mesh_sep_in_target_dist   = np.cumsum(al_new_mesh_sep_in_target_dist)


newSAS_sep_out_midplane_dist = np.cumsum(newSAS_sep_out_midplane_dist)
newSAS_sep_in_midplane_dist  = np.cumsum(newSAS_sep_in_midplane_dist)
newSAS_sep_out_target_dist   = np.cumsum(newSAS_sep_out_target_dist)
newSAS_sep_in_target_dist    = np.cumsum(newSAS_sep_in_target_dist)

v1SAS_sep_out_midplane_dist = np.cumsum(v1SAS_sep_out_midplane_dist)
v1SAS_sep_in_midplane_dist  = np.cumsum(v1SAS_sep_in_midplane_dist)
v1SAS_sep_out_target_dist   = np.cumsum(v1SAS_sep_out_target_dist)
v1SAS_sep_in_target_dist    = np.cumsum(v1SAS_sep_in_target_dist)

#print(newSAS_sep_out_target_dist)
for k in range(19):
    co_sep_out_midplane_dist[k] = co_sep_out_midplane_dist[k]-co_sep_out_midplane_dist[18]
    co_sep_in_midplane_dist[k]  = co_sep_in_midplane_dist[k]-co_sep_in_midplane_dist[18]
    co_sep_out_target_dist[k]   = co_sep_out_target_dist[k]-co_sep_out_target_dist[18]
    co_sep_in_target_dist[k]    = co_sep_in_target_dist[k]-co_sep_in_target_dist[18]

    co_new_mesh_sep_out_midplane_dist[k] = co_new_mesh_sep_out_midplane_dist[k]-co_new_mesh_sep_out_midplane_dist[18]
    co_new_mesh_sep_in_midplane_dist[k]  = co_new_mesh_sep_in_midplane_dist[k] -co_new_mesh_sep_in_midplane_dist[18]
    co_new_mesh_sep_out_target_dist[k]   = co_new_mesh_sep_out_target_dist[k] -co_new_mesh_sep_out_target_dist[18]
    co_new_mesh_sep_in_target_dist[k]    = co_new_mesh_sep_in_target_dist[k] -co_new_mesh_sep_in_target_dist[18]

    
    al_sep_out_midplane_dist[k] = al_sep_out_midplane_dist[k]-al_sep_out_midplane_dist[18]
    al_sep_in_midplane_dist[k]  = al_sep_in_midplane_dist[k]-al_sep_in_midplane_dist[18]
    al_sep_out_target_dist[k]   = al_sep_out_target_dist[k]-al_sep_out_target_dist[18]
    al_sep_in_target_dist[k]    = al_sep_in_target_dist[k]-al_sep_in_target_dist[18]
    
    al_new_mesh_sep_out_midplane_dist[k] = al_new_mesh_sep_out_midplane_dist[k]-al_new_mesh_sep_out_midplane_dist[18]
    al_new_mesh_sep_in_midplane_dist[k]  = al_new_mesh_sep_in_midplane_dist[k]-al_new_mesh_sep_in_midplane_dist[18]
    al_new_mesh_sep_out_target_dist[k]   = al_new_mesh_sep_out_target_dist[k]-al_new_mesh_sep_out_target_dist[18]
    al_new_mesh_sep_in_target_dist[k]    = al_new_mesh_sep_in_target_dist[k]-al_new_mesh_sep_in_target_dist[18]

    
    newSAS_sep_out_midplane_dist[k] = newSAS_sep_out_midplane_dist[k]-newSAS_sep_out_midplane_dist[18]
    newSAS_sep_in_midplane_dist[k]  = newSAS_sep_in_midplane_dist[k]-newSAS_sep_in_midplane_dist[18]
    newSAS_sep_out_target_dist[k]   = newSAS_sep_out_target_dist[k]-newSAS_sep_out_target_dist[18]
    newSAS_sep_in_target_dist[k]    = newSAS_sep_in_target_dist[k]-newSAS_sep_in_target_dist[18]
    
    v1SAS_sep_out_midplane_dist[k] = v1SAS_sep_out_midplane_dist[k]-v1SAS_sep_out_midplane_dist[18]
    v1SAS_sep_in_midplane_dist[k]  = v1SAS_sep_in_midplane_dist[k]-v1SAS_sep_in_midplane_dist[18]
    v1SAS_sep_out_target_dist[k]   = v1SAS_sep_out_target_dist[k]-v1SAS_sep_out_target_dist[18]
    v1SAS_sep_in_target_dist[k]    = v1SAS_sep_in_target_dist[k]-v1SAS_sep_in_target_dist[18]
#print(newSAS_sep_out_target_dist)

    
for i in range(20):
    conv_Xpt_dist[i] = co_distance_center([78,18],[78+i,18])

    
    
for i in range(20):
    al_Xpt_dist[i] = al_distance_center([78,18],[78+i,18])


def con_outer_target_dist():
    return(co_sep_in_target_dist)
def con_inner_target_dist():
    return(co_sep_out_target_dist)

def SAS_inner_target_dist():
    return(al_sep_in_target_dist)
def SAS_outer_target_dist():
    return(al_sep_out_target_dist)
    
def con_newmesh_outer_target_dist():
    return(co_new_mesh_sep_out_target_dist)
def con_newmesh_innerer_target_dist():
    return(co_new_mesh_sep_in_target_dist)

def SAS_newmesh_outer_target_dist():
    return(al_new_mesh_sep_out_target_dist)
def SAS_newmesh_inner_target_dist():
    return(al_new_mesh_sep_in_target_dist)
def newSAS_outer_target_dist():
    return(newSAS_sep_out_target_dist)
def newSAS_inner_target_dist():
    return(newSAS_sep_in_target_dist)

def v1SAS_outer_target_dist():
    return(v1SAS_sep_out_target_dist)
def v1SAS_inner_target_dist():
    return(v1SAS_sep_in_target_dist)