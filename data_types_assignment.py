# data_types_assignment

"""
1- Suppose you invested in Bitcoin at the end of 2020 when 
Bitcoin gained a lot of value. What would be your money at 
the end of a week if you had invested $1000 with an average 
daily increase of 12% ? 
You can solve the problem using Python.

Help
Create a variable capital ($1000)
Create a variable for daily growth (12%)
Create a variable for period (7)
Calculate the final growth rate
Calculate result
Print result
"""
#my answer to question 1:
capital = 1000
daily_growth = 0.12
period = 7

for i in range(period):
    capital  +=  capital * daily_growth
    result = capital

capital = 1000          #money we have in the beginning
net = result - capital  #money we earned
print(net)



"""
2- Print the text in quotes with Python. 
However, you must get the numbers from variables using 
.format() notation. Because the text is long, 
you might consider writing in two lines:

"When we buy bitcoin with 1000 USD at the beginning of the week, 
we would earn 1210.68 USD at the end of the week, with an average gain of 12\%."
"""
#my answer to question 2:
print("""When we buy bitcoin with {C} USD at the beginning of the week,
we would earn {N} USD at the end of the week, with an average gain of {D}."""
.format(C = capital, N = round(net,2), D = daily_growth )) 



"""
3- Get the temperature in Fahrenheit from user and write a code to convert 
it to Celcius. For conversion, you can use this formula: C = (5/9) * (F - 32)

Enter the temperature in Fahrenheit:
user --> 26
output --> Temperature (C) : -3.33
"""
#my answer to question 3:
f = float(input("Enter the temperature in Fahrenheit: "))
c = (5/9) * (f - 32)
print("Temperature (C): {}".format(round(c,2)))



"""
4- Get a three digit number the from user and calculate the sum of the digits in the integer.

user --> 365
output --> "The sum of digits in the number is 14
"""
#my answer to question 4:
num = input ("Enter a three digit number: ")
sum = int(num[0]) + int(num[1]) + int(num[2])
print("The sum of digits in the number is {}".format(sum))



"""
5- Write some code to calculate the hypotenuse of a right angled triangle. 
Get the side lengths from the user.

user --> first side lenth : 6
user --> first side lenth : 8
output --> "The length of the hypotenuse is 10
"""
#my answer to question 5:
side_1 = float(input("First side length: "))
side_2 = float(input("Second side length: "))
hypotenuse = (side_1**2 + side_2**2) ** 0.5
print("The length of the hypotenuse is {}".format(hypotenuse))

