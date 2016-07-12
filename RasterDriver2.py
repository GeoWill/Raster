# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 01:39:35 2013

@author: nrjh
"""

from RasterHandler import createRanRasterSlope
import matplotlib.pyplot as mp
from Flow import flowRaster

rows=10
cols=15
xorg=0.
yorg=0.
nodata=-999.999
cellsize=1.

#raster=createRanRaster()
raster=createRanRasterSlope(rows,cols,cellsize,xorg,yorg,nodata,3,100.,0.,1,1,0.2)   
     
data=raster.getData()

mp.matshow(data)
mp.colorbar()

fr=flowRaster(raster.getData(),raster.getOrgs()[0],raster.getOrgs()[0],raster.getCellsize(),raster.getNoData())
fr.setDownCells()

pointlist=fr.getPointList()

for p in pointlist:
    mp.scatter(p.get_x(),p.get_y())
    
for p in pointlist:
    if (p.getDownnode()!=None):
        x1=p.get_x()
        y1=p.get_y()
        x2=p.getDownnode().get_x()
        y2=p.getDownnode().get_y()
        mp.plot([x1,x2],[y1,y2])

mp.show()