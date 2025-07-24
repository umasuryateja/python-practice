a = 25
print(++a) # 25
#print(a++) # SyntaxError: invalid syntax
print(a++1) # 26
print(--a) # 25
#print(a--) # SyntaxError: invalid syntax
print(a--1) # 24
print(-a) # -25
print(+-a) # -25
print(-+a) # -25

#  Semicolon  demo  program
print('One'); #one
print('Two'); #two
print('Three'); #Three
print('Hyd')  ;  #Hyd                                                                                                                                                print('Sec')  ;    #Sec
print('Cyb')   #Cyb

import math
print(math.floor(10.8)) # 10
print(math.ceil(10.8)) # 11
print(math.floor(25.0)) # 25
print(math.ceil(25.0)) # 25
print(math.floor(-3.5)) # -4
print(math.ceil(-3.5)) # -3
print(math.floor(-9.0)) # -9
print(math.ceil(-9.0)) # -9
print(math.floor(25.1)) # 25
print(math.ceil(25.1)) # 26
#print(floor(3.5)) # NameError: name 'floor' is not defined
#print(ceil(3.5)) # NameError: name 'ceil' is not defined

import math
print(math.gcd(12, 15)) # 3
print(math.gcd(12, 18)) # 6
print(math.gcd(4, 7)) # 1
print(math.gcd(7, 7)) # 7
print(math.gcd(-18, -27)) # 9
print(math.gcd(-4, 6)) # 2
print(math.gcd(0, 7)) # 7
print(math.gcd(3, 0)) # 3
print(math.gcd(0, 0)) # 0
#print(gcd(5, 15)) # NameError: name 'gcd' is not defined

from builtins import abs
print(abs(-35.8)) # 35.8
print(abs(-27)) # 27
print(abs(29.5)) # 29.5
print(abs(32)) # 32
import builtins
print(builtins.abs(-25)) # 25

from builtins import max, min
print(max(10.8, 20.6)) # 20.6
print(min(10.8, 20.6, 5.9, 12.3)) # 5.9
print(max(25, 10.8)) # 25
import builtins
print(builtins.max(10, 20, 30)) # 30
print(builtins.min(10, 20, 15, 5, 12)) # 5

from builtins import pow
print(pow(10, -2)) # 0.01
print(pow(4, pow(3, 2))) # 262144 (because pow(3, 2) = 9, and pow(4, 9) = 262144)
import builtins
print(builtins.pow(2, 3)) # 8
print(builtins.pow(-2, -3)) # -0.125

import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))  # number of keywords
print(type(keyword.kwlist))  # type of kwlist

#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
#35
#<class 'list'>

import keyword
print(keyword.kwlist)  # print kwlist
print(len(keyword.kwlist))  # print number of keywords 35
print(type(keyword.kwlist))  # print type of kwlist <class 'list'>






