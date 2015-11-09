from suds.client import Client
from soa.service import SOAService
import settings

class GestioTiquets(SOAService):

  def __init__(self):
    self.url="https://bus-soa.upc.edu/gN6/GestioTiquetsv2?wsdl"
    self.username_gn6=settings.get("username_gn6")
    self.password_gn6=settings.get("password_gn6")
    self.domini=settings.get("domini")
    SOAService.__init__(self)

  def consulta_tiquets(self,estat='',dataCreacioInici='',dataCreacioFi='',dataTancamentInici='',dataTancamentFi='',client='',solicitant='',ip=''):
    resultat=self.client.service.ConsultaTiquets(
      self.username_gn6,self.password_gn6,self.domini,
      '',estat,dataCreacioInici,dataCreacioFi,dataTancamentInici,dataTancamentFi,client,solicitant,ip)
    return resultat.llistaTiquets


class GestioTiquets2:

  def consulta_tiquets(self,**kwargs):
    return [
     {"codi":1,"titol":"hola"},
     {"codi":2,"titol":"adeu"}
    ]