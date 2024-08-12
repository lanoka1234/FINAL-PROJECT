# Name: Laura Anoka
# Student ID: 2172987
#
# FinalProjectInput.py
# This script reads data from ManufacturerList.csv, PriceList.csv, and ServiceDatesList.csv
# and stores it in a structured format for further processing.

import csv

def read_csv(filename):
    """
    Reads a CSV file and returns a list of dictionaries where each dictionary represents a row.
    
    :param filename: The name of the CSV file to read.
    :return: A list of dictionaries.
    """
    data = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Example usage:
manufacturer_data = read_csv('ManufacturerList.csv')
price_data = read_csv('PriceList.csv')
service_data = read_csv('ServiceDatesList.csv')
