#
# Prime Numbers
# The program that finding prime numbers until the user want to stop asking for the next one.
#

choice = input("Continue finding to next prime number (y/n)? ")
current = 1

def is_prime(n):
	if n % 2 == 0:
		return False

	for i in range(3, int(n**0.5) + 1, 2):
		if n % i == 0:
			return False

	return True

while choice.lower().startswith('y'):
	current += 1

	while is_prime(current) == False:
		current += 1

	print ("Next prime is " + str(current))
	choice = input("Continue finding to next prime number (y/n)? ")