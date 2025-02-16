# Exercise 1: List and Indexing
#
# Create a list named students containing at least three student names (strings).
# Assign the second student’s name to a variable named first_student.
# Assign the last student’s name to a variable named last_student.

def manage_students():
    ## creates a list of students, named kyle kevin and kyrie, assigns the 2nd and last student's names
    ## to variables, and returns a message 

    students =  ["Kyle", "Kevin", "Kyrie"]

    ## this code will assign the Kevin's name to a variable named first_student
    first_student = students[1]

    ## this code will assign the Kyrie name to a variable named last_student
    last_student = students[-1]
    
    ## the result of the tuple
    return first_student, last_student


# Call the function and print the result
print('Exercise 1:', manage_students())

# Exercise 2: Loop and String Concatenation
#
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Create a variable named meal and assign an empty string to it.
# Use a for loop to iterate over the strings in foods and append each string to meal.

def combine_foods():
    
    foods = ("pizza", "taco", "hotdogs") ##tuple for foods
    meal = ""

    for food in foods:
        meal += food + " "

    return meal.strip()


# Call the function and print the result
print('Exercise 2:', combine_foods())

# Exercise 3: Slicing Tuples
#
# Using the slice operator, assign a new tuple containing only the last two food strings in the foods to a variable named last_two_foods.

def slice_foods():
    

    foods = ("candy", "Icecream", "pizza", "taco", "hotdogs")
    last_two_foods = foods[-2:]
    
    return last_two_foods



# Call the function and print the result
print('Exercise 3:', slice_foods())
