weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

bmi = weight / height**2


if bmi < 27:
    print(" You are below the normal range.")
elif bmi < 31:
    print(" You are within the normal range.")
elif bmi < 54:
    print(" You are above the normal range.")
else:
    print(" You are obese.") 
