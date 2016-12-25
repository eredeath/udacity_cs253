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

class Entries(db.Model):
    title = db.StringProperty(required = True)
    body = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)

class blog_home(Handler):
    def render_home(self, title="", body="", error=""):
        entries = db.GqlQuery("SELECT * FROM Entries ORDER BY created DESC")
        self.render("blog.html", title=title, body=body, error=error, entries=entries)

    def get(self):
        self.render_home()
        button = self.request.get("page")
        if button:
            self.redirect(button)
        return

class blog_newpost(Handler):
    def render_newpost(self, title="", body="", error=""):
        self.render("newpost.html", title=subject, body=content, error=error)

    def get(self):
        self.render_newpost()
        button = self.request.get("page")
        if button:
            self.redirect(button)
        return

    def post(self):
        title = self.request.get("subject")
        body = self.request.get("content")
        if title and body:
            a = Entries(title =title, body = body)
            a.put()
            self.redirect('/blog/'+str(a.key().id()))
        else: 
            error = "We need both a title and a body!"
            self.render_newpost(title, body, error)

class post_permalink(Handler):
    def render_post(self, ids, title="", body=""):
        blog_post = Entries.get_by_id (long(ids), parent=None)
        self.render("post_permalink.html", title=title, body=body, blog_post=blog_post)

    def get(self, ids):
        self.render_post(ids)
        button = self.request.get("page")
        if button:
            self.redirect(button)
        return
