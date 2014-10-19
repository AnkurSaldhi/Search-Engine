#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi

form="""
<form method="post">
<label>
<b>Enter Some Text To ROT13 :-</b>
<br>
<br>
BIGGER BOX
<textarea name="text" style="height:100px;width:400px;">%(rot)s</textarea>
<br>
</label>
<input type="submit">
</form>
"""

def escape_html(s):
    return cgi.escape(s, quote=True)

class MainHandler(webapp2.RequestHandler):
    def write_form(self,rot=""):
        self.response.out.write(form %{"rot":escape_html(rot)})
        
    def get(self):
        self.write_form()

    def post(self):
        str1=""
        str1=self.request.get('text')
        #self.response.out.write(escape_html(str1))

        str2=""
        for i in str1:
            j=ord(i)
      
            if (j>=65 and j<=90):
                if j+13<=90:
                    str2+=chr(j+13)
                else:
                    str2+=chr(j-13)
            elif (j>=97 and j<=122):
                if j+13<=122:
                    str2+=chr(j+13)
                else:
                    str2+=chr(j-13)
            else:
                str2+=i   
          
        #self.response.out.write(escape_html(str2))
        self.write_form(str2)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
