person = {"name": "Alice", "age": 25, "city": "New York"}
print("Accessing values person")
# Accessing values
print(person)
# Add new key-value pair
person["address"] = "123 Main St"
print("Accessing values person after adding address")
print(person)
# Update existing key-value pair
print("Accessing values person after updating age")
person["age"] = 26  
print(person)

# Remove key-value pair
print("Accessing values person after removing city")
if "city" in person:
    del person["city"]
print(person)