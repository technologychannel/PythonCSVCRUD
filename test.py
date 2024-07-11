import csv
from customer import Customer

id = input("Enter customer id: ")
all_customers = []

with open('customers.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        #print(f"{row} Hello")
        c = Customer(id=row[0], name=row[1], phone=row[4], balance=float(row[2]), citizenship=row[3])
        all_customers.append(c)

record_found = False
customer = Customer(id="", name="", phone="", balance=0, citizenship="")
for c in all_customers:
    if c.id == id:
        record_found = True
        customer = c
        break
    else:
        record_found = False
if record_found == True:
    print("record is found: ")
    customer.display_customer()
else: print("Customer id not found.")
          