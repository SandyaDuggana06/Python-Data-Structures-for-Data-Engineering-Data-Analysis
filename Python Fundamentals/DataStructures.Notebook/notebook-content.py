# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

'''
Lists
append()
extend()
insert()
remove()
pop()
clear()
index()
count()
sort()
reverse()
Tuples
count()
index()


Sets
add()
update()
remove()
discard()
pop()
clear()


union()
intersection()
difference()
symmetric_difference()


Dictionaries
get()
keys()
values()
items()
pop()
popitem()
update()
clear()
setdefault()
'''


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 1**

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
'''
Lists add and remove elements
Print all customers.
Print the first and last customer.
Add "Michael".
Remove "John".
Count how many times "Anna" appears.
'''
customers = ["Anna", "Mark", "John", "Sarah", "Anna", "David"]
print(customers)
print(customers[0])
print(customers[-1])
customers.append('Michael')
customers.remove('John')
print(customers)
print(customers.count('Anna'))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 2**

# CELL ********************

'''
Print all product names.
Print all prices.
Calculate the total value.
Find the most expensive product.
Add "headphones": 150.

max(dictionary) → largest key
max(dictionary.values()) → largest value
max(dictionary, key=dictionary.get) → key with the largest value
max(dictionary.items(), key=lambda x: x[1]) → key-value pair with the largest value
'''
products = {
    "laptop": 1200,
    "mouse": 25,
    "keyboard": 80,
    "monitor": 300
}

print("products are  ",products)
print("dictinary keys ",products.keys())
print("dictinary values ",products.values())
products['headphones']=150
print("products are  ",products)
print("sum of products cost is  ",sum(products.values()))

item= max(products, key=products.get)
print("Costliest item ",item)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 3**

# CELL ********************

'''
Find all unique countries.
Count the unique countries.
Add "Netherlands".
Remove "Spain".
'''

countries = [
    "Germany", "France", "Germany",
    "Spain", "France", "Italy", "Germany"
]

unique_countries = set(countries)

print(unique_countries)

count_countries = len(unique_countries)
print(count_countries)

countries.append('Netherlands')
countries.remove('Spain')
print(countries)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 4**

# CELL ********************

'''
Print each employee's ID and name.
Find the employee with ID "E002".
Count employees.
Add a new employee.

'''

employees = [
    ("E001", "Anna", "Data Engineer"),
    ("E002", "Mark", "Developer"),
    ("E003", "John", "Data Analyst"),
]

# 1. Print each employee's ID and name
for employee_id,name, role in employees:
    print(employee_id,name)

# 2. Find employee with ID "E002"
for employee in employees:
    if employee[0] =='E002':
        print(employee)

# 3. Count employees
print(len(employees))

# 4. Add a new employee
employees.append(("E004", "Sarah", "Designer"))
print(employees)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 5**

# CELL ********************

'''

Calculate:

total
average
minimum
maximum
number of transactions above 300'''

transactions = [120, 450, 80, 1200, 50, 300]
print(sum(transactions))
print(sum(transactions)/len(transactions))
print(min(transactions))
print(max(transactions))
trans_above_300 = [trans for trans in transactions if trans >300]
print("transactions above 300 ",trans_above_300)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 6**

# CELL ********************

'''

Write a function:

get_customer_name(customer_id)

It should return the customer's name or "Unknown" if the ID doesn't exist.
'''

customers = {
    101: "Anna",
    102: "Mark",
    103: "John",
    104: "Sarah"
}

def get_customer_name(customer_id):
    if customer_id in customers:
        print('id exists')
        print(customers[customer_id])
    else:
        print('unknown')

get_customer_name(101)
get_customer_name(110)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 7**

# CELL ********************

'''
Create a new structure containing only unique order IDs.

Then preserve the original order.
list → set:   set(my_list)
set → list:   list(my_set)
'''
orders = [1001, 1002, 1001, 1003, 1004, 1002, 1005]
unique_orders= set(orders)
print(unique_orders)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 8**

# CELL ********************

'''
{
    "Electronics": ["Laptop", "Mouse", "Phone"],
    "Furniture": ["Desk", "Chair"]
}
'''

products = [
    ("Laptop", "Electronics"),
    ("Mouse", "Electronics"),
    ("Desk", "Furniture"),
    ("Chair", "Furniture"),
    ("Phone", "Electronics")
]

products_dict= dict(products)
print(products_dict)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 9**

# CELL ********************


'''
seperate them into valid_transactions
invalid_transactions
'''

transactions = [100, -50, 200, 0, 500, -20]

valid_transactions= [trans for trans in transactions if trans>0]
invalid_transactions= [trans for trans in transactions if trans<=0]
print(valid_transactions)
print(invalid_transactions)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 10**

# CELL ********************

'''Use a set to find unique email addresses.

Then determine how many duplicate emails existed.'''


emails = [
    "anna@example.com",
    "mark@example.com",
    "anna@example.com",
    "john@example.com",
    "mark@example.com"
]

emails_set=set(emails)
print(emails_set)
num_of_duplicates= len(emails)-len(emails_set)
print(num_of_duplicates)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 11**

# CELL ********************

'''Calculate total spending per customer for the below set
{
    "C001": 550,
    "C002": 300,
    "C003": 450
}
'''

orders = [
    ("O001", "C001", 250),
    ("O002", "C002", 100),
    ("O003", "C001", 300),
    ("O004", "C003", 450),
    ("O005", "C002", 200)
]

totals = {}

for order_id,customer_id,amount in orders:
    # get customer_id and amount
    
    if customer_id in totals:
        totals[customer_id]=totals[customer_id]+amount
    else:
        totals[customer_id] = amount

print(totals)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 12**

# CELL ********************

# Customer order count

#Using the same dataset, calculate the number of orders per customer.

