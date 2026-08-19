# Python Data Structures for Data Engineering & Data Analysis

A practical, pattern-focused guide to Python's built-in data structures for **Data Engineering and Data Analysis**.

This notebook contains 70 hands-on exercises covering four interconnected areas: Python Data Structures, Python Patterns, Nested Data & JSON-style structures, and Functions & Error Handling.

The focus is not simply on learning Python syntax.

The goal is to learn how to answer:

> **"Given this data problem, which Python data structure or pattern should I use?"**

---

## 🎯 What This Repository Covers

This repository covers the core Python data-structure patterns needed before moving deeper into tools such as:

* Pandas
* PySpark
* SQL
* Data pipelines
* ETL/ELT
* Data quality frameworks
* APIs and JSON
* Data processing systems

### Core Python Data Structures

* Lists
* Tuples
* Sets
* Dictionaries
* Nested lists
* Nested dictionaries
* Lists of dictionaries
* Dictionaries containing lists
* Dictionaries containing dictionaries

### Core Python Patterns

* Indexing
* Slicing
* Iteration
* `enumerate()`
* `zip()`
* Tuple/list unpacking
* `*args` / `**kwargs` style unpacking
* List comprehensions
* Dictionary comprehensions
* Nested comprehensions
* `sorted()`
* `min()`
* `max()`
* `any()`
* `all()`
* `lambda`
* Functions
* `try/except`

### Data Engineering Patterns

* Filtering
* Transformation
* Aggregation
* Grouping
* Lookup
* Joining/enrichment
* Deduplication
* Business-key deduplication
* Data validation
* Data-quality checks
* Data reconciliation
* Incremental processing
* Nested-data processing
* ETL processing

---

# 📚 Why Data Structures Matter in Data Engineering

Before using Pandas, PySpark or other data-processing frameworks, it is important to understand how data is represented and manipulated in Python.

A typical data pipeline may involve:

```text
Raw Data
   ↓
Python objects
   ↓
Validation
   ↓
Cleaning
   ↓
Deduplication
   ↓
Transformation
   ↓
Enrichment / Join
   ↓
Aggregation
   ↓
Output
```

The choice of Python data structure affects how efficiently and clearly each step can be implemented.

For example:

```python
customer_ids = {101, 102, 103}
```

A `set` is useful when the primary requirement is uniqueness or membership testing.

While:

```python
customers = {
    101: "Anna",
    102: "Mark",
    103: "John"
}
```

A `dictionary` is useful when the requirement is fast lookup.

---

# 🧠 The Data Structure Decision Guide

| Requirement             | Recommended Structure |
| ----------------------- | --------------------- |
| Ordered collection      | `list`                |
| Allow duplicates        | `list`                |
| Unique values           | `set`                 |
| Fast membership testing | `set`                 |
| Key → value lookup      | `dict`                |
| One structured record   | `dict`                |
| Multiple records        | `list[dict]`          |
| Fixed-position record   | `tuple`               |
| Nested JSON-like data   | `dict` + `list`       |
| Group records by key    | `dict`                |
| Track processed IDs     | `set`                 |
| Lookup by ID            | `dict`                |

### A useful mental model

```text
Many records
    ↓
list

Unique IDs / membership
    ↓
set

Lookup by key
    ↓
dict

One structured record
    ↓
dict

Fixed immutable record
    ↓
tuple
```

---

# 1. Lists

A list is:

* ordered
* mutable
* allows duplicates
* index-based

```python
transactions = [100, 200, 300, 100]
```

## Common operations

```python
transactions[0]
transactions[-1]

transactions.append(400)
transactions.extend([500, 600])

transactions.remove(200)
transactions.pop()

len(transactions)
transactions.count(100)
```

## When to use a list

Use a list when:

* order matters
* duplicates are allowed
* you need sequential processing
* you are storing multiple records

Typical Data Engineering example:

```python
records = [
    {"id": 1, "amount": 100},
    {"id": 2, "amount": 200},
    {"id": 3, "amount": 300}
]
```

