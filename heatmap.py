import xml.etree.ElementTree as ET
import urllib.request
import numpy as np
import gmaps

gmaps.configure(api_key="AI.." #your API key

restaurants = []

with urllib.request.urlopen('http://www.visithelsinki.fi/misc/feeds/helsinki_tourism_poi.xml') as url:
    data = url.read().decode('utf-8')
    
    root = ET.fromstring(data)
    
    i = 8

    while (i < 1684):
        type1 = str(root[0][i][6].text)
        
        if (type1 == 'RAVINTOLA'):
            try:
                
                latitude = float(root[0][i][40].text)
                longitude = float(root[0][i][39].text)
            
                coordinates = []
                coordinates.append(latitude)
                coordinates.append(longitude)
            
                restaurants.append(coordinates)
            except TypeError:
                pass
        i += 1
    restaurants = np.array(restaurants)
    
fig = gmaps.figure()
heatmap_layer = gmaps.heatmap_layer(restaurants)
heatmap_layer.max_intensity = 1
heatmap_layer.point_radius = 6
fig.add_layer(heatmap_layer)
fig
