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

from enum import Enum, EnumMeta
from decimal import Decimal
from datetime import date, time, datetime
import json

class Types(Enum, metaclass=EnumMeta):
    """	Supported types mapped to the underlying SQL databases. """
    BOOLEAN = 0
    '''
    A boolean value that is supported in the database either by a BIT
    type or a Y/N or T/F single byte string.
    '''
    DECIMAL = 10
    ''' A numeric value with fixed number of decimal places. '''
    INTEGER = 11
    ''' A numeric integer or long value. '''
    FLOAT = 13
    ''' A numeric double (float) value. '''
    COMPLEX = 14
    ''' A numeric complex value. '''
    DATE = 20
    ''' A date value with ISO format "2022-12-21" '''
    TIME = 21
    ''' A time value with ISO format "10:25:05.135000000" '''
    DATETIME = 22
    ''' A date-time value with ISO format "2022-12-21T10:25:05.135000000" '''
    BINARY = 30
    '''
    A binary value, stored in the underlying database in fields of types
    for instance TINYBLOB, BLOB, MEDIUMBLOB or LONGBLOB depending on the length.
    '''
    STRING = 40
    '''
    A string value, stored in the underlying database in fields of types
    for instance VARCHAR, TINYTEXT, TEXT, MEDIUMTEXT or LONGTEXT depending on the length. 
    '''
    JSON = 50
    '''
    A JSON object value, stored in the underlying database as a STRING.
    '''

class JSON:
    """ JSON value encapsulation. """
    def __init__(self) -> None:
        """ Creates an empty JSON object."""
        self.__data: dict = {}
    def __init(self, json_data) -> None:
        """ Creates a JSON object dumping json string data. """
        self.__data: dict = json.loads(json_data)
    def loads(self, json_data) -> None:
        """ Loads the argument json_data string and merges it with this JSON internal dictionary data. """
        self.__data |= json.loads(json_data)
    def dumps(self) -> str:
        """ Dumps the internal dict data and returns a json string representation. """
        return json.dumps(self.__data)
    def merge(self, data: dict) -> None:
        """ Merges the argument dictionary data with this JSON internal dictionary data. """
        if type(data) is not dict: raise "Data to merge must be of dict type"
        self.__data |= data
    def data(self) -> dict:
        """ Gives access to the internal Python data dictionary. """
        return self.__data
    def __str__(self) -> str:
        return str(self.__data)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, JSON):
            return self.__data == other.__data
        if isinstance(other, dict):
            return self.__data == other
        return super().__eq__(other)

def check_valid_type(val) -> bool:
    """
    Check whether the argument type is a supported type.
    :param val: The argument value.
    :return: A bool.
    """
    if isinstance(val, bool): return True
    if isinstance(val, Decimal): return True
    if isinstance(val, int): return True
    if isinstance(val, float): return True
    if isinstance(val, complex): return True
    if isinstance(val, date): return True
    if isinstance(val, time): return True
    if isinstance(val, datetime): return True
    if isinstance(val, bytes): return True
    if isinstance(val, str): return True
    if isinstance(val, JSON): return True
    return False

def get_type(val) -> Types:
    """
    Returns the Types type corresponding to the value
    :param val: The value to look up the supported type.
    :return: The supported Types type.
    :exception A TypeError if the value type is not among the supported types.
    """
    if type(val) == bool: return Types.BOOLEAN
    if type(val) == Decimal: return Types.DECIMAL
    if type(val) == int: return Types.INTEGER
    if type(val) == float: return Types.FLOAT
    if type(val) == complex: return Types.COMPLEX
    if type(val) == date: return Types.DATE
    if type(val) == time: return Types.TIME
    if type(val) == datetime: return Types.DATETIME
    if type(val) == bytes: return Types.BINARY
    if type(val) == str: return Types.STRING
    if type(val) == JSON: return Types.JSON
    raise TypeError(f"Not supported type: {type(val)}")