This **list of dictionaries** is one of the most important structures to become comfortable with.

---

# 2. Tuples

A tuple is:

* ordered
* immutable
* allows duplicates

```python
employee = ("E001", "Anna", "Data Engineer")
```

Tuple unpacking:

```python
employee_id, name, role = employee
```

Useful for:

* fixed records
* returning multiple values
* iteration
* lightweight structured data

Example:

```python
orders = [
    ("O001", "C001", 500),
    ("O002", "C002", 200)
]
```

---

# 3. Sets

A set contains unique values.

```python
countries = {
    "Germany",
    "India",
    "France"
}
```

## Common operations

```python
a | b       # union
a & b       # intersection
a - b       # difference
a ^ b       # symmetric difference
```

## Data Engineering patterns

### Find common records

```python
common = system_a & system_b
```

### Find records missing from B

```python
missing_from_b = system_a - system_b
```

### Find all unique records

```python
all_records = system_a | system_b
```

### Incremental processing

```python
new_ids = incoming_ids - processed_ids
```

Sets are especially useful for:

* deduplication
* reconciliation
* membership testing
* incremental processing

---

# 4. Dictionaries

A dictionary stores:

```text
key → value
```

Example:

```python
customers = {
    "C001": "Anna",
    "C002": "Mark",
    "C003": "John"
}
```

## Common operations

```python
customers["C001"]

customers.get("C001")

customers.get("C999", "UNKNOWN")

customers.keys()
customers.values()
customers.items()
```

## Why dictionaries matter in Data Engineering

Dictionaries are extremely useful for:

* lookups
* joins
* grouping
* aggregation
* configuration
* structured records
* JSON-like data

---

# 5. The Most Important Structure: List of Dictionaries

Real-world data frequently looks like:

```python
transactions = [
    {
        "id": 1,
        "customer": "C001",
        "amount": 100
    },
    {
        "id": 2,
        "customer": "C002",
        "amount": 250
    }
]
```

Think of it as:

```text
List
 ├── Dictionary → Record 1
 ├── Dictionary → Record 2
 └── Dictionary → Record 3
```

You should become very comfortable with:

```python
for transaction in transactions:
    print(transaction["amount"])
```

---

# 6. Nested Dictionaries

Example:

```python
customers = {
    "C001": {
        "name": "Anna",
        "country": "Germany",
        "orders": []
    }
}
```

Access values from outside → inside:

```python
customers["C001"]["name"]
```

For deeper structures:

```python
customers["C001"]["orders"][0]["amount"]
```

### Mental model

```text
customers
    ↓
C001
    ↓
orders
    ↓
first order
    ↓
amount
```

When working with nested structures, break the problem into levels instead of trying to write the entire expression at once.

---

# 7. `enumerate()`

Use `enumerate()` when you need both:

* position
* value

```python
for index, value in enumerate(values):
    print(index, value)
```

Start from 1:

```python
for row_number, value in enumerate(values, start=1):
    print(row_number, value)
```

### Data Engineering use cases

* source row numbers
* error reporting
* logging
* record numbering
* debugging

---

# 8. `zip()`

Use `zip()` when you need to process corresponding values from multiple collections.

```python
names = ["Anna", "Mark"]
salaries = [70000, 80000]

for name, salary in zip(names, salaries):
    print(name, salary)
```

### Create a dictionary

```python
employees = dict(zip(names, salaries))
```

### Create structured records

```python
records = [
    {
        "name": name,
        "salary": salary
    }
    for name, salary in zip(names, salaries)
]
```

Think:

> **`zip()` = combine corresponding positions.**

---

# 9. List Comprehensions

Basic:

```python
result = [x * 2 for x in values]
```

Filtering:

```python
valid = [x for x in values if x > 0]
```

Transform + filter:

```python
large = [
    x * 1.19
    for x in values
    if x > 500
]
```

### Decision rule

Use a comprehension when the transformation is simple and readable.

If the logic becomes complicated, use a normal loop.

Readable code is more important than writing the shortest possible code.

