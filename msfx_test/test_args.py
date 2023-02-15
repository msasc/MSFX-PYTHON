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

def example_function(arg=None):
    if arg is not None:
        print("The argument has been passed, with value:", arg)
    else:
        print("The argument has not been passed")

example_function() # The argument has not been passed
example_function(None) # The argument has not been passed
example_function("foo") # The argument has been passed, with value: foo
