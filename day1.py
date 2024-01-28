name = input("Enter your name: ")
print("Hello World!\nThis is"+" "+name+"❤️  and she has "+str(len(name))+" characters in her name.") 
# input will take input from user in console

age = input("What is your current age? ") # variable age
print(name+" is "+age+" years old.")

# swapping
a = int(input("a: "))
b = int(input("b: "))
print("BEFORE->a: "+str(a)+" b: "+str(b))
c = a
a = b
b = c
print("AFTER SWAP->a: "+str(a)+" b: "+str(b))

# var names cannot be like 1name, mint@, user name -> Syntax Error
print("Now WELCOME TO BAND NAME GENERATOR!")
city = input("What is the name of the city you grew up in?\n")
pet = input("What is the name of your pet?\n")
print("Your band name is "+ city +" "+ pet +"!")