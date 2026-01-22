#Adrián Solís león 2ºDAM

import pandas as pd
import datapane as dp

df = pd.read_csv("uso_servicios_municipales.csv")

datos = df.groupby(["numero_usos"], sort=False).value_counts()

tabla_dinamica = dp.DataTable(datos, label="tabla dinámica")

reporte = dp.Report(
    dp.Text("##Resumen-ejecutivo-Uso de servicios municipales"),
    dp.Text("##Con esta tabla podemos ver los diferentes usos" \
    "de los servivios usados en el municipio, ya sea por distrito y año"),
    tabla_dinamica,    
    )

reporte.save("Solis_Adrian_E2_resumen.html", open=True)



