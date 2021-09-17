import datetime
import time
from PyQt5.QtCore import QDate

class CajaDate:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
        self.date = datetime.date(self.year,self.month,self.day) 
        self.ts = self.date.toordinal()

    def __str__(self):
        return str(self.date)
    
    def to_qdate(self):
        return QDate(self.year,self.month,self.day)
    
    def set_date(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
        self.date = datetime.date(self.year,self.month,self.day) 
        self.ts = self.date.toordinal()
        
    def timestamp(self):
        return self.ts