orders = [
    ("O001", "C001", 250),
    ("O002", "C002", 100),
    ("O003", "C001", 300),
    ("O004", "C003", 450),
    ("O005", "C002", 200)
]

order_count={}
for order_id,customer_id,amount in orders:
    if customer_id in order_count:
        order_count[customer_id]+=1
    else:
        order_count[customer_id]=1

print(order_count)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 13**

# CELL ********************

'''
Highest-spending customer

Using the orders dataset:

calculate total spending per customer
identify the highest-spending customer
return both customer ID and amount
'''
orders = [
    ("O001", "C001", 250),
    ("O002", "C002", 100),
    ("O003", "C001", 300),
    ("O004", "C003", 450),
    ("O005", "C002", 200)
]


customer_spend ={}

for order_id,customer_id,amount in orders:
    if customer_id in customer_spend:
        customer_spend[customer_id]+=amount
    else:
        customer_spend[customer_id]=amount


print(customer_spend)


max_spend= max(customer_spend.items(), key=lambda x:x[1])
print("Customer who spent the most",max_spend)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 14**

# CELL ********************

'''Find:

products with inventory < 10
total inventory
product with highest inventory
product with lowest inventory


'''

inventory = {
    "laptop": 10,
    "mouse": 50,
    "keyboard": 20,
    "monitor": 5
}

prod_highest_inventory= max(inventory.items(), key=lambda x:x[1])
print(prod_highest_inventory)

prod_lowest_inventory= min(inventory.items(), key= lambda x:x[1])
print(prod_lowest_inventory)

sum_inventory=sum(inventory.values())
print(sum_inventory)

less_inventory=[key for key in inventory if inventory[key]<10]

print(less_inventory)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 15**

# CELL ********************

'''create {
    "Data": ["Anna", "John"],
    "Engineering": ["Mark", "David"],
    "HR": ["Sarah"]
}'''

employees = [
    ("E01", "Anna", "Data"),
    ("E02", "Mark", "Engineering"),
    ("E03", "John", "Data"),
    ("E04", "Sarah", "HR"),
    ("E05", "David", "Engineering")
]


dept_dict= {}

for emp_id, emp_name, emp_dept in employees:
    if(emp_dept not in dept_dict):
        dept_dict[emp_dept]=[]
  
    dept_dict[emp_dept].append(emp_name)


print(dept_dict)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 16**

# CELL ********************

'''Find:

customers in both systems
customers only online
customers only in stores
all customers

Operation	Symbol	Method
Union	|	.union()
Intersection	&	.intersection()
Difference	-	.difference()
Symmetric difference	^	.symmetric_difference()
Subset	<=	.issubset()
Superset	>=	.issuperset()
'''

online_customers = {"C001", "C002", "C003", "C005"}
store_customers = {"C002", "C003", "C004", "C006"}

customersinbothsystems =set(online_customers)& set(store_customers)
print(customersinbothsystems)

customersonlyonline =set(online_customers)- set(store_customers)
print(customersonlyonline)

customersonlyinstores =set(store_customers)& set(online_customers)
print(customersonlyinstores)

allcustomers =set(online_customers)| set(store_customers)
print(allcustomers)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 17**

# CELL ********************

''' Find:

records missing from B
records missing from A
records existing in both
total unique records'''
system_a = {1001, 1002, 1003, 1004, 1005}
system_b = {1002, 1003, 1004, 1006}
 
recordsmissinginB=system_a-system_b
recordsmissinginA=system_b-system_a
recordsexistinginboth= system_b&system_a
totaluniquerecords= system_b|system_a
print(recordsmissinginB)
print(recordsmissinginA)
print(recordsexistinginboth)
print(totaluniquerecords)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 18**

# CELL ********************

''' Identify duplicate customer IDs.

Then create a deduplicated list.'''

customers = [
    ("C001", "Anna"),
    ("C002", "Mark"),
    ("C001", "Anna"),
    ("C003", "John"),
    ("C002", "Mark")
]
seen = set()
duplicates = set()
deduplicated = []


for customer_id,name in customers:
    if customer_id in seen:
        duplicates.add(customer_id)
    else:
        seen.add(customer_id)
        deduplicated.append((customer_id, name))

print("Duplicate IDs:", duplicates)
print("Deduplicated:", deduplicated)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 19**

# CELL ********************

''' categorise <100       → small
100–499    → medium
500+       → large '''

transactions = [
    ("T001", 50),
    ("T002", 250),
    ("T003", 1000),
    ("T004", 25),
    ("T005", 700)
]
trans_dict={"small":[],
"medium":[],
"large":[]}

for trans_id, amount in transactions:
    if amount < 100:
        trans_dict['small' ].append(amount)
    elif amount>=100 and amount <=499:
        trans_dict['medium'].append(amount)
    else:
        trans_dict['large'].append(amount)

print(trans_dict)   



# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 20**

# CELL ********************

''' Customer 360 dictionary
 {
    "C001": {
        "name": "Anna",
        "country": "Germany"
    },
    ...
}'''

customers = [
    ("C001", "Anna", "Germany"),
    ("C002", "Mark", "France"),
    ("C003", "John", "Germany")
]

customer_360={}

for customer_id, customer_name , customer_country in customers:
    customer_360[customer_id]= {
        "name": customer_name,
        "country": customer_country
    }

print(customer_360)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 21**

# CELL ********************

''' Order/customer join using dictionaries Create enriched orders:
[
    ("O001", "Anna", 500),
    ("O002", "Mark", 200),
    ("O003", "Anna", 300),
    ("O004", "UNKNOWN", 100)
] '''
customers = {
    "C001": "Anna",
    "C002": "Mark",
    "C003": "John"
}
orders = [
    ("O001", "C001", 500),
    ("O002", "C002", 200),
    ("O003", "C001", 300),
    ("O004", "C999", 100)
]


