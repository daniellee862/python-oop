
from datetime import date
from datetime import datetime

class Northcoder:
    def __init__(self, name, location, course, graduation_date):
        self.name = name
        self.location = location
        self.course = course
        self.graduation_date = graduation_date

    def greet(self, greeting):
        return f'Hello {greeting}, my name is {self.name}'
    
    def alumni(self):
        graduation_format = datetime.strptime(self.graduation_date, '%B %Y')
        today = datetime.today()
        if graduation_format < today:
            return True
        else:
            return False
       
    







