# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
'''
You will encounter lists everywhere:

customers = [...]
orders = [...]
files = [...]
columns = [...]
api_records = [...]
1. Creating a list
customers = [
    "John",
    "Mary",
    "David"
]

You can access elements using indexes:

print(customers[0])

Output:

John
2. List indexing
orders = [1001, 1002, 1003, 1004]
print(orders[0])
print(orders[2])
print(orders[-1])

Result:

1001
1003
1004

Same indexing concept as strings.

3. List slicing
orders = [1001, 1002, 1003, 1004, 1005]
print(orders[0:3])

Result:

[1001, 1002, 1003]
4. Adding elements
append()
orders = [1001, 1002]

orders.append(1003)

print(orders)

Result:

[1001, 1002, 1003]
insert()
orders.insert(0, 999)
5. Removing elements
orders.remove(1002)

Or:

orders.pop()

pop() removes the last element.

You can also:

orders.pop(1)

to remove the element at index 1.

6. List length
len(orders)

Very useful when checking how many records you received from an API:

print(f"Received {len(orders)} records")
7. Checking membership
if 1003 in orders:
    print("Order exists")

Very useful for validation.

Transformation
[expression for item in list]

Transformation + filtering
[expression for item in list if condition]

'''

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#print First product Last product and Number of products

products = [
    "Laptop",
    "Mouse",
    "Keyboard",
    "Monitor"
]

print(products)
#print(f'first product is {products[0]} last product is {products[-1]} and length of products is {len(products)}')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# ADD Headphones
products.append('head phones')
print(products)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#remove mouse
products.remove('Mouse')
print(products)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#create a list and print first price, last price, first 3 prices, number of prices

prices = [100, 250, 75, 500, 120]

print(f'first price is {prices[0]}')
print(f'last price is {prices[-1]}')
print(f'first 3 prices are {prices[0:3]}')
print(f'Number of prices are {len(prices)}')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Data engineering exercise
#create a new list cleaned countries

countries = [
    " germany ",
    "GERMANY",
    " India ",
    "INDIA",
    " france "
]

cleaned_countries=[]

for country in countries:
    cleaned_country=country.strip().title()
    cleaned_countries.append(cleaned_country)
print(cleaned_countries)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# try ,except blocks
raw_prices = [
    "100.50",
    "250",
    "75.25",
    "invalid",
    "500"
     ]
valid_prices=[]
for price in raw_prices:
    try:

        price=float(price)
        valid_prices.append(price)
    
    except ValueError:
        price=0

print(valid_prices)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#list comprehensions
numbers = [1, 2, 3, 4, 5]

squared_numbers = []

for number in numbers:
    squared_numbers.append(number ** 2)
    
# using list comprehension

squared_numbers=[number **2 for number in numbers]
print(squared_numbers)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#cleaning names using list comprehensions
raw_names = [
    " john smith ",
    "MARY JONES",
    " david brown ",
    "SARAH WILSON"
]

cleaned_names=[ name.strip().title() for name in raw_names]
print(cleaned_names)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Create a list containing only the valid numeric values.
raw_quantities = [
    "10",
    "25",
    "invalid",
    "50",
    "100"
]

valid_quantities =[ quantity for quantity in raw_quantities if(quantity.isdigit())]
print(valid_quantities)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

amounts = [100, -50, 250, 0, 75, -20, 300]

valid_amounts=[amount for amount in amounts if amount>0]
print(valid_amounts)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

raw_amounts = [
    "100",
    "250",
    "invalid",
    "75",
    "abc",
    "500"
]

valid_amounts=[int(amount) for amount in raw_amounts if amount.isdigit()]
print(valid_amounts)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

raw_names = [
    " john smith ",
    "",
    "MARY JONES",
    "   ",
    "david brown",
    "SARAH WILSON",
    " "
]

cleaned_names= [ name.strip().title() for name in raw_names if name.strip()]

print(cleaned_names)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

