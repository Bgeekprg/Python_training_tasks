def weight_converter():
    print("Weight Converter")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    print("3. Kilograms to Ounces")
    print("4. Ounces to Kilograms")
    print("5. Pounds to Ounces")
    print("6. Ounces to Pounds")
    
    try:

        choice = int(input("Choose the conversion option (1-6): "))

        if choice==1:
            kg=float(input("Enter kilogram = "))
            return f"{kg} Kg = {kg*2.20462} pounds"

        elif choice==2:
            pound=float(input("Enter Pound = "))
            return f"{pound} pound = {pound/2.20462} kg"

        elif choice==3:
            kg=float(input("Enter kilogram = "))
            return f"{kg} Kg = {kg*35.274} ounce"

        elif choice==4:
            ounce=float(input("Enter Ounce = "))
            return f"{ounce} ounce = {ounce/35.274} kg"
        
        elif choice==5:
            pound=float(input("Enter Pound = "))
            return f"{pound} pound = {pound*16} ounce"
        
        elif choice==6:
            ounce=float(input("Enter Ounce = "))
            return f"{ounce} ounce = {ounce/16} pounds"
        
        else:
            return "Enter valid choice !"

    except:
        print("Enter Integer choice only")
        exit(0)

print(weight_converter())
