import sys
import pymongo
from datetime import datetime
from datetime import timedelta
from bson.son import SON

class Consultes:

  def __init__(self):
    client = pymongo.MongoClient()  
    self.db=client.ticketsdb    

  def busca(self,text):
    return list(self.db.tickets.find({"$text":{"$search":text}})
     .sort("estat",1)
     )

  def busca2(self,text):
    return list(self.db.tickets.find({"$text":{"$search":text}})
     .sort([("estat",pymongo.ASCENDING),("dataTancament",pymongo.DESCENDING), ("dataCreacio",pymongo.DESCENDING)])
     )

  def obrim_diaris(self):
    return self.agreguem('dayOfYear','dataCreacio')

  def tanquem_diaris(self):
    return self.agreguem('dayOfYear','dataTancament')

  def obrim_setmanals(self):
    return self.agreguem('week','dataCreacio')

  def tanquem_setmanals(self):
    return self.agreguem('week','dataTancament')

  def obrim_mensuals(self):
    return self.agreguem('month','dataCreacio')

  def tanquem_mensuals(self):
    return self.agreguem('month','dataTancament')

  def agreguem(self,periode,tipusData):
    # La cosa rara del SON es perque un diccionari de python no conserva l'ordre i aixo si
    pipeline=[
      {"$match": {tipusData:{"$ne":None}}},
      {"$project": {periode:{"$"+periode:"$"+tipusData},"any":{"$year":"$"+tipusData}}},
      {"$group": {"_id": {"any":"$any",periode:"$"+periode}, "tickets": {"$sum":1}}},
      {"$sort": SON([("_id.any",1),("_id."+periode,1)])}
    ]
    resultat=list(self.db.tickets.aggregate(pipeline))
    return resultat

  def agreguem_diari(self,tipusData):
    # La cosa rara del SON es perque un diccionari de python no conserva l'ordre i aixo si
    pipeline=[
      {"$match": {tipusData:{"$ne":None}}},      
      {"$project": {"dia": {"$dateToString": { "format": "%Y-%m-%d", "date":"$"+tipusData}}}},
      {"$group": {"_id": "$dia", "tickets": {"$sum":1}}},
      {"$sort": {"_id":1}}
    ]
    resultat=list(self.db.tickets.aggregate(pipeline))
    return resultat

  def oberts_mensuals(self):
    obrim=self.obrim_mensuals()
    tanquem=self.tanquem_mensuals()
    periode="month"
    obrim_map={}
    tanquem_map={}
    for t in obrim: obrim_map[(t["_id"]["any"],t["_id"][periode])]=t["tickets"]
    for t in tanquem: tanquem_map[(t["_id"]["any"],t["_id"][periode])]=t["tickets"]
    any_inici=obrim[0]["_id"]["any"]
    any_fi=tanquem[-1]["_id"]["any"]
    n_oberts=0
    llistes={'mes':[],'obrim':[],'tanquem':[],'oberts':[]}
    for a in range(any_inici,any_fi+1):
      for s in range(1,13):
        try:
          n_obrim=obrim_map[(a,s)]
        except:
          n_obrim=0
        try:
          n_tanquem=tanquem_map[(a,s)]
        except:
          n_tanquem=0          
        n_oberts+=n_obrim-n_tanquem
        llistes['mes'].append("%d-%d-%d" % (a,s,1));
        llistes['obrim'].append(n_obrim)
        llistes['tanquem'].append(n_tanquem)
        llistes['oberts'].append(n_oberts)
    return llistes

  def oberts_diaris(self):
    obrim=self.agreguem_diari('dataCreacio')
    tanquem=self.agreguem_diari('dataTancament')
    periode="dayOfYear"
    obrim_map={}
    tanquem_map={}
    for t in obrim: obrim_map[t["_id"]]=t["tickets"]
    for t in tanquem: tanquem_map[t["_id"]]=t["tickets"]
    dia_inici=obrim[0]["_id"]
    dia_fi=tanquem[-1]["_id"]
    n_oberts=0
    llistes={'dia':[],'obrim':[],'tanquem':[],'oberts':[]}
    dia=datetime.strptime(dia_inici,'%Y-%m-%d')
    fi=datetime.strptime(dia_fi,'%Y-%m-%d')
    while dia <= fi:                    
      d=dia.strftime("%Y-%m-%d")
      try:
        n_obrim=obrim_map[d]
      except:
        n_obrim=0
      try:
        n_tanquem=tanquem_map[d]
      except:
        n_tanquem=0          
      n_oberts+=n_obrim-n_tanquem
      llistes['dia'].append(d);
      llistes['obrim'].append(n_obrim)
      llistes['tanquem'].append(n_tanquem)
      llistes['oberts'].append(n_oberts)
      dia+=timedelta(days = 1)
    return llistes    