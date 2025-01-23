# BMI Calculator : 
# - You need to make finding out your BMI quicker and easier, by creating a program that takes a person's weight , height and name as input and outputs the corresponding BMI category.

# The resulting number indicates one of the following categories:
# Underweight = less than 18.5
# Normal = more or equal to 18.5 and less than 25
# Overweight = more or equal to 25 and less than 30
# Obesity = 30 or more

def calculateBMI(weight,height):
    bmi = weight/height**2

    #checks and return the BMI category as per result
    if bmi < 18.5:
        return f" {round(bmi,2)}(Underweight)"
    elif bmi >=18.5 and bmi<25:
        return f" {round(bmi,2)}(Normal)"
    elif bmi >=25 and bmi<30:
        return f" {round(bmi,2)}(Overweight)"
    else:
        return f" {round(bmi,2)}(Obesity)"


print("----------BMI Calculator----------")
#get the input of name,weight and height
name = input("Enter Name =")
try:
    weight = float(input("Enter ur Weight(Kg) ="))
    if weight<=0:
        raise Exception("Weight can not be zero or minus")
    height = float(input("Enter your Height(meter) ="))
    if height<=0:
        raise Exception("Height can not be zero or minus")

    print("-----------------------------------------")
    print(f"{name} your BMI is = {calculateBMI(weight,height)}")
except ValueError:
    print("Please enter only Decimal values !")
except Exception as e:
    print(e)


