from sebaot_logging import start_sebaot_application, stop_sebaot_application
from excel_operations import read_operations_gs, extract_operations
from imprimir_listado import generar_listado_sebaot
from calculos import calcular_suma_vigente, calcular_exclusion, calcular_inclusion, calcular_suma_vigente2



ubicacionOperaciones = "C:/Users/francisco/Desktop/Excel/PlanillaDeOperaciones.xlsx"
ubicacionListado = "C:/Users/francisco/Desktop/Excel/listado.xlsx"

if __name__ == "__main__":
    # Start the Sebaot application
    start_sebaot_application()

    # Read the operations from the Excel sheet
    new_operations = read_operations_gs(ubicacionOperaciones)

    # Itera a través de los números de documento en el diccionario:
    for documento, fecha_inicio, fecha_vencimiento, suma_asegurada in zip(new_operations["nro_documento"], new_operations["fecha_inicio"], new_operations["fecha_vencimiento"], new_operations["suma_asegurada"]):
        # Llama a la función generar_listado_sebaot para cada número de documento:
        generar_listado_sebaot(documento)
        print("Listado generado para el documento:", documento)
        listado_operaciones = extract_operations(ubicacionListado)
        monto_vigente = calcular_suma_vigente(fecha_inicio, fecha_vencimiento, listado_operaciones["Poliza"], listado_operaciones["Desde"], listado_operaciones["Hasta"])
        print("Suma vigente 1: " + str(monto_vigente))
        monto_vigente2 = calcular_suma_vigente2(fecha_inicio, fecha_vencimiento, listado_operaciones["Poliza"], listado_operaciones["Desde"], listado_operaciones["Hasta"])
        print("Suma vigente 2: " + str(monto_vigente2))
        monto_inclusion = calcular_inclusion(monto_vigente, suma_asegurada)
        monto_exclusion = calcular_exclusion(monto_vigente, suma_asegurada)
        print("Inclusion 1: " + str(monto_inclusion))
        print("Exclusion 1: " + str(monto_exclusion))
        monto_inclusion2 = calcular_inclusion(monto_vigente2, suma_asegurada)
        monto_exclusion2 = calcular_exclusion(monto_vigente2, suma_asegurada)
        print("Inclusion 2: " + str(monto_inclusion2))
        print("Exclusion 2: " + str(monto_exclusion2))
        
    stop_sebaot_application()    

