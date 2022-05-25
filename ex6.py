#defining variables
types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

#printing variables
print(x)
print(y)

#printing strings with variables
print(f"I said: {x}")
print(f"I also said: '{y}'")

#defining variables
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"


print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
