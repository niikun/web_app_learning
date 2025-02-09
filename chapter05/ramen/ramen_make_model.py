import os
from PIL import Image
from keras.models import Sequential
from keras.layers import Conv2D,MaxPooling2D,Flatten,Dense,Dropout
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import numpy as np


labels = ["salt","soya_source","spicy","miso","chilled"]
base_dir = "./data"
img_w,img_h = 32,32

images = []
labels_num = []

for no,label in enumerate(labels):
    label_dir = os.path.join(base_dir,label)
    for filename in os.listdir(label_dir):
        if not filename.endswith(".jpg"):
            continue
        img_path = os.path.join(label_dir,filename)
        print("load_image",img_path)
        img = Image.open(img_path)
        img = img.resize((img_w,img_h))
        for angle in range(0,360,45):
            img_rot = img.rotate(angle)
            img_rot = img_rot.resize((img_w,img_h))
            images.append(np.array(img_rot)/255.0)
            labels_num.append(labels.index(label))

X = np.array(images)
y = to_categorical(np.array(labels_num))

print("X.shape",X.shape)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.1)

model = Sequential([
    Conv2D(32,(3,3),activation="relu",input_shape=(img_w,img_h,3)),
    MaxPooling2D(pool_size=(2,2)),
    Conv2D(64,(3,3),activation="relu"),
    MaxPooling2D(pool_size=(2,2)),
    Conv2D(128,(3,3),activation="relu"),
    MaxPooling2D(pool_size=(2,2)),
    Flatten(),
    Dense(512,activation="relu"),
    Dropout(0.5),
    Dense(len(labels),activation="softmax")
])

model.compile(
    loss="categorical_crossentropy",
    optimizer="adam",
    metrics=["accuracy"]
)

model.fit(X_train,y_train,epochs=27,batch_size=128,validation_split=0.2)
score = model.evaluate(X_test,y_test)
print("score",score[1])

model.save("data/ramen.keras")
