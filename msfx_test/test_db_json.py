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

from msfx.db.types import JSON

db_json = JSON()
json_data = '{"name": "John Doe", "age": 30, "city": "New York"}'
db_json.loads(json_data)
print(db_json)

data = {"sarque": "Pinfor", "teste": "KAR"}
db_json.merge(data)
print(db_json)
