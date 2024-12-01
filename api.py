import requests

# Send a GET request
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)  # HTTP status code: 200 means success
print(response.json())       # Convert response to JSON


#--------------------------------------------------------------------------------
import requests

# Send a POST request
data = {"title": "foo", "body": "bar", "userId": 1}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
print(response.status_code)  # 201 (Created)
print(response.json())       # JSON response

#---------------------------------------------------------------------------------------
import json

# JSON string
json_data = '{"name": "John", "age": 30}'
python_obj = json.loads(json_data)  # Convert to dictionary
print(python_obj["name"])           # Access value


#-----------------------------------------------------------------------------------------
import json

# Python dictionary
data = {"name": "Alice", "age": 25}
json_data = json.dumps(data)        # Convert to JSON string
print(json_data)                    # {"name": "Alice", "age": 25}