raw_quantities = [
    "10",
    " 25 ",
    "invalid",
    "",
    " 50",
    "abc",
    "100 "
]

valid_values =[int(value.strip()) for value in raw_quantities if value.strip().isdigit()]

print(valid_values)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

raw_prices = [
    "100.50",
    "250",
    " 75.25 ",
    "invalid",
    "",
    "500.75"
]

def is_valid_price(value):
    try:
        float(value.strip())
        return True
    except ValueError:
        return False

valid_prices =[ float(price.strip()) for price in raw_prices if is_valid_price(price)]



# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

raw_quantities = [
    "10",
    "25",
    "invalid",
    "50",
    "100"
]

new_quantities = [int(value) for value in raw_quantities if value.isdigit()]
print(new_quantities)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

raw_amounts = [
    "100.50",
    "250",
    "invalid",
    " 75.25 ",
    "",
    "500.75",
    "abc"
]

def clean_amount(amount):
   try:
    return float(amount.strip())
    
   except ValueError:
    return None

new_values =[value 
for value in [clean_amount(amount) for amount in raw_amounts]
if value is not None]
print(new_values)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

raw_ages = [
    "25",
    " 30 ",
    "invalid",
    "42",
    "",
    "35",
    "unknown"
]

def clean_ages(value):
    try:
        return int(value.strip())
    except ValueError:
        return None

cleaned_ages =[age 
for age in [clean_ages(value) for value in raw_ages]
if age is not None

]
print(cleaned_ages)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

raw_scores = [
    "95",
    " 88 ",
    "invalid",
    "72",
    "",
    "100",
    "abc",
    " 65 "
]

def clean_scores(value):
    try:
        return int(value.strip())
    except:
        return None
score_value =[clean_scores(value) for value in raw_scores]
clean_scores= [score for score in score_value if score is not None]
print(clean_scores)



# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

raw_ages = [
    "25",
    " 17 ",
    "42",
    "invalid",
    "65",
    "0",
    " 30 ",
    "-5"
]

def clean_scores(value):
    try:
        return int(value.strip())
    except:
        return None
score_value =[clean_scores(value) for value in raw_ages]
clean_scores= [score for score in score_value if score is not None and score >=18]
print(clean_scores)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

numbers = [10, 20, 30, 40, 50]
print(numbers[0],numbers[-1], len(numbers),numbers[0:3])

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

countries = ["Germany", "India", "France", "Spain"]

print(countries[0], countries[2],countries[3])

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

numbers = [10, 20, 30]
numbers.append(40)
print(numbers)
numbers.extend([50,60])
print(numbers)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Insert 30 between 20 and 40.
numbers = [10, 20, 40, 50]
numbers.insert(2,30)
print(numbers)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Remove the first 20.
numbers = [10, 20, 30, 20, 40]
numbers.remove(20)
print(numbers)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Use pop() to remove 30.
numbers = [10, 20, 30, 40]
removed_value= numbers.pop(2)
print(numbers)
print(removed_value)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#ascending order list

scores = [85, 40, 92, 67, 55, 99]
sorted_scores=sorted(scores)
print(sorted_scores)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#create another list sorted in descending order.
scores = [85, 40, 92, 67, 55, 99]
sorted_scores=sorted(scores,reverse=True)
print(sorted_scores)



# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

raw_values = [
    "10",
    "25",
    "invalid",
    "50",
    "100"
]

clean_values= [int(value) for value in raw_values if value.isdigit()]
print(clean_values)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# create new list containing age>18
users = [
    {"id": 101, "age": 25},
    {"id": 102, "age": 17},
    {"id": 103, "age": 35},
    {"id": 104, "age": 15},
    {"id": 105, "age": 42}
]
adult_users = [user for user in users if user["age"] > 18]

print(adult_users)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Extract a column
users = [
    {"id": 101, "name": "John"},
    {"id": 102, "name": "Alice"},
    {"id": 103, "name": "Bob"}
]

names=[]
for user in users:
    name=user['name']
    names.append(name)

