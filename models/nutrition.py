import pandas as pd

def get_food_recommendations(calories, preferences):
    # Static food data
    food_data = pd.DataFrame({
        "Food": ["Salad", "Grilled Chicken", "Smoothie", "Pasta"],
        "Calories": [200, 400, 300, 600],
        "Type": ["Vegetarian", "Non-Vegetarian", "Vegan", "Vegetarian"]
    })

    # Filter by preferences
    filtered_food = food_data[food_data["Type"].isin(preferences)]
    recommendations = filtered_food[filtered_food["Calories"] <= calories]
    return recommendations.to_dict(orient="records") if not recommendations.empty else []
