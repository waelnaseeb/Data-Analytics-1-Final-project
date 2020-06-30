import csv
import matplotlib.pyplot as plt

with open("retail_data.csv.txt", "r") as f: #read the CSV file
  reader = csv.DictReader(f)
  retail_data = list(reader)
  
  def cust_stats(): #customer status function
    cust_total_qty = [] #a list of quantities of each parcsel sold to the customer 
    cust_total_mny = [] #a list of total cost of each parcel sold to the customer
    cust_purchased_products = [] #a list of products sold to the customer
    wood_sales = [] # wooden items sold to the given customer
    customer_id = input("Please insert the customer ID: ") #ask the user to insert the customerID 
    
    for x in retail_data:
      if x['CustomerID'] == customer_id: #lookup customerID line by line
        cust_total_qty.append(float(x['Quantity'])) #add the quantity of a sold item to the list
        cust_total_mny.append(float(x['UnitPrice']) * float(x['Quantity'])) #add the cost of sold items to the list
        if x['StockCode'] not in cust_purchased_products:
          cust_purchased_products.append(x['StockCode']) #add the total cost of each percel
        if 'wood' in x['Description'].lower(): #lookup wooden products
          wood_sales.append(float(x['UnitPrice']) * float(x['Quantity']))# add the cost of wooden items to the list      
      
    print(f'The total quantity the customer {customer_id} purchased: {sum(cust_total_qty)}\nThe total cost of items the customer  purchased: {round(sum(cust_total_mny),2)} euro\nThe customer purchased {len(cust_purchased_products)} unique products so far\nAmoung items sold to the customer {len(wood_sales)} wooden items with a total cost of: {round(sum(wood_sales),2)} euro')


def sales_analysis(): #sales analysis function
    cust_spend = {} #a dictionary contains customerID (key) and total cost of his purchased items (value) 
    product_sale = {} #a dictionary contains stock code (key) and total quantity sold of this item(value)
    
    for x in retail_data: 
      if x['CustomerID'] not in cust_spend: # to add a new customerID if not already exist in the dictionary
        cust_spend[x['CustomerID']] = float(x['UnitPrice']) * float(x['Quantity'])
      else: #increment the cost of sold items to the value of customerID that already exists in the dictionary
        cust_spend[x['CustomerID']] += float(x['UnitPrice']) * float(x['Quantity'])
      if x['StockCode'] not in product_sale: # to add a new stock code if not already exist in the dictionary
        product_sale[x['StockCode']] = float(x['Quantity'])
      else: #increment the quantity sold of a given item to the value of stockcode that already exists in the dictionary
        product_sale[x['StockCode']] += float(x['Quantity'])
      
    best_customer_amount = max(cust_spend.values()) #find the customer that spent the highest amount of money on our products
    best_customer = [k for k, v in cust_spend.items() if v == best_customer_amount] #find the customer that spent the highest amount of money on our products
    best_product_qty = max(product_sale.values()) #find the best sold product
    best_product = [k for k, v in product_sale.items() if v == best_product_qty]
    print(f"We have {len(cust_spend)} customers in total\nWe have {len(product_sale)} products in total")
    print(f"The best customer: {best_customer} with a total amount of purchases {round(best_customer_amount,2)} euro\nBest selling product: {best_product} with a total quantity of {best_product_qty} units sold")
    
    #Plotting customers best customers with total amount of purchases > 2000
    plt.bar(x=[i for i in cust_spend.keys() if cust_spend[i] > 2000], height=[i for i in cust_spend.values() if i > 2000], width=0.5, align='center')
    # Add some text for x,y axes 
    plt.ylabel("Customer's total cost of purchases €")
    plt.xlabel('CustomerID of customers with total amount of purchases > 2000 €')
    plt.show()

#cust_stats() #call the function
sales_analysis() #call the function







  

