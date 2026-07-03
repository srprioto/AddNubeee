blocks2 = []
num_rows2 = len(df2)

for i in range(0, num_rows2, 5):
    block_df = df2.iloc[i:i+5]
    
    pairs = []
    func_name = None
    
    for idx, row in block_df.iterrows():
        code = str(row[0]).strip()
        age = str(row[1]).strip()
        func = row[2]
        
        pairs.append(f'"{age}":"{code}"')
        
        if pd.notna(func) and str(func).strip() != "":
            func_name = str(func).strip()
            
    dict_str = ", ".join(pairs)
    
    if not func_name:
        func_name = ""
        
    blocks2.append((dict_str, func_name))

# Format the python output
output_lines2 = []
output_lines2.append("INDICADORESMULTIPLE_2 = [")
for b in blocks2:
    output_lines2.append("    (")
    output_lines2.append(f"        '{b[0]}',")
    output_lines2.append(f'        "{b[1]}"')
    output_lines2.append("    ),")
output_lines2.append("]")

output_content2 = "\n".join(output_lines2)

# Save to .py file
with open("indicadores_multiple_bloque3.py", "w", encoding="utf-8") as f:
    f.write(output_content2)

print(f"Processed {len(blocks2)} blocks successfully for second file.")