---

# 10. Dictionary Comprehensions

Example:

```python
prices = {
    "Laptop": 1200,
    "Mouse": 25,
    "Keyboard": 80
}
```

Filter:

```python
expensive = {
    product: price
    for product, price in prices.items()
    if price > 100
}
```

Transform:

```python
with_tax = {
    product: price * 1.19
    for product, price in prices.items()
}
```

---

# 11. Nested Comprehensions

Example:

```python
data = [
    [1, 2],
    [3, 4],
    [5, 6]
]
```

Flatten:

```python
flat = [
    value
    for row in data
    for value in row
]
```

Result:

```python
[1, 2, 3, 4, 5, 6]
```

Use carefully. If a nested comprehension becomes difficult to read, use normal loops.

---

# 12. Filtering Pattern

When a problem says:

* valid
* invalid
* greater than
* less than
* matching
* only
* exclude

Think:

```python
[item for item in items if condition]
```

Example:

```python
valid = [
    transaction
    for transaction in transactions
    if transaction["amount"] > 0
]
```

---

# 13. Transformation Pattern

When a problem says:

* convert
* clean
* calculate
* modify
* derive

Think:

```python
[transform(item) for item in items]
```

Example:

```python
amounts_with_vat = [
    amount * 1.19
    for amount in amounts
]
```

---

# 14. Counting Pattern

When the question asks:

> How many records satisfy a condition?

Use:

```python
count = sum(
    1
    for record in records
    if condition
)
```

Example:

```python
failed_count = sum(
    1
    for record in transactions
    if record["status"] == "failed"
)
```

---

# 15. `any()` and `all()`

### `any()`

Answers:

> Does at least one item satisfy the condition?

```python
has_invalid = any(
    amount < 0
    for amount in amounts
)
```

### `all()`

Answers:

> Do all items satisfy the condition?

```python
all_valid = all(
    amount > 0
    for amount in amounts
)
```

### Data-quality use

```python
has_missing_id = any(
    record["id"] is None
    for record in records
)
```

---

# 16. `sorted()` + `key`

Simple sorting:

```python
sorted(values)
```

Descending:

```python
sorted(values, reverse=True)
```

Sorting dictionaries:

```python
sorted(
    employees,
    key=lambda x: x["salary"]
)
```

Descending:

```python
sorted(
    employees,
    key=lambda x: x["salary"],
    reverse=True
)
```

### Multi-field sorting

```python
sorted(
    employees,
    key=lambda x: (
        x["department"],
        x["salary"]
    )
)
```

Think:

> **`key=` tells Python what value to sort by.**

---

# 17. `min()` and `max()`

Simple:

```python
minimum = min(amounts)
maximum = max(amounts)
```

With dictionaries:

```python
highest_paid = max(
    employees,
    key=lambda x: x["salary"]
)
```

---

# 18. Unpacking

Tuple/list:

```python
employee = ("E001", "Anna", "Data")

employee_id, name, department = employee
```

Remaining values:

```python
first, *remaining = values
```

Dictionary unpacking:

```python
combined = {
    **customer,
    **address
}
```

---

# 19. Lookup Pattern

If you repeatedly need:

```text
customer ID → customer name
```

create a dictionary:

```python
lookup = {
    customer["id"]: customer["name"]
    for customer in customers
}
```

Then:

```python
name = lookup.get(customer_id, "UNKNOWN")
```

This is the Python equivalent of thinking about a lookup table before implementing a join.

---

# 20. Join / Enrichment Pattern

Customers:

```python
customers = [
    {"id": "C001", "name": "Anna"},
    {"id": "C002", "name": "Mark"}
]
```

Orders:

```python
orders = [
    {"id": "O001", "customer_id": "C001"},
    {"id": "O002", "customer_id": "C999"}
]
```

Build lookup:

```python
lookup = {
    customer["id"]: customer["name"]
    for customer in customers
}
```

Enrich:

```python
for order in orders:
    order["customer_name"] = lookup.get(
        order["customer_id"],
        "UNKNOWN"
    )
```

