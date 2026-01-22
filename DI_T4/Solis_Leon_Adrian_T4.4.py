#Adrián solís León 2ºDAM

import pandas as pd
import datapane as dp

# Cargamos el CSV 
df = pd.read_csv("DI_U05_A02_PP_E_01.csv")

# Ventas por tipo de producto (para gráfico de tarta)
ventas_tipo = df.groupby(["Tipo de producto"]).sum(numeric_only=True)

# Ventas por año (para gráfico de líneas)
ventas_ano = df.groupby(["Año"], sort=False).sum(numeric_only=True)

# Ventas por región (para gráfico de barras)
ventas_region = df.groupby(["Región"]).sum(numeric_only=True)

# Tabla resumen por año y tipo de producto
tabla_ano_tipo = df.pivot_table(
    index="Año",
    columns="Tipo de producto",
    values="Ventas",
    aggfunc="sum"
)

# Gráfico de tarta de la distribución por tipo de producto
grafico_tarta = ventas_tipo.plot.pie(
    y="Ventas",
    legend=False,
    ylabel=""
)
bloque_tarta = dp.Plot(grafico_tarta, label="Tarta por tipo de producto")

# Gráfico de líneas de la evolución de ventas por año
grafico_lineas = ventas_ano.plot(
    y="Ventas",
    marker="o",
    title="Evolución de ventas por año"
)
bloque_lineas = dp.Plot(grafico_lineas, label="Líneas por año")

# Gráfico de barras de las ventas por región
grafico_barras = ventas_region.plot.bar(
    y="Ventas",
    title="Ventas por región"
)
bloque_barras = dp.Plot(grafico_barras, label="Barras por región")

# Tabla completa de datos
bloque_tabla_completa = dp.DataTable(df, label="Tabla completa")

# Tabla resumen por año y tipo
bloque_tabla_resumen = dp.DataTable(tabla_ano_tipo.reset_index(), label="Tabla resumen año-tipo")

# Agrupamos algunos componentes en una cuadrícula para aprovechar el espacio
grupo_resumen = dp.Group(
    dp.Text("### Resumen visual de las ventas"),
    bloque_tarta,
    bloque_barras,
    columns=2, 
)

# Selector para alternar entre tabla completa y tabla resumen
selector_tablas = dp.Select(
    blocks=[
        bloque_tabla_completa,
        bloque_tabla_resumen
    ]
)

# Selector para alternar entre diferentes vistas gráficas
selector_graficos = dp.Select(
    blocks=[
        bloque_lineas,
        bloque_tarta,
        bloque_barras
    ]
)

# Página 1 con la visión general de todo
pagina_general = dp.Page(
    title="Visión general",
    blocks=[
        dp.Text("# Informe de ventas"),
        dp.Text("## 1. Resumen general"),
        grupo_resumen,         
        dp.Text("## 2. Evolución temporal"),
        bloque_lineas
    ]
)

# Página 2 con las tablas y selectores
pagina_detalle = dp.Page(
    title="Detalle y tablas",
    blocks=[
        dp.Text("## 3. Tablas de datos"),
        dp.Text("Puedes alternar entre la tabla completa y la tabla resumen:"),
        selector_tablas,        
        dp.Text("## 4. Diferentes vistas gráficas"),
        dp.Text("Selecciona la vista que quieras ver:"),
        selector_graficos       
    ]
)

#Crea el informe
reporte = dp.Report(
    pagina_general,   
    pagina_detalle    
)

# Lo guarda y lo abre en el navegador
reporte.save("solis_adrian_T4.4.html", open=True)