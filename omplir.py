import sys
from datetime import date
from pymongo import MongoClient
from pymongo import TEXT
from soa.tiquets import GestioTiquets
from soa.tiquets import GestioTiquets2

class Omplir:

  def __init__(self,gn6):
    client = MongoClient()
    self.db=client.ticketsdb
    self.gn6=gn6

  def crea(self):
    for i in range(2010,2016):
      print "Insertem tickets oberts de l'any %d" % i
      inici="01-01-%d" % i
      fi="01-01-%d" % (i+1)
      tickets=self.gn6.consulta_tiquets(dataCreacioInici=inici,dataCreacioFi=fi)
      self.inserta_tickets(tickets)
    self.db.tickets.create_index([("$**",TEXT)],default_language="english")    
    self.guarda_actualitzacio()

  def guarda_actualitzacio(self):  
    self.db.actualitzacio.remove()
    self.db.actualitzacio.insert_one({"_id":1,"dataActualitzacio":self.avui()})

  def ultima_actualitzacio(self):  
  	return self.db.actualitzacio.find_one({"_id":1})["dataActualitzacio"]

  def avui(self):
    return date.today().strftime("%d-%m-%Y")

  def inserta_nous_tickets(self):
    actualitzacio=self.ultima_actualitzacio()
    avui=self.avui()
    print "Insertant tickets entre %s i %s" % (actualitzacio, avui)
    oberts=self.gn6.consulta_tiquets(dataCreacioInici=actualitzacio,dataCreacioFi=avui)
    print "%d tickets oberts" % len(oberts)
    self.inserta_tickets(oberts)
    tancats=self.gn6.consulta_tiquets(dataTancamentInici=actualitzacio,dataTancamentFi=avui)
    print "%d tickets tancats" % len(tancats)
    self.inserta_tickets(tancats)
    self.guarda_actualitzacio()

  def inserta_tickets(self,tickets):
    for t in tickets: self.inserta_ticket(t)  

  def inserta_ticket(self,ticket):
    self.db.tickets.replace_one({"_id":ticket["codi"]},ticket)

  def mostra(self):
    for t in self.db.tickets.find(): print t

print "Insertant dades al mongo..."
omplir=Omplir(GestioTiquets2())
if len(sys.argv)>1 and sys.argv[1]=='-c': omplir.crea()
omplir.inserta_nous_tickets()
omplir.mostra()
