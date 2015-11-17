import sys
from datetime import date
from dateutil.parser import parse
from pymongo import MongoClient
from pymongo import TEXT
from soa.tiquets import GestioTiquets
import logging

class Omplir:

  def __init__(self,gn6):
    client = MongoClient()
    self.db=client.ticketsdb
    self.gn6=gn6

  def crea(self):
    self.db.tickets.remove()
    for i in range(2015,2016):
      print "Insertem tickets oberts de l'any %d" % i
      inici="01-01-%d" % i
      fi="01-01-%d" % (i+1)
      tickets=self.gn6.consulta_tiquets_dades(dataCreacioInici=inici,dataCreacioFi=fi,estat="TIQUET_STATUS_OBERT")
      print "%d tickets oberts" % len(tickets)
      self.inserta_tickets(tickets)
      tickets=self.gn6.consulta_tiquets_dades(dataCreacioInici=inici,dataCreacioFi=fi,estat="TIQUET_STATUS_PEND")
      print "%d tickets pendents" % len(tickets)
      self.inserta_tickets(tickets)
      tickets=self.gn6.consulta_tiquets_dades(dataCreacioInici=inici,dataCreacioFi=fi,estat="ESTAT_OBERT_PENDENT")
      print "%d tickets oberts pendents" % len(tickets)
      self.inserta_tickets(tickets)      
      tickets=self.gn6.consulta_tiquets_dades(dataTancamentInici=inici,dataTancamentFi=fi,estat="TIQUET_STATUS_TANCAT")
      print "%d tickets tancats" % len(tickets)
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
    oberts=self.gn6.consulta_tiquets_dades(dataCreacioInici=actualitzacio,dataCreacioFi=avui,estat="TIQUET_STATUS_OBERT")
    print "%d tickets oberts" % len(oberts)
    self.inserta_tickets(oberts)
    tancats=self.gn6.consulta_tiquets_dades(dataTancamentInici=actualitzacio,dataTancamentFi=avui,estat="TIQUET_STATUS_TANCAT")
    print "%d tickets tancats" % len(tancats)
    self.inserta_tickets(tancats)
    self.guarda_actualitzacio()

  def inserta_tickets(self,tickets):
    for t in tickets: self.inserta_ticket(t)  

  def inserta_ticket(self,ticket):
    ticket=self.convertir_a_dict(ticket)
    ticket["_id"]=ticket["codiTiquet"]
    self.db.tickets.replace_one({"_id":ticket["_id"]},ticket,True)
    print "Ticket %s creat" % ticket["_id"]

  def convertir_a_dict(self,ticket):    
    ticket=dict((name, unicode(getattr(ticket, name))) for name in dir(ticket) if not name.startswith('__')) 
    print ticket
    ticket['dataCreacio']=self.convertir_a_date(ticket['dataCreacio'])
    ticket['dataTancament']=self.convertir_a_date(ticket['dataTancament'])
    return ticket

  def convertir_a_date(self,data):    
    try:
      return parse(data)
    except:
      return None

  def mostra(self):
    for t in self.db.tickets.find(): print t

print "Insertant dades al mongo..."
logging.getLogger('suds').setLevel(logging.CRITICAL)
omplir=Omplir(GestioTiquets())
if len(sys.argv)>1 and sys.argv[1]=='-c': omplir.crea()
omplir.inserta_nous_tickets()
#omplir.mostra()
