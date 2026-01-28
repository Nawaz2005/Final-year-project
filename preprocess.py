from sklearn.preprocessing import LabelEncoder, MinMaxScaler

def preprocess_tabular(df):
    le = LabelEncoder()
    df["Surgical_Type"] = le.fit_transform(df["Surgical_Type"])

    scaler = MinMaxScaler()
    num_cols = ["Age", "BMI", "HbA1c"]
    df[num_cols] = scaler.fit_transform(df[num_cols])

    X_tab = df[["Age","BMI","Smoker","HbA1c","Surgical_Type"]].values
    y = df["Days_to_Heal"].values

    return X_tab, y
