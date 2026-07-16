# -*- coding: utf-8 -*-
"""
Autor: Yo!
Fecha: 2026
"""

NOMBRE_TABLA = "FACT_DISC_SNAPSHOT_NINOS"

# CONSTANTE: INDICADORES SOLO (Para SP_CargarFuncionAMatriz)
# Formato: (NombreColumna, FuncionSQL)

INDICADORESSOLO = [    
    
    ('NDQ29', "dbo.Ninos_ConCert('P072,P073','N,R')"),
    ('NDQ30', "dbo.Ninos_ConCert('P070','N,R')"),

]

# CONSTANTE: INDICADORES MULTIPLE (Para SP_CargarFuncionAMatriz_Multi)
# Formato: (MapeoColumnasJSON, FuncionSQL)

INDICADORESMULTIPLE = [
    (
        '"0d-11A":"NDQ119", "12A-17A":"NDQ120", "18A-29A":"NDQ121", "30A-59A":"NDQ122", "60A+":"NDQ123"',
        "dbo.Multiples_ConCert('fisico', 'sensorial', 'N,R');"
    ),
    (
        '"0d-11A":"NDQ124", "12A-17A":"NDQ125", "18A-29A":"NDQ126", "30A-59A":"NDQ127", "60A+":"NDQ128"',
        "dbo.Multiples_SinCert('fisico', 'sensorial', 'N,R');"
    ),
    
]