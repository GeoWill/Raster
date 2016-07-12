# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 14:21:56 2016

@author: user
"""
import numpy as np

class Raster(object):
    
    '''A class to represent 2-D Rasters'''

# Basic constuctor method
    def __init__(self,data,xorg,yorg,cellsize,nodata=-999.999):
        self._data=np.array(data)
        self._orgs=(xorg,yorg)
        self._cellsize=cellsize
        self._nodata=nodata
        
    def getData(self):
        return self._data
        
#return the shape of the data array      
    def getShape(self):
        return self._data.shape    
#return number of rows    
    def getRows(self):
        return self._data.shape[0]
#return number of columns        
    def getCols(self):
        return self._data.shape[1]
        
    def getOrgs(self):
        return self._orgs
        
    def getCellsize(self):
        return self._cellsize
    
    def getNoData(self):
        return self._nodata
    
    def slope(self):
        """Calculates local slope of each cell from x and y slopes.
        Returns raster of slope values. 
        For a raster of size (i,j) returned raster 
        will be of size((i-2),(j-2))"""
        rows = self.getRows() #set variables
        cols = self.getCols()
        cellSize = self.getCellsize()
        data = self.getData()
        #create empty list to make new raster from
        slopeData = []
        #iterate through raster
        #calculation needs 'r-1' and 'r+1' therefore start one step in and
        #finish one step from end.
        for r in range(1,rows-1):
            #create an empty list for each row            
            rowData=[] 
            for c in range(1,cols-1):
                #calculate slopes
                xSlope = (data[r+1,c]-data[r-1,c])/(2*cellSize)
                ySlope = (data[r,c+1]-data[r,c-1])/(2*cellSize)
                slope = np.sqrt((xSlope*xSlope)+(ySlope*ySlope))
                rowData.append(slope) #append clope values to list             
            slopeData.append(rowData) #append row list to array list
        #create a new raster containing slope data
        #lower left origin should be one cell in on x and y direction
        slopeRaster=Raster(slopeData, self.getOrgs()[0]+cellSize, 
                           self.getOrgs()[1]+cellSize, cellSize, 
                            self.getNoData())           
        return slopeRaster  #return new raster.
        