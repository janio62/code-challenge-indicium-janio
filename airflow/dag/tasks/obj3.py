# Importing necessary libraries
import pandas as pd
from pymongo import MongoClient
import sys

# Getting the date from the command line argument
date = input("Enter the date in YYYY-MM-DD format: ")

# Extracting local data
orders = pd.read_csv("/data/postgres/orders/{0}/data.csv".format(date))
products = pd.read_csv("/data/postgres/products/{0}/data.csv".format(date))
customers = pd.read_csv("/data/postgres/customers/{0}/data.csv".format(date))
order_details = pd.read_csv("/data/csv/{0}/data.csv".format(date))

# Transforming data
orders = orders[['order_id','order_date','customer_id']].set_index('order_id')
products = products[['product_id','product_name']].set_index('product_id')
customers = customers[['customer_id','company_name']].set_index('customer_id')
orders = orders.join(customers, on='customer_id')
order_details = order_details.join(products, on='product_id')

data = []

for order_id in order_details.order_id.unique():
    json_order = order_details[order_details.order_id == order_id].drop("order_id", axis=1).to_dict("records")
    order = {
        "order_id": order_id,
        "order_date": orders.loc[order_id]['order_date'],
        "company_name": orders.loc[order_id]['company_name'],
        "products": json_order,
        "db_execution_date": date
    }
    data.append(order)

details = pd.DataFrame(data).to_dict("records")
