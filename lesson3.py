import os
import jinja2
import webapp2

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env= jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                              autoescape=True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params) 

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class Art(db.Model):
    title = db.StringProperty(required = True)
    art = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)

class ascii_chan(Handler):
    def render_front(self, title="", art="", error=""):
        arts = db.GqlQuery("SELECT * FROM Art ORDER BY created DESC")
        self.render("ascii_chan.html", title=title, art=art, error=error, arts=arts)

    def get(self):
        self.render_front()
        button = self.request.get("page")
        if button:
            self.redirect(button)
        return
    def post(self):
        title = self.request.get("title")
        art = self.request.get("art")
        if title and art:
            a = Art(title =title, art = art)
            a.put()
            self.redirect('/lesson3/ascii_chan')
        else: 
            error = "We need both a title and some artwork!"
            self.render_front(title, art, error)

app = webapp2.WSGIApplication( [('/lesson3/ascii_chan', ascii_chan)], debug=True)