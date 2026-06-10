# 1. Positive, Negative, or Zero
num=int(input())
if num>0:
    print(f"{num} is positive")
elif num<0:
    print(f"{num} is negative")
else:
    print(f"{num} is not positive nor negative")

# even or odd
num = int(input())
if num%2==0:
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")

# voting eligibility
age = int(input("enter the age : "))

if age>=18:
    print("you are eligible to vote")
else:
    print("Not eligible")

# pass or fail
marks = int(input("enter the marks : "))

if marks>=40:
    print("pass")
else:
    print("fail")

# largest of two numbers

num_1 = int(input("enter the number 1 : "))
num_2 = int(input("enter the number 2 : "))

if num_1 > num_2:
    print(f"{num_1} is greater")
else:
    print(f"{num_2} is greater")

# temperature checker
temperature = int(input("enter the temperature"))

if temperature>35:
    print("Hot")
elif 20<=temperature<=35:
    print("Warm")
else:
    print("cold")

# ATM withdrawal
balance = int(input("balance : "))
withdrawal_amount = int(input("enter the amount : "))

if withdrawal_amount <= balance:
    print("withdawal successful")
else:
    print("Insuffiecient Balance")

# number guessing
guess_number = int(input("enter the number"))

if guess_number>10:
    print("too high")
elif guess_number<10:
    print("too low")
else:
    print("correct")

# triangle type

side_1 = int(input("enter side A : "))
side_2 = int(input("enter side B : "))
side_3 = int(input("enter side C : "))

if side_1 == side_2 and side_1 == side_3:
    print("Equilateral triangle")
elif side_1 == side_2 or side_1 == side_3:
    print("Isosceles triangle")
else:
    print("Scalene")
