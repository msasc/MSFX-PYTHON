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
from datetime import date, time, datetime
from msfx.db.types import Types, JSON, check_valid_type, get_type

class Value:
    """
    A value encapsulates a reference to one of the supported types.
    """
    def __init__(self, value):
        """
        Constructs a Value with one of the supported types.
        :param value:
            The data value or the Types type and the internal value will be None.
        """

        # Argument value can not be None.
        if value is None:
            raise Exception("Argument value can not be None.")

        self.__value = None
        self.__type = None

        # The type is passed as argument.
        if isinstance(value, Types):
            self.__type = value
            return

        # Check that the type of the argument value is supported.
        if not check_valid_type(value):
            raise Exception(f"Invalid type for argument value: {type(value)}")

        # Assign value and type.
        self.__value = value
        self.__type = get_type(value)

    def type(self) -> Types: return self.__type
    def value(self) -> object: return self.__value

    def is_none(self) -> bool: return self.__value is None
    def is_boolean(self) -> bool: return self.__type == Types.BOOLEAN
    def is_decimal(self) -> bool: return self.__type == Types.DECIMAL
    def is_integer(self) -> bool: return self.__type == Types.INTEGER
    def is_float(self) -> bool: return self.__type == Types.FLOAT
    def is_complex(self) -> bool: return self.__type == Types.COMPLEX
    def is_date(self) -> bool: return self.__type == Types.DATE
    def is_time(self) -> bool: return self.__type == Types.TIME
    def is_datetime(self) -> bool: return self.__type == Types.DATETIME
    def is_binary(self) -> bool: return self.__type == Types.BINARY
    def is_string(self) -> bool: return self.__type == Types.STRING
    def is_JSON(self) -> bool: return self.__type == Types.JSON

    def is_numeric(self) -> bool:
        if (self.__type == Types.DECIMAL or
            self.__type == Types.INTEGER or
            self.__type == Types.FLOAT or
            self.__type == Types.COMPLEX):
            return True
        return False

    def get_boolean(self) -> bool:
        if not self.is_boolean(): raise Exception("Type is not BOOLEAN")
        if self.is_none(): return False
        return bool(self.__value)

    def get_decimal(self) -> Decimal:
        if not self.is_numeric(): raise Exception("Type is not NUMERIC")
        if self.is_none(): return Decimal(0)
        return Decimal(self.__value)

    def get_integer(self) -> int:
        if not self.is_numeric(): raise Exception("Type is not NUMERIC")
        if self.is_none(): return 0
        return int(self.__value)

    def get_float(self) -> float:
        if not self.is_numeric(): raise Exception("Type is not NUMERIC")
        if self.is_none(): return 0.0
        return float(self.__value)

    def get_complex(self) -> complex:
        if not self.is_numeric(): raise Exception("Type is not NUMERIC")
        if self.is_none(): return complex(0)
        return complex(self.__value)

    def get_date(self) -> date or None:
        if not self.is_date(): raise Exception("Type is not DATE.")
        if self.is_none(): return None
        return self.__value

    def get_time(self) -> time or None:
        if not self.is_time(): raise Exception("Type is not TIME.")
        if self.is_none(): return None
        return self.__value

    def get_datetime(self) -> datetime or None:
        if not self.is_datetime(): raise Exception("Type is not DATETIME.")
        if self.is_none(): return None
        return self.__value

    def get_binary(self) -> bytes:
        if not self.is_binary(): raise Exception("Type is not BINARY.")
        if self.is_none(): return bytes([])
        return self.__value

    def get_string(self) -> str:
        if not self.is_string(): raise Exception("Type is not STRING.")
        if self.is_none(): return ""
        return self.__value

    def get_JSON(self) -> JSON:
        if not self.is_JSON(): raise Exception("Type is not JSON.")
        if self.is_none(): return JSON()
        return self.__value

    def set_none(self): self.__value = None

    def set_boolean(self, value: bool):
        if not self.is_boolean(): raise Exception("Type is not BOOLEAN")
        if not isinstance(value, bool): raise Exception("Argument value is not BOOLEAN")
        self.__value = value

    def set_decimal(self, value: Decimal):
        if not isinstance(value, Decimal): raise Exception("Argument value is not DECIMAL")
        self.set_number(value)

    def set_integer(self, value: int):
        if not isinstance(value, int): raise Exception("Argument value is not INTEGER")
        self.set_number(value)

    def set_float(self, value: int):
        if not isinstance(value, float): raise Exception("Argument value is not FLOAT")
        self.set_number(value)

    def set_complex(self, value: int):
        if not isinstance(value, complex): raise Exception("Argument value is not COMPLEX")
        self.set_number(value)

    def set_number(self, value):
        # This Value must be numeric.
        if not self.is_numeric(): raise Exception("Type is not NUMERIC")

        # If the argument value is complex and this Value is not complex,
        # retrieve just the real part of value.
        if isinstance(value, complex) and not self.is_complex(): value = complex(value).real

        # Internally DECIMAL: if None just cast, otherwise preserve the scale.
        if self.is_decimal():
            if self.is_none():
                self.__value = Decimal(value)
            else:
                exp = self.get_decimal().as_tuple().exponent
                self.__value = Decimal(value).quantize(Decimal(10) ** exp, rounding=ROUND_HALF_UP)
            return

        # Internally INTEGER, just cast. Note that it will trunc.
        if self.is_integer(): self.__value = int(value); return

        # Internally FLOAT, just cast.
        if self.is_float(): self.__value = float(value); return

        # Internally COMPLEX, just cast.
        if self.is_complex(): self.__value = complex(value); return

    def set_date(self, value: date):
        if not isinstance(value, date): raise Exception("Argument value is not DATE")
        if not self.is_date(): raise Exception("Type is not DATE")
        self.__value = value

    def set_time(self, value: time):
        if not isinstance(value, time): raise Exception("Argument value is not TIME")
        if not self.is_time(): raise Exception("Type is not TIME")
        self.__value = value

    def set_datetime(self, value: datetime):
        if not isinstance(value, datetime): raise Exception("Argument value is not DATETIME")
        if not self.is_datetime(): raise Exception("Type is not DATETIME")
        self.__value = value

    def set_binary(self, value: bytes):
        if not isinstance(value, bytes): raise Exception("Argument value is not BINARY")
        if not self.is_binary(): raise Exception("Type is not BINARY")
        self.__value = value

    def set_string(self, value: str):
        if not isinstance(value, str): raise Exception("Argument value is not STRING")
        if not self.is_string(): raise Exception("Type is not STRING")
        self.__value = value

    def set_JSON(self, value: JSON):
        if not isinstance(value, JSON): raise Exception("Argument value is not JSON")
        if not self.is_JSON(): raise Exception("Type is not JSON")
        self.__value = value

    def __lt__(self, other: object) -> bool:
        return super().__lt__(other)

    def __le__(self, other: object) -> bool:
        return super().__le__(other)

    def __eq__(self, other: object) -> bool:
        # Other is a Value.
        if isinstance(other, Value):
            return self.__value == other.__value
        # Other is comparable.
        comparable: bool = False
        if self.is_boolean(): comparable = isinstance(other, bool)
        if self.is_numeric():
            comparable = (
                isinstance(other, Decimal) or
                isinstance(other, int) or
                isinstance(other, float) or
                isinstance(other, complex)
            )
        if self.is_date(): comparable = isinstance(other, date)
        if self.is_time(): comparable = isinstance(other, time)
        if self.is_datetime(): comparable = isinstance(other, datetime)
        if self.is_binary(): comparable = isinstance(other, bytes)
        if self.is_string(): comparable = isinstance(other, str)
        if self.is_JSON(): comparable = isinstance(other, JSON)
        if comparable:
            return self.__value == other
        return False

    def __ne__(self, other: object) -> bool:
        return super().__ne__(other)

    def __gt__(self, other: object) -> bool:
        return super().__gt__(other)

    def __ge__(self, other: object) -> bool:
        return super().__ge__(other)

    def __str__(self) -> str:
        if self.is_none(): return ""
        return str(self.__value)

