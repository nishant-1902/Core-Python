# if statement or if..else

# 1.check if number is positive
# num = int(input("Enter a number :"))
# if num > 0:
#     print("Number is positive")
# else:
#     print("Number is negative")

# 2.check if a person is adult
# num = int(input("Enter a age :"))
# if num >= 18:
#     print("You are adult")
# else:
#     print("You are baby")

# 3.check if string contains 'a'
# text = 'Nisant'
# if 'a' in text:
#     print("The letter a is present")

# 4.check if number is even
# num = int(input("Enter a number :"))
# if num % 2 == 0:
#     print("Number is even")
# else:
#     print("Number is odd")

# 5.compare two numbers
# a = int(input("Enter first number :"))
# b = int(input("Enter second number :"))
# if a > b:
#     print("first number is greater")
# else:
#     print("second number is greater")


# elif

# 1. grade system
# marks = int(input("Enter marks :"))
# if marks >= 90:
#     print("Grade A")
# elif marks > 80:
#     print("Grade B")
# elif marks > 70:
#     print("Grade c")
# elif marks > 60:
#     print("Grade D")
# else:
#     print("low grade")

# 2.day of week
# day = 5
# if day == 1:
#     print("monday")
# elif day == 2:
#     print("tuesday")
# elif day == 3:
#     print("wednesday")
# elif day == 4:
#     print("thursday")
# elif day == 5:
#     print("friday")
# elif day == 6:
#     print("saturday")
# else:
#     print("sunday")

# 3.compare three numbers
# a = int(input("Enter first number :"))
# b = int(input("Enter second number :"))
# c = int(input("Enter third number :"))
# if a > b and a > c:
#     print("first number is greater")
# elif b > a and b > c:
#     print("second number is greater")
# else:
#     print("third number is greater")

# 4.temprature check
# temp = 23
# if temp > 35:
#     print("Hot day")
# elif temp > 25:
#     print("Normal day")
# elif temp > 20:
#     print("Cold day")
# else:
#     print("cold day")

# 5. check age group
# age = 18
# if age < 13:
#     print("child")
# elif age < 20:
#     print("teen")
# elif age < 60:
#     print("adult")
# else:
#     print("senior citizen")

# nested if

# 1.check positive and even number
# num = 10
# if num > 0:
#     if num % 2 == 0:
#         print("Positive Even Numbers")

# 2.student result
# marks = 67
# if marks >= 40:
#     if marks > 70:
#         print("Distinction")
#     else:
#         print("pass")

# 3. ATM PIN check
# pin = 1234
# entered_pin = 1234
# if entered_pin == pin:
#     if 100 <= 500:
#         print("Transaction allowed")
#     else:
#         print("low balance")

# 4. Check vowel
ch = 'a'
if ch.isalpha():
    if ch in "aeiou":
        print("Vowel")

# 5. Check login system
# username = "admin"
# password = "1234"
# if username == "admin":
#     if password == "1234":
#         print("Login successful")