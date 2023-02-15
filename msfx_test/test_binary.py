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
# Convert an integer to binary representation

num = 1500
binary = bin(num)
print("Binary representation of", num, "is", binary)

# Convert binary representation to integer
binary_num = int(binary, 2)
print("Integer representation of", binary, "is", binary_num)

# Binary Left Shift operator
left_shift = num << 2
print("Left Shift of", num, "is", left_shift)

# Binary Right Shift operator
right_shift = num >> 2
print("Right Shift of", num, "is", right_shift)

# Binary AND operator
and_op = 5 & 3
print("AND of 5 and 3 is", and_op)

# Binary OR operator
or_op = 5 | 3
print("OR of 5 and 3 is", or_op)

# Binary NOT operator
not_op = ~5
print("NOT of 5 is", not_op)

# Binary XOR operator
xor_op = 5 ^ 3
print("XOR of 5 and 3 is", xor_op)
