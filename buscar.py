import sys
import pymongo

class Consultes:

  def __init__(self):
    client = pymongo.MongoClient()  
    self.db=client.ticketsdb    

  def busca(self,text):
    return list(self.db.tickets.find({"$text":{"$search":text}})
     .sort([("estat",pymongo.ASCENDING),("dataTancament",pymongo.DESCENDING), ("dataCreacio",pymongo.DESCENDING)])
     )

  def obrim_setmanals(self):
    return [{"_id":{"any":2014,"setmana":10},"tickets":2},
            {"_id":{"any":2015,"setmana":3},"tickets":2}]

  def tanquem_setmanals(self):
    return [{"_id":{"any":2014,"setmana":11},"tickets":1},
            {"_id":{"any":2015,"setmana":6},"tickets":2}]

  def oberts_setmanals(self):
    obrim=self.obrim_setmanals()
    tanquem=self.tanquem_setmanals()
    obrim_map={}
    tanquem_map={}
    for t in obrim: obrim_map[(t["_id"]["any"],t["_id"]["setmana"])]=t["tickets"]
    for t in tanquem: tanquem_map[(t["_id"]["any"],t["_id"]["setmana"])]=t["tickets"]
    any_inici=obrim[0]["_id"]["any"]
    any_fi=tanquem[-1]["_id"]["any"]
    n_oberts=0
    tickets=[]
    for a in range(any_inici,any_fi+1):
      for s in range(0,52):
        try:
          n_obrim=obrim_map[(a,s)]
        except:
          n_obrim=0
        try:
          n_tanquem=tanquem_map[(a,s)]
        except:
          n_tanquem=0          
        n_oberts+=n_obrim-n_tanquem
        linia={"_id":{"any":a,"setmana":s},"obrim":n_obrim,"tanquem":n_tanquem,"oberts":n_oberts}
        tickets.append(linia)
        print linia
    return {"oberts-setmanals":tickets}