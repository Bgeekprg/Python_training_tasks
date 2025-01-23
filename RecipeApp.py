def menu():
    print("1: Add Recipe")
    print("2: Update Recipe")
    print("3: Delete Recipe")
    print("4: View Recipes")
    print("5: Exit")

# Add function for adding recipe in list
def Add(recipe, id):
    name = input("Enter name of Recipe =")
    if name == "":
        print("You must have to enter value for name!")
        return False
    Type = input("Enter Recipe Type =")
    if Type == "":
        print("You must have to enter value for type!")
        return False
    description = input("Enter description =")
    if description == "":
        print("You must have to enter value for description!")
        return False

    newRecipe = {"id": id, "Name": name, "Type": Type, "Description": description}
    recipe.append(newRecipe)
    return True  

# Update the Recipe by its Id
def Update(recipe, uid):
    
    indx = None
    for i in range(len(recipe)):
        if recipe[i]["id"] == uid:
            indx = i
            break

    if indx is not None:
        name = input("Enter name of Recipe =")
        if name == "":
            print("You must have to enter value for name!")
            return
        Type = input("Enter Recipe Type =")
        if Type == "":
            print("You must have to enter value for type!")
            return
        description = input("Enter description =")
        if description == "":
            print("You must have to enter value for description!")
            return

        # Update the recipe details
        recipe[indx]["Name"] = name
        recipe[indx]["Type"] = Type
        recipe[indx]["Description"] = description
        print("Recipe is Updated!")
    else:
        print("Recipe not found with the given id!")

# Delete the recipe by its Id
def Delete(recipe, id):
    for i in range(len(recipe)):
        if recipe[i]["id"] == id:
            recipe.pop(i)
            print("Recipe is deleted!")
            return  
    print("Recipe not found with the given id!")

# Display the recipes
def View(recipe):
    if len(recipe) == 0:
        print("No recipes to display!")
    else:
        for i in recipe:
            print(f"ID: {i['id']}")
            print(f"Name: {i['Name']}")
            print(f"Type: {i['Type']}")
            print(f"Description: {i['Description']}")
            print("-" * 40)

recipe = []
choice = None
id = 1
while True:
    try:
        menu()
        choice = int(input("Enter your choice ="))

        if choice == 1:
            if Add(recipe, id):
                id += 1  # Increment the id after successful addition

        elif choice == 2:
            if len(recipe) > 0:
                uid = int(input("Enter id =>"))
                Update(recipe, uid)
            else:
                print("Recipe Book is empty!")

        elif choice == 3:
            if len(recipe) > 0:
                uid = int(input("Enter id =>"))
                Delete(recipe, uid)
            else:
                print("Recipe Book is empty!")

        elif choice == 4:
            View(recipe)

        elif choice == 5:
            exit(0)

        else:
            print("Enter a valid choice!")

        input("Please press Enter to continue\n")

    except ValueError:
        print("Please enter an integer value for choice")
        input("Please press Enter to continue\n")
        continue
