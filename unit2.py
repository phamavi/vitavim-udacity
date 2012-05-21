#!/usr/bin/env python
#
#
#
import cgi
import string
import re

import webapp2

import forms

class Unit2Handler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('Hello, Unit 2!')

    class ROT13Handler(webapp2.RequestHandler):
        def get(self):
            self.response.out.write(forms.rot13 % {'input' : ''})

        def post(self):
            input = self.request.get('text')
            input = str(input)

            # ROT13
            transin = u'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
            transout = u'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
            transtable = string.maketrans(transin, transout)
            rot13 = input.translate(transtable)
            # Escape
            output = cgi.escape(rot13, quote=True)

            self.response.out.write(forms.rot13 % {'input' : output})

    class UserSignupHandler(webapp2.RequestHandler):
        USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        PASSWORD_RE = re.compile(r"^.{3,20}$")
        EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

        def get(self):
            self.response.out.write(forms.usersignup % {'username': '',
                                                        'password': '',
                                                        'verify': '',
                                                        'email': '',
                                                        'error': ''})

        def post(self):
            username = cgi.escape(self.request.get('username'), quote=True)
            password = cgi.escape(self.request.get('password'), quote=True)
            verify = cgi.escape(self.request.get('verify'), quote=True)
            email = cgi.escape(self.request.get('email'), quote=True)

            validated = True 
            errors = {
                "username": '',
                "password": '',
                "verify": '',
                "email": ''
            }
            # Validate
            if not self.validate(username, self.USER_RE):
                validated = False
                errors["username"] = "Invalid username."

            if not self.validate(password, self.PASSWORD_RE):
                validated = False
                errors["password"] = "Invalid password."

            if email and not self.validate(email, self.EMAIL_RE):
                validated = False
                errors["email"] = "Invalid email."

            if not password == verify:
                errors["verify"] = "Password does not match verify."
                validated = False

            if validated:
                # Redirect to a welcome page
                self.redirect("/Unit2/Thanks?user=" + username)
            else:
                error = "There was a problem with validation. " + ' '.join(errors)
                # Re-render the form
                self.response.out.write(forms.usersignup % {'username': username,
                                                            'password': '',
                                                            'verify': '',
                                                            'email': email,
                                                            'username_error': errors["username"],
                                                            'password_error': errors["password"],
                                                            'verify_error': errors["verify"],
                                                            'email_error': errors["email"]})

        def validate(self, text, compiled_re):
            return text and compiled_re.match(text)

    class ThanksHandler(webapp2.RequestHandler):
        def get(self):
            username = cgi.escape(self.request.get('user'), quote=True)
            if username:
                self.response.out.write("Thanks, %s!" % username)
            else:
                self.response.out.write("Thanks!")
