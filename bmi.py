print( ''' 
 ____  __  __ _____    _____          _      _____ _    _ _            _______ ____  _____  
 |  _ \|  \/  |_   _|  / ____|   /\   | |    / ____| |  | | |        /\|__   __/ __ \|  __ \ 
 | |_) | \  / | | |   | |       /  \  | |   | |    | |  | | |       /  \  | | | |  | | |__) |
 |  _ <| |\/| | | |   | |      / /\ \ | |   | |    | |  | | |      / /\ \ | | | |  | |  _  / 
 | |_) | |  | |_| |_  | |____ / ____ \| |___| |____| |__| | |____ / ____ \| | | |__| | | \ \ 
 |____/|_|  |_|_____|  \_____/_/    \_\______\_____|\____/|______/_/    \_\_|  \____/|_|  \_\
                                                                                                                                                                                       ''')
print("Welcome to the BMI calculator")
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = round(weight / height ** 2)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f" Your BMI is {bmi}, you have a normal weight.")

elif bmi < 30:
    print(f" Your BMI is {bmi}, you are overweight.")
    
elif bmi < 35:
    print(f" Your BMI is {bmi}, you are obese")
    
else:
    print(f" your BMI is {bmi} , you are clinically obese")
    