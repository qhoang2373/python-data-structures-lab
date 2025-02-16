# Exercise 1: List and Indexing
#
# Create a list named students containing at least three student names (strings).
# Assign the second student’s name to a variable named first_student.
# Assign the last student’s name to a variable named last_student.

def manage_students():
    # your code here
    students =  ["Kyle", "Kevin", "Kyrie"]

    ## this code will assign the Kevin's name to a variable named first_student
    first_student = students[1]

    ## this code will assign the Kyrie name to a variable named last_student
    last_student = students[-1]
    
    ## the result of the tuple
    return first_student, last_student

# Call the function and print the result
print('Exercise 1:', manage_students())
