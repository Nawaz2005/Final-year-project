import cv2
import numpy as np
from tensorflow.keras.models import load_model
from recommendations import get_recommendation

# -------- LOAD MODEL --------
model = load_model("healing_model.h5", compile=False)

# -------- USER INPUT --------
image_path = "images/img_P0001.png"   # change this to test other images

age = 45
bmi = 26.5
smoker = 0
hba1c = 7.2
surgery_type = "Abdominal"

# ----- NORMALIZE INPUTS (same as training) -----
age_n = age / 100
bmi_n = bmi / 50
hba1c_n = hba1c / 15


# -------- PREPROCESS IMAGE --------
img = cv2.imread(image_path)
img = cv2.resize(img, (224,224))
img = img / 255.0
img = np.expand_dims(img, axis=0)

# -------- PREPROCESS TABULAR --------
surgery_map = {"Abdominal":0, "Cardiac":1, "General":2, "Neuro":3, "Orthopedic":4}
tab = np.array([[age_n, bmi_n, smoker, hba1c_n, surgery_map[surgery_type]]])


# -------- PREDICTION --------
pred = model.predict([img, tab])
days = round(pred[0][0], 2)

print("Predicted Healing Days:", days)

# -------- RECOMMENDATION --------
advice = get_recommendation(days, smoker, hba1c)

print("\nWound Care Recommendations:")
for a in advice:
    print("-", a)
