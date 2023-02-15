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

data_dict = {1: "One", 2: "Two", 3: "Three"}
data_tuple = ("One", "Two", "Three")
data_list = ["One", "Two", "Three"]

print(len(data_dict))
print(len(data_tuple))
print(len(data_list))

data_list.append("Four")
print(len(data_list))
print(1 not in data_dict.keys())
print("One" in data_list)

list1: list = ["Hello", "my", "friend", ","]
list2: list = ["is", "it", "me", "you", "are", "looking", "for", "?"]
print(list1 + list2)

dict1 = {1: "One", 2: "Two"}
dict2 = {2: "Two-two", 3: "Three"}
d = dict1 | dict2
print(d)
print(d[2])

dict3 = {2: "Two", 3: "Three", 4: "Four"}
d |= dict3
print(d)

d1 = {1: "One", 2: "Two"}
d2 = {1: "One", 2: "Two"}
print(d1 == d2)
print(d1.get(3))


