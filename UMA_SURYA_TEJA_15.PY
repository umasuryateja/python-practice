# Float object demo program (Home work)
a = 10.8
print(a) # print value of float object ‘a’ i.e. 10.8
print(type(a)) # print type of object ‘a’ i.e. <class ‘float’>
print(id(a)) #print address of object ‘a’ example: 2515744510512(random value)
b = 25.
print(b) # print value of float object ‘b’ i.e. 25.0
print(type(b)) # print type of object ‘b’ i.e. <class ‘float’>
c = .689
print(c) # print value of float object ‘c’ i.e. 0.689
d = 3.4E2
print(d) # print value of float object ‘d’ i.e. 340.0 (3.4*10^2)
print(type(d)) # print type of object ‘d’ i.e. <class ‘float’>
e = 9.62e-2
print(e) # print value of float object ‘e’ i.e. 0.0962 (9.62*10^-2)
#print(9.8.2) # error only single dot is valid in a decimal number not more than one


# Complex object demo program
a = 3 + 4j
print(a) # print value of complex object ‘a’ i.e. 3 + 4j
print(type(a)) # print type of object ‘a’ i.e. <class ‘complex’>
print(id(a)) # print address of object ‘a’ example: 2654870376336 (random value)
print(a . real) # print real part of the complex number ‘a’ i.e. 3.0
print(a.imag) # print imaginary part of the complex number ‘a’ i.e. 4.0
print(type(a.real)) # print the type of the real part of 'a' i.e. <class ‘float’>
print(type(a.imag)) # print the type of the imaginary part of 'a' i.e. <class ‘float’>
# Find outputs (Home work)
a = 6j
print(a) # print the value of object ‘a’ i.e. 6j
print(type(a)) # print the type of object ‘a’ i.e. <class ‘complex’>
print(a.real) # print real part of the complex number ‘a’ i.e. 0.0
print(a.imag) # print imaginary part of the complex number ‘a’ i.e. 6.0
#print(5 + j6) # error j must come after the numeric 
#print(3 + 4i) # error i is not valid in python 
#print(4+j) # error j is invalid until a numeric value add before it
print(4 + 1j) # print the value of object i.e. 4 + 1j
print(4 + 0j) # print the value of object i.e. 4 + 0j


# bool object demo program (Home work)
a = True
print(a) # print the value of object ‘a’ i.e. True
print(type(a)) # print the type of object ‘a’ i.e. <class ‘bool’>
print(id(a)) # print the address of object ‘a’ example: 2654870376346 (random number)
b = False
print(b) # print the value of object ‘b’ i.e. False
print(type(b)) # print the type of object ‘b’ i.e. <class ‘bool’>
print(True + True) # print the value (1 + 1 = 2)
print(True + False) # print the value (1 + 0 = 1)
print(False + True) # print the value (0 + 1 = 1)
print(False + False) # print the value (0 + 0 = 0)
print(True + True + True) # print the value (1 + 1 + 1 = 3)
print(25 + 10.8 + True) # print the value (25 + 10.8 + 1 = 36.8)
print(True > False) # print the value True
print(True) # print the value True
print(False) # print the value False
#print(true) # error 'True' is a keyword, it must start with an uppercase T
#print(false) # error 'False' is a keyword, it must start with an uppercase F
# Find outputs (Home work)
a = 0O6247
print(a) # print the value of object ‘a’ i.e. 3239
print(type(a)) # print the type of ‘a’ i.e. <class ‘int’>
print(id(a)) # print the address of object ‘a’ example: 2654870377897 (random number)
b = 0o6247
print(id(b)) # print the address of object ‘a’ example: 26548703774234 (random number)
print(b) # print the value of object ‘b’ i.e. 3239
c = 3239
print(c) # print the value of object ‘c’ i.e. 3239
print(id(c)) # print the address of object ‘a’ example: 2654870377899 (random number)
#print(0o9248) # error octal values are valid from only (0-7)
# Find outputs (Home work)
a = 0XA7B9
print(a) # print the value of object ‘a’ i.e. 42937
print(type(a)) # print the type of ‘a’ i.e. <class ‘int’>
b = 0xBEEF
print(b) # print the value of object ‘a’ i.e. 48879
#print(A7B9) "error A7B9 is not a defined variable. It should be written as a string 'A7B9' or as a hex literal 0xA7B9."
print('A7B9') # print the value ‘A7B9’
#print(0XBEER) # error hexagonal allows alphabets upto F only (A-F) here R is invalid
#print(0XHYD) # error hexagonal allows alphabets upto F only (A-F) here Hand Y is invalid
#print(0xA7G9B) # error hexagonal allows alphabets upto F only (A-F) here G is invalid
# Find outputs (Home work)
a = 9248
print(a) # print the value of object ‘a’ i.e. 9248
print(type(a)) # print the type of object ‘a’ i.e. <class ‘int’>
