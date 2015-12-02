import sys
import pymongo
from datetime import datetime
from datetime import timedelta
from bson.son import SON

class Indicadors:

  def __init__(self):
    client = pymongo.MongoClient()  
    self.db=client.ticketsdb    

  def tickets_per_dies_oberts(self):
    # La cosa rara del SON es perque un diccionari de python no conserva l'ordre i aixo si
    pipeline=[
      {"$match": {"dataTancament":{"$ne":None}}},
      {"$project": {"dies":{"$trunc":{"$divide":[{"$subtract":["$dataTancament","$dataCreacio"]},1000*60*60*24]}}}},
      {"$group": {"_id":"$dies","tickets":{"$sum":1}}},
      {"$sort": {"_id":1}}
    ]
    resultat=list(self.db.tickets.aggregate(pipeline))
    return resultat
