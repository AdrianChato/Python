#Adrián Solís león 2ºDAM

import pandas as pd
import datapane as dp

df = pd.read_csv("uso_servicios_municipales.csv")

datos = df.groupby(["distrito"], sort=False).value_counts()

tabla_dinamica = dp.DataTable(datos, label="tabla dinámica")

reporte = dp.Report(tabla_dinamica)

reporte.save("Solis_Adrian_E1_tabla.html", open=True)
