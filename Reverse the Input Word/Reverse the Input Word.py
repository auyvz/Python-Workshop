#
# Reverse the Input Word from the user
#

string = input("Enter a string: ")
#vowels = ['a', 'e', 'i', 'o', 'u']

s = string.lower()
a = s.count('a')
e = s.count('e')
i = s.count('i')
o = s.count('o')
u = s.count('u')

print ("There are " + str(a+e+i+o+u) + " vowels.")

print (str(a) + "a ")
print (str(e) + "e")
print (str(i) + "i")
print (str(o) + "o")
print (str(u) + "u")