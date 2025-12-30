from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "electricity_model.pkl")

model = pickle.load(open(MODEL_PATH, "rb"))

@app.route("/", methods=["GET", "POST"])
def home():
    bill = None
    suggestions = []

    if request.method == "POST":
        units = int(request.form["units"])
        season = int(request.form["season"])
        appliances = int(request.form["appliances"])
        family = int(request.form["family"])
        ac_hours = int(request.form["ac_hours"])
        fridge_hours = int(request.form["fridge_hours"])
        heavy_hours = int(request.form["heavy_hours"])

        # Predict bill
        bill = int(model.predict([[units, season, appliances, family]])[0])

        # Generate suggestions
        if units > 300:
            suggestions.append("Very high consumption: Reduce AC & heavy appliance usage.")
        elif units > 200:
            suggestions.append("Moderate-high usage: Use energy-efficient appliances.")
        else:
            suggestions.append("Good usage: Maintain current energy habits.")

        if season == 2:  # summer
            suggestions.append("Tip: Use AC at 24–26°C to save electricity.")
        if ac_hours > 5:
            suggestions.append("Reduce AC usage hours per day to save electricity.")
        if fridge_hours > 24:
            suggestions.append("Check fridge settings; optimize fridge usage.")
        if heavy_hours > 2:
            suggestions.append("Limit heavy appliances usage per day.")

    return render_template("index.html", bill=bill, suggestions=suggestions)

if __name__ == "__main__":
    app.run(debug=True)
