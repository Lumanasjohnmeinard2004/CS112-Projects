# Welcome message
print("Welcome to the BMI Checker!")

# Get user input for weight (in kilograms) and height (in meters)
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI using the formula: BMI = weight (kg) / (height (m) ^ 2)
bmi = weight / (height ** 2)

# Determine the BMI category based on WHO guidelines
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal Weight"
elif 25.0 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obese"

# Display the calculated BMI and category
print(f"Your BMI is: {bmi:.2f}")
print(f"You are categorized as: {category}")

