# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 15:32:08 2016

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 01:39:35 2013

@author: nrjh
"""

from RasterHandler import createRanRaster, createRanRasterSlope, readRaster
import matplotlib.pyplot as mp
from Flow import flowRaster

def plotleaves(flownode,colour):
    upnodes=flownode.getUpnodes()
    for node in upnodes:
        x1=flownode.get_x()
        y1=flownode.get_y()
        x2=node.get_x()
        y2=node.get_y()
        mp.plot([x1,x2],[y1,y2],color=colour)
        if (node.numUpnodes()>0):
            plotleaves(node,colour)

rows=20
cols=30
xorg=0.
yorg=0.
xp=5
yp=5
nodata=-999.999
cellsize=1.
levels=4
datahi=100.
datalow=0
randpercent=0.2

colours=["black","red","blue","yellow","green","cyan","white","orange","grey","brown"]

#raster=createRanRaster()
#raster=createRanRasterSlope(rows,cols,cellsize,xorg,yorg,nodata,levels,datahi,datalow,xp,yp,randpercent)   
raster=readRaster('Raster_test2.txt')
print 'raster read'
     
data=raster.getData()

mp.matshow(data)
mp.colorbar()


fr=flowRaster(raster.getData(),raster.getOrgs()[0],raster.getOrgs()[0],raster.getCellsize(),raster.getNoData())
fr.setDownCells()

pointlist=fr.getPointList()

for p in pointlist:
    mp.scatter(p.get_x(),p.get_y())
    
#for p in pointlist:
#    if (p.getDownnode()!=None):
#        x1=p.get_x()
#        y1=p.get_y()
#        x2=p.getDownnode().get_x()
#        y2=p.getDownnode().get_y()
#        mp.plot([x1,x2],[y1,y2],color="black")

pits=fr.getPits()
for p in pits:
    mp.scatter(p.get_x(),p.get_y(),color="red")

fr.setUpCells()

i=-1
for p in pits:
    i+=1
    j=i%len(colours)
    plotleaves(p,colours[j])

mp.show()

