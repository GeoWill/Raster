# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 14:36:23 2013

@author: nrjh
"""

import numpy as np
from Raster import Raster
from Points import Point2D

class flowNode(Point2D):
    
    def __init__(self,x,y):
        Point2D.__init__(self,x,y)
        self._downnode=None
        self._upnodes=[]
        self._pitflag=None
        
    def setDownnode(self,downnode):
        self._downnode=downnode 
    def getDownnode(self):
        return self._downnode 
        
    def setUpnode(self,node):
        self._upnodes.append(node)
    def getUpnodes(self):
        return self._upnodes
    
    def setPitFlag(self,arg):
        if arg == True:
            self._pitflag=True
        elif arg == False:
            self._pitflag=False
        else:
            print "set pit flage True or False"
    def getPitFlag(self):
        return self._pitflag
        
    def numUpnodes(self):
        return len(self._upnodes)
        

class flowRaster(Raster):

#Basic raster data held in superclass
    def __init__(self,data,xorg,yorg,cellsize,nodata=-999.999):
        Raster.__init__(self,data,xorg,yorg,cellsize,nodata)        
        self.nodes=[]
        for i in range(self.getRows()):
            for j in range(self.getCols()):
                y=(i)*cellsize+xorg
                x=(j)*cellsize+yorg
                self.nodes.append(flowNode(x,y))
            
        self._nodearray=np.array(self.nodes)
        self._nodearray.shape=(self.getRows(),self.getCols())
        
    def getPointList(self):
        return self.nodes

    def _getIterator(self):
        ilist=[1,-1,1,0,1,1,0,-1,0,1,-1,-1,-1,0,-1,1]        
        ip=np.array(ilist)
        ip.shape=(8,2)
        return ip
        
        
    def setDownCells(self):
       
       rows=self.getRows()
       cols=self.getCols()
       it=self._getIterator()
       for r in range(rows):
           for c in range(cols):
               lowest=self._data[r,c]
               lowloc=None
               for i in range(8):
                   rr=r+it[i,0]
                   cc=c+it[i,1]
                   if (rr>-1 and rr<rows and cc>-1 and cc<cols):
                       if (self._data[rr,cc]<lowest):
                           lowest=self._data[rr,cc]
                           lowloc=i
                      
               if (lowloc!=None):
                   rr=r+it[lowloc,0]
                   cc=c+it[lowloc,1]
                   self._nodearray[r,c].setDownnode(self._nodearray[rr,cc])
                   self._nodearray[r,c].setPitFlag(False)
               else:
                   self._nodearray[r,c].setPitFlag(True)
            
    def setUpCells(self):
        it=self._getIterator()
        rows=self.getRows()
        cols=self.getCols()
        
        for r in range(self.getRows()):
            for c in range(self.getCols()):
                for i in range(8):
                    rr=r+it[i,0]
                    cc=c+it[i,1]
                    if (rr>-1 and rr<rows and cc>-1 and cc<cols):
                        if (self._nodearray[rr,cc].getDownnode()==self._nodearray[r,c]):
                            self._nodearray[r,c].setUpnode(self._nodearray[rr,cc])
    
    def getPits(self):
        pits=[]
        print self._nodearray.shape
        for r in range(self.getRows()):
            for c in range(self.getCols()):
                if self._nodearray[r,c].getPitFlag():
                    pits.append(self._nodearray[r,c])
        return pits
                            