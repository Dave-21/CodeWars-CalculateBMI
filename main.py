def bmi(weight, height):
    bmiVal = weight/(height**2)
    if bmiVal <= 30:
        if bmiVal <= 18.5:
            return "Underweight"
        elif bmiVal <= 25:
            return "Normal"
        return "Overweight"
    elif bmiVal > 30:
        return "Obese"

print(bmi(50, 1.80))