#Adrián Solís León 2ºDAM

import pandas as pd
import datapane as dp

fichero_csv = "DI_U05_A02_PP_E_01.csv"
df = pd.read_csv(fichero_csv)

total_ventas = df['Ventas'].sum()

ventas_por_anio = df.groupby('Año')['Ventas'].sum()
anio_top = ventas_por_anio.idxmax()

ventas_2021 = df[df['Año'] == 2021]['Ventas'].sum()
ventas_2020 = df[df['Año'] == 2020]['Ventas'].sum()


logotipo = dp.Media(file='DI_U05_A02_PP_E_02.jpg') 

titulo = dp.HTML(
    '<p style="font-size:30px; text-align:center; color:#ffffff; background-color:#2c3e50; padding:10px;">'
    'Informe de Ventas Anuales</p>'
)

resumen_texto = dp.Text(
    "### Resumen Ejecutivo\n"
    "Este informe presenta la evolución de las ventas globales. Estos datos son críticos para la dirección "
    "ya que permiten identificar tendencias de consumo, evaluar el crecimiento interanual y "
    "optimizar la asignación de recursos en las regiones más rentables."
)

indicadores_resumen = dp.Group(
    dp.BigNumber(heading="Total Ventas Acumuladas", value=f"{total_ventas} €"),
    dp.BigNumber(heading="Año Récord de Ventas", value=anio_top),
    columns=2
)

comparativa_2021 = dp.BigNumber(
    heading="Ventas Totales 2021",
    value=f"{ventas_2021} €",
    change=ventas_2021 - ventas_2020,
    is_upward_change=ventas_2021 > ventas_2020
)

tabla_interactiva = dp.DataTable(df)

fichero_adjunto = dp.Attachment(file=fichero_csv, caption="Descargar datos originales (CSV)")

report = dp.Report(
    logotipo,
    titulo,
    resumen_texto,
    indicadores_resumen,
    comparativa_2021,
    tabla_interactiva,
    fichero_adjunto
)

report.save(path='Informe_Ejercicio2.html', open=True)