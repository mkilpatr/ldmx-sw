#!/usr/bin/python

# we need the ldmx configuration package to construct the object
from LDMX.Framework import ldmxcfg

HcalTracks = ldmxcfg.Producer( "HcalMipTrigger" , "ldmx::HcalMipTriggerProducer" )

# name of collection that contains the hcal hits 
HcalTracks.parameters["HcalHitCollectionName"] = "hcalDigis"
HcalTracks.parameters["HcalHitPassName"] = "recon"

# hcal specifications
HcalTracks.parameters["NumLayersBackHcal"]   = 81 
HcalTracks.parameters["NumLayersTopHcal"]    = 81 
HcalTracks.parameters["NumLayersBottomHcal"] = 81 
HcalTracks.parameters["NumLayersLeftHcal"]   = 81 
HcalTracks.parameters["NumLayersRightHcal"]  = 81 

# minimum PE for a single hit to be considered non-noise
HcalTracks.parameters["MinimumPE"] = 5.5

# maximum Energy of a group of hits to be considered a mip
HcalTracks.parameters["MaximumEnergy"] = 4000.0

# maximum difference (in strips) between a hit and the centerline of a track
HcalTracks.parameters["MaximumStripDifference"] = 2

# Minimum number of layers hit in track to be considered valid track
HcalTracks.parameters["MinTrackLayerHits"] = 5

# Name of track collection to be added to event bus
HcalTracks.parameters["HcalMipTriggerObjectName"] = "hcalMipTrigger"
 