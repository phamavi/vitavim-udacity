#!/usr/bin/env python
#
#
#
import cgi
import string
import re

import webapp2

import forms

class Unit3Handler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('Hello, Unit 3!')

    class Blog(object):
        class FrontpageHandler(webapp2.RequestHandler):
            def get(self):
                self.response.out.write("Hello front page that lists entries. <a newpost>")

        class NewpostHandler(webapp2.RequestHandler):
            def get(self):
                self.response.out.write("Here's a form. <input subject> <input content>")

            def post(self):
                self.response.out.write("Redirect to the thing")
                post_id = str(p.key().id())
                self.redirect('/blog/%s' % post_id)

        class PostHandler(webapp2.RequestHandler):
            def get(self, post_id):
                # p = Post.get_by_id(post_id)
                self.response.out.write("Oh man. You retrieved blog post %s" % post_id)
