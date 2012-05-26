#!/usr/bin/env python

rot13 = """
<form method="post">
    ROT13
    <br>
    <textarea name="text">%(input)s</textarea>
    <br>
    <input type="submit">
</form>
"""

usersignup = """
<form method="post">
    User Signup
    <br>
    <label for="username">Username</label>
    <input type="text" name="username" value="%(username)s"></input>
    <span style="color:red">%(username_error)s</span>

    <br>
    <label for="password">Password</label>
    <input type="password" name="password" value=""></input>
    <span style="color:red">%(password_error)s</span>

    <br>
    <label for="verify">Verify</label>
    <input type="password" name="verify" value=""></input>
    <span style="color:red">%(verify_error)s</span>

    <br>
    <label for="email">Email</label>
    <input type="text" name="email" value="%(email)s"></input>
    <span style="color:red">%(email_error)s</span>

    <br>
    <input type="submit">
</form>
"""

newblogpost = """
<form method="post">
    New Post
    <br>
    <label for="subject">Subject</label>
    <input type="text" name="subject"></input>

    <br>
    <label for="content">Content</label>
    <textarea name="content"></textarea>

    <br>
    <span style="color:red">%(error)s</span>
    
    <br>
    <input type="submit"></input>
</form>
"""
