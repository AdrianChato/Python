#Adrián Solís león 2ºDAM

import pandas as pd
import datapane as dp

df = pd.read_csv("uso_servicios_municipales.csv")

datos_tabla = df.groupby(["distrito"], sort=False).value_counts()
tabla_dinamica = dp.DataTable(datos_tabla, label="tabla dinámica")

datos_tarta = df.groupby(["servicio"], sort=False).sum()
tarta = datos_tarta.plot.pie(y="servicio", legend=False, ylabel="")
grafico_tarta = dp.Plot(tarta)

datos_lineas = df.groupby(["anio"], sort=False).sum()
lineas = datos_lineas.plot(y="anio", marker="o")
grafico_lineas = dp.Plot(lineas)

datos_barras = df.groupby(["distrito"], sort=False).sum()
barras = datos_barras.plot.bar(y="distrito")
grafico_barras = dp.Plot(barras)

#Al no ir el 3 que no se porque no funciona este tampoco, pero esta bien hecho

grupo = dp.Group(tabla_dinamica, columns=1)

selector = dp.Select(blocks=[grafico_barras,grafico_lineas,grafico_tarta], ylabel="graficos")

pagina_grupo = dp.Page(title="tabla", blocks=[grupo])
pagina_graficos = dp.Page(title="graficos", blocks=[selector])

reporte = dp.Report(pagina_graficos, pagina_grupo)

reporte.save("Solis_Adrian_E4_informe_organizado.html", open=True)