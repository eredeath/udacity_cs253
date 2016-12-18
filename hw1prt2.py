import webapp2
import re

form="""
<form method="post">
      <table>
        <tr>
          <td class="label">
            Username
          </td>
          <td>
            <input type="text" name="username" value="%(usr_val)s">
          </td>
          <td class="error">%(usr_error)s</td>
        </tr>

        <tr>
          <td class="label">
            Password
          </td>
          <td>
            <input type="password" name="password" value="">
          </td>
          <td class="error">%(pswrd_error)s</td>
        </tr>

        <tr>
          <td class="label">
            Verify Password
          </td>
          <td>
            <input type="password" name="verify" value="">
          </td>
          <td class="error">%(pswrd_verify_error)s</td>
        </tr>

        <tr>
          <td class="label">
            Email (optional)
          </td>
          <td>
            <input type="text" name="email" value="%(email_val)s">
          </td>
          <td class="error">%(email_error)s</td>
        </tr>
      </table>

      <input type="submit">
    </form>
"""

class hw1prt2(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(form % {"usr_val": "",
                                        "email_val": "",
                                        "usr_error": "",
                                        "pswrd_error": "",
                                        "pswrd_verify_error": "",
                                        "email_error": ""})
    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        verify   = self.request.get('verify')
        email    = self.request.get('email')

        user_error_msg = ""
        password_error_msg = ""
        password_verify_error_msg = ""
        email_error_msg = ""

        err_uname = not(valid_username(username))
        err_pwrd = not(valid_password(password))
        err_pwrd_match = not(comp_passwords(password,verify))
        err_email = not(valid_email(email) or not(email))
        if err_uname:
            user_error_msg = "invalid username"
        elif err_pwrd:
            password_error_msg = "invalid passowrd"
        elif err_pwrd_match:
            password_verify_error_msg = "passwords do not match"
        
        if err_email:
            email_error_msg = "invalid e-mail address"

        if not(err_uname or err_pwrd or err_pwrd_match or err_email):
         	  self.redirect("/hw1/prt2/verified?username="+username)
        
        self.response.out.write(form % {"usr_val": username,
                                        "email_val": email,
                                        "usr_error": user_error_msg,
                                        "pswrd_error": password_error_msg,
                                        "pswrd_verify_error": password_verify_error_msg,
                                        "email_error": email_error_msg})
        

class verified(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(verified_page %{"username": self.request.get('username')})

verified_page="""
<div>Welcome, %(username)s</div>
"""

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
EMAIL_RE= re.compile(r"^[\S]+@[\S]+.[\S]+$")

def valid_username(username):
    return USER_RE.match(username)

def valid_password(password):
    return PASS_RE.match(password)

def valid_email(email):
    return EMAIL_RE.match(email)

def comp_passwords(pwrd, vpwrd):
    return (pwrd == vpwrd)