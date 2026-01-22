#Adrián Solís León 2ºDAM

import pandas as pd
import datapane as dp

df = pd.read_csv("DI_U05_A02_PP_E_01.csv")

ventas_tipo = df.groupby(["Tipo de producto"]).sum()

#Grafico de tartas

grafico_tarta = ventas_tipo.plot.pie(
     y="Ventas",
    legend=False,
    ylabel=""
)
bloque_tarta = dp.Plot(grafico_tarta)

#Grafico de Lineas

ventas_ano = df.groupby(["Año"], sort = False).sum()
ultimos_2 = ventas_ano.tail(3)

grafico_lineas = ultimos_2.plot(y="Ventas")
bloque_lineas = dp.Plot(grafico_lineas)

#Grafico de barras

ventas_region = df.groupby(["Región"]).sum()

grafico_barras = ventas_region.plot.bar(y="Ventas")
bloque_barras = dp.Plot(grafico_barras)

#Union de todo

reporte = dp.Report(
    dp.Text("# Informe de ventas"),

    dp.Text("## 1. Distribución por tipo de producto"),
    bloque_tarta,

    dp.Text("## 2. Evolución en los últimos 2 años"),
    bloque_lineas,

    dp.Text("## 3. Ventas por región"),
    bloque_barras,
)

#Creacion del HTML

reporte.save("informe_ventas.html", open=True)