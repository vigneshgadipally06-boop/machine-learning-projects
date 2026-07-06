import joblib
import pandas as pd

model = joblib.load("models/model.pkl")

sample = pd.read_csv("data/Food_Delivery_Times.csv")

sample = pd.get_dummies(sample, drop_first=True)
sample = sample.fillna(sample.mean(numeric_only=True))

sample = sample.drop("Delivery_Time_min", axis=1)

prediction = model.predict(sample.iloc[:1])

print("Predicted Delivery Time:", prediction[0])