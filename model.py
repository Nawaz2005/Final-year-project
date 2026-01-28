from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Input, Concatenate
from tensorflow.keras.models import Model

def build_multimodal_model(tab_shape):
    base_model = MobileNetV2(weights="imagenet", include_top=False, input_shape=(224,224,3))
    base_model.trainable = False

    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(128, activation="relu")(x)

    image_model = Model(inputs=base_model.input, outputs=x)

    tab_input = Input(shape=(tab_shape,))
    t = Dense(64, activation="relu")(tab_input)
    t = Dense(32, activation="relu")(t)

    combined = Concatenate()([image_model.output, t])
    z = Dense(64, activation="relu")(combined)
    z = Dense(1, activation="linear")(z)

    final_model = Model(inputs=[image_model.input, tab_input], outputs=z)

    final_model.compile(optimizer="adam", loss="mse", metrics=["mae"])
    return final_model
