# primitive data types

name = "Urvashi" # string
print(type(name))
print(name+" Bhargava")
print("12"+"34")

print(12+34) # int
print(123_456_789) # large integers

print(3.14) # float

boolz = True # boolean
boolz = False

num = input("Enter a two digit number: ")
tens = int(num[0])
ones = int(num[1])
print("Sum is "+str(tens+ones))

# PEMDASLR (), **, *, /, +, -

print(2**3**2) # right to left-> 3**2=9, then 2**9 = 512
height = input("Enter height in meters: ")
weight = input("Enter weight in kilograms: ")

bmi = int(weight) / (float(height)*float(height))
print("Your BMI is: "+str(int(bmi)))

print(round(8/3,4)) # round upto 4 decimal points
print(8//3) # floor division as result is int



