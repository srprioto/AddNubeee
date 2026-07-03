# -*- coding: utf-8 -*-
"""
Autor: Yo!
Fecha: 2026
"""

NOMBRE_TABLA = "FACT_DISC_SNAPSHOT_REHABFISIC_BL1"

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
        '"0d-11A":"NDQ689", "12A-17A":"NDQ690", "18A-29A":"NDQ691", "30A-59A":"NDQ692", "60A+":"NDQ693"',
        "dbo.RehabFisica_ConCert('A178,A1782,T889', 'N,R');"
    ),
    (
        '"0d-11A":"NDQ1509", "12A-17A":"NDQ1510", "18A-29A":"NDQ1511", "30A-59A":"NDQ1512", "60A+":"NDQ1513"',
        "dbo.RehabFisica_EnRiesgo('T200,T201,T202,T203,T204,T205,T206,T355,T356,T357', 'N,R');"
    ),
]

