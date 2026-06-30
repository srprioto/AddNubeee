# -*- coding: utf-8 -*-
"""
Catálogo de Indicadores - Modos Unitario y Múltiple
Autor: Sistema Automatizado
Fecha: 2026
"""

# ====================================================================================
# CONSTANTE: INDICADORES SOLO (Para SP_CargarFuncionAMatriz)
# ====================================================================================
# Formato: (NombreColumna, FuncionSQL)
INDICADORESSOLO = [
    ('NDQ29', "dbo.Ninos_Riesgo('P072,P073','N,R')"),
    ('NDQ30', "dbo.Ninos_SinCert('P072,P073','N,R')"),
    # Puedes seguir agregando más indicadores individuales aquí...
]

# ====================================================================================
# CONSTANTE: INDICADORES MULTIPLE (Para SP_CargarFuncionAMatriz_Multi)
# ====================================================================================
# Formato: (MapeoColumnasJSON, FuncionSQL)
INDICADORESMULTIPLE = [
    (
        '"0d-11A":"NDQ124", "12A-17A":"NDQ125", "18A-29A":"NDQ126", "30A-59A":"NDQ127", "60A+":"NDQ128"', "dbo.Multiples_SinCert('fisico', 'sensorial', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ129", "12A-17A":"NDQ130", "18A-29A":"NDQ131", "30A-59A":"NDQ132", "60A+":"NDQ133"', 
        "dbo.Multiples_EnRiesgo('fisico', 'sensorial', 'N,R')"
    ),
    
]