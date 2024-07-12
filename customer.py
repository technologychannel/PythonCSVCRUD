class Customer:
    def __init__(self, id, name, phone, balance, citizenship):
        self.id = id
        self.name = name
        self.phone = phone
        self.balance = balance
        self.citizenship = citizenship
    
    def display_customer(self):
        print(f"Customer id is {self.id}")
        print(f"Customer name is {self.name}")
        print(f"Customer phone is {self.phone}")
        print(f"Customer balance is {self.balance}")
        print(f"Customer citizenship is {self.citizenship}")



# updated_list = []
# for cust in lists:
#     if cust.id != "1":
#         updated_list.append(cust)

# c.convert_customer_to_csv(updated_list)