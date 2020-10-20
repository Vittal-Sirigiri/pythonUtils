import sys
import numpy as np
import math
import folium
import pandas as pd

def get_dist_mat(taskLats, taskLngs, vehLats, vehLngs):
  
    # index 0 of tuple has lat
    # index 1 of tuple has lng
    sLats = np.array([[taskLats[k]  for k in range(len(taskLats))] for l in range(len(vehLats))])
    sLngs = np.array([[taskLngs[k]  for k in range(len(taskLats))] for l in range(len(vehLats))])

    dLats = np.array([[vehLats[l]  for k in range(len(taskLats))] for l in range(len(vehLats))])
    dLngs = np.array([[vehLngs[l]  for k in range(len(taskLats))] for l in range(len(vehLats))])

    R = 6373.0

    s_lat = sLats*np.pi/180.0                      
    s_lng = np.deg2rad(sLngs)     
    e_lat = np.deg2rad(dLats)                       
    e_lng = np.deg2rad(dLngs)  

    d = np.sin((e_lat - s_lat)/2)**2 + np.cos(s_lat)*np.cos(e_lat) * np.sin((e_lng - s_lng)/2)**2

    return 2 *1000 * R * np.arcsin(np.sqrt(d))

def drawFoliumMap(inputShapefile, mapName, tooltipName):
    for ix in inputShapefile.index:
        if inputShapefile.loc[ix,'geometry'].type == 'Polygon':
            folium.Polygon([coord[::-1] for coord in inputShapefile.loc[ix,'geometry'].exterior.coords], tooltip=inputShapefile.loc[ix,tooltipName]).add_to(mapName)
        else:
            for mpGeom in inputShapefile.loc[ix,'geometry']:
                folium.Polygon([coord[::-1] for coord in mpGeom.exterior.coords], tooltip=inputShapefile.loc[ix,tooltipName]).add_to(mapName)

def splitLatLngFromText(inputString):
    lat = np.float(inputString.split(',')[0][1:])
    lng = np.float(inputString.split(',')[1][:-2])
    return(lat, lng)