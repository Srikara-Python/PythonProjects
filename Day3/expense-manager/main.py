import csv
import json
from re import sub
from decimal import Decimal

def csv_to_json_dictionary(csv_file, json_file):

    # create a dictionary
    data = dict()

    # open csv reader called DictReader
    with open(csv_file, encoding='utf-8-sig') as csvf:
        csvReader = csv.DictReader(csvf)

        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
            
            # Assuming a column named 'date' to
            # be primary key
            key = rows['Date']
            data[key] = rows

        # Open a json writer, and use json.dump()
        with open(json_file, 'w', encoding='utf-8') as jsonf:
            jsonf.write(json.dumps(data, indent=4))

        return "Json Created"

def csv_to_json_custom_fields(csv_file, json_file):

    with open(csv_file, encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    with open(json_file, 'w') as f:
        json.dump(rows, f)

    return "Json Converted"

def add_record(csv_file, data):
    
    with open(csv_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)

    return "Record Added"

def record_count(json_file):
    num_lines = sum(1 for line in open(json_file))
    return num_lines

def total_expense(json_file):
    # Create a Decimal sum to store value
    sum = Decimal()
    
    # open the json file
    with open(json_file) as f:
        data = json.load(f)

    # For each, get the expense and using regex
    # sub = searc and replace: 
    # search any char if not a digit[0-9], '.'
    # e.g. $ , - and replace with blank ''
    for x in data:
        exp = Decimal(sub(r'[^\d.]','',x['expense'])) 
        sum += exp

    # Round the sum to 2 decimal 
    return round(sum,2)
    
def total_expense_type(json_file, type='all'):
    
    
    # open the json file
    with open(json_file) as f:
        data = json.load(f)

    # If no type passed, group all types
    # and return sum of each
    if type == 'all':
        
        # Create a Dictionary/Hash sum to store value
        sum = dict()

        for x in data:
            exp = float(sub(r'[^\d.]','',x['expense']))
            
            if x['type'] in sum:
                sum[x['type']] += exp
            else:
                sum[x['type']] = exp

        # This will sort the dictionary by the values 
        # of each entry within the dictionary 
        # from smallest to largest.
        # To sort in ascending reverse=False
        sum = dict(sorted(sum.items(), key=lambda item: item[1], reverse=True))

        return sum
    else:
        # Create a Decimal sum to store value
        sum = Decimal()

        # For each, get the expense and using regex
        # sub = searc and replace: 
        # search any char if not a digit[0-9], '.'
        # e.g. $ , - and replace with blank ''
        for x in data:
            if x['type'].lower() == type.lower():
                exp = Decimal(sub(r'[^\d.]','',x['expense'])) 
                sum += exp
        return round(sum,2)
    # Round the sum to 2 decimal 
    return False
    

csvFilePath  = 'csv/records.csv'
jsonFilePath = 'json/records.json'
jsonDictFilePath = 'json/records-dict.json'
userCsv = 'csv/users.csv'
test = 'json/test.json'

data = ['6/1/2021','Fuel','30']


# Load JSON and sum 
print(total_expense(jsonFilePath))
# print(total_expense_type(jsonFilePath, 'car'))
print(total_expense_type(jsonFilePath))

# Get File Line Count
# print("Size before: ",record_count(csvFilePath))

# Add Record
# print(add_record(csvFilePath, data))
# print("Size before: ",record_count(csvFilePath))

# Convert CSV to JSON
# print(csv_to_json_dictionary(csvFilePath, jsonDictFilePath))
# print(csv_to_json_custom_fields(csvFilePath, jsonFilePath))