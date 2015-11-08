from suds.client import Client
from soa.service import SOAService
import settings

class GestioTiquets(SOAService):

  def __init__(self):
    self.url="https://bus-soa.upc.edu/gN6/GestioTiquetsv3?wsdl"
    self.username_gn6=settings.get("username_gn6")
    self.password_gn6=settings.get("password_gn6")
    self.domini=settings.get("domini")
    SOAService.__init__(self)

  def consulta_tiquets(self,**kwargs):
    resultat=self.client.service.ConsultaTiquetsDades(
      username=self.username_gn6,
      password=self.password_gn6,
      domini=self.domini,**kwargs)
    return resultat


class GestioTiquets2:

  def consulta_tiquets(self,**kwargs):
    return [
     {"codi":1,"titol":"hola"},
     {"codi":2,"titol":"adeu"}
    ]