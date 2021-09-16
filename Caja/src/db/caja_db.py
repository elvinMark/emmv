from tinydb import TinyDB, Query
import os
import time

class CajaDB:
    def __init__(sefl,db_dir):
        self.incomes_cash_db = TinyDB(os.path.join(db_dir,"incomes_cash.json"))
        self.incomes_ticket_db= TinyDB(os.path.join(db_dir,"incomes_check.json"))
        self.incomes_ticket_db = TinyDB(os.path.join(db_dir,"incomes_ticket.json"))
        self.outcomes_db = TinyDB(os.path.join(db_dir,"outcomes.json"))
        self.codes_db = TinyDB(os.path.join(db_dir,"codes.json"))

        self.cursors_db = TinyDB(os.path.join(db_dir,"cursors.json"))

    def insert_new_code()
