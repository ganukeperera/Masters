from google import genai

class BMICalculator:
    def __init__(self, weight_kg: float, height_m: float):
        self.weight_kg = weight_kg
        self.height_m = height_m

    @property
    def bmi(self) -> float:
        return self.weight_kg / (self.height_m ** 2)

    @property
    def category(self) -> str:
        bmi = self.bmi
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25.0:
            return "Normal weight"
        elif bmi < 30.0:
            return "Overweight"
        else:
            return "Obese"

    def display(self):
        print(f"\nYour BMI: {self.bmi:.2f}")
        print(f"Category: {self.category}")

class Recommendation:
    API_KEY = "AIzaSyAvwGIK6Q13swT18NRZfkTdnXDXb4DEneM"

    def get_recommendation(self, bmi: float, age: int, gender: str):
        client = genai.Client(api_key=self.API_KEY)

        system_prompt = (
            "You are a friendly and knowledgeable health advisor at a wellness clinic in Auckland, New Zealand. "
            "Give advice that is practical, encouraging, and tailored to the person's specific profile. "
            "Always prioritise safety and recommend consulting a doctor for medical concerns."
        )
        
        user_prompt = (
            f"I am a {age}-year-old {gender} with a BMI of {bmi}. "
            f"Create a personalised one-week diet and exercise plan for me. "
            f"Structure your response as follows:\n\n"
            f"1. **Overview** - A brief summary of the approach based on my BMI category.\n"
            f"2. **Weekly Diet Plan** - A 7-day meal plan (breakfast, lunch, dinner, snacks) "
            f"that repeats across the week with small variations.\n"
            f"3. **Weekly Exercise Plan** - A 7-day workout schedule with exercise names, "
            f"duration, and intensity suited to my profile.\n"
            f"4. **Weekly Progression** - How to adjust diet and exercise intensity across "
            f"weeks 1 to 4.\n"
            f"5. **Key Tips** - 3 to 5 specific tips tailored to my age, gender, and BMI.\n\n"
            f"Keep advice practical, safe, and realistic for a beginner."
        )
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=user_prompt,
            config=genai.types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0.7,       # balanced creativity (0.0 - 1.0)
                top_p=0.9,             # consider top 90% likely words
                top_k=40,              # limit to 40 probable next words
                max_output_tokens=1500, # maximum response length
                stop_sequences=["---END---"],  # model stops if it outputs this token
            ),
        )
        print(response.text)

class BMIApp:

    def run(self):
        print("=== BMI Calculator ===")
        age = int(input("Enter your age (years): "))
        gender = str(input("Enter your gender (male/female): "))
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (m): "))

        calc = BMICalculator(weight, height)
        Recommendation().get_recommendation(calc, age, gender)

if __name__ == "__main__":
    BMIApp().run()