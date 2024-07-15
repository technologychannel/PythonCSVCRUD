from customer import Customer
import csv
import controller as cc

all_customers = []
print("Update Customer")
id = input("Enter customer id to update: ")
with open('customers.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        #print(f"{row} Hello")
        c = Customer(id=row[0], name=row[1], phone=row[4], balance=float(row[2]), citizenship=row[3])
        all_customers.append(c)

record_found = False
customer = Customer(id="", name="", phone="", balance=0, citizenship="")



index = 0

for i in range(len(all_customers)):
    if all_customers[i].id == id:
            record_found = True
            customer = all_customers[i]
            index = i
            break
    else:
        record_found = False

 
if record_found == True:
    print("record is found: ")
    customer.display_customer()
    print("Enter new details: ")
    cu = customer
    cu.id = input("Enter new customer id: ")
    cu.name = input("Enter new customer name: ")
    cu.balance = float(input("Enter customer balance: "))
    cu.citizenship = input("Enter customer citizenship number: ")
    cu.phone = input("Enter customer phone: ")
    all_customers[index] = cu
    cc.convert_customer_to_csv(all_customers)
    print("Record Updated Succesfully.")
    
else:
     print("Customer id not found.")