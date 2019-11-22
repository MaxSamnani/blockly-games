"""Blockly Games: Pond Online

Copyright 2019 Google LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

"""Given a duck id get the duck. If no duck id exists get all ducks belonging to the user.
"""

__author__ = "aschmiedt@google.com (Abby Schmiedt)"

import cgi
import json
from pond_storage import *

forms = cgi.FieldStorage()

if forms.has_key("duckId"):
  urlsafe_key = forms["duckId"].value
  duck_key = ndb.Key(urlsafe=urlsafe_key)
  duck = duck_key.get()
  if (verify_duck(duck)):
    print("Content-Type: application/json\n")
    print(json.dumps({'name': duck.name, 'duckUrl': duck.key.urlsafe(), 'code': {'js': duck.code.js, 'opt_xml': duck.code.opt_xml}}))
else:
  duckList = get_user_ducks()
  print("Content-Type: application/json\n")
  print(json.dumps({"duckList": duckList}))