enriched_orders=[]

for order_id,customer_id,amount in orders:
    customer= customers.get(customer_id,"unknown")
    enriched_order = {
    "order_id": order_id,
    "customer_id": customer_id,
    "name": customer,
    "amount": amount}
    enriched_orders.append(enriched_order)

print(enriched_orders)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 22**

# CELL ********************

'''
Build a data-quality report showing:

missing IDs
missing names
duplicate IDs
valid records
invalid records
'''

customers = [
    {"id": "C001", "name": "Anna"},
    {"id": "C002", "name": None},
    {"id": None, "name": "John"},
    {"id": "C002", "name": "Mark"},
    {"id": "C004", "name": "Sarah"}
]

invalid_cust=[]
for customer in customers:
    if(customer["id"] is None or customer["name"] is None):
        invalid_cust.append(customer)
print("invalid customers are ", invalid_cust)

missing_ids=[]
for customer in customers:
    if customer["id"] is None:
        missing_ids.append(customer)
print("customers with missing ids",missing_ids)

missing_names = []
for customer in customers:
    if customer["name"] is None:
        missing_names.append(customer)
print("customers with missing names",missing_names)

seen = set()
duplicates = set()

for customer in customers:
    customer_id = customer["id"]

    if customer_id in seen:
        duplicates.add(customer_id)
    else:
        seen.add(customer_id)


print("customers which are not duplicates ",seen)
print("customers which are duplicate ", duplicates)

valid_records=[]

for customer in customers:
    if customer["id"] is not None and customer["name"] is not None:
        valid_records.append(customer)

print("valid customers are  ",valid_records)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 23**

# CELL ********************

'''
Deduplicate using email as the business key.

Keep the latest record.

'''
customers = [
    {"id": 1, "email": "a@test.com", "name": "Anna"},
    {"id": 2, "email": "b@test.com", "name": "Mark"},
    {"id": 3, "email": "a@test.com", "name": "Anna Updated"}
]

deduplicated = {}

for customer in customers:
    email = customer["email"]
    deduplicated[email] = customer

print(deduplicated)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 24**

# CELL ********************

''' calculate product
total_quantity
total_revenue'''

sales = [
    ("Laptop", 2, 1200),
    ("Mouse", 10, 25),
    ("Laptop", 1, 1200),
    ("Keyboard", 5, 80),
    ("Mouse", 3, 25)
]

product_sales={}

for product, quantity,price in sales:
    if product not in product_sales:
        product_sales[product]={
            "total_quantity":0,
            "total_revenue":0
        }
        
        product_sales[product]["total_quantity"]+=quantity
        product_sales[product]["total_revenue"]+=quantity*price

print(product_sales)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 25**

# CELL ********************

''' Calculate average salary by department.

Then identify the highest-paid employee in each department.'''

employees = [
    {"id": "E01", "name": "Anna", "department": "Data", "salary": 70000},
    {"id": "E02", "name": "Mark", "department": "Data", "salary": 80000},
    {"id": "E03", "name": "John", "department": "HR", "salary": 60000},
    {"id": "E04", "name": "Sarah", "department": "HR", "salary": 65000},
]

salary_total={}
employee_count={}
average_salary={}

for employee in employees:
    department=employee['department']
    salary=employee['salary']
    if department not in salary_total:
        salary_total[department]=salary
        employee_count[department]=1
    else:
        salary_total[department]=salary_total[department]+salary
        employee_count[department]=employee_count[department]+1
    
for department in salary_total:
    average_salary[department]=salary_total[department]/employee_count[department]

print("average salary in department",average_salary)

highest_paid={}



for employee in employees:
    department=employee['department']
    salary= employee['salary']
    employee_id= employee['id']
    name=employee['name']
    if department not in highest_paid:
        
        highest_paid[department]={
            "id":employee_id,
            "name":name,
            "salary":salary

        }
        
    elif salary > highest_paid[department]['salary']:
        highest_paid[department]={
             "id":employee_id,
            "name":name,
            "salary":salary

        }
    
      
print("highest paid employees are " ,highest_paid)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 26**

# CELL ********************

#Multi-source reconciliation
'''  Determine:
customers in all three
customers in exactly two
customers appearing in only one system
master customer set '''

crm = {"C001", "C002", "C003", "C004"}
erp = {"C002", "C003", "C005"}
website = {"C001", "C003", "C006"}

all_three = crm & erp & website

exactly_two = (
    (crm & erp) |
    (crm & website) |
    (erp & website)
) - all_three

print(all_three)
print(exactly_two)

master = crm | erp | website
only_one = master - (
    (crm & erp) |
    (crm & website) |
    (erp & website)
)

print(only_one)

print(master)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 27**
# **The pattern to remember ⭐
# When you want a dictionary of lists:
# data = {}
# 
# if key not in data:
#     data[key] = []
# 
# data[key].append(value)
# **

# CELL ********************

''' Transaction fraud detection
Flag transactions where:
amount > 1000
then produce
{
    customer_id: {
        "total_transactions": ...,
        "total_amount": ...,
        "fraud_count": ...
    }
}
'''
transactions = [
    {"customer": "C001", "amount": 100},
    {"customer": "C001", "amount": 150},
    {"customer": "C001", "amount": 5000},
    {"customer": "C002", "amount": 200},
    {"customer": "C002", "amount": 7000}
]

fraud_transactions={}
for transaction in transactions:
    customer= transaction['customer']
    amount= transaction['amount']
    if amount >1000:
        if customer not in fraud_transactions:
            fraud_transactions[customer]=[]
        fraud_transactions[customer].append(transaction)          
print("fraud transactions are ",fraud_transactions)

customer_report={}

