import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split   # ✅ make sure this is here
import pickle
import os
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "electricity_data.csv")

data = pd.read_csv(DATA_PATH)

data["season"] = data["season"].map({
    "winter": 0,
    "monsoon": 1,
    "summer": 2
})

X = data[["units", "season", "appliances", "family_members"]]
y = data["bill"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

MODEL_PATH = os.path.join(BASE_DIR, "electricity_model.pkl")
with open(MODEL_PATH, "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved successfully")
