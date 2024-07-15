import controller as c

option_text = """
What do you want to do?
1. Add Customer
2. View All Customer
3. View Customer By ID
4. Update Customer 
5. Delete Customer
"""

option = int(input(option_text))

if option == 1:
    c.add_customer()
elif option == 2:
    c.view_allcustomers()
elif option == 3:
    print("View Customer By Id")
    c.view_singlecustomer()
elif option == 4:
    print("Update Customer")
    c.update_customer()
elif option == 5:
    print("Delete Customer")
    c.delete_customer()
else:
    print("Invalid Option Given")


## Create Class Product[id, name, price, qty]
## Make sure you will be able to add product, view all product
## , view single product, delete product.
