import geopandas as gpd
import matplotlib.pyplot as plt

GEOJSON_FILE = "N03-20240101.geojson"
map = gpd.read_file(GEOJSON_FILE,encoding="utf-8")
osaka = map[map["N03_001"]=="大阪府"]
print(osaka)

osaka.plot(edgecolor="gray",facecolor="yellow")
plt.axis("off")

plt.show()