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
'''1. Creating strings
customer_name = "John Smith"
country = 'Germany'

Both are valid.

You can also use triple quotes for multiline strings:

message = """
Pipeline started
Records extracted
Pipeline completed
"""
2. String indexing

Each character has a position.

name = "Python"
P  y  t  h  o  n
0  1  2  3  4  5

So:

print(name[0])

gives:

P

And:

print(name[3])

gives:

h

Python also supports negative indexing:

print(name[-1])

Output:

n
print(name[-2])

Output:

o
Important

Python indexing starts at 0, not 1.

3. String slicing

You can extract part of a string.

name = "Python"
print(name[0:3])

Output:

Pyt

The general form is:

string[start:end]

The end position is not included.

For example:

name[0:3]

means:

positions 0, 1, 2
Useful slicing
name[:3]

First 3 characters.

name[3:]

Everything from position 3 onward.

name[:]

Entire string.

You can also use a step:

name[::2]
4. String length

Use:

len()

Example:

customer_name = "John Smith"

print(len(customer_name))

This counts spaces too.

5. Changing case

Very common in data cleaning.

country = "Germany"

print(country.upper())
print(country.lower())

Output:

GERMANY
germany

Also:

name = "john smith"

print(name.title())

Output:

John Smith
6. Removing whitespace

This is extremely important in Data Engineering.

Suppose your source contains:

country = "  Germany  "

Use:

country.strip()

Result:

Germany

You also have:

country.lstrip()

removes whitespace from the left.

country.rstrip()

removes whitespace from the right.

A very common cleaning operation is:

clean_country = country.strip().lower()

For:

"  Germany  "

you get:

germany
7. Replacing values

Use:

replace()

Example:

country = "United States"

country = country.replace(" ", "_")

print(country)

Result:

United_States

Another example:

email = "john@example.com"

email = email.replace("example.com", "company.com")
8. Splitting strings

This is extremely useful when processing raw data.

full_name = "John Smith"

parts = full_name.split(" ")

print(parts)

Output:

["John", "Smith"]

You can then access:

print(parts[0])
print(parts[1])
Data Engineering example

Suppose you receive:

email = "john.smith@gmail.com"

You can extract the domain:

domain = email.split("@")[1]

print(domain)

Result:

gmail.com
9. Joining strings

The opposite of split() is often join().

parts = ["John", "Smith"]

full_name = " ".join(parts)

print(full_name)

Result:

John Smith

Another example:

columns = ["customer_id", "customer_name", "country"]

result = ",".join(columns)

print(result)

Output:

customer_id,customer_name,country

This becomes useful when generating CSV-like data or dynamic SQL.

10. Checking whether a string contains something

Use:

"in"

Example:

email = "john@gmail.com"

print("@gmail.com" in email)

Result:

True

Another example:

country = "Germany"

print("Ger" in country)

Result:

True
11. startswith() and endswith()

Very useful when processing files.

filename = "orders_2026.csv"

print(filename.startswith("orders"))
True

And:

print(filename.endswith(".csv"))
True

For example:

if filename.endswith(".csv"):
    print("Process CSV file")

This becomes very useful when we start working with files.

12. Checking string content

Python gives you useful methods:

text.isdigit()
text.isalpha()
text.isalnum()
text.isspace()

Example:

quantity = "100"

print(quantity.isdigit())

Result:

True

This is useful when validating raw data.

For example:

quantity = "100"

if quantity.isdigit():
    quantity = int(quantity)
13. f-strings ⭐

You absolutely need to master this.

Instead of:

name = "John"
country = "Germany"

print("Customer " + name + " is from " + country)

use:

print(f"Customer {name} is from {country}")

Much cleaner.

You can also calculate inside an f-string:

quantity = 5
price = 20

print(f"Total: {quantity * price}")

Result:

Total: 100
14. Formatting numbers

For Data Engineering and reporting, this is useful.

amount = 123456.789

print(f"{amount:.2f}")

Result:

123456.79

You can also use commas:

print(f"{amount:,.2f}")

Result:

123,456.79
15. Strings are immutable ⭐

This is an important Python concept.

You cannot directly change one character of a string.

This will fail:

name = "John"

name[0] = "B"

Instead, create a new string:

name = "John"

name = "B" + name[1:]

print(name)

Result:

Bohn

Methods such as:

.upper()
.lower()
.strip()
.replace()

do not modify the original string.

They return a new string.

🔥 Data Engineering Example

Imagine a customer record arrives from an API:

customer_name = "  JOHN SMITH "
email = " JOHN.SMITH@GMAIL.COM "
country = " germany "

We want clean data.

customer_name = customer_name.strip().title()
email = email.strip().lower()
country = country.strip().title()

Now:

John Smith
john.smith@gmail.com
Germany

This is exactly the type of transformation you'll eventually perform with Pandas.

'''

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

customer_name = "  sandya duggana  "
#Printing customer_name
print(customer_name)
# Capitalising customer_name
print(customer_name.upper())
# lower case
print(customer_name.lower())
# title
print(customer_name.title())
length
print(len(customer_name))
#removal of extra spaces
print(customer_name.strip())
customer_name= customer_name.strip()
#printing length after space removal
print(len(customer_name))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