print(names)

#using list comprehension
names = [user["name"] for user in users]
print(names)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Calculate Total
orders = [
    {"order_id": 1, "amount": 100},
    {"order_id": 2, "amount": 250},
    {"order_id": 3, "amount": 75},
    {"order_id": 4, "amount": 300}
]

order_total= sum([order['amount'] for order in orders])
print(order_total)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Create a new list containing only completed transactions and sum of amount

transactions = [
    {"id": 1, "amount": 100, "status": "completed"},
    {"id": 2, "amount": 250, "status": "failed"},
    {"id": 3, "amount": 150, "status": "completed"},
    {"id": 4, "amount": 300, "status": "completed"},
    {"id": 5, "amount": 50, "status": "failed"}
]
completed_transactions = [
    transaction
    for transaction in transactions
    if transaction["status"] == "completed"
]
print(completed_transactions)

amount_sum= sum([trans['amount'] for trans in completed_transactions])

print("total amount is ",amount_sum)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Duplicate Detection
user_ids = [101, 102, 103, 101, 104, 102, 105]

#duplicate_ids=[id for id in user_ids if user_ids.count(id)>1]
duplicate_ids = list(set(
    id for id in user_ids
    if user_ids.count(id) > 1
))

print(duplicate_ids)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

raw_transactions = [
    {"id": "101", "amount": "100.50", "status": "completed"},
    {"id": "102", "amount": "invalid", "status": "completed"},
    {"id": "103", "amount": "250.00", "status": "failed"},
    {"id": "104", "amount": "300.75", "status": "completed"},
    {"id": "105", "amount": "50", "status": "completed"}
]



def clean_trans(trans):
        try:
            trans['id']= int(trans['id'])
        
        except(ValueError):
            trans['id']= None
    
        try:
            trans['amount']=float(trans['amount'])
        except(ValueError):
            trans['amount']=None
        return trans

        
clean_transactions = [clean_trans(trans) for trans in raw_transactions]
#print(clean_trans)

clean_completed_trans = [trans for trans in clean_transactions if trans['status']=='completed']


clean_completed_trans_amount =[trans for trans in clean_completed_trans if trans['amount'] is not None]

transaction_amount=sum([trans['amount'] for trans in clean_completed_trans_amount])

print(transaction_amount)
print(clean_completed_trans_amount)

valid_ids=[trans['id'] for trans in clean_completed_trans_amount]
print(valid_ids)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

transactions = [
    {"id": 101, "amount": 100, "status": "completed"},
    {"id": 102, "amount": 200, "status": "failed"},
    {"id": 103, "amount": 300, "status": "completed"},
    {"id": 104, "amount": 1500, "status": "completed"},
    {"id": 105, "amount": 50, "status": "failed"},
    {"id": 106, "amount": 400, "status": "completed"},
]


completed_transactions = [trans for trans in transactions if trans['status']=='completed']
print(completed_transactions)

total_amount =sum([trans['amount'] for trans in completed_transactions])
print(total_amount)

ids= [trans['id'] for trans in completed_transactions]
print(ids)

max_amount=0
for item in completed_transactions:
    if item['amount']>max_amount:
        max_amount=item['amount'] 
print(max_amount)
highest_trans =[trans for trans in completed_transactions if trans['amount']==max_amount]
print(highest_trans)

amountMoreThan200 = [trans['amount'] for trans in completed_transactions if trans['amount']>=200]
print(amountMoreThan200)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# What's the difference between:
# 
# append()
# 
# and:
# 
# extend()
# 
# ?
# 
# Q16
# 
# What's the difference between:
# 
# sort()
# 
# and:
# 
# sorted()
# 
# ?
# 
# Q17
# 
# What's the difference between:
# 
# remove()
# 
# and:
# 
# pop()
# 
# ?
# 
# Q18
# 
# What is the difference between a shallow copy and simply assigning:
# 
# b = a

# MARKDOWN ********************

