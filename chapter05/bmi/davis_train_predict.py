import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv("davis_bmi.csv")
print("---元のCSVデータ---")
print(df[0:3])
values = df[["height","weight"]].values
label = df["label"].values
train_data, test_data, train_label, test_label = train_test_split(values, label,test_size=0.1)
print("---学習用データ---")
print(train_data[0:3])
print("---テスト用データ---")
print(test_data[0:3])
clf = RandomForestClassifier()
clf.fit(train_data, train_label)
print("---予測結果---")
predict = clf.predict(test_data)
print("正解データ=", test_label[0:3])
print("予測データ=", predict[0:3])

print("---正解率---")
print(accuracy_score(test_label, predict))
