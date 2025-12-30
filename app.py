import pickle
from bill_calculator import calculate_bill

# Load trained model
with open("electricity_model.pkl", "rb") as f:
    model = pickle.load(f)

print("SMART ELECTRICITY BILL PREDICTOR (INDIA)")
print("--------------------------------------")

units = int(input("Enter units consumed: "))
season = input("Season (winter/monsoon/summer): ").lower()
appliances = int(input("Number of appliances: "))
family = int(input("Number of family members: "))

season_map = {"winter": 0, "monsoon": 1, "summer": 2}
season_value = season_map[season]

# ML Prediction
predicted_bill = model.predict([[units, season_value, appliances, family]])

# Slab Bill
actual_bill = calculate_bill(units)

print("\n----- RESULTS -----")
print(f"Predicted Bill (ML): ₹{int(predicted_bill[0])}")
print(f"Actual Slab Bill: ₹{actual_bill}")

if predicted_bill[0] > actual_bill:
    print("⚠️ High usage detected. Try reducing appliance usage.")
else:
    print("✅ Usage is within efficient range.")
