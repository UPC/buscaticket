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

  def consulta_tiquet(self,codi):
    resultat=self.consulta_tiquets(codi=codi)
    print resultat
    return resultat.llistaTiquets[0]

  def consulta_tiquets(self,**kwargs):
    resultat=self.client.service.ConsultaTiquets(
      username=self.username_gn6,
      password=self.password_gn6,
      domini=self.domini,**kwargs)
    return resultat

  def afegir_comentari_tiquet(self,**kwargs):
    resultat=self.client.service.AfegirComentariTiquet(
      username=self.username_gn6,
      password=self.password_gn6,
      domini=self.domini,**kwargs)
    return resultat

  def alta_tiquet(self,solicitant,client='', assumpte='', descripcio='', equipResolutor='', assignatA='', producte='', subservei='', urgencia='GRAVETAT_MITJA', impacte='', proces='PROCES_AUS', procesOrigen='', estat='TIQUET_STATUS_OBERT', ip='', enviarMissatgeCreacio='S', enviarMissatgeTancament='N', imputacioAutomatica='N', infraestructura=''):
    resultat=self.client.service.AltaTiquet(
      self.username_gn6,
      self.password_gn6,
      self.domini,
      solicitant,
      client,
      assumpte,
      descripcio,
      equipResolutor,
      assignatA,
      producte,
      subservei,
      urgencia,
      impacte,
      proces,
      procesOrigen,
      estat,
      ip,
      enviarMissatgeCreacio,
      enviarMissatgeTancament,
      imputacioAutomatica,
      infraestructura)
    return resultat

  def annexar_fitxer_tiquet(self,codiTiquet,usuari,nomFitxer,fitxerBase64):
    resultat=self.client.service.AnnexarFitxerTiquet(
      self.username_gn6,
      self.password_gn6,
      self.domini,
      codiTiquet,
      usuari,
      nomFitxer,
      fitxerBase64)
    return resultat
	
  def modificar_tiquet(self,
    codiTiquet,
    equipResolutor='',
    assignatCn='',
    proces='',
    estat='',
    dataCaducitat='',
    codiTancament='',
    producte='',
    subservei='',
    tipus='',
    dataResol='',
    solicitant='',
    client='',
    telefonSolicitant='',
    emailSolicitant='',
    dadesContacteSolicitant='',
    numInventari='',
    numElements='',
    ip='',
    assumpte='',
    descripcio='',
    origen='',
    urgencia='',
	impacte=''
    ):
    resultat=self.client.service.ModificarTiquet(
      self.username_gn6,
      self.password_gn6,
      self.domini,
	  codiTiquet,
      equipResolutor,
      assignatCn,
      proces,
      estat,
      dataCaducitat,
      codiTancament,
      producte,
      subservei,
      tipus,
      dataResol,
      solicitant,
      client,
      telefonSolicitant,
      emailSolicitant,
      dadesContacteSolicitant,
      numInventari,
      numElements,
      ip,
      assumpte,
      descripcio,
      origen,
      urgencia,
	  impacte
	  )
    return resultat

	
