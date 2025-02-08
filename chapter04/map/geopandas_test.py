import geopandas as gpd
import matplotlib.pyplot as plt

GEOJSON_FILE = "N03-20240101.geojson"

map = gpd.read_file(GEOJSON_FILE,encoding="utf-8")
map.plot(edgecolor="gray",facecolor="none")
plt.axis("off")
plt.savefig("map.png")
plt.show()