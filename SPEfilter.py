#!/usr/bin/env python
import numpy as np
import os
import glob
from collections import Counter
import matplotlib.pyplot as plt

#data readin
SPE_pDOM = []
SPE_mDOM = []
SPE_DEgg = []
with open('/data/user/smccarthy/gen2_files/weighting/pDOM/final/SPEarray.txt', 'r') as filehandle:  
    for line in filehandle:
        currentdatap = line[:-1]
        SPE_pDOM.append(currentdatap) 
with open('/data/user/smccarthy/gen2_files/weighting/mDOM/final/SPEarray.txt', 'r') as filehandle:  
    for line in filehandle:
        currentdatam = line[:-1]
        SPE_mDOM.append(currentdatam) 
with open('/data/user/smccarthy/gen2_files/weighting/DEgg/final/SPEarray.txt', 'r') as filehandle:  
    for line in filehandle:
        currentdatad = line[:-1]
        SPE_DEgg.append(currentdatad)

DOM_u = np.unique(DOMs_pDOM)
DOM_u_ind = np.where(DOM_u == DOMs_pDOM)
#data is of format [DOM, charge, time]
DOM_u = np.unique(SPE_pDOM[1])
DOM_u_ind = np.where(DOM_u == SPE_pDOM)
event = []
j = 0
print(DOM_u)
while j < len(DOM_u):
    i = 0
    while i < len(SPE_pDOM):
        if SPE_pDOM[0][i] == DOM_u[j]:
            chgperDOM+=weight*SPE_pDOM[1][i]
            i+=1
    #DOM level cut    
    if chgperDOM > 2.0:
        event.append([obj2,SPE_pDOM[2][j]]) 
    j+=1
    #add further implementations once we know this works

#data is of format [DOM, charge, time]
DOM_u = np.unique(SPE_DEgg[1])
DOM_u_ind = np.where(DOM_u == SPE_DEgg)
event = []
j = 0
print(len(SPE_DEgg))
while j < len(DOM_u):
    i = 0
    while i < len(SPE_DEgg):
        if SPE_DEgg[0][i] == DOM_u[j]:
            chgperDOM+=weight*SPE_DEgg[1][i]
            i+=1
    #DOM level cut    
    if chgperDOM > 2.0:
        event.append([obj2,SPE_DEgg[2][j]]) 
    j+=1
    #add further implementations once we know this works


#Event level cut
dom1_3 = []
dom2_3 = []
dom3_3 = []
dom4_3 = []
dom5_3 = []
dom10_3 = []
dom1_5 = []
dom2_5 = []
dom3_5 = []
dom4_5 = []
dom5_5 = []
dom10_5 = []
dom1_10 = []
dom2_10 = []
dom3_10 = []
dom4_10 = []
dom5_10 = []
dom10_10 = []

for time in event:
    #3 microsecond cut
    ind3 = (event[2] <= (3000.+time)) & (event[2] >= time)
    event3 = event[ind3]
    if(len(np.where(event3)>1):
        dom1_3.append(time)
    if(len(np.where(event3)>2):
        dom2_3.append(time)
    if(len(np.where(event3)>3):
        dom3_3.append(time)
    if(len(np.where(event3)>4):
        dom4_3.append(time)
    if(len(np.where(event3)>5):
        dom5_3.append(time)
    if(len(np.where(event3)>10):
        dom10_3.append(time)
    #5 microsecond cut
    ind5 = (event[2] <= (5000.+time)) & (event[2] >= time)
    event5 = event[ind5]
    if(len(np.where(event5)>1):
        dom1_5.append(time)
    if(len(np.where(event5)>2):
        dom2_5.append(time)
    if(len(np.where(event5)>3):
        dom3_5.append(time)
    if(len(np.where(event5)>4):
        dom4_5.append(time)
    if(len(np.where(event5)>5):
        dom5_5.append(time)
    if(len(np.where(event5)>10):
        dom10_5.append(time)
    #10 microsecond cut
    ind10 = (event[2] <= (10000.+time)) & (event[2] >= time)
    event10 = event[ind10]
    if(len(np.where(event10)>1):
        dom1_10.append(time)
    if(len(np.where(event10)>2):
        dom2_10.append(time)
    if(len(np.where(event10)>3):
        dom3_10.append(time)
    if(len(np.where(event10)>4):
        dom4_10.append(time)
    if(len(np.where(event10)>5):
        dom5_10.append(time)
    if(len(np.where(event10)>10):
        dom10_10.append(time)
