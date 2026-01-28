from tensorflow.keras.models import load_model
from data_loader import load_dataset
from preprocess import preprocess_tabular

model = load_model("healing_model.h5", compile=False)

df, X_images = load_dataset()
X_tab, y = preprocess_tabular(df)

pred = model.predict([X_images, X_tab])

print("\nSample Predictions:\n")
for i in range(10):
    print(f"Patient {i+1} | Actual: {round(y[i],2)} days | Predicted: {round(pred[i][0],2)} days")

