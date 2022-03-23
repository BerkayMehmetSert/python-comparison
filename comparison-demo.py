# 1- Less than 2 numbers entered?
a = input("Enter 1. number: ")
b = input("Enter 2. number: ")
result = (a>b) 
print("The result is: ", result)

# 2- 
exam1 = int(input("Enter exam 1 score: "))
exam2 = int(input("Enter exam 2 score: "))
exam3 = int(input("Enter exam 3 score: "))
average= (exam1+exam2+exam3)/3
print("The average is: ", average)
result = (average>=50) 
print("The result is: ", result)

# 3- odd or even
number = int(input("Enter a number: "))
result = (number%2==0)
print("The result is: ", result)

# 4- negative or positive
number = int(input("Enter a number: "))
result = (number<0)
print("The result is: ", result)

# 5- Email and password check 

email= 'email@gmail.com'
password='abc123'
inputEmail= input("Enter email: ")
inputPassword= input("Enter password: ")
isEmail= (inputEmail==email) 
isPassword= (inputPassword==password)
print("The result is: ", isEmail)
print("The result is: ", isPassword)