import pandas as pd

# ==========================================
# 1. Leer el archivo detectando el separador
# ==========================================

nombre_archivo_csv = "item.csv"

# Detectar el separador automáticamente
with open(nombre_archivo_csv, "r", encoding="utf-8-sig") as f:
    primera_linea = f.readline()

if primera_linea.count(";") >= 2:
    separador = ";"
elif primera_linea.count(",") >= 2:
    separador = ","
elif "\t" in primera_linea:
    separador = "\t"
else:
    raise ValueError("No se pudo detectar el separador del archivo.")

print(f"Separador detectado: '{separador}'")

# Leer el archivo
df = pd.read_csv(
    nombre_archivo_csv,
    sep=separador,
    header=None,
    encoding="utf-8-sig"
)

# ==========================================
# 2. Procesar los datos
# ==========================================

blocks = []
num_rows = len(df)

# Agrupar las filas en bloques de 5
for i in range(0, num_rows, 5):
    block_df = df.iloc[i:i + 5]

    pairs = []
    func_name = None

    for _, row in block_df.iterrows():
        code = str(row[0]).strip()
        age = str(row[1]).strip()

        # Evitar error si la tercera columna no existe
        func = row[2] if len(row) > 2 else None

        # Construir el diccionario edad:código
        pairs.append(f'"{age}":"{code}"')

        # La función SQL solo viene en la primera fila del bloque
        if pd.notna(func) and str(func).strip() != "":
            func_name = str(func).strip()

    dict_str = ", ".join(pairs)

    if func_name is None:
        func_name = ""

    blocks.append((dict_str, func_name))

# ==========================================
# 3. Construir el archivo de salida
# ==========================================

output_lines = []
output_lines.append("INDICADORESMULTIPLE = [")

for dict_str, func_name in blocks:
    output_lines.append("    (")
    output_lines.append(f"        '{dict_str}',")
    output_lines.append(f'        "{func_name}"')
    output_lines.append("    ),")

output_lines.append("]")

output_content = "\n".join(output_lines)

# ==========================================
# 4. Guardar el resultado
# ==========================================

nombre_salida = "resultado_indicadores.py"

with open(nombre_salida, "w", encoding="utf-8") as f:
    f.write(output_content)

print("\n======================================")
print("Conversión exitosa.")
print(f"Separador utilizado : '{separador}'")
print(f"Bloques procesados  : {len(blocks)}")
print(f"Archivo generado    : {nombre_salida}")
print("======================================")