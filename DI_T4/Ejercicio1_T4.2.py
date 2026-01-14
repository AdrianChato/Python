#Adrián Solís León 2ºDAM

import pandas as pd
import datapane as dp

fichero_csv = "DI_U05_A02_02.csv"
df = pd.read_csv(fichero_csv)

tabla_interactiva = dp.DataTable(df)

titulo = dp.HTML(
    '<p style="font-size:24px; text-align:center; color:#ffffff; background-color:#2c3e50; padding:10px;">'
    'Ejercicio 1: Análisis de Ventas Mensuales</p>'
)

report = dp.Report(
    titulo,
    tabla_interactiva
)

report.save(path="Informe_Ejercicio1.html", open=True)