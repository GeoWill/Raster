# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 12:42:44 2016

@author: s0568630
"""

from RasterHandler import readRaster, writeRasterToAscii
import matplotlib.pyplot as mp

#read in a raster from file
raster = readRaster("raster_test2.txt")
#extract data for plotting
rasData = raster.getData()

#calculate slope of raster data
slopeRas = raster.slope()
slopeData = slopeRas.getData()
        
#plot and show the two rasters
mp.matshow(rasData)
mp.colorbar()
mp.title('raster_test2')
mp.matshow(slopeData)
mp.colorbar()
mp.title('raster_test2_slope')
mp.show()

#write the slope raster to file
writeRasterToAscii('raster_test2_slope.txt',slopeRas)