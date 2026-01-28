import pandas as pd
import os
import cv2
import numpy as np

IMG_SIZE = 224

def load_dataset(csv_path="images/post_surgical_healing_dataset_500.csv"):
    print("Loading dataset...")

    df = pd.read_csv(csv_path)

    print("Total samples:", len(df))

    # Check missing images
    missing = 0
    for img in df["Image_File"]:
        img_name = img + ".png"
        path = os.path.join("images", img_name)
        if not os.path.exists(path):
            missing += 1

    print("Missing images:", missing)

    # Load images
    image_data = []
    for img in df["Image_File"]:
        img_name = img + ".png"
        path = os.path.join("images", img_name)

        img_arr = cv2.imread(path)
        img_arr = cv2.resize(img_arr, (IMG_SIZE, IMG_SIZE))
        img_arr = img_arr / 255.0
        image_data.append(img_arr)

    X_images = np.array(image_data)
    print("Loaded images shape:", X_images.shape)

    return df, X_images
