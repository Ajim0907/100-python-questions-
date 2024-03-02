# accept 3 ages and find the highest between them

age1 = int(input("enter your first age "))
age2 =int(input("enter your  second age "))
age3 =int(input("enter your third age "))

max = age1
if age1 <age2 :
    max = age2
    if age2 < age3:
        max = age3

print(f"your highest age is {max}")
