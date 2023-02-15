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

from decimal import Decimal, ROUND_HALF_UP

d = Decimal(str(10.325))
print(d)
print(d.as_tuple())
d = d.quantize(Decimal(10) ** -3, rounding=ROUND_HALF_UP)
print(d)
print(d.as_tuple())

t = d.as_tuple()
print(-t.exponent)

print(int(Decimal("3.25")))
print(float(Decimal("3.25")))
print(complex(Decimal("3.25")))

print(isinstance(10, int))
print(isinstance(float(10), float))
print(float(Decimal(3.125)).as_integer_ratio())
print(25/8)

print(complex(10, 1).real)
print(float(complex(10, 1).real))
print(float(Decimal(10.5)))

print(float(10) == int(10))
print(float(10) == Decimal(10))

def get_scale(val: float) -> int:
    dec: Decimal = Decimal(val)
    return -dec.as_tuple().exponent

print(get_scale(10.325))
print(Decimal(10.325))
print(float(10.325))
print(float(10))
