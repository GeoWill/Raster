# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 16:54:07 2016

@author: s0568630
"""

import matplotlib.pyplot as mp
from RasterHandler import readRaster, writeRasterToAscii

raster=readRaster("RasterTest.txt")

data=raster.getData()

print 'original data'
print data

mp.matshow(data)
mp.colorbar()
mp.title('RasterTest')

slopeRaster = raster.slope()
slopedata=slopeRaster.getData()

print 'slope data'
print slopedata
        
writeRasterToAscii('RasterTest_slope.asc', slopeRaster)

mp.matshow(slopedata)
mp.colorbar()
mp.title('RasterTest_slope')

mp.show()