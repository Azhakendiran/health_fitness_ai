import unittest
from models.nutrition import get_food_recommendations

class TestNutrition(unittest.TestCase):
    def test_recommendations(self):
        result = get_food_recommendations(300, ["Vegetarian", "Vegan"])
        self.assertTrue(len(result) > 0)
        self.assertTrue(all(r["Calories"] <= 300 for r in result))

if __name__ == "__main__":
    unittest.main()
