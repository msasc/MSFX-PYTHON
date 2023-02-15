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

import msfx.db.view
import msfx.db.table
from msfx.db.types import Types, JSON
from msfx.db.value import Value
from decimal import Decimal, ROUND_HALF_UP

class Field:
    """
    Field metadata definition.
    """
    def __init__(self, field = None):
        """
        Default constructor.
        """
        self.__name: str or None = None
        self.__alias: str or None = None
        self.__type: Types or None = None
        self.__length: int or None = None
        self.__decimals: int or None = None

        self.__persistent: bool = False
        self.__primary_key: bool = False
        self.__nullable: bool = True

        self.__function: str or None = None

        self.__table = None
        self.__view = None

        self.__properties: dict = {}

        if field is not None:
            if not isinstance(field, Field):
                raise Exception("Argument field must be a Field instance")
            self.__name = field.__name
            self.__alias = field.__alias
            self.__type = field.__type
            self.__length = field.__length
            self.__decimals = field.__decimals

            self.__persistent = field.__persistent
            self.__primary_key = field.__primary_key
            self.__nullable = field.__nullable

            self.__function = field.__function

            self.__table = field.__table
            self.__view = field.__view

            self.__properties |= field.__properties

    def get_name(self) -> str or None:
        return self.__name
    def get_alias(self) -> str or None:
        if self.__alias is None: return self.get_name()
        return self.__alias
    def get_type(self) -> Types or None:
        return self.__type
    def get_length(self) -> int or None:
        return self.__length
    def get_decimals(self) -> int or None:
        return self.__decimals

    def is_persistent(self) -> bool:
        return self.__persistent
    def is_primary_key(self) -> bool:
        return self.__primary_key
    def is_nullable(self) -> bool:
        return self.__nullable

    def get_function(self) -> str or None:
        return self.__function

    def get_table(self):
        return self.__table
    def get_view(self) -> msfx.db.view.View or None:
        return self.__view

    def get_properties(self) -> dict:
        return self.__properties

    def get_default_value(self) -> Value:
        if self.__type == Types.BOOLEAN:
            return Value(False)
        if self.__type == Types.DECIMAL:
            decimals = self.__decimals
            if decimals is None: decimals = 0
            return Value(Decimal(0).quantize(Decimal(10) ** -decimals, rounding=ROUND_HALF_UP))
        if self.__type == Types.INTEGER:
            return Value(int(0))
        if self.__type == Types.FLOAT:
            return Value(float(0))
        if self.__type == Types.COMPLEX:
            return Value(complex(0))
        if self.__type == Types.DATE:
            return Value(Types.DATE)
        if self.__type == Types.TIME:
            return Value(Types.TIME)
        if self.__type == Types.DATETIME:
            return Value(Types.DATETIME)
        if self.__type == Types.BINARY:
            return Value(bytes([]))
        if self.__type == Types.STRING:
            return Value("")
        if self.__type == Types.JSON:
            return Value(JSON())

        pass

    def set_name(self, name: str):
        if not isinstance(name, str):
            raise Exception("Invalid argument type")
        self.__name = name
    def set_alias(self, alias: str):
        if not isinstance(alias, str):
            raise Exception("Invalid argument type")
        self.__alias = alias
    def set_type(self, type: Types):
        if not isinstance(type, Types):
            raise Exception("Invalid argument type")
        self.__type = type
    def set_length(self, length: int):
        if not isinstance(length, int):
            raise Exception("Invalid argument type")
        if length <= 0:
            raise Exception("Invalid argument value")
        self.__length = length
    def set_decimals(self, decimals: int):
        if not isinstance(decimals, int):
            raise Exception("Invalid argument type")
        if decimals < 0:
            raise Exception("Invalid argument value")
        if self.__type is not Types.DECIMAL:
            raise Exception("Field type is not DECIMAL")
        self.__decimals = decimals

    def set_persistent(self, persistent: bool):
        if not isinstance(persistent, bool):
            raise Exception("Invalid argument type")
        self.__persistent = persistent
    def set_primary_key(self, primary_key: bool):
        if not isinstance(primary_key, bool):
            raise Exception("Invalid argument type")
        self.__primary_key = primary_key
    def set_nullable(self, nullable: bool):
        if not isinstance(nullable, bool):
            raise Exception("Invalid argument type")
        self.__nullable = nullable

    def set_function(self, function: str or None):
        if function is None:
            self.__function = None
            return
        if not isinstance(function, str):
            raise Exception("Invalid argument type")
        if len(function) == 0:
            raise Exception("Invalid empty function")
        self.__function = function

    def set_table(self, table):
        if table is not None and not isinstance(table, msfx.db.table.Table):
            raise Exception("Invalid argument type")
        self.__table = table
    def set_view(self, view):
        if view is not None and not isinstance(view, msfx.db.view.View):
            raise Exception("Invalid argument type")
        self.__view = view

    def __str__(self) -> str:
        s: str = str(self.get_name()) + ", " + str(self.get_type())
        if self.__length is not None:
            s += ", " + str(self.__length)
        if self.__decimals is not None:
            s += ", " + str(self.__decimals)
        if self.__table is not None:
            s += ", table: " + str(self.__table.get_name())
        return s

class Fields:
    """
    An ordered list of fields that can efficiently be accessed by index or by key or field alias.
    The aliases must be unique. Appending a field with the alias of an existing one raises an error.
    """
    def __init__(self):

        self.__fields: list = []
        self.__keys: list = []
        self.__indexes: dict = {}

        self.__persistent_fields: list = []
        self.__primary_key_fields: list = []
        self.__default_values: list = []

    def append(self, field: Field) -> None:
        """
        Append a new field.
        :param field: The field to append to the list.
        """
        if not isinstance(field, Field): raise Exception("Invalid argument field")
        self.__fields.append(field)
        self.__setup__()

    def __setup__(self) -> None:
        """
        Setup internal lists and maps based on the current list of fields.
        """

        self.__keys.clear()
        self.__indexes.clear()
        self.__persistent_fields.clear()
        self.__primary_key_fields.clear()
        self.__default_values.clear()

        for i in range(len(self.__fields)):
            field: Field = self.__fields[i]
            key: str = field.get_alias()

            self.__keys.append(key)
            self.__indexes[key] = i

            if field.is_persistent():
                self.__persistent_fields.append(field)
            if field.is_primary_key():
                self.__primary_key_fields.append(field)

            self.__default_values.append(field.get_default_value())



