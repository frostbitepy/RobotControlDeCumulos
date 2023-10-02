import datetime


"""
def calcular_suma_vigente(inicio, vencimiento, capitales, fechasDesde, fechasHasta):
  
  Calcula la suma vigente de un conjunto de pólizas, teniendo en cuenta las fechas de vigencia de cada póliza.

  Args:
    inicio: Fecha de inicio del período de vigencia.
    vencimiento: Fecha de vencimiento del período de vigencia.
    capitales: Lista de capitales de las pólizas.
    polizas: Lista de nombres de las pólizas.
    endosos: Lista de endosos de las pólizas.
    fechasDesde: Lista de fechas de inicio de vigencia de las pólizas.
    fechasHasta: Lista de fechas de vencimiento de vigencia de las pólizas.

  Returns:
    La suma vigente de las pólizas.
  

  # Convertimos las fechas a formato datetime.

  # fechasDesde = [datetime.datetime.strptime(fecha.replace('/','-'),'%d-%m-%Y') for fecha in fechasDesde]
  # fechasHasta = [datetime.datetime.strptime(fecha.replace('/','-'),'%d-%m-%Y') for fecha in fechasHasta]

  # Calculamos el rango de fechas de vigencia de cada póliza.

  rangos_fechas = [(fechaInicio, fechaFin) for (fechaInicio, fechaFin) in zip(fechasDesde, fechasHasta)]

  # Creamos un DataFrame con los datos de las pólizas.

  df = pd.DataFrame({
    'capital': capitales,
    'fechaInicio': fechasDesde,
    'fechaFin': fechasHasta
  })

  # Calculamos la suma de los capitales de las pólizas que están vigentes.

  montoVigente = np.sum(df[df['fechaInicio'] <= inicio].capital) + np.sum(df[df['fechaFin'] >= inicio].capital)

  return montoVigente 
"""

# Realiza la suma de los capitales de las polizas vigentes teniendo en cuenta 
# si las fechas se superponen.
def calcular_suma_vigente(inicio, vencimiento, capitales, fechasDesde, fechasHasta):
  montoVigente = 0
  fechaInicio = datetime.datetime.strptime(inicio.replace('/','-'),'%d-%m-%Y')
  fechaFin = datetime.datetime.strptime(vencimiento.replace('/','-'),'%d-%m-%Y')
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



  
  
  
