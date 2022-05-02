# Define a variable and assigned it a value of 10
types_of_people = 10

# Insert the variable into a new string which we assign to the variable x
x = f"There are {types_of_people} types of people."

# Defined a variable with the string "binary"
binary = "binary"
# Define a variable with the string "don't"
do_not = "don't"

# Embed those two string variables into a new string and assign it to y
y = f"Those who know {binary} and those who {do_not}."

# Print the value of variable x and y
print(x)
print(y)

# Print a string with the value for variable x and y using f-string
print(f"I said: {x}")
print(f"I also said: '{y}'")

# Assign a boolean value to variable
hilarious = False
# Define a new string variable with a placeholder
joke_evaluation = "Isn't that joke so funny?! {}"

# Print out the value of the joke_evaluation variable, using format() and
# passing the hilarious variable into it.
print(joke_evaluation.format(hilarious))

# Assign a new variable w and e and assign a string in each
w = "This is the left side of..."
e = "a string with a right side."

# Print out a new string by concatenating the variables w and e
print(w + e)