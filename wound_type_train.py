from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model

IMG = 224
BATCH = 8

gen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train = gen.flow_from_directory(
    "wound_images",
    target_size=(IMG, IMG),
    batch_size=BATCH,
    class_mode="categorical",
    subset="training"
)

val = gen.flow_from_directory(
    "wound_images",
    target_size=(IMG, IMG),
    batch_size=BATCH,
    class_mode="categorical",
    subset="validation"
)

base = MobileNetV2(weights="imagenet", include_top=False, input_shape=(224,224,3))
base.trainable = False

x = GlobalAveragePooling2D()(base.output)
x = Dense(64, activation="relu")(x)
out = Dense(3, activation="softmax")(x)

model = Model(base.input, out)
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

model.fit(train, validation_data=val, epochs=10)
model.save("wound_type_model.h5")

print("✅ Wound type model saved")
