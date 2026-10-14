# Alexandro Aguilar Valadez NC = 0007
# NL = 1
import sys
import os
import io
import pandas as pd

# Permitir importar dicc-0007.py desde la subcarpeta hermana (si aplica)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'datos-de-entrada-ml-0007')))

# Datos de empleados
datos_empleados = {
    "Nombre": ["Luis", "Elena", "Pedro", "Rosa", "Jorge", "Marta"],
    "Edad": [28, 34, 45, 29, 38, 52],
    "Salario": [15000, 18000, 22000, 16000, 20000, 25000]
}

print("Alexandro Aguilar Machine Learning pandas, NC 0007")

# Variable para almacenar las salidas y guardarlas en el archivo .md
contenido_md = []
encabezado_pie = "Alexandro Aguilar Machine Learning pandas, NC 0007"
contenido_md.append(f"# Reporte de Análisis de Datos - Pandas\n\n`{encabezado_pie}`\n")

def registrar(titulo, contenido):
    """Muestra el resultado en terminal y lo formatea para el archivo Markdown."""
    print(f"\n--- {titulo} ---")
    print(contenido)
    contenido_md.append(f"## {titulo}\n```text\n{contenido}\n```\n")

# 1. Convertir diccionario a DataFrame
# (Nota: Si lo importas desde dicc_0007, usa: df = pd.DataFrame(dicc_0007.datos_empleados))
df = pd.DataFrame(datos_empleados)
registrar("1. DataFrame Convertido", df)

# 2. Información Estructural
registrar("2.1 Primeras Filas (head)", df.head(2))
registrar("2.2 Últimas Filas (tail)", df.tail(2))
registrar("2.3 Dimensiones (Filas, Columnas)", df.shape)
registrar("2.4 Tipos de Datos por Columna", df.dtypes)

# Capturar salida de df.info()
buffer = io.StringIO()
df.info(buf=buffer)
registrar("2.5 Información General (info)", buffer.getvalue())

# 3. Estadísticas Generales de una Columna Numérica (Salario)
registrar("3. Estadísticas Generales de la Columna 'Salario'", df['Salario'].describe())

# 4. Ordenar Ascendente por Salario
df_asc_salario = df.sort_values(by="Salario", ascending=True)
registrar("4. Ordenar Ascendente por Salario", df_asc_salario)

# 5. Ordenar Descendente por Edad
df_desc_edad = df.sort_values(by="Edad", ascending=False)
registrar("5. Ordenar Descendente por Edad", df_desc_edad)

# 7. Guardar el archivo resultados-ml-0007.md dentro de resultados-0007
carpeta_resultados = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'resultados-0007'))
os.makedirs(carpeta_resultados, exist_ok=True)
ruta_archivo_md = os.path.join(carpeta_resultados, "resultados-ml-0007.md")

contenido_md.append(f"`{encabezado_pie}`")

with open(ruta_archivo_md, "w", encoding="utf-8") as f:
    f.write("\n".join(contenido_md))

print(f"\n[ÉXITO] Archivo generado correctamente en: {ruta_archivo_md}")
print("Alexandro Aguilar Machine Learning pandas, NC 0007")
