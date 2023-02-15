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

from msfx.db.field import Field, Fields

class Table:
    """
    A table definition.
    """
    def __init__(self):
        self.__name: str or None = None
        self.__fields: Fields = Fields()

    def appendField(self, field: Field):
        self.__fields.append(field)

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        if not isinstance(name, str):
            raise Exception("Argument name must be str")
        self.__name = name

class TableRef:
    """
    A reference of a table within the context of a database or a view.
    """
    def __init__(self, table: Table, schema: str or None, alias: str or None = None):
        """
        Creates a table reference.
        :param table: The table definition.
        :param schema: The schema within the database.
        :param alias: An optional alias.
        """
        if not isinstance(table, Table):
            raise Exception("Invalid type for argument table")
        if schema is not None and not isinstance(schema, str):
            raise Exception("Invalid type for argument schema")
        if alias is not None and not isinstance(alias, str):
            raise Exception("Invalid type for argument alias")
        self.__table: Table = table
        self.__schema = schema
        self.__alias = alias

    def get_table(self):
        return self.__table
    def get_alias(self):
        if self.__alias is not None:
            return self.__alias
        return self.__table.get_name()
    def get_schema(self):
        return self.__schema

