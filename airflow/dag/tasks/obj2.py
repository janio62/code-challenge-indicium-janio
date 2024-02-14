# Importing necessary libraries
import shutil
import os
import sys

# Getting the date from the command line argument
date = input("Enter the date in YYYY-MM-DD format: ")

# Defining input and output file paths
input_file = "/data/order_details.csv"
output = "/data/csv/{0}/data.csv".format(date)

# Creating the output directory if it doesn't exist
os.makedirs(os.path.dirname(output), exist_ok=True)

# Copying the input file to the output location
try:
    shutil.copy(input_file, output)
    print("File copied successfully!")
except Exception as e:
    print("Error copying file:", e)
