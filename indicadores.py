# -*- coding: utf-8 -*-
"""
Autor: Yo!
Fecha: 2026
"""

NOMBRE_TABLA = "FACT_DISC_SNAPSHOT_CERT_EESS"

# CONSTANTE: INDICADORES SOLO (Para SP_CargarFuncionAMatriz)
# Formato: (NombreColumna, FuncionSQL)

# INDICADORESSOLO = [    
#     ('NDQ29', "dbo.Ninos_ConCert('P072,P073','N,R')"),
#     ('NDQ30', "dbo.Ninos_ConCert('P070','N,R')"),
# ]



INDICADORESSOLO = [

	('NDQ4784', "dbo.Actores_N('APP91', 'C0001', '2')"),
	('NDQ4785', "dbo.Actores_N('APP92', 'C0001', '2')"),
	

]




# CONSTANTE: INDICADORES MULTIPLE (Para SP_CargarFuncionAMatriz_Multi)
# Formato: (MapeoColumnasJSON, FuncionSQL)

# INDICADORESMULTIPLE = [
#     (
#         '"0d-11A":"NDQ119", "12A-17A":"NDQ120", "18A-29A":"NDQ121", "30A-59A":"NDQ122", "60A+":"NDQ123"',
#         "dbo.Multiples_ConCert('fisico', 'sensorial', 'N,R')"
#     )    
# ]



INDICADORESMULTIPLE = [
    (
        '"0d-11A":"NDQ3839", "12A-17A":"NDQ3840", "18A-29A":"NDQ3841", "30A-59A":"NDQ3842", "60A+":"NDQ3843"',
        "dbo.Certif_Eess_Eva()"
    ),
    (
        '"0d-11A":"NDQ3844", "12A-17A":"NDQ3845", "18A-29A":"NDQ3846", "30A-59A":"NDQ3847", "60A+":"NDQ3848"',
        "dbo.Certif_Eess_Cali()"
    ),
    (
        '"0d-11A":"NDQ3849", "12A-17A":"NDQ3850", "18A-29A":"NDQ3851", "30A-59A":"NDQ3852", "60A+":"NDQ3853"',
        "dbo.Certif_Eess_Cert()"
    ),
]