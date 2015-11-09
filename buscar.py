import sys
from pymongo import MongoClient

def busca(text):
  print "Buscant "+text
  client = MongoClient()
  db=client.ticketsdb
  return db.tickets.find({"$text":{"$search":text}})


if len(sys.argv)<1:
  print "Falta un parametre amb el text a buscar"
  exit()

tickets=busca(sys.argv[1])
for t in tickets: 
  print t["codiTiquet"] 
  print "https://gn6.upc.edu/tiquets/control/tiquetDetallDadesGenerals?requirementId=%s" % t["codiTiquet"]
  print t["assumpte"]
  print t["dataCreacio"]
  print t["dataTancament"]  
  print ""
