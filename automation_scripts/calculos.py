import datetime
import numpy as np
import pandas as pd

def calcular_suma_vigente(inicio, vencimiento, capitales, fechasDesde, fechasHasta):
  """
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
  """

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


if __name__ == "__main__":
    inicio = "01/01/2023"
    vencimiento = "31/12/2023"
    capitales = [10000, 20000, 30000]
    fechasDesde = ["01/01/2023", "02/01/2023", "03/01/2023"]
    fechasHasta = ["31/12/2023", "30/12/2023", "29/12/2023"]

    montoVigente = calcular_suma_vigente(inicio, vencimiento, capitales, fechasDesde, fechasHasta)

    print(montoVigente)

  
  
  
