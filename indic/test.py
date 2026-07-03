with open("item.csv", "r", encoding="utf-8") as f:
    for i in range(15):
        linea = f.readline()
        print(f"{i+1}: {repr(linea)}")