for transaction in transactions:
    customer= transaction['customer']
    amount=transaction['amount']
    if customer not in customer_report:
        customer_report[customer]={
            "total_transactions":0,
            "total_amount":0,
            "fraud_count":0
        }
    
    customer_report[customer]["total_transactions"]=customer_report[customer]['total_transactions']+1
    customer_report[customer]["total_amount"]=customer_report[customer]['total_amount']+amount
    if amount > 1000:
            customer_report[customer]["fraud_count"] += 1

print(customer_report)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 28**

# CELL ********************

'''Build a mini ETL pipeline
Extract
   ↓
Validate
   ↓
Deduplicate
   ↓
Transform
   ↓
Load
remove duplicates
reject negative amounts
calculate a 19% VAT field
produce clean records
produce rejected records
'''
orders = [
    {"id": 1, "customer": "C001", "amount": 100},
    {"id": 2, "customer": "C002", "amount": -50},
    {"id": 3, "customer": "C001", "amount": 300},
    {"id": 2, "customer": "C002", "amount": -50}
]

reject=[]
valid=[]

for order in orders:
    id=order['id']
    customer=order['customer']
    amount=order['amount']
    
    if amount<0:
        reject.append(order)
    else:
        valid.append(order)


#Deduplicate

seen=set()
clean_records=[]

for order in valid:
    if order['id'] not in seen:
        seen.add(order['id'])
        clean_records.append(order)
    

for order in clean_records:
    order["VAT"] = order["amount"] * 0.19

print("Clean records:", clean_records)
print("Rejected records:", reject)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 29**

# CELL ********************

''' Incremental processing
Identify only new records.

Then extend the processed ID set.

Think about why a set is better than a list for this operation.

incremental data processing / ETL pipelines
new = set(incoming) - processed
processed.update(new)'''


processed_ids = {1001, 1002, 1003}

incoming_ids = [1002, 1003, 1004, 1005, 1006]

new_ids=set(incoming_ids)-processed_ids
print("new ids are ",new_ids)

processed_ids.update(new_ids)
print("processed ids are ", processed_ids)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 30**

# CELL ********************

''' Combine columns
columns = ["id", "name", "department"]
values = [101, "Anna", "Data"]

Create:
{ "id": 101, "name": "Anna", "department": "Data" }
zip() in Python is used to combine two or more lists (or other iterables) element-by-element.'''

columns = ["id", "name", "department"]
values = [101, "Anna", "Data"]
result=zip(columns,values)
print(list(result))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 31**

# CELL ********************

'''Create employee records


Create:

[
    {"name": "Anna", "department": "Data", "salary": 70000},
    ...
]

Use zip().'''


names = ["Anna", "Mark", "John", "Sarah"]
departments = ["Data", "Engineering", "HR", "Data"]
salaries = [70000, 80000, 60000, 75000]

employees=[]



for name, department,salary in zip(names,departments,salaries):
    employees.append({
        'name':name,
        'department':department,
        'salary':salary
    })

print(employees)  



# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 33**

# CELL ********************

'''Compare 2 datasets
Using zip():

compare corresponding values
identify changed values
calculate the difference '''


system_a = [100, 200, 300, 400] 
system_b = [100, 250, 300, 450]

print(list(zip(system_a, system_b)))

for a,b in zip(system_a, system_b):
    if a==b:
        print("no change in value",a,b)
    else:
        print("change in value",a,b)
        print("difference is ",abs(a - b))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 34**

# CELL ********************

''' Detect mismatched records
ids = [101, 102, 103, 104]
names = ["Anna", "Mark", "John", "Sarah"]
departments = ["Data", "Data", "HR", "Engineering"]

Create records and then find employees belonging to the "Data" department.'''

ids = [101, 102, 103, 104]
names = ["Anna", "Mark", "John", "Sarah"]
departments = ["Data", "Data", "HR", "Engineering"]
employees=[]
for id,name, department in zip(ids,names,departments):
    employees.append({
        'id':id,
        'name':name,
        'department':department
    })

print("All employees are ",employees)

data_employees=[]

for employee in employees:
    if employee['department']=='Data':
        data_employees.append(employee)

print("Data employees are ",data_employees)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 35**

# CELL ********************

''' Add row numbers
transactions = [100, 250, 500, 750]

Produce:

1: 100
2: 250
3: 500
4: 750 '''

transactions = [100, 250, 500, 750]
for i,amount in enumerate(transactions,1):
    print(i,amount)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 36**

# CELL ********************

'''Find invalid records with row numbers
transactions = [100, -50, 200, -10, 500]

Return:

row 2 → -50
row 4 → -10'''

transactions = [100, -50, 200, -10, 500]

for i,amount in enumerate(transactions,1):
    if amount <0:
        print(i, amount)



# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 37**

# CELL ********************

'''  records = [
    {"id": "C001", "name": "Anna"},
    {"id": "C002", "name": "Mark"},
    {"id": "C003", "name": "John"}
]

Add:

"source_row": 1

to the first record, 2 to the second, etc.'''
records = [
    {"id": "C001", "name": "Anna"},
    {"id": "C002", "name": "Mark"},
    {"id": "C003", "name": "John"}
]

for i, record in enumerate(records,start=1):
    record["source_row"] = i

print(records)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 38**

# CELL ********************

'''  Filter valid transactions
amounts = [100, -20, 300, 0, 500, -50]

Create a list containing only positive amounts.'''


amounts = [100, -20, 300, 0, 500, -50]

valid_transactions = [amount for amount in amounts if amount>0]
print(valid_transactions)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 39**

# CELL ********************

''' Transform amounts

Convert:

amounts = [100, 200, 300]

into amounts including 19% VAT.

Expected:

119
238
357'''

amounts = [100, 200, 300]
vat_included =[amount+amount*.19 for amount in amounts]
print(vat_included)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 40**

