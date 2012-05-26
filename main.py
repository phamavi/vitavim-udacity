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

import unit1
import unit2
import unit3
import forms


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('Hello, Udacity!')

app = webapp2.WSGIApplication([('/', MainHandler),

                               ('/Unit1/', unit1.Unit1Handler),
                               
                               ('/Unit2/', unit2.Unit2Handler),
                               ('/Unit2/ROT13', unit2.Unit2Handler.ROT13Handler),
                               ('/Unit2/UserSignup', unit2.Unit2Handler.UserSignupHandler),
                               ('/Unit2/Thanks', unit2.Unit2Handler.ThanksHandler),

                               ('/Unit3/', unit3.Unit3Handler),
                               ('/Unit3/Blog', unit3.Unit3Handler.Blog.FrontpageHandler),
                               ('/Unit3/Blog/newpost', unit3.Unit3Handler.Blog.NewpostHandler),
                               ('/Unit3/Blog/([0-9]+)', unit3.Unit3Handler.Blog.PostHandler),
                              ],
                              debug=True)
