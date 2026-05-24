


import pandas as pd
import numpy as np
import tensorflow as tf

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error

from tensorflow.keras.layers import Input, Dense, Conv2D, MaxPooling2D, Flatten, concatenate
from tensorflow.keras.models import Model


IMG_SIZE = 64
EPOCHS = 20
BATCH_SIZE = 2

# ---------------- LOAD CSV ----------------
df = pd.read_csv("csvdata.csv", index_col=0)
df = df.head(200)

print("Dataset size:", df.shape)

# ---------------- ENCODING ----------------
df = pd.get_dummies(df, columns=["City", "Location"], drop_first=True)

# ---------------- FEATURES ----------------
features = [col for col in df.columns if col != "Price"]
X_tab = df[features]

scaler = StandardScaler()
X_tab = scaler.fit_transform(X_tab)

price_scaler = StandardScaler()
y_scaled = price_scaler.fit_transform(df[["Price"]])

# ---------------- LOAD IMAGES ----------------
def load_image(img_id):
    path = f"images/{img_id}.jpg"
    img = tf.keras.preprocessing.image.load_img(
        path,
        target_size=(IMG_SIZE, IMG_SIZE)
    )
    img = tf.keras.preprocessing.image.img_to_array(img) / 255.0
    return img

images = np.array([load_image(i) for i in range(1, len(df) + 1)])

print("Images loaded:", images.shape)

# ---------------- SPLIT ----------------
X_tab_train, X_tab_test, X_img_train, X_img_test, y_train, y_test = train_test_split(
    X_tab,
    images,
    y_scaled,
    test_size=0.2,
    random_state=42
)

# ---------------- IMAGE MODEL (UPDATED CNN) ----------------
image_input = Input(shape=(IMG_SIZE, IMG_SIZE, 3))

x = Conv2D(16, (3,3), activation='relu')(image_input)
x = MaxPooling2D()(x)

x = Conv2D(32, (3,3), activation='relu')(x)
x = MaxPooling2D()(x)

x = Flatten()(x)
x = Dense(32, activation='relu')(x)


# ---------------- TABULAR MODEL ----------------
tabular_input = Input(shape=(len(features),))

t = Dense(16, activation='relu')(tabular_input)


# ---------------- COMBINE ----------------
combined = concatenate([x, t])

z = Dense(16, activation='relu')(combined)


output = Dense(1)(z)

# ---------------- MODEL ----------------
model = Model(inputs=[image_input, tabular_input], outputs=output)

model.compile(optimizer='adam', loss='mse', metrics=['mae'])

model.summary()

# ---------------- TRAIN (UPDATED EPOCHS) ----------------
model.fit(
    [X_img_train, X_tab_train],
    y_train,
    epochs=EPOCHS,
    batch_size=BATCH_SIZE
)

# ---------------- PREDICT ----------------
preds = model.predict([X_img_test, X_tab_test])

preds = price_scaler.inverse_transform(preds)
y_test_real = price_scaler.inverse_transform(y_test)

# ---------------- RESULTS ----------------
mae = mean_absolute_error(y_test_real, preds)
rmse = np.sqrt(mean_squared_error(y_test_real, preds))

print("\nFINAL METRICS")
print("MAE:", mae)
print("RMSE:", rmse)

print("\nACTUAL vs PREDICTED:")

for i in range(len(y_test_real)):
    actual = int(y_test_real[i][0])
    predicted = int(round(preds[i][0]))
    print(f"Actual: {actual:,} | Predicted: {predicted:,}")



