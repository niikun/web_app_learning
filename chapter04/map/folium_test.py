import folium

m  = folium.Map(location=[37.5665, 126.9780], zoom_start=5)
m.save("map.html")