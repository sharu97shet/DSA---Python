class stack:
    def __init__(self):
        self.values=[]
    def push(self, x):
        self.values=[x]+self.values
    def pop(self,x):
        return self.values.pop(x)

s=stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)

print(s.values)
s.pop(3)

print("after pop operation")
print(s.values)



import requests

# Make a GET request to the specified route
response = requests.get("https://coderbyte.com/api/challenges/json/age-counting")

# Check if the request was successful
if response.status_code == 200:
    # Extract the data from the response
    data = response.json()
    
    # Extract the value associated with the 'data' key
    data_string = data['data']
    
    # Split the data string into individual items
    items = data_string.split(', ')
    
    # Initialize a variable to count the number of items with age >= 50
    varOcg = 0
    
    # Loop through the items and count the ones with age >= 50
    for item in items:
        # Split each item into key-value pairs
        key, value = item.split('=')
        # Check if the age is greater than or equal to 50
        if key.strip() == 'age' and int(value) >= 50:
            varOcg += 1
            
    # Print the final count
    print("Number of items with age greater than or equal to 50:", varOcg)
    
    # __define-ocg__ keyword in the comment
    # This solution counts the number of items with age greater than or equal to 50
else:
    print("Failed to retrieve data from the API.")

