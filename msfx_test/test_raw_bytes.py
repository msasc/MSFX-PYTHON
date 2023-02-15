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
# Create a bytes object from a string

string = "Hello, World!"
bytes_obj = string.encode()
print(type(bytes_obj))
print("Bytes representation of '" + string + "' is", bytes_obj)

# Create a string from a bytes object
decoded_string = bytes_obj.decode()
print("String representation of", bytes_obj, "is '" + decoded_string + "'")

# Concatenating bytes objects
concat_bytes = bytes([72, 101, 108, 108, 111]) + bytes([32, 87, 111, 114, 108, 100, 33])
print("Concatenated bytes:", concat_bytes)

# Slicing bytes objects
sliced_bytes = bytes_obj[7:12]
print("Sliced bytes:", sliced_bytes)

# Indexing bytes objects
indexed_byte = bytes_obj[0]
print("Byte at index 0:", indexed_byte)

simple_bytes1 = bytes([72, 87, 123])
simple_bytes2 = bytes([123, 87, 72])
simple_bytes_sum = simple_bytes1 + simple_bytes2
print(simple_bytes_sum.decode())