# CELL ********************

''' amounts = [50, 150, 300, 700, 1000]

Return the amounts greater than 200 after adding 19% VAT.'''
amounts = [50, 150, 300, 700, 1000]
new_amounts = [amount+amount*.19 for amount in amounts]
print(new_amounts)

new_valid_amounts = [amount for amount in new_amounts if amount > 200]
print(new_valid_amounts)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 41**

# CELL ********************

''' Clean strings 
countries = [
    " germany ",
    "INDIA",
    " France ",
    "germany"
]

Create:

["Germany", "India", "France", "Germany"]

Use a list comprehension.'''

countries = [
    " germany ",
    "INDIA",
    " France ",
    "germany"
]
clean_countries = [country.title() for country in countries]
print(clean_countries)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 42**

# CELL ********************

''' Extract dictionary values
transactions = [
    {"id": 1, "amount": 100},
    {"id": 2, "amount": 250},
    {"id": 3, "amount": 500}
]

Create a list containing only the amounts.
Pattern to remember ⭐

For a list of dictionaries, to extract one field:

[field["key"] for field in list]
'''

transactions = [
    {"id": 1, "amount": 100},
    {"id": 2, "amount": 250},
    {"id": 3, "amount": 500}
]
amount_list=[]
for transaction in transactions:
    amount=transaction['amount']
    amount_list.append(amount)

print(amount_list)

# list comprehension
amount_list = [transaction["amount"] for transaction in transactions]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 43**

# CELL ********************

''' Flatten a list
data = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8]
]

Produce:

[1, 2, 3, 4, 5, 6, 7, 8]'''

data = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8]
]

flatten_list=[]

for l in data:
    for num in l:
        flatten_list.append(num)

print(flatten_list)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 44**

# CELL ********************

'''Flatten transaction batches
batches = [
    [{"id": 1}, {"id": 2}],
    [{"id": 3}, {"id": 4}],
    [{"id": 5}]
]

Create one flat list containing all records.'''


batches = [
    [{"id": 1}, {"id": 2}],
    [{"id": 3}, {"id": 4}],
    [{"id": 5}]
]

flatten_list=[]
for batch in batches:
    for nested_batch in batch:
        flatten_list.append(nested_batch)

print(flatten_list)

result ={'id':[]}
for output in flatten_list:
    result['id'].append(output['id'])

print(result)
#flatten_list = [record for batch in batches for record in batch]


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 45**

# CELL ********************

''' Extract nested values
customers = [
    {
        "id": "C001",
        "orders": [
            {"id": "O001", "amount": 100},
            {"id": "O002", "amount": 200}
        ]
    },
    {
        "id": "C002",
        "orders": [
            {"id": "O003", "amount": 500}
        ]
    }
]

Create a list of all order amounts.

Expected:

[100, 200, 500] '''

customers = [
    {
        "id": "C001",
        "orders": [
            {"id": "O001", "amount": 100},
            {"id": "O002", "amount": 200}
        ]
    },
    {
        "id": "C002",
        "orders": [
            {"id": "O003", "amount": 500}
        ]
    }
]

amount=[]
for customer in customers:
    order_dict=customer['orders']
    for each in order_dict:
        amount.append(each['amount'])

print(amount)

''' amount = [
    order["amount"]
    for customer in customers
    for order in customer["orders"]
] '''

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 46**

# CELL ********************

'''  Create price lookup
products = [
    ("Laptop", 1200),
    ("Mouse", 25),
    ("Keyboard", 80)
]

Create:

{
    "Laptop": 1200,
    "Mouse": 25,
    "Keyboard": 80
}

Use a dictionary comprehension.'''

products = [
    ("Laptop", 1200),
    ("Mouse", 25),
    ("Keyboard", 80)
]

dict={}

for product, price in products:
    dict[product]= price

print(dict)

# dictionary comprehension version is {key: value for item in iterable}

price_lookup = {
    product: price
    for product, price in products
}

print(price_lookup)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 47**

# CELL ********************

'''Filter dictionary
prices = {
    "Laptop": 1200,
    "Mouse": 25,
    "Keyboard": 80,
    "Monitor": 300
}

Create a dictionary containing only products costing more than 100.

{key: value for key, value in dictionary.items() if condition}'''

prices = {
    "Laptop": 1200,
    "Mouse": 25,
    "Keyboard": 80,
    "Monitor": 300
}


updated_products={}

for product,price in prices.items():
    if(price>100):
        updated_products[product]=price

print(updated_products)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 48**

# CELL ********************

'''Transform dictionary values

Increase every price by 10%. 
pattern to remember
{
    key: transformed_value
    for key, value in dictionary.items()
}'''

prices = {
    "Laptop": 1200,
    "Mouse": 25,
    "Keyboard": 80,
    "Monitor": 300
}


updated_prices ={ product:price+price*.10 for product, price in prices.items()}

print(updated_prices)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 49**

# CELL ********************

'''Reverse a dictionary
departments = {
    "E01": "Data",
    "E02": "HR",
    "E03": "Engineering"
}

Create:

{
    "Data": "E01",
    "HR": "E02",
    "Engineering": "E03"
}'''

departments = {
    "E01": "Data",
    "E02": "HR",
    "E03": "Engineering"
}

reverse_departments={ dept:emp for emp,dept in departments.items()}
print(reverse_departments)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 50**

# CELL ********************

'''Check for invalid data
amounts = [100, 200, -50, 300]

Use any() to determine whether at least one amount is invalid.'''

amounts = [100, 200, -50, 300]

valid_amounts=any([num<0 for num in amounts])
print(valid_amounts)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 51**

# CELL ********************

''' Validate all records
amounts = [100, 200, 300, 500]

Use all() to determine whether every amount is positive.'''

