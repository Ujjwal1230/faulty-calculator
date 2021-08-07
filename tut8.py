print("Enter first number")
a = int(input())
print("Enter second number")
b = int(input())
print("which operator you want to use:\n'+'\n'-'\n'*'\n'/'\n'%'")
operator = input()

if a==55 and b==7 and operator=='+':
    print(72)
elif a==66 and b==11 and operator=='-':
    print(3)
elif a==52 and b==7 and operator=='*':
    print(300)
elif a==72 and b==6 and operator=='/':
    print(121)
elif operator=='+':
    sum = a+b
    print(sum)
elif operator=='-':
    subtraction = a-b
    print(subtraction)
elif operator=='*':
    multiply = a*b
    print(multiply)
elif operator=='/':
    division = a/b
    print(division)
elif operator=='%':
    modulus = a%b
    print(modulus)
else:
    print("you have not entered number")
