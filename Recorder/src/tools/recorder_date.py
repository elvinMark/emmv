import datetime


class RecorderDate:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    def toDate(self):
        return datetime.date(self.year,self.month,self.day)

    def toOrdinal(self):
        self.toDate().toordinal()
    
    def setDate(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.year}-{self.month}-{self.day}"