amounts = [100, 200, 300, 500]
valid_amounts=all([num>0 for num in amounts])
print(valid_amounts)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 52**

# CELL ********************

''' Data-quality validation
records = [
    {"id": "C001", "amount": 100},
    {"id": "C002", "amount": 200},
    {"id": None, "amount": 300}
]

Use any() to determine whether any record has a missing ID.

Use all() to determine whether every record has a valid ID. '''

records = [
    {"id": "C001", "amount": 100},
    {"id": "C002", "amount": 200},
    {"id": None, "amount": 300}
]


valid= any(record['id'] is None for record in records)
print(valid)

valid_all=all(record['id'] is not None for record in records)
print(valid_all)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 53**

# CELL ********************

'''Sort transactions
transactions = [
    {"id": 1, "amount": 500},
    {"id": 2, "amount": 100},
    {"id": 3, "amount": 750}
]

Sort by amount ascending.

Then sort descending.

Pattern to memorize

For dictionaries:

sorted(
    data,
    key=lambda x: x["field"]
)

For tuples:

sorted(
    data,
    key=lambda x: x[1]
)

And descending:

sorted(
    data,
    key=lambda x: x["field"],
    reverse=True
)

The key idea is:

sorted() = sort
key= = what should I sort by?
lambda = a quick function telling Python what that value is
'''
transactions = [
    {"id": 1, "amount": 500},
    {"id": 2, "amount": 100},
    {"id": 3, "amount": 750}
]
result= sorted(transactions, key= lambda trans:trans['amount'])
print(result)

desc_result= sorted(transactions, key= lambda trans:trans['amount'], reverse= True)
print(desc_result)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 54**

# CELL ********************

#Sort employees by salary and identify the highest-paid employee.
employees = [
    {"name": "Anna", "salary": 70000},
    {"name": "Mark", "salary": 85000},
    {"name": "John", "salary": 60000}
]

result= sorted(employees, key= lambda emp:emp['salary'], reverse=True)

print(result)

print("highest paid employee is ", result[0]['name'])

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 55**

# CELL ********************

''' 
Sort by:

department
salary descending'''

employees = [
    {"name": "Anna", "department": "Data", "salary": 70000},
    {"name": "Mark", "department": "Engineering", "salary": 80000},
    {"name": "John", "department": "Data", "salary": 85000},
    {"name": "Sarah", "department": "Data", "salary": 65000}
]

sort = sorted(employees, key= lambda emp:(-emp['salary'],emp['department']), reverse= True)
print(sort)



# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 56**

# CELL ********************

'''
Tuple unpacking
employee = ("E001", "Anna", "Data", 70000)

Unpack into:

employee_id
name
department
salary
'''
employee = ("E001", "Anna", "Data", 70000)
employee_id, name, department, salary = employee
print(employee_id)
print(name)
print(department)
print(salary)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 57**

# CELL ********************

''' columns = ["id", "name", "department", "salary", "country"]

Unpack into:

first
second
*remaining

Determine the result.'''
columns = ["id", "name", "department", "salary", "country"]
first,second,*remaining =columns
print(first)
print(second)
print(remaining)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 58**

# CELL ********************

#Create one dictionary containing all fields using **.

customer = {
    "id": "C001",
    "name": "Anna"
}

location = {
    "country": "Germany"
}

all_info={**customer,**location}
print(all_info)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 59**

# CELL ********************

''' 

The four structures you should recognize
List of dictionaries
[
    {"id": 1},
    {"id": 2}
]

Usually processed with:

for record in records:
Dictionary of dictionaries
{
    "C001": {"name": "Anna"},
    "C002": {"name": "Mark"}
}

Usually processed with:

for key, value in data.items():
Dictionary containing a list
{
    "orders": [100, 200, 300]
}

Access:

data["orders"]
Dictionary → list → dictionary
{
    "orders": [
        {"id": 1, "amount": 100},
        {"id": 2, "amount": 200}
    ]
}

Loop:

for order in data["orders"]:
    print(order["amount"])
🧠 The main skill

When working with nested data, always ask:

"What type am I looking at right now?"

For example:

customers[0]["orders"][1]["amount"]
customers          → list
customers[0]       → dictionary
["orders"]         → list
[1]                → dictionary
["amount"]         → number

Once you can identify the type at each level, nested data becomes much easier to work with.

Pattern to remember

For nested customer → orders → amount:

customer_id: sum(order["amount"] for order in customer["orders"])

This is a very useful pattern for calculating total spending/revenue per customer.

Find:

all customer names
all order IDs
all order amounts
total revenue
total revenue per customer
highest-value order'''


customers = {
    "C001": {
        "name": "Anna",
        "country": "Germany",
        "orders": [
            {"id": "O001", "amount": 200},
            {"id": "O002", "amount": 300}
        ]
    },
    "C002": {
        "name": "Mark",
        "country": "France",
        "orders": [
            {"id": "O003", "amount": 500}
        ]
    }
}


customer_names=[value['name'] for key,value in customers.items()]

print("Customer names are ",customer_names)

order_ids=[
    order["id"]
    for customer in customers.values()
    for order in customer["orders"]
]

print("order ids are ",order_ids)


order_amounts=[order['amount']
for customer in customers.values()
for order in customer['orders']]

print("order amounts are ",order_amounts)

order_total= sum(order_amounts)
print("order total is ",order_total)


total_revenue_per_cust={}

for customer_id, customer in customers.items():
    total=0

    for order in customer['orders']:
        total= order['amount']+total
    total_revenue_per_cust[customer_id]=total

print(total_revenue_per_cust)

all_orders=[]

for customer in customers.values():
    for orders in customer['orders']:
        all_orders.append(orders)

highest_order=max(all_orders, key= lambda order:order['amount'])

print("highest order is ", highest_order)

