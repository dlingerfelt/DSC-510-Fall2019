'''
    File: indentationExample.py
    Author: Pritam shrestha
    Assignment: 5.1
    Date:09/28/2019
    Course: DSC 510 - Introduction to programming
    Desc: This program will Define 2 functions
        1 . performCalculation which takes one parameter as operator and based on the passing
        operator it will perform the operations(-,+,/,*).
        2.  calculateAverage which takes no parameters.

'''
def performCalculation(operator):



# getting first input from user
   x=float(input("Enter the first number"))
   firt_number=x
# getting second inout from user
   y=float(input("Enter the second number"))
   second_number=y
# initializing vale in the beginning
   result=None

# for addition
   if operator== '+':
      result=x+y
      print(result)

# for substraction

   elif operator=='-':
      result=x-y
      print(result)

# for division

   elif operator=='/':
# checking value is 0 or not
      if y!=0:

         result=x/y
         print(result)
      else:
         print("Divide by Zero will create infinity")
         print("Please enter the valid number")

   elif operator=='*':
      result=x*y
      print(result)


# for example i am passing - operator
def calculateAverage ():
   # getting input from user
    averageInput = int(input('How many numbers would you like to average?'))
    total = 0
   # setting range for iteration
    for i in range(0, averageInput):
    	number = int(input('Please enter a valid number: '))

    	total = total + number
       #calculating average
    print('Your average is ', total/averageInput)

operation = ['+','-','/','*']

# using while loop to iterate until the condition is true.
while True:
   inputOperator=input("Please enter the operator or average for arithmetic operation !")
   inputOperator=inputOperator.lower()
   if inputOperator in operation:
      performCalculation(inputOperator)

   elif inputOperator=="average":
      calculateAverage()
   else:
      print("Please enter the valid input!")
      print("Run the program again entering like '-','+','/','*' and'average!!!")
      break
print("The program has ran successfully!!!")