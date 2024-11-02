
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    elif 30 <= bmi < 34.9:
        return "Obesity (Class 1)"
    elif 35 <= bmi < 39.9:
        return "Obesity (Class 2)"
    else:
        return "Obesity (Class 3)"

def main():
    print("Welcome to the BMI Calculator!")
    
    # Get user input
    weight = float(input("Please enter your weight in kilograms: "))
    height = float(input("Please enter your height in meters: "))
    
    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    
    # Display the result
    print(f"Your BMI is: {bmi:.2f}")
    
    # Determine and display BMI category
    category = get_bmi_category(bmi)
    print(f"You are classified as: {category}")

if __name__ == "__main__":
    main()