#highest_value_order=max()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 60**

# CELL ********************

'''  customers without orders
orders with amount <= 0
customers with total spending > 400'''

customers = {
    "C001": {
        "name": "Anna",
        "country": "Germany",
        "orders": [
            {"id": "O001", "amount": 200},
            {"id": "O002", "amount": 300}
        ]
    },
    "C002": {
        "name": "Mark",
        "country": "France",
        "orders": [
            {"id": "O003", "amount": 500}
        ]
    }
}


for customer_id,customer in customers.items():
    if not customer['orders']:
        print("customer without orders", customer_id)
    else:
        print("customer with orders ", customer_id)

for customer_id,customer in customers.items():
    for order in customer['orders']:
        if order['amount']<=0:
            print("order with 0 amount", order)
        else:
            print(f"order amount is {order['amount']} for {order['id']}")
#total=0
cust={}
for customer_id, customer in customers.items():
    total=0
    for order in customer['orders']:
        total=order['amount']+total
    cust[customer_id]=total

print(cust)

cust_spending=[key for key,value in cust.items() if value >400]
print(cust_spending)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 61**

# CELL ********************

'''Transaction cleaner

Write:

def clean_transaction(transaction):
    ...

Input:

{
    "id": "101",
    "amount": "250.50"
}

Return:

{
    "id": 101,
    "amount": 250.50
}'''

transaction={
    "id": "101",
    "amount": "250.50"
}

def clean_transaction(transaction):
        clean_trans={     "id":int(transaction['id']),
                        "amount":float(transaction['amount'])}
        return clean_trans
clean_transaction(transaction)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 62**

# CELL ********************

'''
Create:

def convert_amount(value):
    ...

Rules:

valid number → return float
invalid value → return None

Test:

"100"
"250.50"
"invalid"
"300"
'''

def convert_amount(value):
    try:
        return float(value)
    except(ValueError):
        return None

print(convert_amount("100"))
print(convert_amount("250.50"))
print(convert_amount("invalid"))
print(convert_amount("300"))


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Excercise 63**

# CELL ********************

''' 
def is_valid_transaction(transaction):
    ...

A transaction is valid when:

ID exists
amount exists
amount > 0

Return True or False.'''

def is_valid_transaction(transaction):
    if (
        transaction.get("id") is not None
        and transaction.get("amount") is not None
        and transaction["amount"] > 0
    ):
        return True
    return False

print(is_valid_transaction({"id": 101, "amount": 250}))


print(is_valid_transaction({"id": None, "amount": 250}))


print(is_valid_transaction({"id": 101, "amount": 0}))


print(is_valid_transaction({"id": 101, "amount": -50}))


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Excercise 64**

# CELL ********************

''' Raw transaction cleaning
transactions = [
    {"id": "101", "amount": "100.50"},
    {"id": "102", "amount": "invalid"},
    {"id": "103", "amount": "250"},
    {"id": "104", "amount": None}
]

Produce:

valid_records = [...]
invalid_records = [...]

Use try/except.'''

transactions = [
    {"id": "101", "amount": "100.50"},
    {"id": "102", "amount": "invalid"},
    {"id": "103", "amount": "250"},
    {"id": "104", "amount": None}
]
valid_records=[]
invalid_records=[]
for transaction in transactions:
    try:
        transaction['amount']=float(transaction['amount'])
        valid_records.append(transaction)
    except(ValueError,TypeError):
        invalid_records.append(transaction)

print("valid records are ", valid_records)
print("invalid records are ",invalid_records)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 65**

# CELL ********************


'''
Convert:

ID → int
amount → float
quantity → int

Invalid records should be rejected. '''

records = [
    {"id": "1", "amount": "100", "quantity": "2"},
    {"id": "2", "amount": "invalid", "quantity": "3"},
    {"id": "3", "amount": "250", "quantity": "invalid"}
]
valid_records = []
invalid_records = []

for record in records:
    try:
        record['id']=int(record['id'])
        record['amount']=float(record['amount'])
        record['quantity']=int(record['quantity'])
        valid_records.append(record)
    except(ValueError,TypeError):
        invalid_records.append(record)

print(valid_records)
print(invalid_records)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Excercise 66**

# CELL ********************

''' Build a lookup
customers = [
    {"id": "C001", "name": "Anna"},
    {"id": "C002", "name": "Mark"},
    {"id": "C003", "name": "John"}
]

Transform into:

{
    "C001": "Anna",
    "C002": "Mark",
    "C003": "John"
}

Then use the dictionary to enrich:

orders = [
    {"id": "O001", "customer_id": "C001", "amount": 500},
    {"id": "O002", "customer_id": "C999", "amount": 100}
]

Unknown customers should become "UNKNOWN". ''' 


customers = [
    {"id": "C001", "name": "Anna"},
    {"id": "C002", "name": "Mark"},
    {"id": "C003", "name": "John"}
]

orders = [
    {"id": "O001", "customer_id": "C001", "amount": 500},
    {"id": "O002", "customer_id": "C999", "amount": 100}
]


customer_lookup={}

for customer in customers:
    customer_lookup[customer['id']]=customer['name']

print(customer_lookup)

enriched_orders = []

for order in orders:
    customer_id=order['customer_id']
    enriched_order={
        "id": order["id"],
        "customer_id": customer_id,
        "customer_name": customer_lookup.get(customer_id, "UNKNOWN"),
        "amount": order["amount"]
    }
    
    enriched_orders.append(enriched_order)

print(enriched_orders)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Excercise 67**

# CELL ********************

''' transactions = [
    {"customer": "C001", "amount": 100},
    {"customer": "C002", "amount": 200},
    {"customer": "C001", "amount": 300},
    {"customer": "C002", "amount": 400},
    {"customer": "C003", "amount": 500}
]

Create:

{
    "C001": [100, 300],
    "C002": [200, 400],
    "C003": [500]
}

Then calculate total amount per customer.'''

