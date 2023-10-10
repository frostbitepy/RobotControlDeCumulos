import datetime
from automation_scripts.script_logger import logger

# Realiza la suma de los capitales de las polizas vigentes teniendo en cuenta 
# si las fechas se superponen.
def calcular_suma_vigente(inicio, vencimiento, capitales, fechasDesde, fechasHasta):
    montoVigente = 0
    logger.info("Fechas desde: %s", fechasDesde)
    logger.info("Fechas hasta: %s", fechasHasta)
    try:
    # Code that might raise an exception
      datetime.datetime.strptime(inicio.replace('/','-'),'%d-%m-%Y')
      datetime.datetime.strptime(vencimiento.replace('/','-'),'%d-%m-%Y')
      logger.info("Se ralizo la conversion de formato de fechas")
    except:
    # Code to handle the exception
      fechaInicio = inicio
      fechaFin = vencimiento
      logger.info("No se realizo la conversion de formato de fechas") 

    logger.info("Fecha inicio: %s", fechaInicio)
    logger.info("Fecha fin: %s", fechaFin)
    for(desde,hasta,capital) in zip(fechasDesde,fechasHasta,capitales):    
      # desde = datetime.datetime.strptime(desde.replace('/','-'),'%d-%m-%Y')
      # hasta = datetime.datetime.strptime(hasta.replace('/','-'),'%d-%m-%Y')
      if (fechaInicio >= desde and fechaInicio <= hasta) or (fechaFin >= desde and fechaFin <= hasta):
        montoVigente += capital

    return montoVigente


def calcular_inclusion(montoVigente, montoRecibido):
    limiteCumulo = 3000000000
    if montoVigente >= limiteCumulo:
      montoInclusion = 0
      montoExclusion = montoRecibido
    elif (limiteCumulo - montoVigente) < montoRecibido:
      if (limiteCumulo - montoVigente) <= 0:
        montoInclusion = 0
        montoExclusion = montoRecibido
      else:
        montoInclusion = limiteCumulo - montoVigente
        montoExclusion = montoRecibido - montoInclusion
    elif (limiteCumulo - montoVigente) >= montoRecibido:
      montoInclusion = montoRecibido
      montoExclusion = 0

    return montoInclusion

def calcular_exclusion(montoVigente, montoRecibido):
    limiteCumulo = 3000000000
    if montoVigente >= limiteCumulo:
      montoInclusion = 0
      montoExclusion = montoRecibido
    elif (limiteCumulo - montoVigente) < montoRecibido:
      if (limiteCumulo - montoVigente) <= 0:
        montoInclusion = 0
        montoExclusion = montoRecibido
      else:
        montoInclusion = limiteCumulo - montoVigente
        montoExclusion = montoRecibido - montoInclusion
    elif (limiteCumulo - montoVigente) >= montoRecibido:
      montoInclusion = montoRecibido
      montoExclusion = 0

    return montoExclusion



  
  
  
