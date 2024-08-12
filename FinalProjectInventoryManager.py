# Name: Laura Anoka
# Student ID: 2172987
#
# FinalProjectInventoryManager.py
# This script processes the inventory data and generates the required reports: 
# FullInventory.csv, item type inventory lists, PastServiceDateInventory.csv, and DamagedInventory.csv.

import csv
from datetime import datetime

class InventoryManager:
    def __init__(self, manufacturer_data, price_data, service_data):
        self.inventory = self.merge_data(manufacturer_data, price_data, service_data)

    def merge_data(self, manufacturer_data, price_data, service_data):
        """
        Merges data from manufacturer, price, and service date CSV files into a single structure.
        
        :param manufacturer_data: List of manufacturer dictionaries.
        :param price_data: List of price dictionaries.
        :param service_data: List of service date dictionaries.
        :return: A list of merged inventory dictionaries.
        """
        inventory = []
        price_dict = {item['item_id']: item['price'] for item in price_data}
        service_dict = {item['item_id']: item['service_date'] for item in service_data}

        for item in manufacturer_data:
            item_id = item['item_id']
            item['price'] = price_dict.get(item_id, 'Unknown')
            item['service_date'] = service_dict.get(item_id, 'Unknown')
            inventory.append(item)
        
        return inventory

    def generate_full_inventory(self):
        """
        Generates the FullInventory.csv file, sorted alphabetically by manufacturer name.
        """
        sorted_inventory = sorted(self.inventory, key=lambda x: x['manufacturer_name'])
        with open('FullInventory.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.inventory[0].keys())
            writer.writeheader()
            writer.writerows(sorted_inventory)

    def generate_item_type_inventory(self):
        """
        Generates separate inventory files for each item type.
        """
        item_types = set([item['item_type'] for item in self.inventory])
        for item_type in item_types:
            filtered_items = [item for item in self.inventory if item['item_type'] == item_type]
            with open(f'{item_type.capitalize()}Inventory.csv', mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['item_id', 'manufacturer_name', 'price', 'service_date', 'damaged'])
                writer.writeheader()
                writer.writerows(sorted(filtered_items, key=lambda x: x['item_id']))

    def generate_past_service_date_inventory(self):
        """
        Generates the PastServiceDateInventory.csv file for items past their service date.
        """
        today = datetime.today()
        past_service_items = [item for item in self.inventory if datetime.strptime(item['service_date'], '%m/%d/%Y') < today]
        sorted_items = sorted(past_service_items, key=lambda x: datetime.strptime(x['service_date'], '%m/%d/%Y'))
        with open('PastServiceDateInventory.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['item_id', 'manufacturer_name', 'item_type', 'price', 'service_date', 'damaged'])
            writer.writeheader()
            writer.writerows(sorted_items)

    def generate_damaged_inventory(self):
        """
        Generates the DamagedInventory.csv file for items that are damaged.
        """
        damaged_items = [item for item in self.inventory if item.get('damaged') == 'damaged']
        sorted_items = sorted(damaged_items, key=lambda x: float(x['price']), reverse=True)
        with open('DamagedInventory.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['item_id', 'manufacturer_name', 'item_type', 'price', 'service_date'])
            writer.writeheader()
            writer.writerows(sorted_items)

# Example usage:
inventory_manager = InventoryManager(manufacturer_data, price_data, service_data)
inventory_manager.generate_full_inventory()
inventory_manager.generate_item_type_inventory()
inventory_manager.generate_past_service_date_inventory()
inventory_manager.generate_damaged_inventory()
