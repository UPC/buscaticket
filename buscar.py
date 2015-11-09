import sys
from pymongo import MongoClient

def busca(text):
  client = MongoClient()  
  db=client.ticketsdb
  return list(db.tickets.find({"$text":{"$search":text}}))
