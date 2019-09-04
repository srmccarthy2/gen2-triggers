#!/usr/bin/env python

#import icecube stuff
import icecube
from icecube import icetray, dataclasses, dataio
from icecube import phys_services, simclasses, MuonGun
from I3Tray import I3Tray
from icecube.icetray import I3Units
from icecube.MuonGun import load_model, StaticSurfaceInjector, Cylinder, OffsetPowerLaw, BundleConfiguration, BundleEntry
import numpy as np
from collections import Counter
import os
import glob

#pDOMdata
SPE_data = []
weights = []
energies =[]
cos_zeniths = []
area_eff = []
pDOM_files = glob.glob('/data/user/msilva/metaprojects/Gen2-Scripts/RECO_SPEs/MCReco_pDOM.i3.bz2')
for item in pDOM_files:
    f = dataio.I3File(item)
    for frame in f:
        if ("I3RecoPulseSeriesMapGen2" in frame):
            model = icecube.MuonGun.load_model('GaisserH4a_atmod12_SIBYLL') #natural rate
            muon = frame["MCMuon"]
            flux = model.flux(MuonGun.depth(muon.pos.z), np.cos(muon.dir.zenith), 1)*model.energy(MuonGun.depth(muon.pos.z), np.cos(muon.dir.zenith), 1, 0, muon.energy)
            weight = flux*frame['MuonEffectiveArea'].value
            weights.append(weight)
            energies.append(weight*frame["MCMuon"].energy)
            cos_zeniths.append(weight*np.cos(frame["MCMuon"].dir.zenith))
            area_eff.append(frame["MuonEffectiveArea"].value)
            for DOM, MCPE in frame["I3RecoPulseSeriesMapGen2"]:
                for SPE in MCPE:
                    DOM = str(DOM[0]) +',' + str(DOM[1]) 
                    data = [DOM,SPE.charge, SPE.time, weight, cos_zenith, area_eff]
                    SPE_data.append(data)

with open('/data/user/smccarthy/gen2_files/weighting/pDOM/final/SPEarray.txt', 'w') as filehandle:  
    for listitem in SPE_data:
        filehandle.write('\n'% listitem)  
with open('/data/user/smccarthy/gen2_files/weighting/pDOM/final/energies.txt', 'w') as filehandle:  
    for listitem in energies:
        filehandle.write('%f\n' % listitem) 
with open('/data/user/smccarthy/gen2_files/weighting/pDOM/final/cos_zeniths.txt', 'w') as filehandle:  
    for listitem in cos_zeniths:
        filehandle.write('%f\n' % listitem) 
with open('/data/user/smccarthy/gen2_files/weighting/pDOM/final/area_eff.txt', 'w') as filehandle:  
    for listitem in area_eff:
        filehandle.write('%f\n' % listitem) 
with open('/data/user/smccarthy/gen2_files/weighting/pDOM/final/weights.txt', 'w') as filehandle:  
    for listitem in weights:
        filehandle.write('%f\n' % listitem) 
				
#mDOMdata
SPE_data = []
weights = []
energies =[]
cos_zeniths = []
area_eff = []
mDOM_files = glob.glob('/data/user/msilva/metaprojects/Gen2-Scripts/RECO_SPEs/MCReco_mDOM.i3.bz2')
for item in mDOM_files:
    f = dataio.I3File(item)
    for frame in f:
        if ("I3RecoPulseSeriesMapGen2" in frame):
            model = icecube.MuonGun.load_model('GaisserH4a_atmod12_SIBYLL') #natural rate
            muon = frame["MCMuon"]
            flux = model.flux(MuonGun.depth(muon.pos.z), np.cos(muon.dir.zenith), 1)*model.energy(MuonGun.depth(muon.pos.z), np.cos(muon.dir.zenith), 1, 0, muon.energy)
            weight = flux*frame['MuonEffectiveArea'].value
            weights.append(weight)
            energies.append(weight*frame["MCMuon"].energy)
            cos_zeniths.append(weight*np.cos(frame["MCMuon"].dir.zenith))
            area_eff.append(frame["MuonEffectiveArea"].value)
            for DOM, MCPE in frame["I3RecoPulseSeriesMapGen2"]:
                for SPE in MCPE:
                    data = [str(DOM[0]) +',' + str(DOM[1]),SPE.charge, SPE.time, weight, cos_zenith, area_eff]
                    np.concatenate((SPE_data, data))
