# Prompt for input
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

# Validate input before proceeding
if weight <= 0 or height <= 0:
    print("Weight and height must be positive numbers.")
else:
    # Calculate BMI
    bmi = round(weight / (height ** 2), 2)

    # Determine category
    def bmi_category(bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    category = bmi_category(bmi)

    # Display result
    print(f"\nYour BMI is: {bmi}")
    print(f"You are classified as: {category}")
