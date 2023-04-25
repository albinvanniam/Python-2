import csv 

shoplist = []
cost = {} 
stock  = {}
print"The Available Categoties are:"
category={1:'Electronics',2:'FoodItems',3:'Garments'}
for k,v in category.items():
    print k,v
n=input("Enter Your Choice:")
if n==1:
    electronics={1:'iphone',2:'xiaomi',3:'Samsung'}
    for k,v in electronics.items():
        print k,v
    x=input("Enter the Model")
    if x==1:
        with open ('iphone.csv','r') as file:
            reader = csv.DictReader(file)
            cost = {row["item"]:row["cost"] for row in reader}

        with open ('iphone.csv','r') as file:
           reader = csv.DictReader(file)
           stock = {row["item"]:row["stock"] for row in reader}
    if x==2:
        with open ('xiaomi.csv','r') as file:
            reader = csv.DictReader(file)
            cost = {row["item"]:row["cost"] for row in reader}

        with open ('xiaomi.csv','r') as file:
            reader = csv.DictReader(file)
            stock = {row["item"]:row["stock"] for row in reader}
    if x==3:
        with open ('samsung.csv','r') as file:
            reader = csv.DictReader(file)
            cost = {row["item"]:row["cost"] for row in reader}

        with open ('samsung.csv','r') as file:
           reader = csv.DictReader(file)
           stock = {row["item"]:row["stock"] for row in reader}
if n==2:
    with open ('Fooditems.csv','r') as file:
        reader = csv.DictReader(file)
        cost = {row["item"]:row["cost"] for row in reader}

    with open ('Fooditems.csv','r') as file:
       reader = csv.DictReader(file)
       stock = {row["item"]:row["stock"] for row in reader}
if n==3:
    with open ('Garments.csv','r') as file:
        reader = csv.DictReader(file)
        cost = {row["item"]:row["cost"] for row in reader}

    with open ('Garments.csv','r') as file:
       reader = csv.DictReader(file)
       stock = {row["item"]:row["stock"] for row in reader}
    
    


def display_stock():
   print "\n WELCOME TO THE GoDeal"
   print "\nStock Available"
   print "\nItems  Cost"
   print "-------------"
   for key in stock:
      print key,"\t", cost[key]

def compute_bill(sub):
    total = 0
    for item in sub:
        if stock[item] > 0 :
           total += int(cost[item])
           stock[item] = int(stock[item])-1
    return total

def fill_cart():
   display_stock()
   
   i = 0
   while 1:
      i += 1 
      item = raw_input("Enter your Item to the List (Press enter to stop): ")
      if item not in stock and item !='':
         print "Item not in Stock"
         item = raw_input("Enter your Item to the List (Press enter to stop): ")
      if item=='':
         break
      shoplist.append(item)
   print "The items in your cart are",shoplist 

def display_order():
    print "\nThank you for placing order. Your Order Details are:"
    print "Items Cost"
    print "----------"
    for item in shoplist:
       print item,"\t", cost[item],"\t"
    print"-----------"
    
    bill_cost = compute_bill(shoplist)
    print "Total Bill Cost: ", bill_cost


fill_cart()
display_order()
