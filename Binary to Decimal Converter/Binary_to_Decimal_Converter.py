# Binary to Decimal Converter
# The program that  convert a decimal number to binary or a binary number to its decimal equivalent
#

def b_to_d(number):
    rev = str(number)[::-1]
    counter = 0
    decimal = 0
    while counter < len(rev):
        if int(rev[counter]) == 1:
            decimal += 2**counter
        counter += 1
    return decimal

def d_to_b(number):
	binary = ''
	while number > 1:
		binary = str(number % 2) + binary
		number = number // 2
	return str(1) + binary

print ("""
	1. Binary to Decimal Conversion
	2. Decimal to Binary Conversion\n""")

choice = int(input("Choose conversion type: "))

if choice == 1:
	number = int(input("Number to convert: "))
	print ("Decimal of %s is %s" % (number, b_to_d(number)))
elif choice == 2:
	number = int(input("Number to convert: "))
	print ("Binary of %s is %s" % (number, d_to_b(number)))
else:
	print ("Invalid Choice")