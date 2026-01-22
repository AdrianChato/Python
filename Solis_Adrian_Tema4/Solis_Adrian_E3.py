#Adrián Solís león 2ºDAM

import pandas as pd
import datapane as dp

df = pd.read_csv("uso_servicios_municipales.csv")

#Esta bien pero me da error, me da error de version con el .sum y la versión, algo muy raro, pero esta bien creo

datos = df.groupby(["servicio"], sort=False).sum()
tarta = datos.plot.pie(y="servicio", legend=False, ylabel="")
grafico_tarta = dp.Plot(tarta)

datos2 = df.groupby(["anio"], sort=False).sum()
lineas = datos2.plot(y="anio", marker="o")
grafico_lineas = dp.Plot(lineas)

datos3 = df.groupby(["distrito"], sort=False).sum()
barras = datos3.plot.bar(y="distrito")
grafico_barras = dp.Plot(barras)

reporte = dp.Report(
    grafico_tarta,
    grafico_lineas,
    grafico_barras
)

reporte.save("Solis_Adrian_E3_graficos.html", open=True)