---

# 21. Grouping Pattern

When the question says:

> group by customer / department / product

Think:

```python
grouped = {}

for record in records:
    key = record["customer"]

    if key not in grouped:
        grouped[key] = []

    grouped[key].append(record)
```

Result:

```python
{
    "C001": [...],
    "C002": [...]
}
```

---

# 22. Aggregation Pattern

When the question says:

> total / sum / revenue per customer

Think:

```python
totals = {}

for record in records:
    key = record["customer"]

    if key not in totals:
        totals[key] = 0

    totals[key] += record["amount"]
```

---

# 23. Deduplication Pattern

### Simple uniqueness

```python
unique_values = set(values)
```

### Preserve original order

```python
seen = set()
result = []

for value in values:
    if value not in seen:
        seen.add(value)
        result.append(value)
```

---

# 24. Business-Key Deduplication

Suppose email is the business key:

```python
customers = [
    {"id": 1, "email": "a@test.com", "name": "Anna"},
    {"id": 2, "email": "b@test.com", "name": "Mark"},
    {"id": 3, "email": "a@test.com", "name": "Anna Updated"}
]
```

Think:

```text
business key = email
```

Then use the email to determine uniqueness.

This pattern is important in:

* customer data
* CDC processing
* master data
* ETL pipelines
* data quality

---

# 25. Reconciliation Pattern

Given:

```python
system_a = {1, 2, 3, 4}
system_b = {2, 3, 4, 5}
```

### Missing from B

```python
system_a - system_b
```

### Missing from A

```python
system_b - system_a
```

### Existing in both

```python
system_a & system_b
```

### All unique records

```python
system_a | system_b
```

---

# 26. Incremental Processing Pattern

Processed:

```python
processed_ids = {1, 2, 3}
```

Incoming:

```python
incoming_ids = {2, 3, 4, 5}
```

New records:

```python
new_ids = incoming_ids - processed_ids
```

Then:

```python
processed_ids.update(new_ids)
```

This pattern is fundamental to incremental data processing.

---

# 27. Validation Pattern

Separate records:

```python
valid_records = []
invalid_records = []

for record in records:
    if condition:
        valid_records.append(record)
    else:
        invalid_records.append(record)
```

Typical validation rules:

```text
ID must exist
Amount must be positive
Email must exist
Quantity must be numeric
Date must be valid
Status must be allowed
```

---

# 28. Error Handling Pattern

When input may be invalid:

```python
try:
    amount = float(value)
except (ValueError, TypeError):
    amount = None
```

For pipelines:

```python
valid_records = []
invalid_records = []

for record in records:
    try:
        record["amount"] = float(record["amount"])
        valid_records.append(record)
    except (ValueError, TypeError):
        invalid_records.append(record)
```

---

# 29. Nested Data Pattern

For:

```python
customer["orders"][0]["amount"]
```

Break it down:

```text
customer
    ↓
orders
    ↓
first order
    ↓
amount
```

For multiple nested records:

```python
for customer in customers:
    for order in customer["orders"]:
        ...
```

Then ask:

> Can I filter, transform, flatten or aggregate these values?

---

# 30. The Data Engineering Problem-Solving Framework

For almost every Python data problem, use this sequence:

```text
1. Understand the input
        ↓
2. Understand the required output
        ↓
3. Identify the operation
        ↓
4. Choose the data structure
        ↓
5. Write the simple loop
        ↓
6. Test edge cases
        ↓
7. Simplify with Python patterns
```

### Keyword → Pattern mapping

| Problem wording              | Think                  |
| ---------------------------- | ---------------------- |
| unique                       | `set`                  |
| duplicate                    | `set` / `seen`         |
| lookup                       | `dict`                 |
| join                         | lookup dictionary      |
| group by                     | dictionary             |
| total per                    | accumulator dictionary |
| missing from                 | set difference         |
| common                       | set intersection       |
| all records                  | set union              |
| filter                       | `if`                   |
| transform                    | expression             |
| count                        | `sum()`                |
| at least one                 | `any()`                |
| every                        | `all()`                |
| rank/order                   | `sorted()`             |
| position                     | `enumerate()`          |
| combine corresponding values | `zip()`                |
| unpack                       | `*` / `**`             |
| nested records               | nested loops           |
| invalid input                | `try/except`           |
| new records                  | set difference         |
| preserve order               | list + `seen` set      |

