# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 12:48:50 2016

@author: s0568630
"""

import numpy as np
from Raster import Raster
import matplotlib.pyplot as mp
from RasterHandler import readRaster, writeRasterToAscii

raster=readRaster("RasterTest.txt")

data=raster.getData()

print 'original data'
print data

mp.matshow(data)
mp.colorbar()


slopeRaster = raster.slope()
slopedata=slopeRaster.getData()

print 'slopedata'
print slopedata
        
writeRasterToAscii('slopetest.asc', slopeRaster)

mp.matshow(slopedata)
mp.colorbar()

mp.show()