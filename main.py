import webapp2
from lesson1 import *
from valid_date import *
from hw1 import *
from hw1prt2 import *
from lesson2 import *
from lesson3 import *
from blog import *
from collections import namedtuple

class root(Handler):
    def get(self):
        button = self.request.get('page')
        if button:
            self.redirect(button)         
        self.render("root.html", pages = pages)

Page = namedtuple('Page', ['address', 'class_name', 'name'])        

pages = [
        Page('/', root, 'root'),
        Page('/lesson1', lesson1, 'lesson 1'),
        Page('/thanks', ThanksHandler, 'Thanks Handler for lesson 1'),
        Page('/hw1/prt1', hw1, 'Hw1 Prt1 (Rot13)'),
        Page('/hw1/prt2', hw1prt2, 'Hw1 Prt2 (User registration)'),
        Page('/hw1/prt2/verified', verified, 'Hw1 Prt2 Verified'),
        Page('/lesson2', template_refactored, 'Lesson 2 (shopping list)'),
        Page('/lesson2/fizzbuzz', FizzBuzzHandler, 'fizzbuzz'),
        Page('/lesson3/ascii_chan', ascii_chan, 'Ascii Chan'),
        Page('/blog', blog_home, 'Blog'),
        Page('/blog/newpost', blog_newpost, 'Blog Newpost'),
        Page('/blog/(\d+)', post_permalink, 'Post')
    ]         

app = webapp2.WSGIApplication( pages, debug=True)