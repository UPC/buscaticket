import sys
import pymongo

def busca(text):
  client = pymongo.MongoClient()  
  db=client.ticketsdb
  return list(db.tickets.find({"$text":{"$search":text}})
  	                    .sort([("dataTancament",pymongo.DESCENDING), ("dataCreacio",pymongo.DESCENDING)])
  )

  #.sort([("dataTancament",pymongo.DESCENDING), ("dataCreacio",pymongo.DESCENDING)])

