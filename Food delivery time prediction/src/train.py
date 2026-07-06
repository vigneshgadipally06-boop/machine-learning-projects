import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from preprocessing import preprocess

df = pd.read_csv("data/Food_Delivery_Times.csv")

df = preprocess(df)

X = df.drop("Delivery_Time_min", axis=1)
y = df["Delivery_Time_min"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

joblib.dump(model, "models/model.pkl")

print("Model Saved Successfully")