months = ['january',
          'february',
          'march',
          'april',
          'may',
          'june',
          'july',
          'august',
          'september',
          'october',
          'november',
          'december']
          
def valid_month(month):
    for month_name in months:
        if month.lower()==month_name:
            return month.capitalize()
    return
    
def valid_day(day):
    if day and day.isdigit():
        day = int(day)
        if (day <= 31) and (day > 0):
            return day
        
def valid_year(year):
    if year and year.isdigit():
        year = int(year)
        if( year >= 1900 ) and (year <= 2020):
            return year