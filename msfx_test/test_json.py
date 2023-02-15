#  Copyright (c) 2023 Miquel Sas.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
class MyClass:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return self.value > other.value

    def __le__(self, other):
        return self.value <= other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __ne__(self, other):
        return self.value != other.value

import json

# A Python object
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Convert the Python object to a JSON object
json_data = json.dumps(data)

print(json_data)
print(data)
print(type(data))
print(type(json_data))
print(data["name"])
# Output:
# {"name": "John Doe", "age": 30, "city": "New York"}

import json

# A JSON object
json_data = '{"name": "John Doe", "age": 30, "city": "New York"}'

# Convert the JSON object to a Python object
data = json.loads(json_data)

print(data)
print(type(data))
# Output:
# {'name': 'John Doe', 'age': 30, 'city': 'New York'}

