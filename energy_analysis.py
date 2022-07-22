#! /usr/bin/env python
from __future__ import print_function
import netCDF4
import os
import matplotlib
if not os.getenv("DISPLAY"): matplotlib.use('Agg')
import matplotlib.pylab as plt
import sys
import numpy
import subprocess

if os.access('b2mn.exe.dir/b2tallies.nc', os.R_OK):
  f=netCDF4.Dataset('b2mn.exe.dir/b2tallies.nc','r')
else:
  f=netCDF4.Dataset('b2tallies.nc','r')
vreg=f.dimensions['vreg'].size
xreg=f.dimensions['xreg'].size
yreg=f.dimensions['yreg'].size
ns=f.dimensions['ns'].size
time=f.dimensions['time'].size
times=f.variables['times']
fhexreg=f.variables['fhexreg']
fheyreg=f.variables['fheyreg']
fhixreg=f.variables['fhixreg']
fhiyreg=f.variables['fhiyreg']

plt.bar(1,-fhexreg[:,1]-fhixreg[:,1], label='-W')
plt.bar(2,-fhexreg[:,2]-fhixreg[:,2], label='-w')
plt.bar(3,fhexreg[:,3]+fhixreg[:,3], label='e')
plt.bar(4,fhexreg[:,4]+fhixreg[:,4], label='E')
plt.bar(5,fheyreg[:,2]+fhiyreg[:,2], label='core')
plt.bar(6,fheyreg[:,4]+fhiyreg[:,4], label='sep')
plt.bar(7,numpy.sum(fheyreg[:,5:8],axis=1)+numpy.sum(fhiyreg[:,5:8],axis=1), label='mcw')
plt.bar(8,-fheyreg[:,1]-fhiyreg[:,1]-fheyreg[:,3]-fhiyreg[:,3], label='-pfw')
if  matplotlib.__version__ <=  '0.98.1':
  plt.legend(loc=0)
else:
  plt.legend(loc=0, frameon=False)
plt.xlabel('time [s]')
plt.ylabel('energy fluxes [W]')

cwd=os.getcwd()
l=0
ncwd=''
for i in cwd.split('/'):
  if l + 1 + len(i) < 100:
    ncwd = ncwd + '/' + i
    l = l + 1 + len(i)
  else:
    ncwd = ncwd + '/\n' + i
    l = len(i)
plt.suptitle(ncwd[1:], fontsize=10)
  
if os.getenv('SOLPS_PYTHON_PLOT') is None:
  plt.show()
else:
  plt.savefig('energy_analysis.' + os.getenv('SOLPS_PYTHON_PLOT'))




