import pandas as pd

# 1. Lee tu archivo CSV (asegúrate de que el nombre coincida)
nombre_archivo_csv = 'item.csv' 
df = pd.read_csv(nombre_archivo_csv, header=None)

blocks = []
num_rows = len(df)

# 2. Agrupa las filas en bloques de 5 en 5
for i in range(0, num_rows, 5):
    block_df = df.iloc[i:i+5]
    
    pairs = []
    func_name = None
    
    for idx, row in block_df.iterrows():
        code = str(row[0]).strip()
        age = str(row[1]).strip()
        func = row[2]
        
        # Arma los mapeos "edad":"código"
        pairs.append(f'"{age}":"{code}"')
        
        # Captura la función SQL que está en la primera fila de las 5
        if pd.notna(func) and str(func).strip() != "":
            func_name = str(func).strip()
            
    dict_str = ", ".join(pairs)
    
    if not func_name:
        func_name = ""
        
    blocks.append((dict_str, func_name))

# 3. Construye el formato de texto final para el array de Python
output_lines = []
output_lines.append("INDICADORESMULTIPLE_2 = [")
for b in blocks:
    output_lines.append("    (")  # <-- Aquí estaba el error, debe ser solo esto
    output_lines.append(f"        '{b[0]}',")
    output_lines.append(f'        "{b[1]}"')
    output_lines.append("    ),")
output_lines.append("]")

output_content = "\n".join(output_lines)

# 4. Exporta y guarda el resultado directamente a un archivo .py
nombre_salida = "resultado_indicadores.py"
with open(nombre_salida, "w", encoding="utf-8") as f:
    f.write(output_content)

print(f"¡Conversión exitosa!")
print(f"Se procesaron {len(blocks)} bloques.")
print(f"El archivo se guardó como: '{nombre_salida}' en tu carpeta actual.")