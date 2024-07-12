from customer import Customer
import csv
import controller as c

all_customers = []

# Convert customers to csv
def convert_customer_to_csv(listofcustomer):
    file = open("customers.csv", "w")
    file.write("")
    file.close()
    for c in listofcustomer:
        f = open("customers.csv", "a")
        f.write(f"{c.id},{c.name},{c.balance},{c.citizenship},{c.phone}\n")
        f.close()

# Convert csv to customer list
def convert_csv_to_customer_list():
    all_customers = []
    with open('customers.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            c = Customer(id=row[0], name=row[1], phone=row[4], balance=float(row[2]), citizenship=row[3])
            all_customers.append(c)
    return all_customers

# Add customer
def add_customer():
    print("Addding customer")
    c = Customer(id="", name="", phone="", balance=0, citizenship="") # Blank Object
    c.id = input("Enter customer id: ")
    c.name = input("Enter customer name: ")
    c.balance = float(input("Enter customer balance: "))
    c.citizenship = input("Enter customer citizenship number: ")
    c.phone = input("Enter customer phone: ")
    f = open("customers.csv", "a")
    f.write(f"{c.id},{c.name},{c.balance},{c.citizenship},{c.phone}\n")
    f.close()
    print(f"Customer {c.name} added successfully.")

# View All Customer
def view_allcustomers():
    print("View All Customers")
    f = open("customers.csv","r")
    print(f.read())

# View Single Customer
def view_singlecustomer():
    print("View Single Customer")
    id = input("Enter customer id: ")
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

def delete_customer():
    print(f"Deleting custumer")
    lists = c.convert_csv_to_customer_list()
    updated_customer = []
    idtodelete= input("Enter customer id: ")
    record_found = False
    for customer in lists:
        if customer.id == idtodelete:
            record_found = True
        else:
            updated_customer.append(customer)

    if record_found:
        c.convert_customer_to_csv(updated_customer)
        print("Deleted Successfully")
    else:
        print("No record found")

def update_customer(id):
    print(f"Updating customer id {id}")
    
def search_customer(first_name):
    print("Searching customer")