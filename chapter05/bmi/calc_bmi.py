import pandas as pd

df = pd.read_csv("Davis.csv",index_col=False)

df = df[['height','weight']]

df = df[df["weight"] < 140]

df["bmi"] = df["weight"] / (df["height"] / 100) ** 2

df["label"] = pd.cut(
    df["bmi"],
    bins=[0, 18.5, 25, float("inf")],
    labels=["thin", "normal", "fat"]
)

df.to_csv("davis_bmi.csv",index=False)