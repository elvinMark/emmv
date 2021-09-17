from tinydb import TinyDB, Query
import os
import time

class CajaDB:
    def __init__(self,db_dir):
        self.incomes_cash_db = TinyDB(os.path.join(db_dir,"incomes_cash.json"))
        self.incomes_ticket_db= TinyDB(os.path.join(db_dir,"incomes_check.json"))
        self.incomes_ticket_db = TinyDB(os.path.join(db_dir,"incomes_ticket.json"))
        self.outcomes_db = TinyDB(os.path.join(db_dir,"outcomes.json"))
        self.codes_db = TinyDB(os.path.join(db_dir,"codes.json"))

        self.cursors_db = TinyDB(os.path.join(db_dir,"cursors.json"))

        self.query = Query()

    def insert_new_asset(self,name):
        tmp_ = self.cursors_db.search(self.query.type == "codes")
        if len(tmp_) < 1:
            raise Exception("Could not find codes type in the database")
        else:
            cursor = tmp_[0]["cursor"] + 1
            self.codes_db.insert({"code":cursor,"name":name})
            self.cursors_db.update({"cursor":cursor},self.query.type == "codes")
            return cursor
        return None
    
    def search_asset_by_name(self,name):
        return self.codes_db.search(self.query.name == name)

    def search_asset_by_code(self,code):
        return self.codes_db.search(self.query.code == code)
    
    def list_all_assets(self):
        return self.codes_db.all()

    def insert_new_input_cash(self,name,details,amount,date):
        self.incomes_cash_db.insert({"name":name,"details":details,"amount":amount,"date":date})
        
