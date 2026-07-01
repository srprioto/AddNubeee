# -*- coding: utf-8 -*-
"""
Autor: Yo!
Fecha: 2026
"""

NOMBRE_TABLA = "FACT_DISC_SNAPSHOT_AYUDATECN"

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
        '"0d-11A":"NDQ119", "12A-17A":"NDQ120", "18A-29A":"NDQ121", "30A-59A":"NDQ122", "60A+":"NDQ123"', 
        "dbo.Multiples_ConCert('fisico', 'sensorial', 'N,R');"
    ),
    (
        '"0d-11A":"NDQ124", "12A-17A":"NDQ125", "18A-29A":"NDQ126", "30A-59A":"NDQ127", "60A+":"NDQ128"', 
        "dbo.Multiples_SinCert('fisico', 'sensorial', 'N,R');"
    ),
    (
        '"0d-11A":"NDQ129", "12A-17A":"NDQ130", "18A-29A":"NDQ131", "30A-59A":"NDQ132", "60A+":"NDQ133"', 
        "dbo.Multiples_EnRiesgo('fisico', 'sensorial', 'N,R');"
    ),
    (
        '"0d-11A":"NDQ134", "12A-17A":"NDQ135", "18A-29A":"NDQ136", "30A-59A":"NDQ137", "60A+":"NDQ138"', 
        "dbo.Multiples_ConCert('fisico', 'sensorial', 'N,C,R');"
    ),
    (
        '"0d-11A":"NDQ139", "12A-17A":"NDQ140", "18A-29A":"NDQ141", "30A-59A":"NDQ142", "60A+":"NDQ143"', 
        "dbo.Multiples_SinCert('fisico', 'sensorial', 'N,C,R');"
    ),
    (
        '"0d-11A":"NDQ144", "12A-17A":"NDQ145", "18A-29A":"NDQ146", "30A-59A":"NDQ147", "60A+":"NDQ148"', 
        "dbo.Multiples_EnRiesgo('fisico', 'sensorial', 'N,C,R');"
    ),
    (
        '"0d-11A":"NDQ149", "12A-17A":"NDQ150", "18A-29A":"NDQ151", "30A-59A":"NDQ152", "60A+":"NDQ153"', 
        "dbo.Multiples_ConCert('sensorial', 'fisico', 'N,R');"
    ),
    (
        '"0d-11A":"NDQ154", "12A-17A":"NDQ155", "18A-29A":"NDQ156", "30A-59A":"NDQ157", "60A+":"NDQ158"', 
        "dbo.Multiples_SinCert('sensorial', 'fisico', 'N,R');"
    ),
    (
        '"0d-11A":"NDQ159", "12A-17A":"NDQ160", "18A-29A":"NDQ161", "30A-59A":"NDQ162", "60A+":"NDQ163"', 
        "dbo.Multiples_EnRiesgo('sensorial', 'fisico', 'N,R');"
    ),
    (
        '"0d-11A":"NDQ164", "12A-17A":"NDQ165", "18A-29A":"NDQ166", "30A-59A":"NDQ167", "60A+":"NDQ168"', 
        "dbo.Multiples_ConCert('sensorial', 'fisico', 'N,C,R');"
    ),
    (
        '"0d-11A":"NDQ169", "12A-17A":"NDQ170", "18A-29A":"NDQ171", "30A-59A":"NDQ172", "60A+":"NDQ173"', 
        "dbo.Multiples_SinCert('sensorial', 'fisico', 'N,C,R');"
    ),
    (
        '"0d-11A":"NDQ174", "12A-17A":"NDQ175", "18A-29A":"NDQ176", "30A-59A":"NDQ177", "60A+":"NDQ178"', 
        "dbo.Multiples_EnRiesgo('sensorial', 'fisico', 'N,C,R');"
    ),
    (
        '"0d-11A":"NDQ179", "12A-17A":"NDQ180", "18A-29A":"NDQ181", "30A-59A":"NDQ182", "60A+":"NDQ183"', 
        "dbo.Multiples_ConCert('fisico', 'mental', 'N,R');"
    ),
    (
        '"0d-11A":"NDQ184", "12A-17A":"NDQ185", "18A-29A":"NDQ186", "30A-59A":"NDQ187", "60A+":"NDQ188"', 
        "dbo.Multiples_SinCert('fisico', 'mental', 'N,R');"
    ),
    (
        '"0d-11A":"NDQ189", "12A-17A":"NDQ190", "18A-29A":"NDQ191", "30A-59A":"NDQ192", "60A+":"NDQ193"', 
        "dbo.Multiples_EnRiesgo('fisico', 'mental', 'N,R');"
    ),
    (
        '"0d-11A":"NDQ194", "12A-17A":"NDQ195", "18A-29A":"NDQ196", "30A-59A":"NDQ197", "60A+":"NDQ198"', 
        "dbo.Multiples_ConCert('fisico', 'mental', 'N,C,R');"
    ),
    (
        '"0d-11A":"NDQ199", "12A-17A":"NDQ200", "18A-29A":"NDQ201", "30A-59A":"NDQ202", "60A+":"NDQ203"', 
        "dbo.Multiples_SinCert('fisico', 'mental', 'N,C,R');"
    ),
    (
        '"0d-11A":"NDQ204", "12A-17A":"NDQ205", "18A-29A":"NDQ206", "30A-59A":"NDQ207", "60A+":"NDQ208"', 
        "dbo.Multiples_EnRiesgo('fisico', 'mental', 'N,C,R');"
    ),
    (
        '"0d-11A":"NDQ209", "12A-17A":"NDQ210", "18A-29A":"NDQ211", "30A-59A":"NDQ212", "60A+":"NDQ213"', 
        "dbo.Multiples_ConCert('mental', 'fisico', 'N,R');"
    ),
    (
        '"0d-11A":"NDQ214", "12A-17A":"NDQ215", "18A-29A":"NDQ216", "30A-59A":"NDQ217", "60A+":"NDQ218"', 
        "dbo.Multiples_SinCert('mental', 'fisico', 'N,R');"
    ),
    (
        '"0d-11A":"NDQ219", "12A-17A":"NDQ220", "18A-29A":"NDQ221", "30A-59A":"NDQ222", "60A+":"NDQ223"', 
        "dbo.Multiples_EnRiesgo('mental', 'fisico', 'N,R');"
    ),
    (
        '"0d-11A":"NDQ224", "12A-17A":"NDQ225", "18A-29A":"NDQ226", "30A-59A":"NDQ227", "60A+":"NDQ228"', 
        "dbo.Multiples_ConCert('mental', 'fisico', 'N,C,R');"
    ),
    (
        '"0d-11A":"NDQ229", "12A-17A":"NDQ230", "18A-29A":"NDQ231", "30A-59A":"NDQ232", "60A+":"NDQ233"', 
        "dbo.Multiples_SinCert('mental', 'fisico', 'N,C,R');"
    ),
    (
        '"0d-11A":"NDQ234", "12A-17A":"NDQ235", "18A-29A":"NDQ236", "30A-59A":"NDQ237", "60A+":"NDQ238"', 
        "dbo.Multiples_EnRiesgo('mental', 'fisico', 'N,C,R');"
    ),
    (
        '"0d-11A":"NDQ239", "12A-17A":"NDQ240", "18A-29A":"NDQ241", "30A-59A":"NDQ242", "60A+":"NDQ243"', 
        "dbo.Multiples_ConCert('sensorial', 'mental', 'N,R');"
    ),
    (
        '"0d-11A":"NDQ244", "12A-17A":"NDQ245", "18A-29A":"NDQ246", "30A-59A":"NDQ247", "60A+":"NDQ248"', 
        "dbo.Multiples_SinCert('sensorial', 'mental', 'N,R');"
    ),
    (
        '"0d-11A":"NDQ249", "12A-17A":"NDQ250", "18A-29A":"NDQ251", "30A-59A":"NDQ252", "60A+":"NDQ253"', 
        "dbo.Multiples_EnRiesgo('sensorial', 'mental', 'N,R');"
    ),
    (
        '"0d-11A":"NDQ254", "12A-17A":"NDQ255", "18A-29A":"NDQ256", "30A-59A":"NDQ257", "60A+":"NDQ258"', 
        "dbo.Multiples_ConCert('sensorial', 'mental', 'N,C,R');"
    ),
    (
        '"0d-11A":"NDQ259", "12A-17A":"NDQ260", "18A-29A":"NDQ261", "30A-59A":"NDQ262", "60A+":"NDQ263"', 
        "dbo.Multiples_SinCert('sensorial', 'mental', 'N,C,R');"
    ),
    (
        '"0d-11A":"NDQ264", "12A-17A":"NDQ265", "18A-29A":"NDQ266", "30A-59A":"NDQ267", "60A+":"NDQ268"', 
        "dbo.Multiples_EnRiesgo('sensorial', 'mental', 'N,C,R');"
    ),
    (
        '"0d-11A":"NDQ269", "12A-17A":"NDQ270", "18A-29A":"NDQ271", "30A-59A":"NDQ272", "60A+":"NDQ273"', 
        "dbo.Multiples_ConCert('mental', 'sensorial', 'N,R');"
    ),
    (
        '"0d-11A":"NDQ274", "12A-17A":"NDQ275", "18A-29A":"NDQ276", "30A-59A":"NDQ277", "60A+":"NDQ278"', 
        "dbo.Multiples_SinCert('mental', 'sensorial', 'N,R');"
    ),
    (
        '"0d-11A":"NDQ279", "12A-17A":"NDQ280", "18A-29A":"NDQ281", "30A-59A":"NDQ282", "60A+":"NDQ283"', 
        "dbo.Multiples_EnRiesgo('mental', 'sensorial', 'N,R');"
    ),
    (
        '"0d-11A":"NDQ284", "12A-17A":"NDQ285", "18A-29A":"NDQ286", "30A-59A":"NDQ287", "60A+":"NDQ288"', 
        "dbo.Multiples_ConCert('mental', 'sensorial', 'N,C,R');"
    ),
    (
        '"0d-11A":"NDQ289", "12A-17A":"NDQ290", "18A-29A":"NDQ291", "30A-59A":"NDQ292", "60A+":"NDQ293"', 
        "dbo.Multiples_SinCert('mental', 'sensorial', 'N,C,R');"
    ),
    (
        '"0d-11A":"NDQ294", "12A-17A":"NDQ295", "18A-29A":"NDQ296", "30A-59A":"NDQ297", "60A+":"NDQ298"', 
        "dbo.Multiples_EnRiesgo('mental', 'sensorial', 'N,C,R');"
    ),
    (
        '"0d-11A":"NDQ299", "12A-17A":"NDQ300", "18A-29A":"NDQ301", "30A-59A":"NDQ302", "60A+":"NDQ303"', 
        "dbo.Multiples_Triple_ConCert('N,R');"
    ),
    (
        '"0d-11A":"NDQ304", "12A-17A":"NDQ305", "18A-29A":"NDQ306", "30A-59A":"NDQ307", "60A+":"NDQ308"', 
        "dbo.Multiples_Triple_SinCert('N,R');"
    ),
    (
        '"0d-11A":"NDQ309", "12A-17A":"NDQ310", "18A-29A":"NDQ311", "30A-59A":"NDQ312", "60A+":"NDQ313"', 
        "dbo.Multiples_Triple_EnRiesgo('N,R');"
    ),
    (
        '"0d-11A":"NDQ314", "12A-17A":"NDQ315", "18A-29A":"NDQ316", "30A-59A":"NDQ317", "60A+":"NDQ318"', 
        "dbo.Multiples_Triple_ConCert('N,C,R');"
    ),
    (
        '"0d-11A":"NDQ319", "12A-17A":"NDQ320", "18A-29A":"NDQ321", "30A-59A":"NDQ322", "60A+":"NDQ323"', 
        "dbo.Multiples_Triple_SinCert('N,C,R');"
    ),
    (
        '"0d-11A":"NDQ324", "12A-17A":"NDQ325", "18A-29A":"NDQ326", "30A-59A":"NDQ327", "60A+":"NDQ328"', 
        "dbo.Multiples_Triple_EnRiesgo('N,C,R');"
    ),
]