with open('/data/user/smccarthy/gen2_files/weighting/mDOM/final/SPEarray.txt', 'w') as filehandle:  
    for listitem in SPE_data:
        filehandle.write('%f\n' % listitem)  
with open('/data/user/smccarthy/gen2_files/weighting/mDOM/final/energies.txt', 'w') as filehandle:  
    for listitem in energies:
        filehandle.write('%f\n' % listitem) 
with open('/data/user/smccarthy/gen2_files/weighting/mDOM/final/cos_zeniths.txt', 'w') as filehandle:  
    for listitem in cos_zeniths:
        filehandle.write('%f\n' % listitem) 
with open('/data/user/smccarthy/gen2_files/weighting/mDOM/final/area_eff.txt', 'w') as filehandle:  
    for listitem in area_eff:
        filehandle.write('%f\n' % listitem) 
with open('/data/user/smccarthy/gen2_files/weighting/mDOM/final/weights.txt', 'w') as filehandle:  
    for listitem in weights:
        filehandle.write('%f\n' % listitem) 
				
#DEggdata
SPE_data = []
weights = []
energies =[]
cos_zeniths = []
area_eff = []
pDOM_files = glob.glob('/data/user/msilva/metaprojects/Gen2-Scripts/RECO_SPEs/MCReco_DEgg.i3.bz2')
for item in pDOM_files:
    f = dataio.I3File(item)
    for frame in f:
        if ("I3RecoPulseSeriesMapGen2" in frame):
            model = icecube.MuonGun.load_model('GaisserH4a_atmod12_SIBYLL') #natural rate
            muon = frame["MCMuon"]
            flux = model.flux(MuonGun.depth(muon.pos.z), np.cos(muon.dir.zenith), 1)*model.energy(MuonGun.depth(muon.pos.z), np.cos(muon.dir.zenith), 1, 0, muon.energy)
            weight = flux*frame['MuonEffectiveArea'].value
            weights.append(weight)
            energies.append(weight*frame["MCMuon"].energy)
            cos_zeniths.append(weight*np.cos(frame["MCMuon"].dir.zenith))
            area_eff.append(frame["MuonEffectiveArea"].value)
            for DOM, MCPE in frame["I3RecoPulseSeriesMapGen2"]:
                for SPE in MCPE:
                    data = [str(DOM[0]) +',' + str(DOM[1]),SPE.charge, SPE.time, weight, cos_zenith, area_eff]
                    np.concatenate((SPE_data, data))
with open('/data/user/smccarthy/gen2_files/weighting/DEgg/final/SPEarray.txt', 'w') as filehandle:  
    for listitem in SPE_data:
        filehandle.write('%f\n' % listitem)  
with open('/data/user/smccarthy/gen2_files/weighting/DEgg/final/energies.txt', 'w') as filehandle:  
    for listitem in energies:
        filehandle.write('%f\n' % listitem) 
with open('/data/user/smccarthy/gen2_files/weighting/DEgg/final/cos_zeniths.txt', 'w') as filehandle:  
    for listitem in cos_zeniths:
        filehandle.write('%f\n' % listitem) 
with open('/data/user/smccarthy/gen2_files/weighting/DEgg/final/area_eff.txt', 'w') as filehandle:  
    for listitem in area_eff:
        filehandle.write('%f\n' % listitem) 
with open('/data/user/smccarthy/gen2_files/weighting/DEgg/final/weights.txt', 'w') as filehandle:  
    for listitem in weights:
        filehandle.write('%f\n' % listitem) 
