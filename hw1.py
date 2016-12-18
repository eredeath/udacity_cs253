import webapp2

rot13="""
<form method="post">
    <textarea name="text" cols="80" rows="10">%(user_input)s</textarea>
    <br>
    <input type="submit" value="ROT-13 me!">
</form>
"""

class hw1(webapp2.RequestHandler):
    def post(self):
        user_input = self.request.get('text')
        self.response.out.write(rot13 % {"user_input": transmute(user_input)})
    def get(self):
        self.response.out.write(rot13 % {"user_input": ''})

rot13_dic = {'a':'n',
             'b':'o',
             'c':'p',
             'd':'q',
             'e':'r',
             'f':'s',
             'g':'t',
             'h':'u',
             'i':'v',
             'j':'w',
             'k':'x',
             'l':'y',
             'm':'z',
             'n':'a',
             'o':'b',
             'p':'c',
             'q':'d',
             'r':'e',
             's':'f',
             't':'g',
             'u':'h',
             'v':'i',
             'w':'j',
             'x':'k',
             'y':'l',
             'z':'m'}

def transmute(s):
    new_s =''
    for achar in s:
        if achar.isalpha():
            if achar.isupper():
                achar = achar.lower()
                new_s+=rot13_dic[achar].upper()
            else:
                new_s+=rot13_dic[achar]
        else:
            new_s+=achar
    return new_s

#app = webapp2.WSGIApplication([
#    ('/', hw1),
#], debug=True)