# We have a number.
number = 124584

# Assigning last digit of the number in res
# variable.
res = number % 10

# Now, continue a loop until
# the number becomes less than 9.
while number > 9:

	# integer division of the number and reassigning
	# it.
	number = number // 10

# Here, our number only contain one digit.
# So, add this number in res variable.
res += number

# Now, display our output
print('Addition of first and last digit of number is', res)
