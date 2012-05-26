#!/usr/bin/env python
#
#
#
import cgi

import webapp2
from google.appengine.ext import db

import forms

class Post(db.Model):
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)

    def get_html(self):
        return "<div class='post'>" + \
               "<div class='post-subject'>%s</div>" % self.subject + \
               "<div class='post-content'>%s</div>" % self.content

class Unit3Handler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('Hello, Unit 3!')

    class Blog(object):
        class FrontpageHandler(webapp2.RequestHandler):
            def get(self):
                # get all the posts
                posts = db.GqlQuery("SELECT * FROM Post "
                                    "ORDER BY created DESC")
                header_string = "<h1>This is the blog</h1>"
                body_string = ''
                for post in posts:
                    body_string += post.get_html()
                
                self.response.headers['Content-Type'] = 'text/html'
                self.response.out.write(header_string + body_string)

        class NewpostHandler(webapp2.RequestHandler):
            def get(self):
                self.response.headers['Content-Type'] = 'text/html'
                self.response.out.write(forms.newblogpost % {'error': ''})

            def post(self):
                subject = cgi.escape(self.request.get("subject"))
                content = cgi.escape(self.request.get("content"))

                if subject and content:
                    post = Post(subject=subject, content=content)
                    post.put()
                    post_id = str(post.key().id())
                    self.redirect('/Unit3/Blog/%s' % post_id)
                else:
                    self.response.out.write(forms.newblogpost % {'error': 'Subject and content are required!'})

        class PostHandler(webapp2.RequestHandler):
            def get(self, post_id):
                p = Post.get_by_id(int(post_id))
                self.response.headers['Content-Type'] = 'text/html'
                if p:
                    self.response.out.write(p.get_html())
                else:
                    self.response.out.write("No post by that ID!")
