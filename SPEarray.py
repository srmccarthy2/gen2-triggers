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
            energy = frame["MCMuon"].energy
            cos_zenith = np.cos(frame["MCMuon"].dir.zenith)
            eff_area = frame["MuonEffectiveArea"].value
            for DOM, MCPE in frame["I3RecoPulseSeriesMapGen2"]:
                for SPE in MCPE:
                    DOMstr = str((DOM[0])+ (DOM[1]))
                    DOMs = int(DOMstr)
                    data = [DOMs,SPE.charge, SPE.time, weight, cos_zenith, eff_area, energy]
                    SPE_data.append(data)
file = '/data/user/smccarthy/gen2_files/weighting/pDOM/final/SPEarray.txt'
np.savetxt(file,SPE_data) 
with open('/data/user/smccarthy/gen2_files/weighting/pDOM/final/weights.txt', 'w') as filehandle:  
    for listitem in weights:
        filehandle.write('%f\n' % listitem)

#mDOMdata
SPE_data = []
weights = []
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
            energy = frame["MCMuon"].energy
            cos_zenith = np.cos(frame["MCMuon"].dir.zenith)
            eff_area = frame["MuonEffectiveArea"].value
            for DOM, MCPE in frame["I3RecoPulseSeriesMapGen2"]:
                for SPE in MCPE:
                    DOMstr = str((DOM[0])+ (DOM[1]))
                    DOMs = int(DOMstr)
                    data = [DOMs,SPE.charge, SPE.time, weight, cos_zenith, eff_area, energy]
                    SPE_data.append(data)
file = '/data/user/smccarthy/gen2_files/weighting/mDOM/final/SPEarray.txt'
np.savetxt(file,SPE_data) 
with open('/data/user/smccarthy/gen2_files/weighting/mDOM/final/weights.txt', 'w') as filehandle:  
    for listitem in weights:
        filehandle.write('%f\n' % listitem)

#DEggdata
SPE_data = []
weights = []
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
            energy = frame["MCMuon"].energy
            cos_zenith = np.cos(frame["MCMuon"].dir.zenith)
            eff_area = frame["MuonEffectiveArea"].value
            for DOM, MCPE in frame["I3RecoPulseSeriesMapGen2"]:
                for SPE in MCPE:
                    DOMstr = str((DOM[0])+ (DOM[1]))
                    DOMs = int(DOMstr)
                    data = [DOMs,SPE.charge, SPE.time, weight, cos_zenith, eff_area, energy]
                    SPE_data.append(data)
file = '/data/user/smccarthy/gen2_files/weighting/DEgg/final/SPEarray.txt'
np.savetxt(file,SPE_data) 
with open('/data/user/smccarthy/gen2_files/weighting/DEgg/final/weights.txt', 'w') as filehandle:  
    for listitem in weights:
        filehandle.write('%f\n' % listitem)
