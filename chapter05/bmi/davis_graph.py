import pandas as pd
import matplotlib.pyplot as plt
import matplotlib_fontja

df = pd.read_csv("davis_bmi.csv")
normal = df[df["label"]=="normal"]
fat = df[df["label"]=="fat"]
thin = df[df["label"]=="thin"]

plt.scatter(normal["height"], normal["weight"], c="blue", label="normal",marker="o")
plt.scatter(fat["height"], fat["weight"], c="red", label="fat",marker="x")  
plt.scatter(thin["height"], thin["weight"], c="green", label="thin",marker="v")

plt.xlabel("身長")
plt.ylabel("体重")
plt.title("DavisデータのBMI分布")
plt.legend()
plt.savefig("davis_bmi.png")
plt.show()