---

# 31. Data Engineering Mini ETL Pattern

A common Python structure:

```text
EXTRACT
   ↓
VALIDATE
   ↓
DEDUPLICATE
   ↓
TRANSFORM
   ↓
ENRICH
   ↓
AGGREGATE
   ↓
LOAD
```

Example:

```python
records = extract()

valid, invalid = validate(records)

clean = deduplicate(valid)

transformed = transform(clean)

enriched = enrich(transformed)

summary = aggregate(enriched)

load(summary)
```

The same concepts later appear in:

* Pandas
* PySpark
* SQL
* Fabric pipelines
* ETL/ELT frameworks

The syntax changes, but the underlying thinking remains similar.

---

# 32. Common Mistakes to Avoid

### Mistake 1 — Using a list when uniqueness is required

Instead of repeatedly checking:

```python
if customer_id not in customer_ids:
```

consider whether a set is more appropriate.

---

### Mistake 2 — Using a set when order matters

A set is not the right answer when the requirement is:

> preserve the original order.

Use a `seen` set + result list.

---

### Mistake 3 — Complex comprehensions

Avoid turning this:

```python
result = [
    ...
]
```

into an unreadable one-liner.

A normal loop is often better.

---

### Mistake 4 — Accessing dictionaries unsafely

Instead of:

```python
customer["name"]
```

when the key may not exist:

```python
customer.get("name")
```

---

### Mistake 5 — Ignoring edge cases

Always think about:

```text
empty input
None
duplicates
missing keys
invalid values
negative numbers
zero
unknown IDs
unexpected data types
```

---

# 33. What You Should Be Able to Do Before Moving On

You should be comfortable with:

* [ ] Lists
* [ ] Tuples
* [ ] Sets
* [ ] Dictionaries
* [ ] Nested structures
* [ ] List comprehensions
* [ ] Dictionary comprehensions
* [ ] `enumerate()`
* [ ] `zip()`
* [ ] `sorted()`
* [ ] `min()` / `max()`
* [ ] `any()` / `all()`
* [ ] `lambda`
* [ ] Unpacking
* [ ] Filtering
* [ ] Transformation
* [ ] Grouping
* [ ] Aggregation
* [ ] Lookup
* [ ] Join/enrichment
* [ ] Deduplication
* [ ] Business-key deduplication
* [ ] Reconciliation
* [ ] Validation
* [ ] Error handling
* [ ] Incremental processing
* [ ] Nested-data processing
* [ ] Mini ETL

---



## About This Repository

This repository is designed as a practical learning and reference resource for anyone building a foundation in Python for Data Engineering and Data Analysis.

The emphasis is on **problem-solving patterns**, not just syntax.

The exercises progress from basic data structures to realistic data-processing scenarios such as:

* data validation
* deduplication
* reconciliation
* joins
* aggregation
* incremental processing
* nested data
* ETL pipelines


## Key Takeaway

The objective is not to memorize Python syntax.

The objective is to develop the ability to look at a data problem and think:

```text
What is my data?
        ↓
What output do I need?
        ↓
Which data structure fits?
        ↓
Which Python pattern solves it?
        ↓
How do I handle bad data and edge cases?
```

That problem-solving ability is the foundation for writing reliable Python data-processing code.

---

## Exercises

The exercises cover the progression from basic Python data structures to practical Data Engineering patterns.

---

## Next Step

After becoming comfortable with these patterns, the next stage is to apply the same thinking to:

**Pandas → SQL → PySpark → ETL/ELT → Data Engineering Projects**

---

## Author

Learning and building practical Data Engineering skills through hands-on projects and problem-driven practice.
