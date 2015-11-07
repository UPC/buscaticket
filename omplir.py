import sys
from pymongo import MongoClient
from pymongo import TEXT

def crea():
  client = MongoClient()
  db=client.ticketsdb
  db.tickets.create_index([("$**",TEXT)],default_language="english")

def inserta():
  client = MongoClient()
  db=client.ticketsdb
  db.tickets.replace_one({"_id":1},{
  	"_id":1,
  	"usuari":"jaume.moral",
  	"subject":"Hi ha alguna cosa que no em funciona",
  	"text":"Aqui explico millor que tinc problemes amb el firefox"
  })
  db.tickets.replace_one({"_id":2},{
  	"_id":2,
  	"usuari":"albert.obiols",
  	"subject":"S'ha deposar una noticia",
  	"text":"El titol es <b>Conferencia de google</b>"
  })



def mostra():
  client = MongoClient()
  db=client.ticketsdb  
  for t in db.tickets.find(): print t

print "Insertant dades al mongo..."
crea()
inserta()
mostra()
