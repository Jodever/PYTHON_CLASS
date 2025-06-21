# variables 
#integer = 5

#birth_year = 2000
#current_year = 2025

#age = current_year - birth_year
#print(age)

#firstname = "Joshua"
#middlename = "Don't worry"
#lastname = "Okpare"

#print(f"My nanes are ",firstname, middlename, lastname)

# numbers
# length = 92
# breath = 48.8

# area = length * breath

# print(f"area is,", float(area))


# quantity = 9
# price_for_bought_quantity = 9 * 1.49
# amount_paid = 20

# print(f"balance is,",amount_paid - price_for_bought_quantity)

# area_of_room_in_sq_feet = 5.5**2
# cost_of_replacement = 500 * area_of_room_in_sq_feet
# print(f"cost of replacement is: ",cost_of_replacement)

# decimal = 17
# print(f"Binary representaion is: ",bin(decimal))


#strings
# street = "\nalden"
# city = "\nLos Angeles"
# country = "\nUSA"

# adress = "The adress is "+ street+city+country
# address = f"The adress is {street} {city} {country}"

# print(address)
#print(address)

# sent = "Earth revolves around the sun"

# print(sent[6:14])

# print(sent[-3:])

# fruits = 5
# vegetables = 2
# print(f"I eat {fruits} fruits and {vegetables} vegetables")

# s='maine 200 banana khaye'
# s=s.replace('banana','samosa')
# s=s.replace('200','10')
# print("Using two line replace:",s)

# s='maine 200 banana khaye'
# s=s.replace('banana','samosa').replace('200','10')
# print("Using single line:",s)

#lists
# expense = [2200,2350,2600,2130,2190]

# print(expense[1] - expense[0])
# print(expense[0] + expense[1] + expense[2] + expense[3])
# print(2000  in expense)

# for i in expense:
#     if i == 2000:
#         print(i)
#     else:
#         print(False)

# expense.append(1980)
# expense[3] = (expense[3] + 200)

# print(expense)

# heros=['spider man','thor','hulk','iron man','captain america']

# print(len(heros))


#if statement

# india = ["mumbai", "banglore", "chennai", "delhi"]
# pakistan = ["lahore","karachi","islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]

# choice = input("Enter a city name: ")

# if choice in india:
#     print("India")
# elif choice in pakistan:
#     print("Pakistan")
# elif choice in bangladesh:
#     print("bangladesh")
# else:
#     print("not in scope")choice = input("Enter a city name: ")

# choice1 = input("Enter a city name: ")
# choice2 = input("Enter a city name: ")

# if choice1 in india and choice2 in india:
#     print("Both cities in India")
# elif choice1 in pakistan and choice2 in pakistan:
#     print("Both cities in Pakistan")
# elif choice1 in bangladesh and choice2  in bangladesh:
#     print("Both cities in Bangladesh")
# else:
#     print("not in same country")



#Ask user to enter his fasting sugar level
#If it is below 80 to 100 range then print that sugar is low
#If it is above 100 then print that it is high otherwise print that it is normal


# sugar_level = int(input("What is your sugar level?: "))

# if sugar_level < 80:
#     print("Sugar level is low")
# elif sugar_level > 100:
#     print("Sugar level too high")
# else:
#     print("Sugar level is normal")

var = 10

print(type(var))