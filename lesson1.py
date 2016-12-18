import webapp2

form="""
<form method="post">
    What is your birthday?
    <br>
    <label>
        Month
        <input type="text" name="month" value="%(month)s">
    </label>
    <label>
        Day
        <input type="text" name="day" value="%(day)s">
    </label>
    <label>
        Year
        <input type="text" name="year" value="%(year)s">
    </label>
    <div style="color: red">%(error)s</div>
    <br>
    <br>
    <input type="submit">
</form>
"""

class lesson1(webapp2.RequestHandler):
    def write_form(self, error="", month="", day="", year=""):
        self.response.out.write(form % {"error": error,
                                        "month": month,
                                        "day": day,
                                        "year": year})

    def get(self):
        self.write_form()
    
    def post(self): 
        user_month = valid_month(self.request.get('month'))
        if not user_month:
            user_month=""
        user_day = valid_day(self.request.get('day'))
        if not user_day:
            user_day=""
        user_year = valid_year(self.request.get('year'))
        if not user_year:
            user_year=""

        if not (user_month and user_day and user_year):
            self.write_form("That doesn't look like a valid date bro", user_month, user_day, user_year)
        else:
            self.redirect("/thanks")

class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Thanks! That's a totally valid date!")