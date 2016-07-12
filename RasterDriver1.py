# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 01:39:35 2013

@author: nrjh
"""

from RasterHandler import readRaster
from Raster import Raster
import matplotlib.pyplot as mp

raster=readRaster("raster_test2.txt")

data=raster.getData()

print data
        
mp.imshow(data)
mp.colorbar()
mp.matshow(data)
mp.colorbar()

mp.show()