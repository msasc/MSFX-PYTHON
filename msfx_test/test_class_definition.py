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

class CLS:
	STAT_VAR  = ""
	var1 = "static var"
	def __init__(self, var):
		self.var1 = var
		self.var2 = var
		CLS.STAT_VAR = var

cls1 = CLS("Hola")
cls2 = CLS("capullo")

print(cls1.var1)
print(cls1.var2)
print("--------------")
print(cls2.var1)
print(cls2.var2)
print("--------------")
print(cls1.STAT_VAR)
print(cls2.STAT_VAR)
print(CLS.STAT_VAR)
print(CLS.var1)