from http.server import BaseHTTPRequestHandler
from urllib import parse
from pymongo import MongoClient

def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb+srv://dbuser:L3qxWdtlUq4FRpaI@cluster0.bapqrvd.mongodb.net/retentionbot_testdb?retryWrites=true&w=majority&tls=true"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['user_shopping_list']
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()

class handler(BaseHTTPRequestHandler):

	def do_GET(self):
		s = self.path
		dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
		self.send_response(200)
		self.send_header('Content-type','text/plain')
		self.end_headers()

		dbname = get_database()
		collection_name = dbname["user_1_items"]
		item_1 = {
		"_id" : "U1IT00001",
		"item_name" : "Blender",
		"max_discount" : "10%",
		"batch_number" : "RR450020FRG",
		"price" : 340,
		"category" : "kitchen appliance"
		}

		item_2 = {
		"_id" : "U1IT00002",
		"item_name" : "Egg",
		"category" : "food",
		"quantity" : 12,
		"price" : 36,
		"item_description" : "brown country eggs"
		}
		self.wfile.write(item_2)
		collection_name.insert_many([item_1,item_2])

		if "name" in dic:
			message = "Hello, " + dic["name"] + "!"

		else:
			message = "Hello, stranger!"

		self.wfile.write(message.encode())
		return