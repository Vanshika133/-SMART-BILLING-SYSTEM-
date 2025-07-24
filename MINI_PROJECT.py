print("MINI STORE")

# menu item price
chocolate=50
chips=30
cold_drink=25
ice_cream=40

#  store menu
print("-----STORE MENU (WITH STOCK-------")
print("Item No | Item Name     | Price (₹) ")
print("--------------------------------------------")
print("1.      | chocolate          | 50  ")
print("2.      | chips              | 30  ")
print("3.      | cold_drink         | 25  ")
print("4.      | ice_cream          | 40  ")

#bill feature
chocolate=0
item=0
price=0
cart=[]
qty=0

# match case
ch=input("enter your choice (1 to 4) : ")
match ch:
    case '1':
            print("chocolate:")
            price=50
            qty=int(input("How much qty you want"))
            subtotal=chocolate*qty
    case '2':
                print("chips")
                price=30
                subtotal=chips*qty
                qty=int(input("How much qty you want"))
    case '3':
             print("cold drink")
             price=25
             subtotal=cold_drink*qty
             qty=int(input("How much qty you want"))
    case '4':
             print("ice cream:")
             price=40
             subtotal=ice_cream*qty
             qty=int(input("How much qty you want"))

# total price and qty
cart.append(item)
total=price*qty

#subtotal
subtotal=total

# Apply 10% discount if total > ₹200
discount = 0
if subtotal>200:
    discount = 0.10 * subtotal
    total= subtotal - discount

# Apply chocolate discount
choc_discount = 0
if qty > 5:
        choc_discount = 5 * qty
        total -= choc_discount
    
# Delivery charge
delivery_charge = 0
if total>=300:
        delivery_charge = 30
        total += delivery_charge

# Add 5% GST
gst = total * 0.05
total += gst

# final bill
print("\n Final Bill")
print(f"Your choice:{ch}")
print(f"Quantity:{qty}")
print(f"Subtotal: {subtotal}")
print(f"10% Discount: -₹{discount}")
print(f"Chocolate Discount: -{choc_discount}")
print(f"Delivery Charge: {delivery_charge}")
print(f"GST: {gst}:")
print(f"Total to Pay: {total}")
print("Thank you for shopping with us!")

