from data_loader import load_dataset
from preprocess import preprocess_tabular
from model import build_multimodal_model

df, X_images = load_dataset()
X_tab, y = preprocess_tabular(df)

model = build_multimodal_model(X_tab.shape[1])
model.summary()

model.fit(
    [X_images, X_tab],
    y,
    epochs=15,
    batch_size=8,
    validation_split=0.2
)

model.save("healing_model.h5")
print("Model saved")