email = "  JOHN.SMITH@GMAIL.COM  "
# cleaning the email id
print("before cleaning",email)
email=email.strip().lower()
print("after cleaning",email)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

email = "john.smith@gmail.com"
# extract email domain
email_parts=email.split("@")
print(email_parts)
print("domain is ",email_parts[1])

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

customer_id = "DE-CUST-2026-00125"
#extract 2026 and 00125
customer_id_parts= customer_id.split("-")
print(customer_id_parts[2])
print(customer_id_parts[3])


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#File validation
filename = "orders_2026.csv"
if filename.endswith(".csv"):
    print("Process CSV file")
else:
    print('Not a CSV file')


filename = "orders_2026.json"
if filename.endswith(".csv"):
    print("Process CSV file")
else:
    print('Not a CSV file')


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

countries = [
    " germany ",
    "GERMANY",
    " Germany",
    "india ",
    " INDIA"
]

for i in countries:
    i=i.strip().title()
    print(i)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Create cleaned versions
customer_id = " CUST-00125 "
customer_name = "  JOHN SMITH  "
email = " JOHN.SMITH@GMAIL.COM "
country = " germany "
source_file = "customers_2026.csv"

customer_id=customer_id.strip()
customer_name=customer_name.strip().title()
email=email.strip().lower()
country= country.strip().title()

if(source_file.endswith('.csv')):
    print('process the file')
else:
    print("not a csv")

print(f'Customer {customer_id} | {customer_name}|{email} |{country}')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# <u>**LISTS**</u>

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

# MARKDOWN ********************

# # Transformation
# [expression for item in list]
# 
# # Transformation + filtering
# [expression for item in list if condition]

# CELL ********************

name = "  Sandya Duggana  "
name =name.strip()
print(name)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

country = "GERMANY"
country= country.lower()
print(country)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

country = "india"
country=country.upper()
print(country)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

text = "Data Engineering"
text=text.replace("Engineering","Science")
print(text)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

text = "Python,SQL,Power BI,Fabric"
text=text.split(',')
print(text)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

skills = ["Python", "SQL", "PySpark", "Fabric"]
result = " | ".join(skills)

print(result)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

email = "sandya.duggana@gmail.com"
email=email.split('@')
print(email)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

word = "Python"

print(word[0])
print(word[-1])
print(word[0:3])
print(word[-3:])

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

date = "2026-08-12"
date=date.split('-')
print(date[0])
print(date[1])
print(date[2])

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

countries = [
    " germany ",
    "GERMANY",
    " India ",
    "INDIA",
    " france "
]

cleaned_countries= [country.strip().lower() for country in countries]
print(cleaned_countries)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

names = [
    " john ",
    "ALICE",
    " Bob",
    "sarah "
]

cleaned_names= [name.strip().title() for name in names]
print(cleaned_names)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

emails = [
    "  JOHN@GMAIL.COM ",
    "alice@yahoo.com",
    " BOB@OUTLOOK.COM",
    "sarah@gmail.com "
]

emails_cleaned=[email.strip().lower() for email in emails]
print(emails_cleaned)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

raw_names = [
    "  john doe ",
    "ALICE SMITH",
    " bob   jones ",
    "Sarah Brown  "
]

cleaned_names = [" ".join(name.strip().lower().split()) for name in raw_names]
print(cleaned_names)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# interview Questions
# difference between strip and replace
# The main difference is:
# 
# strip() → removes characters from the beginning and end
# replace() → replaces specific characters/text wherever they occur
# 
# 
# Difference between split and join
# The easiest way to remember is:
# 
# split() → string → list
# join() → list → string
# split() breaks a string into a list.
# join() combines strings from a list into one string.
# 
# Why does this:text = "  Data Engineering  "
# text.strip()
# not permanently change text?
# 
# Because Python strings are immutable.
# 
# That means once a string is created, its contents cannot be changed. Methods like strip(), replace(), and lower() create and return a new string instead of modifying the original.
# 
# 
# What does this return?
# 
# "Python"[::-1]
# It returns the string in reverse order:
# 
# "Python"[::-1]
# 
# Output:
# 
# nohtyP
# Why?
# 
# [::-1] is Python slicing syntax:
# 
# [start : stop : step]
# 
# Here:
# 
# [::-1]
# 
# means:
# 
# start → omitted → start from the end when stepping backwards
# stop → omitted → go through the whole string
# step → -1 → move backwards one character at a time


# CELL ********************

customers = [
    {
        "name": "  JOHN DOE ",
        "email": " JOHN@GMAIL.COM ",
        "country": " GERMANY "
    },
    {
        "name": " alice smith",
        "email": "alice@YAHOO.COM",
        "country": "india"
    },
    {
        "name": "  Bob   Jones ",
        "email": " BOB@OUTLOOK.COM ",
        "country": " FRANCE "
    }
]


def clean_customers(cust):
    cust['name']=" ".join(cust['name'].strip().lower().split())
    cust['email']=cust['email'].lower().strip()
    cust['country']=cust['country'].lower().strip()
    return cust

cleaned_customers= [clean_customers(cust) for cust in customers]
print(cleaned_customers)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
