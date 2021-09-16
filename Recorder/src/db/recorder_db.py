from tinydb import TinyDB, Query
import os

class RecorderDB:
    def __init__(self,db_dir):
        self.db_cursors = TinyDB(os.path.join(db_dir,"cursors.json"))
        self.db_clients = TinyDB(os.path.join(db_dir,"clients.json"))
        self.db_products = TinyDB(os.path.join(db_dir,"products.json"))
        self.db_sellers = TinyDB(os.path.join(db_dir,"sellers.json"))
        self.db_stock = TinyDB(os.path.join(db_dir,"stock.json"))
        self.db_orders = TinyDB(os.path.join(db_dir,"orders.json"))
        
        self.query = Query()
        
    def insert_new_client(self,name,address,route):
        cursor = self.db_cursors.search(self.query.type == "client")[0]["cursor"]
        self.db_clients.insert({"code":str(cursor),"name":name,"address":address,"route":route})
        cursor += 1
        self.db_cursors.update({"cursor":cursor},self.query.type == "client")

    def insert_new_product(self,name,price_per_unit,units_per_box,type_of_unit):
        cursor = self.db_cursors.search(self.query.type == "product")[0]["cursor"]
        self.db_products.insert({"code":str(cursor),"name":name,"units_per_box":units_per_box,"price_per_unit":price_per_unit,"type_of_unit":type_of_unit})
        cursor += 1
        self.db_cursors.update({"cursor":cursor},self.query.type == "product")
        
    def insert_new_seller(self,name,route):
        cursor = self.db_cursors.search(self.query.type == "seller")[0]["cursor"]
        self.db_sellers.insert({"code":str(cursor),"name":name,"route":route})
        cursor += 1
        self.db_cursors.update({"cursor":cursor},self.query.type == "seller")
        
    def insert_product_stock(self,code,amount):
        results = self.db_stock.search(self.query.code == code)
        new_amount = amount
        if results:
            prev_amount = results[0]["amount"]
            new_amount += prev_amount
            self.db_stock.update({"amount":new_amount},self.query.code == code)
        else:
            self.db_stock.insert({"code":code,"amount":new_amount})

    def insert_new_order(self,client_code,date,product_details,total_amount):
        cursor = self.db_cursors.search(self.query.type == "order")[0]["cursor"]
        self.db_orders.insert({"code":cursor,"client_code":client_code,"date":date,"product_details":product_details,"total_amount":total_amount})
        cursor += 1
        self.db_cursors.update({"cursor":cursor},self.query.type == "order")
        
    def search_client_by_code(self,code):
        return self.db_clients.search(self.query.code == code)

    def search_client_by_name(self,name):
        return self.db_clients.search(self.query.name.matches(".*"+name+".*"))

    def search_product_by_code(self,code):
        return self.db_products.search(self.query.code == code)

    def search_product_by_name(self,name):
        return self.db_products.search(self.query.name.matches(".*"+name+".*"))

    def search_order_by_date(self,date):
        return self.db_orders.search(self.query.date == date)

    def search_order_by_code(self,code):
        return self.db_orders.search(self.query.code == code)

    def search_seller_by_code(self,code):
        return self.db_sellers.search(self.query.code == code)

    def search_seller_by_route(self,route):
        return self.db_sellers.search(self.query.route == route)
    
    def update_client(self,code,new_info):
        return self.db_clients.update(new_info,self.query.code == code)

    def update_product(self,code,new_info):
        return self.db_products.update(new_info,self.query.code == code)

    def update_seller(self,code,new_info):
        return self.db_sellers.update(new_info,self.query.code == code)
