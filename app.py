from flask import Flask , request, jsonify
from models.nutrition import get_food_recommendations

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message":"Welcome to Personalized Health & Fitness AI"})

@app.route("/profile",methods=["POST"])
def create_profile():
    data = request.json
    return jsonify({"message":"Profile created Successfully!","data":data})

@app.route("/recommendations", methods=["POST"])
def recommend():
     data = request.json
     calories = data.get("calories",2000)
     preferences = data.get("preferences",["Vegetarian"])
     recommendations = get_food_recommendations(calories, preferences)
     return jsonify({"recommendations": recommendations})

if __name__ == "__main__":
    app.run(debug=True)