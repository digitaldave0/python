import json
x =  ('[{ "name":"John", "age":30, "city":"New York"}]')
y = json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')

# the result is a Python dictionary:
print(y["age"])

#convert python to json
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