transactions = [
    {"customer": "C001", "amount": 100},
    {"customer": "C002", "amount": 200},
    {"customer": "C001", "amount": 300},
    {"customer": "C002", "amount": 400},
    {"customer": "C003", "amount": 500}
]

cust_amount={}

for trans in transactions:
    customer=trans['customer']
    amount=trans['amount']
    if customer not in cust_amount:
        cust_amount[customer]=[]
    cust_amount[customer].append(amount)

print(cust_amount)

total={}

for customer, amounts in cust_amount.items():
    total[customer] = sum(amounts)

print(total)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 68**

# CELL ********************

''' source_a = [
    {"id": 1, "amount": 100},
    {"id": 2, "amount": 200},
    {"id": 3, "amount": 300}
]

source_b = [
    {"id": 1, "amount": 100},
    {"id": 2, "amount": 250},
    {"id": 4, "amount": 400}
]

Find:

records present in both
records missing from B
records missing from A
records whose amount changed'''

source_a = [
    {"id": 1, "amount": 100},
    {"id": 2, "amount": 200},
    {"id": 3, "amount": 300}
]

source_b = [
    {"id": 1, "amount": 100},
    {"id": 2, "amount": 250},
    {"id": 4, "amount": 400}
]

a_lookup = {record["id"]: record for record in source_a}
b_lookup = {record["id"]: record for record in source_b}

print("a lookup is ",a_lookup)
print("b lookup is ",b_lookup)

both = set(a_lookup) & set(b_lookup)
print("records present in both ", both)

missing_from_b = set(a_lookup) - set(b_lookup)
print("records missing from b ", missing_from_b)

missing_from_a = set(b_lookup) - set(a_lookup)
print("records missing from a ", missing_from_a)


changed = []

for record_id in set(a_lookup) & set(b_lookup):
    if a_lookup[record_id]["amount"] != b_lookup[record_id]["amount"]:
        changed.append(record_id)

print(changed)



# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Excercise 69**

# CELL ********************

''' processed_ids = {1, 2, 3, 4}

incoming_records = [
    {"id": 3, "amount": 100},
    {"id": 4, "amount": 200},
    {"id": 5, "amount": 300},
    {"id": 6, "amount": 400}
]

Return only new records.

Then update processed_ids.'''
processed_ids = {1, 2, 3, 4}
incoming_records = [
    {"id": 3, "amount": 100},
    {"id": 4, "amount": 200},
    {"id": 5, "amount": 300},
    {"id": 6, "amount": 400}
]
lookup = {record["id"]: record for record in incoming_records}
print(lookup)

new_records=[]

for record in incoming_records:
    if record["id"] not in processed_ids:
        new_records.append(record)

print(new_records)

for record in new_records:
    processed_ids.add(record["id"])

print("Updated processed IDs:")
print(processed_ids)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Excercise 70**

# CELL ********************

'''Input:

orders = [
    {"id": 1, "customer": "C001", "amount": "100"},
    {"id": 2, "customer": "C002", "amount": "-50"},
    {"id": 3, "customer": "C001", "amount": "300"},
    {"id": 2, "customer": "C002", "amount": "-50"},
    {"id": 4, "customer": "C003", "amount": "invalid"}
]

Build:

Extract
   ↓
Validate
   ↓
Deduplicate
   ↓
Transform
   ↓
Aggregate

Produce:

{
    "input_records": ...,
    "valid_records": ...,
    "invalid_records": ...,
    "duplicate_records": ...,
    "total_revenue": ...,
    "unique_customers": ...,
    "revenue_by_customer": ...
}

Constraint:

Use only Python built-in data structures.'''

orders = [
    {"id": 1, "customer": "C001", "amount": "100"},
    {"id": 2, "customer": "C002", "amount": "-50"},
    {"id": 3, "customer": "C001", "amount": "300"},
    {"id": 2, "customer": "C002", "amount": "-50"},
    {"id": 4, "customer": "C003", "amount": "invalid"}
]


# -------------------------
# Extract
# -------------------------

input_records = len(orders)


# -------------------------
# Validate
# -------------------------

valid_records = []
invalid_records = []

for order in orders:
    try:
        amount = float(order["amount"])

        if amount <= 0:
            invalid_records.append(order)
        else:
            valid_records.append(order)

    except (ValueError, TypeError):
        invalid_records.append(order)


# -------------------------
# Deduplicate
# -------------------------

seen_ids = set()
deduplicated_records = []
duplicate_records = []

for order in valid_records:

    if order["id"] in seen_ids:
        duplicate_records.append(order)
    else:
        seen_ids.add(order["id"])
        deduplicated_records.append(order)


# -------------------------
# Transform
# -------------------------

clean_records = []

for order in deduplicated_records:
    clean_order = {
        "id": int(order["id"]),
        "customer": order["customer"],
        "amount": float(order["amount"])
    }

    clean_records.append(clean_order)


# -------------------------
# Aggregate
# -------------------------

total_revenue = 0
unique_customers = set()
revenue_by_customer = {}

for order in clean_records:

    customer = order["customer"]
    amount = order["amount"]

    total_revenue += amount

    unique_customers.add(customer)

    if customer not in revenue_by_customer:
        revenue_by_customer[customer] = 0

    revenue_by_customer[customer] += amount


# -------------------------
# Final report
# -------------------------

report = {
    "input_records": input_records,
    "valid_records": len(valid_records),
    "invalid_records": len(invalid_records),
    "duplicate_records": len(duplicate_records),
    "total_revenue": total_revenue,
    "unique_customers": len(unique_customers),
    "revenue_by_customer": revenue_by_customer
}

print(report)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
