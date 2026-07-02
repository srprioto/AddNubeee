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
        "dbo.RehabFisica_ConCert('A178,A1782,A800,B690,B91X,B941,C720,C721,D334,G041,G042,G048,G049,G050,G051,G052,G058,G114,G320,G35X,G360,G373,G820,G821,G822,G823,G824,G825,G834,G950,G951,G952,G958,G959,G971,M471,M480,M500,Q050,Q051,Q052,Q053,Q054,Q055,Q056,Q057,Q058,Q059,Q060,Q061,Q062,Q063,Q064,Q068,Q069,S140,S141,S240,S241,S340,S341,T093,T889', 'N,R');"
    ),
    (
        '"0d-11A":"NDQ1509", "12A-17A":"NDQ1510", "18A-29A":"NDQ1511", "30A-59A":"NDQ1512", "60A+":"NDQ1513"',
        "dbo.RehabFisica_EnRiesgo('T200,T201,T202,T203,T204,T205,T206,T207,T208,T209,T200,T201,T202,T203,T204,T205,T206,T207,T210,T220,T230,T240,T250,T260,T270,T280,T290,T300,T310,T311,T312,T313,T314,T315,T316,T317,T318,T319,T310,T311,T312,T313,T314,T315,T316,T317,T318,T319,T320,T321,T322,T323,T324,T325,T326,T327,T328,T329,T320,T321,T322,T323,T324,T325,T326,T327,T328,T329,T330,T331,T332,T333,T334,T335,T336,T337,T338,T339,T330,T331,T332,T333,T334,T335,T336,T337,T338,T339,T340,T341,T342,T343,T344,T345,T346,T347,T348,T349,T340,T341,T342,T343,T344,T345,T346,T347,T348,T349,T350,T351,T352,T353,T354,T355,T356,T357,T358,T359,T350,T351,T352,T353,T354,T355,T356,T357', 'N,R');"
    ),
]

