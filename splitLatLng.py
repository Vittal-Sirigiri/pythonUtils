import numpy as np
# if a latlng tuple got converted to text, this wiil
# return a tuple of floats for processing

def splitLatLng(inputString):
	lat = np.float(inputString.split(',')[0][1:])
	lng = np.float(inputString.split(',')[1][:-2])
	return(lat, lng)