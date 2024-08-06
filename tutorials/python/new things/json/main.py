import json

# Sample data
data = {'name': 'John', 'age': 30, 'city': 'New York'}

# Open the JSON file for writing
with open('output.json', 'w') as file:
    json.dump(data, file)