# INDICADORESMULTIPLE = [
#     (
#         '"0d-11A":"NDQ329", "12A-17A":"NDQ330", "18A-29A":"NDQ331", "30A-59A":"NDQ332", "60A+":"NDQ333"', 
#         "dbo.Grupal_ConCert('1', 'N,R');"
#     ),
#     (
#         '"0d-11A":"NDQ334", "12A-17A":"NDQ335", "18A-29A":"NDQ336", "30A-59A":"NDQ337", "60A+":"NDQ338"', 
#         "dbo.Grupal_SinCert('1', 'N,R');"
#     ),
#     (
#         '"0d-11A":"NDQ339", "12A-17A":"NDQ340", "18A-29A":"NDQ341", "30A-59A":"NDQ342", "60A+":"NDQ343"', 
#         "dbo.Grupal_EnRiesgo('1', 'N,R');"
#     ),
#     (
#         '"0d-11A":"NDQ344", "12A-17A":"NDQ345", "18A-29A":"NDQ346", "30A-59A":"NDQ347", "60A+":"NDQ348"', 
#         "dbo.Grupal_ConCert('1', 'N,C,R');"
#     ),
#     (
#         '"0d-11A":"NDQ349", "12A-17A":"NDQ350", "18A-29A":"NDQ351", "30A-59A":"NDQ352", "60A+":"NDQ353"', 
#         "dbo.Grupal_SinCert('1', 'N,C,R');"
#     ),
#     (
#         '"0d-11A":"NDQ354", "12A-17A":"NDQ355", "18A-29A":"NDQ356", "30A-59A":"NDQ357", "60A+":"NDQ358"', 
#         "dbo.Grupal_EnRiesgo('1', 'N,C,R');"
#     ),
#     (
#         '"0d-11A":"NDQ359", "12A-17A":"NDQ360", "18A-29A":"NDQ361", "30A-59A":"NDQ362", "60A+":"NDQ363"', 
#         "dbo.Grupal_ConCert('2', 'N,R');"
#     ),
#     (
#         '"0d-11A":"NDQ364", "12A-17A":"NDQ365", "18A-29A":"NDQ366", "30A-59A":"NDQ367", "60A+":"NDQ368"', 
#         "dbo.Grupal_SinCert('2', 'N,R');"
#     ),
#     (
#         '"0d-11A":"NDQ369", "12A-17A":"NDQ370", "18A-29A":"NDQ371", "30A-59A":"NDQ372", "60A+":"NDQ373"', 
#         "dbo.Grupal_EnRiesgo('2', 'N,R');"
#     ),
#     (
#         '"0d-11A":"NDQ374", "12A-17A":"NDQ375", "18A-29A":"NDQ376", "30A-59A":"NDQ377", "60A+":"NDQ378"', 
#         "dbo.Grupal_ConCert('2', 'N,C,R');"
#     ),
#     (
#         '"0d-11A":"NDQ379", "12A-17A":"NDQ380", "18A-29A":"NDQ381", "30A-59A":"NDQ382", "60A+":"NDQ383"', 
#         "dbo.Grupal_SinCert('2', 'N,C,R');"
#     ),
#     (
#         '"0d-11A":"NDQ384", "12A-17A":"NDQ385", "18A-29A":"NDQ386", "30A-59A":"NDQ387", "60A+":"NDQ388"', 
#         "dbo.Grupal_EnRiesgo('2', 'N,C,R');"
#     ),
#     (
#         '"0d-11A":"NDQ389", "12A-17A":"NDQ390", "18A-29A":"NDQ391", "30A-59A":"NDQ392", "60A+":"NDQ393"', 
#         "dbo.Grupal_ConCert('3', 'N,R');"
#     ),
#     (
#         '"0d-11A":"NDQ394", "12A-17A":"NDQ395", "18A-29A":"NDQ396", "30A-59A":"NDQ397", "60A+":"NDQ398"', 
#         "dbo.Grupal_SinCert('3', 'N,R');"
#     ),
#     (
#         '"0d-11A":"NDQ399", "12A-17A":"NDQ400", "18A-29A":"NDQ401", "30A-59A":"NDQ402", "60A+":"NDQ403"', 
#         "dbo.Grupal_EnRiesgo('3', 'N,R');"
#     ),
#     (
#         '"0d-11A":"NDQ404", "12A-17A":"NDQ405", "18A-29A":"NDQ406", "30A-59A":"NDQ407", "60A+":"NDQ408"', 
#         "dbo.Grupal_ConCert('3', 'N,C,R');"
#     ),
#     (
#         '"0d-11A":"NDQ409", "12A-17A":"NDQ410", "18A-29A":"NDQ411", "30A-59A":"NDQ412", "60A+":"NDQ413"', 
#         "dbo.Grupal_SinCert('3', 'N,C,R');"
#     ),
#     (
#         '"0d-11A":"NDQ414", "12A-17A":"NDQ415", "18A-29A":"NDQ416", "30A-59A":"NDQ417", "60A+":"NDQ418"', 
#         "dbo.Grupal_EnRiesgo('3', 'N,C,R');"
#     ),
#     (
#         '"0d-11A":"NDQ419", "12A-17A":"NDQ420", "18A-29A":"NDQ421", "30A-59A":"NDQ422", "60A+":"NDQ423"', 
#         "dbo.Grupal_ConCert('4', 'N,R');"
#     ),
#     (
#         '"0d-11A":"NDQ424", "12A-17A":"NDQ425", "18A-29A":"NDQ426", "30A-59A":"NDQ427", "60A+":"NDQ428"', 
#         "dbo.Grupal_SinCert('4', 'N,R');"
#     ),
#     (
#         '"0d-11A":"NDQ429", "12A-17A":"NDQ430", "18A-29A":"NDQ431", "30A-59A":"NDQ432", "60A+":"NDQ433"', 
#         "dbo.Grupal_EnRiesgo('4', 'N,R');"
#     ),
#     (
#         '"0d-11A":"NDQ434", "12A-17A":"NDQ435", "18A-29A":"NDQ436", "30A-59A":"NDQ437", "60A+":"NDQ438"', 
#         "dbo.Grupal_ConCert('4', 'N,C,R');"
#     ),
#     (
#         '"0d-11A":"NDQ439", "12A-17A":"NDQ440", "18A-29A":"NDQ441", "30A-59A":"NDQ442", "60A+":"NDQ443"', 
#         "dbo.Grupal_SinCert('4', 'N,C,R');"
#     ),
#     (
#         '"0d-11A":"NDQ444", "12A-17A":"NDQ445", "18A-29A":"NDQ446", "30A-59A":"NDQ447", "60A+":"NDQ448"', 
#         "dbo.Grupal_EnRiesgo('4', 'N,C,R');"
#     ),
#     (
#         '"0d-11A":"NDQ449", "12A-17A":"NDQ450", "18A-29A":"NDQ451", "30A-59A":"NDQ452", "60A+":"NDQ453"', 
#         "dbo.Grupal_ConCert('5', 'N,R');"
#     ),
#     (
#         '"0d-11A":"NDQ454", "12A-17A":"NDQ455", "18A-29A":"NDQ456", "30A-59A":"NDQ457", "60A+":"NDQ458"', 
#         "dbo.Grupal_SinCert('5', 'N,R');"
#     ),
#     (
#         '"0d-11A":"NDQ459", "12A-17A":"NDQ460", "18A-29A":"NDQ461", "30A-59A":"NDQ462", "60A+":"NDQ463"', 
#         "dbo.Grupal_EnRiesgo('5', 'N,R');"
#     ),
#     (
#         '"0d-11A":"NDQ464", "12A-17A":"NDQ465", "18A-29A":"NDQ466", "30A-59A":"NDQ467", "60A+":"NDQ468"', 
#         "dbo.Grupal_ConCert('5', 'N,C,R');"
#     ),
#     (
#         '"0d-11A":"NDQ469", "12A-17A":"NDQ470", "18A-29A":"NDQ471", "30A-59A":"NDQ472", "60A+":"NDQ473"', 
#         "dbo.Grupal_SinCert('5', 'N,C,R');"
#     ),
#     (
#         '"0d-11A":"NDQ474", "12A-17A":"NDQ475", "18A-29A":"NDQ476", "30A-59A":"NDQ477", "60A+":"NDQ478"', 
#         "dbo.Grupal_EnRiesgo('5', 'N,C,R');"
#     ),
#     (
#         '"0d-11A":"NDQ479", "12A-17A":"NDQ480", "18A-29A":"NDQ481", "30A-59A":"NDQ482", "60A+":"NDQ483"', 
#         "dbo.Grupal_ConCert('6', 'N,R');"
#     ),
#     (
#         '"0d-11A":"NDQ484", "12A-17A":"NDQ485", "18A-29A":"NDQ486", "30A-59A":"NDQ487", "60A+":"NDQ488"', 
#         "dbo.Grupal_SinCert('6', 'N,R');"
#     ),
#     (
#         '"0d-11A":"NDQ489", "12A-17A":"NDQ490", "18A-29A":"NDQ491", "30A-59A":"NDQ492", "60A+":"NDQ493"', 
#         "dbo.Grupal_EnRiesgo('6', 'N,R');"
#     ),
#     (
#         '"0d-11A":"NDQ494", "12A-17A":"NDQ495", "18A-29A":"NDQ496", "30A-59A":"NDQ497", "60A+":"NDQ498"', 
#         "dbo.Grupal_ConCert('6', 'N,C,R');"
#     ),
#     (
#         '"0d-11A":"NDQ499", "12A-17A":"NDQ500", "18A-29A":"NDQ501", "30A-59A":"NDQ502", "60A+":"NDQ503"', 
#         "dbo.Grupal_SinCert('6', 'N,C,R');"
#     ),
#     (
#         '"0d-11A":"NDQ504", "12A-17A":"NDQ505", "18A-29A":"NDQ506", "30A-59A":"NDQ507", "60A+":"NDQ508"', 
#         "dbo.Grupal_EnRiesgo('6', 'N,C,R');"
#     )
# ]