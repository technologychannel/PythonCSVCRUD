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

# ## For Testing Only
# c1 = Customer(id="1", name="Bimal Sharma", phone="232323", balance=0, citizenship="1212121")
# c2 = Customer(id="2", name="Yogesh Bharati", phone="4322", balance=55550, citizenship="121121")

# print(c1.name)
# print(c2.name)

