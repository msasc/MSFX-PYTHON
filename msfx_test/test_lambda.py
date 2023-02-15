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
my_list = [(1, 2), (3, 1), (4, 4)]
my_list.sort(key=lambda x: x[1])
print(my_list)
# Output: [(3, 1), (1, 2), (4, 4)]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filtered_list = list(filter(lambda x: x % 2 == 0, my_list))
print(filtered_list)
# Output: [2, 4, 6, 8]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squared_list = list(map(lambda x: x**2, my_list))
print(squared_list)
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81]

def do_something(func, arg):
    return func(arg)

print(do_something(lambda x: x**2, 5))
# Output: 25
