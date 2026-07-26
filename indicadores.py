# -*- coding: utf-8 -*-
"""
Autor: Yo!
Fecha: 2026
"""

# CONSTANTES PARA MODO SOLO (Mantenidas por compatibilidad)
NOMBRE_TABLA = "FACT_DISC_SNAPSHOT_NINOS"

INDICADORESSOLO = [    
    
    ('NDQ29', "dbo.Ninos_ConCert('P072,P073','N,R')"),
    ('NDQ113', "dbo.Ninos_Riesgo('H351','N,C,R')"),
    ('NDQ114', "dbo.Ninos_Riesgo('E030,E031,E033','N,C,R')"),
    ('NDQ116', "dbo.Ninos_Riesgo('P360,P361,P362,P363,P364,P365,P368,P369','N,C,R')"),
    ('NDQ118', "dbo.Ninos_Riesgo('G800,G800,G801,G802,G803,G804,G808,G809','N,C,R')")

]



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
        '"0d-11A":"NDQ124", "12A-17A":"NDQ125", "18A-29A":"NDQ126", "30A-59A":"NDQ127", "60A+":"NDQ128"',
        "dbo.Multiples_ConCert('sensorial', 'físico', 'N,R')"
    )
]



# NUEVA ESTRUCTURA PARA MODO TODO
TODO = {
    "INDICADORESSOLO": {
        "FACT_DISC_SNAPSHOT_CAP_MED_REHAB": [
            ('NDQ1', "dbo.Capa_Med_Reh_1_N()"),
            ('NDQ2', "dbo.Capa_Med_Reh_2_N('99450.01', '2')"),
            ('NDQ3', "dbo.Capa_Med_Reh_2_N('99201,99202,99203,99204,97762,97703', '3')"),
            ('NDQ4', "dbo.Capa_Med_Reh_2_N('97799', '4')"),
            ('NDQ5', "dbo.Capa_Med_Reh_1_S1234('1')"),
            ('NDQ6', "dbo.Capa_Med_Reh_2_S1234('1', '99450.01', '2')"),
            ('NDQ7', "dbo.Capa_Med_Reh_2_S1234('1', '99201,99202,99203,99204,97762,97703', '3')"),
            ('NDQ8', "dbo.Capa_Med_Reh_2_S1234('1', '97799', '4')"),
            ('NDQ9', "dbo.Capa_Med_Reh_1_S1234('2')"),
            ('NDQ10', "dbo.Capa_Med_Reh_2_S1234('2', '99450.01', '2')"),
            ('NDQ11', "dbo.Capa_Med_Reh_2_S1234('2', '99201,99202,99203,99204,97762,97703', '3')"),
            ('NDQ12', "dbo.Capa_Med_Reh_2_S1234('2', '97799', '4')"),
            ('NDQ13', "dbo.Capa_Med_Reh_1_S1234('3')"),
            ('NDQ14', "dbo.Capa_Med_Reh_2_S1234('3', '99450.01', '2')"),
            ('NDQ15', "dbo.Capa_Med_Reh_2_S1234('3', '99201,99202,99203,99204,97762,97703', '3')"),
            ('NDQ16', "dbo.Capa_Med_Reh_2_S1234('3', '97799', '4')"),
            ('NDQ17', "dbo.Capa_Med_Reh_1_S1234('4')"),
            ('NDQ18', "dbo.Capa_Med_Reh_2_S1234('4', '99450.01', '2')"),
            ('NDQ19', "dbo.Capa_Med_Reh_2_S1234('4', '99201,99202,99203,99204,97762,97703', '3')"),
            ('NDQ20', "dbo.Capa_Med_Reh_2_S1234('4', '97799', '4')"),
            ('NDQ21', "dbo.Capa_Med_Reh_1_5ta()"),
            ('NDQ22', "dbo.Capa_Med_Reh_2_5ta('99450.01', '2')"),
            ('NDQ23', "dbo.Capa_Med_Reh_2_5ta('99201,99202,99203,99204,97762,97703', '3')"),
            ('NDQ24', "dbo.Capa_Med_Reh_2_5ta('97799', '4')"),
            ('NDQ25', "dbo.Capa_Med_Reh_1_Last()"),
            ('NDQ26', "dbo.Capa_Med_Reh_2_Last('99450.01', '2')"),
            ('NDQ27', "dbo.Capa_Med_Reh_2_Last('99201,99202,99203,99204,97762,97703', '3')"),
            ('NDQ28', "dbo.Capa_Med_Reh_2_Last('97799', '4')")
        ],

        "FACT_DISC_SNAPSHOT_NINOS": [    
    
            ('NDQ29', "dbo.Ninos_ConCert('P072,P073','N,R')"),
            ('NDQ30', "dbo.Ninos_ConCert('P070','N,R')"),
            ('NDQ31', "dbo.Ninos_ConCert('Q000,Q001,Q002,Q003,Q004,Q005,Q006,Q007,Q008,Q009,Q090,Q091,Q092,Q093,Q094,Q095,Q096,Q097,Q098,Q099,Q310,Q311,Q312,Q313,Q314,Q315,Q316,Q317,Q318,Q319,Q320,Q321,Q322,Q323,Q324,Q325,Q326,Q327,Q328,Q329,Q330,Q331,Q332,Q333,Q334,Q335,Q336,Q337,Q338,Q339,Q330,Q351,Q352,Q353,Q354,Q355,Q356,Q357,Q358,Q359,Q360,Q361,Q362,Q363,Q364,Q365,Q366,Q367,Q368,Q369,Q370,Q371,Q372,Q373,Q374,Q375,Q376,Q377,Q378,Q379,Q380,Q381,Q650,Q651,Q652,Q653,Q654,Q655,Q656,Q657,Q658,Q659,Q660,Q661,Q662,Q663,Q664,Q665,Q666,Q667,Q668,Q669,Q670,Q671,Q672,Q673,Q674,Q675,Q676,Q677,Q678,Q679,Q680,Q681,Q682,Q683,Q684,Q685,Q686,Q687,Q688,Q689,Q690,Q691,Q692,Q693,Q694,Q695,Q696,Q697,Q698,Q699,Q700,Q701,Q702,Q703,Q704,Q705,Q706,Q707,Q708,Q709,Q710,Q711,Q712,Q713,Q714,Q715,Q716,Q717,Q718,Q719,Q720,Q721,Q722,Q723,Q724,Q725,Q726,Q727,Q728,Q729,Q730,Q731,Q732,Q733,Q734,Q735,Q736,Q737,Q738,Q739,Q740,Q741,Q742,Q743,Q744,Q745,Q746,Q747,Q748,Q749,Q760,Q761,Q762,Q763,Q764,Q765,Q766,Q767,Q768,Q769,Q770,Q771,Q772,Q773,Q774,Q775,Q776,Q777,Q778,Q779,Q780,Q781,Q782,Q783,Q784,Q785,Q786,Q787,Q788,Q789,Q796,Q798,Q799,Q871,Q872,Q874,Q875,Q878,Q900,Q901,Q902,Q903,Q904,Q905,Q906,Q907,Q908,Q909,Q910,Q911,Q912,Q913,Q914,Q915,Q916,Q917,Q918,Q919,Q920,Q921,Q922,Q923,Q924,Q925,Q926,Q927,Q928,Q929,Q930,Q931,Q932,Q933,Q934,Q935,Q936,Q937,Q938,Q939,Q950,Q951,Q952,Q953,Q954,Q955,Q956,Q957,Q958,Q959,Q960,Q961,Q962,Q963,Q964,Q965,Q966,Q967,Q968,Q969,Q992,Q998,Q999','N,R')"),
            ('NDQ32', "dbo.Ninos_ConCert('A390,A870,A871','N,R')"),
            ('NDQ33', "dbo.Ninos_ConCert('A850,A851,A858,A860,A861,A862,A863,A864,A865,A866,A867,A868,A869','N,R')"),
            ('NDQ34', "dbo.Ninos_ConCert('P579','N,R')"),
            ('NDQ35', "dbo.Ninos_ConCert('P90X','N,R')"),
            ('NDQ36', "dbo.Ninos_ConCert('P941','N,R')"),
            ('NDQ37', "dbo.Ninos_ConCert('P942','N,R')"),
            ('NDQ38', "dbo.Ninos_ConCert('H351','N,R')"),
            ('NDQ39', "dbo.Ninos_ConCert('E030,E031,E033','N,R')"),
            ('NDQ40', "dbo.Ninos_ConCert('R629,F800,F801,F802,F804,F808,F809,F820,F821,F822,F823,F824,F825,F826,F827,F828,F829,F830,F831,F832,F833,F834,F835,F836,F837,F838,F839,F840,F842,F844,F845,F848,F849,FR41','N,R')"),
            ('NDQ41', "dbo.Ninos_ConCert('P360,P361,P362,P363,P364,P365,P368,P369','N,R')"),
            ('NDQ42', "dbo.Ninos_ConCert('A400,A401,A402,A403,A408,A409,A410,A411,A412,A413,A414,A415,A418,A419','N,R')"),
            ('NDQ43', "dbo.Ninos_ConCert('G800,G800,G801,G802,G803,G804,G808,G809','N,R')"),
            ('NDQ44', "dbo.Ninos_SinCert('P072,P073','N,R')"),
            ('NDQ45', "dbo.Ninos_SinCert('P070','N,R')"),
            ('NDQ46', "dbo.Ninos_SinCert('Q000,Q001,Q002,Q003,Q004,Q005,Q006,Q007,Q008,Q009,Q090,Q091,Q092,Q093,Q094,Q095,Q096,Q097,Q098,Q099,Q310,Q311,Q312,Q313,Q314,Q315,Q316,Q317,Q318,Q319,Q320,Q321,Q322,Q323,Q324,Q325,Q326,Q327,Q328,Q329,Q330,Q331,Q332,Q333,Q334,Q335,Q336,Q337,Q338,Q339,Q330,Q351,Q352,Q353,Q354,Q355,Q356,Q357,Q358,Q359,Q360,Q361,Q362,Q363,Q364,Q365,Q366,Q367,Q368,Q369,Q370,Q371,Q372,Q373,Q374,Q375,Q376,Q377,Q378,Q379,Q380,Q381,Q650,Q651,Q652,Q653,Q654,Q655,Q656,Q657,Q658,Q659,Q660,Q661,Q662,Q663,Q664,Q665,Q666,Q667,Q668,Q669,Q670,Q671,Q672,Q673,Q674,Q675,Q676,Q677,Q678,Q679,Q680,Q681,Q682,Q683,Q684,Q685,Q686,Q687,Q688,Q689,Q690,Q691,Q692,Q693,Q694,Q695,Q696,Q697,Q698,Q699,Q700,Q701,Q702,Q703,Q704,Q705,Q706,Q707,Q708,Q709,Q710,Q711,Q712,Q713,Q714,Q715,Q716,Q717,Q718,Q719,Q720,Q721,Q722,Q723,Q724,Q725,Q726,Q727,Q728,Q729,Q730,Q731,Q732,Q733,Q734,Q735,Q736,Q737,Q738,Q739,Q740,Q741,Q742,Q743,Q744,Q745,Q746,Q747,Q748,Q749,Q760,Q761,Q762,Q763,Q764,Q765,Q766,Q767,Q768,Q769,Q770,Q771,Q772,Q773,Q774,Q775,Q776,Q777,Q778,Q779,Q780,Q781,Q782,Q783,Q784,Q785,Q786,Q787,Q788,Q789,Q796,Q798,Q799,Q871,Q872,Q874,Q875,Q878,Q900,Q901,Q902,Q903,Q904,Q905,Q906,Q907,Q908,Q909,Q910,Q911,Q912,Q913,Q914,Q915,Q916,Q917,Q918,Q919,Q920,Q921,Q922,Q923,Q924,Q925,Q926,Q927,Q928,Q929,Q930,Q931,Q932,Q933,Q934,Q935,Q936,Q937,Q938,Q939,Q950,Q951,Q952,Q953,Q954,Q955,Q956,Q957,Q958,Q959,Q960,Q961,Q962,Q963,Q964,Q965,Q966,Q967,Q968,Q969,Q992,Q998,Q999','N,R')"),
            ('NDQ47', "dbo.Ninos_SinCert('A390,A870,A871','N,R')"),
            ('NDQ48', "dbo.Ninos_SinCert('A850,A851,A858,A860,A861,A862,A863,A864,A865,A866,A867,A868,A869','N,R')"),
            ('NDQ49', "dbo.Ninos_SinCert('P579','N,R')"),
            ('NDQ50', "dbo.Ninos_SinCert('P90X','N,R')"),
            ('NDQ51', "dbo.Ninos_SinCert('P941','N,R')"),
            ('NDQ52', "dbo.Ninos_SinCert('P942','N,R')"),
            ('NDQ53', "dbo.Ninos_SinCert('H351','N,R')"),
            ('NDQ54', "dbo.Ninos_SinCert('E030,E031,E033','N,R')"),
            ('NDQ55', "dbo.Ninos_SinCert('R629,F800,F801,F802,F804,F808,F809,F820,F821,F822,F823,F824,F825,F826,F827,F828,F829,F830,F831,F832,F833,F834,F835,F836,F837,F838,F839,F840,F842,F844,F845,F848,F849,FR41','N,R')"),
            ('NDQ56', "dbo.Ninos_SinCert('P360,P361,P362,P363,P364,P365,P368,P369','N,R')"),
            ('NDQ57', "dbo.Ninos_SinCert('A400,A401,A402,A403,A408,A409,A410,A411,A412,A413,A414,A415,A418,A419','N,R')"),
            ('NDQ58', "dbo.Ninos_SinCert('G800,G800,G801,G802,G803,G804,G808,G809','N,R')"),
            ('NDQ59', "dbo.Ninos_Riesgo('P072,P073','N,R')"),
            ('NDQ60', "dbo.Ninos_Riesgo('P070','N,R')"),
            ('NDQ61', "dbo.Ninos_Riesgo('Q000,Q001,Q002,Q003,Q004,Q005,Q006,Q007,Q008,Q009,Q090,Q091,Q092,Q093,Q094,Q095,Q096,Q097,Q098,Q099,Q310,Q311,Q312,Q313,Q314,Q315,Q316,Q317,Q318,Q319,Q320,Q321,Q322,Q323,Q324,Q325,Q326,Q327,Q328,Q329,Q330,Q331,Q332,Q333,Q334,Q335,Q336,Q337,Q338,Q339,Q330,Q351,Q352,Q353,Q354,Q355,Q356,Q357,Q358,Q359,Q360,Q361,Q362,Q363,Q364,Q365,Q366,Q367,Q368,Q369,Q370,Q371,Q372,Q373,Q374,Q375,Q376,Q377,Q378,Q379,Q380,Q381,Q650,Q651,Q652,Q653,Q654,Q655,Q656,Q657,Q658,Q659,Q660,Q661,Q662,Q663,Q664,Q665,Q666,Q667,Q668,Q669,Q670,Q671,Q672,Q673,Q674,Q675,Q676,Q677,Q678,Q679,Q680,Q681,Q682,Q683,Q684,Q685,Q686,Q687,Q688,Q689,Q690,Q691,Q692,Q693,Q694,Q695,Q696,Q697,Q698,Q699,Q700,Q701,Q702,Q703,Q704,Q705,Q706,Q707,Q708,Q709,Q710,Q711,Q712,Q713,Q714,Q715,Q716,Q717,Q718,Q719,Q720,Q721,Q722,Q723,Q724,Q725,Q726,Q727,Q728,Q729,Q730,Q731,Q732,Q733,Q734,Q735,Q736,Q737,Q738,Q739,Q740,Q741,Q742,Q743,Q744,Q745,Q746,Q747,Q748,Q749,Q760,Q761,Q762,Q763,Q764,Q765,Q766,Q767,Q768,Q769,Q770,Q771,Q772,Q773,Q774,Q775,Q776,Q777,Q778,Q779,Q780,Q781,Q782,Q783,Q784,Q785,Q786,Q787,Q788,Q789,Q796,Q798,Q799,Q871,Q872,Q874,Q875,Q878,Q900,Q901,Q902,Q903,Q904,Q905,Q906,Q907,Q908,Q909,Q910,Q911,Q912,Q913,Q914,Q915,Q916,Q917,Q918,Q919,Q920,Q921,Q922,Q923,Q924,Q925,Q926,Q927,Q928,Q929,Q930,Q931,Q932,Q933,Q934,Q935,Q936,Q937,Q938,Q939,Q950,Q951,Q952,Q953,Q954,Q955,Q956,Q957,Q958,Q959,Q960,Q961,Q962,Q963,Q964,Q965,Q966,Q967,Q968,Q969,Q992,Q998,Q999','N,R')"),
            ('NDQ62', "dbo.Ninos_Riesgo('A390,A870,A871','N,R')"),
            ('NDQ63', "dbo.Ninos_Riesgo('A850,A851,A858,A860,A861,A862,A863,A864,A865,A866,A867,A868,A869','N,R')"),
            ('NDQ64', "dbo.Ninos_Riesgo('P579','N,R')"),
            ('NDQ65', "dbo.Ninos_Riesgo('P90X','N,R')"),
            ('NDQ66', "dbo.Ninos_Riesgo('P941','N,R')"),
            ('NDQ67', "dbo.Ninos_Riesgo('P942','N,R')"),
            ('NDQ68', "dbo.Ninos_Riesgo('H351','N,R')"),
            ('NDQ69', "dbo.Ninos_Riesgo('E030,E031,E033','N,R')"),
            ('NDQ70', "dbo.Ninos_Riesgo('R629,F800,F801,F802,F804,F808,F809,F820,F821,F822,F823,F824,F825,F826,F827,F828,F829,F830,F831,F832,F833,F834,F835,F836,F837,F838,F839,F840,F842,F844,F845,F848,F849,FR41','N,R')"),
            ('NDQ71', "dbo.Ninos_Riesgo('P360,P361,P362,P363,P364,P365,P368,P369','N,R')"),
            ('NDQ72', "dbo.Ninos_Riesgo('A400,A401,A402,A403,A408,A409,A410,A411,A412,A413,A414,A415,A418,A419','N,R')"),
            ('NDQ73', "dbo.Ninos_Riesgo('G800,G800,G801,G802,G803,G804,G808,G809','N,R')"),
            ('NDQ74', "dbo.Ninos_ConCert('P072,P073','N,C,R')"),
            ('NDQ75', "dbo.Ninos_ConCert('P070','N,C,R')"),
            ('NDQ76', "dbo.Ninos_ConCert('Q000,Q001,Q002,Q003,Q004,Q005,Q006,Q007,Q008,Q009,Q090,Q091,Q092,Q093,Q094,Q095,Q096,Q097,Q098,Q099,Q310,Q311,Q312,Q313,Q314,Q315,Q316,Q317,Q318,Q319,Q320,Q321,Q322,Q323,Q324,Q325,Q326,Q327,Q328,Q329,Q330,Q331,Q332,Q333,Q334,Q335,Q336,Q337,Q338,Q339,Q330,Q351,Q352,Q353,Q354,Q355,Q356,Q357,Q358,Q359,Q360,Q361,Q362,Q363,Q364,Q365,Q366,Q367,Q368,Q369,Q370,Q371,Q372,Q373,Q374,Q375,Q376,Q377,Q378,Q379,Q380,Q381,Q650,Q651,Q652,Q653,Q654,Q655,Q656,Q657,Q658,Q659,Q660,Q661,Q662,Q663,Q664,Q665,Q666,Q667,Q668,Q669,Q670,Q671,Q672,Q673,Q674,Q675,Q676,Q677,Q678,Q679,Q680,Q681,Q682,Q683,Q684,Q685,Q686,Q687,Q688,Q689,Q690,Q691,Q692,Q693,Q694,Q695,Q696,Q697,Q698,Q699,Q700,Q701,Q702,Q703,Q704,Q705,Q706,Q707,Q708,Q709,Q710,Q711,Q712,Q713,Q714,Q715,Q716,Q717,Q718,Q719,Q720,Q721,Q722,Q723,Q724,Q725,Q726,Q727,Q728,Q729,Q730,Q731,Q732,Q733,Q734,Q735,Q736,Q737,Q738,Q739,Q740,Q741,Q742,Q743,Q744,Q745,Q746,Q747,Q748,Q749,Q760,Q761,Q762,Q763,Q764,Q765,Q766,Q767,Q768,Q769,Q770,Q771,Q772,Q773,Q774,Q775,Q776,Q777,Q778,Q779,Q780,Q781,Q782,Q783,Q784,Q785,Q786,Q787,Q788,Q789,Q796,Q798,Q799,Q871,Q872,Q874,Q875,Q878,Q900,Q901,Q902,Q903,Q904,Q905,Q906,Q907,Q908,Q909,Q910,Q911,Q912,Q913,Q914,Q915,Q916,Q917,Q918,Q919,Q920,Q921,Q922,Q923,Q924,Q925,Q926,Q927,Q928,Q929,Q930,Q931,Q932,Q933,Q934,Q935,Q936,Q937,Q938,Q939,Q950,Q951,Q952,Q953,Q954,Q955,Q956,Q957,Q958,Q959,Q960,Q961,Q962,Q963,Q964,Q965,Q966,Q967,Q968,Q969,Q992,Q998,Q999','N,C,R')"),
            ('NDQ77', "dbo.Ninos_ConCert('A390,A870,A871','N,C,R')"),
            ('NDQ78', "dbo.Ninos_ConCert('A850,A851,A858,A860,A861,A862,A863,A864,A865,A866,A867,A868,A869','N,C,R')"),
            ('NDQ79', "dbo.Ninos_ConCert('P579','N,C,R')"),
            ('NDQ80', "dbo.Ninos_ConCert('P90X','N,C,R')"),
            ('NDQ81', "dbo.Ninos_ConCert('P941','N,C,R')"),
            ('NDQ82', "dbo.Ninos_ConCert('P942','N,C,R')"),
            ('NDQ83', "dbo.Ninos_ConCert('H351','N,C,R')"),
            ('NDQ84', "dbo.Ninos_ConCert('E030,E031,E033','N,C,R')"),
            ('NDQ85', "dbo.Ninos_ConCert('R629,F800,F801,F802,F804,F808,F809,F820,F821,F822,F823,F824,F825,F826,F827,F828,F829,F830,F831,F832,F833,F834,F835,F836,F837,F838,F839,F840,F842,F844,F845,F848,F849,FR41','N,C,R')"),
            ('NDQ86', "dbo.Ninos_ConCert('P360,P361,P362,P363,P364,P365,P368,P369','N,C,R')"),
            ('NDQ87', "dbo.Ninos_ConCert('A400,A401,A402,A403,A408,A409,A410,A411,A412,A413,A414,A415,A418,A419','N,C,R')"),
            ('NDQ88', "dbo.Ninos_ConCert('G800,G800,G801,G802,G803,G804,G808,G809','N,C,R')"),
            ('NDQ89', "dbo.Ninos_SinCert('P072,P073','N,C,R')"),
            ('NDQ90', "dbo.Ninos_SinCert('P070','N,C,R')"),
            ('NDQ91', "dbo.Ninos_SinCert('Q000,Q001,Q002,Q003,Q004,Q005,Q006,Q007,Q008,Q009,Q090,Q091,Q092,Q093,Q094,Q095,Q096,Q097,Q098,Q099,Q310,Q311,Q312,Q313,Q314,Q315,Q316,Q317,Q318,Q319,Q320,Q321,Q322,Q323,Q324,Q325,Q326,Q327,Q328,Q329,Q330,Q331,Q332,Q333,Q334,Q335,Q336,Q337,Q338,Q339,Q330,Q351,Q352,Q353,Q354,Q355,Q356,Q357,Q358,Q359,Q360,Q361,Q362,Q363,Q364,Q365,Q366,Q367,Q368,Q369,Q370,Q371,Q372,Q373,Q374,Q375,Q376,Q377,Q378,Q379,Q380,Q381,Q650,Q651,Q652,Q653,Q654,Q655,Q656,Q657,Q658,Q659,Q660,Q661,Q662,Q663,Q664,Q665,Q666,Q667,Q668,Q669,Q670,Q671,Q672,Q673,Q674,Q675,Q676,Q677,Q678,Q679,Q680,Q681,Q682,Q683,Q684,Q685,Q686,Q687,Q688,Q689,Q690,Q691,Q692,Q693,Q694,Q695,Q696,Q697,Q698,Q699,Q700,Q701,Q702,Q703,Q704,Q705,Q706,Q707,Q708,Q709,Q710,Q711,Q712,Q713,Q714,Q715,Q716,Q717,Q718,Q719,Q720,Q721,Q722,Q723,Q724,Q725,Q726,Q727,Q728,Q729,Q730,Q731,Q732,Q733,Q734,Q735,Q736,Q737,Q738,Q739,Q740,Q741,Q742,Q743,Q744,Q745,Q746,Q747,Q748,Q749,Q760,Q761,Q762,Q763,Q764,Q765,Q766,Q767,Q768,Q769,Q770,Q771,Q772,Q773,Q774,Q775,Q776,Q777,Q778,Q779,Q780,Q781,Q782,Q783,Q784,Q785,Q786,Q787,Q788,Q789,Q796,Q798,Q799,Q871,Q872,Q874,Q875,Q878,Q900,Q901,Q902,Q903,Q904,Q905,Q906,Q907,Q908,Q909,Q910,Q911,Q912,Q913,Q914,Q915,Q916,Q917,Q918,Q919,Q920,Q921,Q922,Q923,Q924,Q925,Q926,Q927,Q928,Q929,Q930,Q931,Q932,Q933,Q934,Q935,Q936,Q937,Q938,Q939,Q950,Q951,Q952,Q953,Q954,Q955,Q956,Q957,Q958,Q959,Q960,Q961,Q962,Q963,Q964,Q965,Q966,Q967,Q968,Q969,Q992,Q998,Q999','N,C,R')"),
            ('NDQ92', "dbo.Ninos_SinCert('A390,A870,A871','N,C,R')"),
            ('NDQ93', "dbo.Ninos_SinCert('A850,A851,A858,A860,A861,A862,A863,A864,A865,A866,A867,A868,A869','N,C,R')"),
            ('NDQ94', "dbo.Ninos_SinCert('P579','N,C,R')"),
            ('NDQ95', "dbo.Ninos_SinCert('P90X','N,C,R')"),
            ('NDQ96', "dbo.Ninos_SinCert('P941','N,C,R')"),
            ('NDQ97', "dbo.Ninos_SinCert('P942','N,C,R')"),
            ('NDQ98', "dbo.Ninos_SinCert('H351','N,C,R')"),
            ('NDQ99', "dbo.Ninos_SinCert('E030,E031,E033','N,C,R')"),
            ('NDQ100', "dbo.Ninos_SinCert('R629,F800,F801,F802,F804,F808,F809,F820,F821,F822,F823,F824,F825,F826,F827,F828,F829,F830,F831,F832,F833,F834,F835,F836,F837,F838,F839,F840,F842,F844,F845,F848,F849,FR41','N,C,R')"),
            ('NDQ101', "dbo.Ninos_SinCert('P360,P361,P362,P363,P364,P365,P368,P369','N,C,R')"),
            ('NDQ102', "dbo.Ninos_SinCert('A400,A401,A402,A403,A408,A409,A410,A411,A412,A413,A414,A415,A418,A419','N,C,R')"),
            ('NDQ103', "dbo.Ninos_SinCert('G800,G800,G801,G802,G803,G804,G808,G809','N,C,R')"),
            ('NDQ104', "dbo.Ninos_Riesgo('P072,P073','N,C,R')"),
            ('NDQ105', "dbo.Ninos_Riesgo('P070','N,C,R')"),
            ('NDQ106', "dbo.Ninos_Riesgo('Q000,Q001,Q002,Q003,Q004,Q005,Q006,Q007,Q008,Q009,Q090,Q091,Q092,Q093,Q094,Q095,Q096,Q097,Q098,Q099,Q310,Q311,Q312,Q313,Q314,Q315,Q316,Q317,Q318,Q319,Q320,Q321,Q322,Q323,Q324,Q325,Q326,Q327,Q328,Q329,Q330,Q331,Q332,Q333,Q334,Q335,Q336,Q337,Q338,Q339,Q330,Q351,Q352,Q353,Q354,Q355,Q356,Q357,Q358,Q359,Q360,Q361,Q362,Q363,Q364,Q365,Q366,Q367,Q368,Q369,Q370,Q371,Q372,Q373,Q374,Q375,Q376,Q377,Q378,Q379,Q380,Q381,Q650,Q651,Q652,Q653,Q654,Q655,Q656,Q657,Q658,Q659,Q660,Q661,Q662,Q663,Q664,Q665,Q666,Q667,Q668,Q669,Q670,Q671,Q672,Q673,Q674,Q675,Q676,Q677,Q678,Q679,Q680,Q681,Q682,Q683,Q684,Q685,Q686,Q687,Q688,Q689,Q690,Q691,Q692,Q693,Q694,Q695,Q696,Q697,Q698,Q699,Q700,Q701,Q702,Q703,Q704,Q705,Q706,Q707,Q708,Q709,Q710,Q711,Q712,Q713,Q714,Q715,Q716,Q717,Q718,Q719,Q720,Q721,Q722,Q723,Q724,Q725,Q726,Q727,Q728,Q729,Q730,Q731,Q732,Q733,Q734,Q735,Q736,Q737,Q738,Q739,Q740,Q741,Q742,Q743,Q744,Q745,Q746,Q747,Q748,Q749,Q760,Q761,Q762,Q763,Q764,Q765,Q766,Q767,Q768,Q769,Q770,Q771,Q772,Q773,Q774,Q775,Q776,Q777,Q778,Q779,Q780,Q781,Q782,Q783,Q784,Q785,Q786,Q787,Q788,Q789,Q796,Q798,Q799,Q871,Q872,Q874,Q875,Q878,Q900,Q901,Q902,Q903,Q904,Q905,Q906,Q907,Q908,Q909,Q910,Q911,Q912,Q913,Q914,Q915,Q916,Q917,Q918,Q919,Q920,Q921,Q922,Q923,Q924,Q925,Q926,Q927,Q928,Q929,Q930,Q931,Q932,Q933,Q934,Q935,Q936,Q937,Q938,Q939,Q950,Q951,Q952,Q953,Q954,Q955,Q956,Q957,Q958,Q959,Q960,Q961,Q962,Q963,Q964,Q965,Q966,Q967,Q968,Q969,Q992,Q998,Q999','N,C,R')"),
            ('NDQ107', "dbo.Ninos_Riesgo('A390,A870,A871','N,C,R')"),
            ('NDQ108', "dbo.Ninos_Riesgo('A850,A851,A858,A860,A861,A862,A863,A864,A865,A866,A867,A868,A869','N,C,R')"),
            ('NDQ109', "dbo.Ninos_Riesgo('P579','N,C,R')"),
            ('NDQ110', "dbo.Ninos_Riesgo('P90X','N,C,R')"),
            ('NDQ111', "dbo.Ninos_Riesgo('P941','N,C,R')"),
            ('NDQ112', "dbo.Ninos_Riesgo('P942','N,C,R')"),
            ('NDQ113', "dbo.Ninos_Riesgo('H351','N,C,R')"),
            ('NDQ114', "dbo.Ninos_Riesgo('E030,E031,E033','N,C,R')"),
            ('NDQ115', "dbo.Ninos_Riesgo('R629,F800,F801,F802,F804,F808,F809,F820,F821,F822,F823,F824,F825,F826,F827,F828,F829,F830,F831,F832,F833,F834,F835,F836,F837,F838,F839,F840,F842,F844,F845,F848,F849,FR41','N,C,R')"),
            ('NDQ116', "dbo.Ninos_Riesgo('P360,P361,P362,P363,P364,P365,P368,P369','N,C,R')"),
            ('NDQ117', "dbo.Ninos_Riesgo('A400,A401,A402,A403,A408,A409,A410,A411,A412,A413,A414,A415,A418,A419','N,C,R')"),
            ('NDQ118', "dbo.Ninos_Riesgo('G800,G800,G801,G802,G803,G804,G808,G809','N,C,R')")

        ],

        "FACT_DISC_SNAPSHOT_COMUNID_AGENTES": [

            ('NDQ3853', "dbo.Capa_Agent_N('C0006', '1')"),
            ('NDQ3854', "dbo.Capa_Agent_N('C0009,C3141', '1')"),
            ('NDQ3855', "dbo.Capa_Agent_N('C0010', '1')"),
            ('NDQ3856', "dbo.Capa_Agent_N('C3151', '1')"),
            ('NDQ3857', "dbo.Capa_Agent_Cap('C0006', '1')"),
            ('NDQ3858', "dbo.Capa_Agent_Cap('C0009,C3141', '1')"),
            ('NDQ3859', "dbo.Capa_Agent_Cap('C0010', '1')"),
            ('NDQ3860', "dbo.Capa_Agent_Cap('C3151', '1')"),
            ('NDQ3861', "dbo.Capa_Agent_N('C0006', '2')"),
            ('NDQ3862', "dbo.Capa_Agent_N('C0009,C3141', '2')"),
            ('NDQ3863', "dbo.Capa_Agent_N('C0010', '2')"),
            ('NDQ3864', "dbo.Capa_Agent_N('C3151', '2')"),
            ('NDQ3865', "dbo.Capa_Agent_Cap('C0006', '2')"),
            ('NDQ3866', "dbo.Capa_Agent_Cap('C0009,C3141', '2')"),
            ('NDQ3867', "dbo.Capa_Agent_Cap('C0010', '2')"),
            ('NDQ3868', "dbo.Capa_Agent_Cap('C3151', '2')")

        ],

        "FACT_DISC_SNAPSHOT_ACTORES_BL1": [

            ('NDQ3900', "dbo.Actores_N('APP91', 'C0001', '1')"),
            ('NDQ3901', "dbo.Actores_N('APP92', 'C0001', '1')"),
            ('NDQ3902', "dbo.Actores_N('APP93', 'C0001', '1')"),
            ('NDQ3903', "dbo.Actores_N('APP94', 'C0001', '1')"),
            ('NDQ3904', "dbo.Actores_N('APP95', 'C0001', '1')"),
            ('NDQ3905', "dbo.Actores_N('APP96', 'C0001', '1')"),
            ('NDQ3906', "dbo.Actores_N('APP98', 'C0001', '1')"),
            ('NDQ3907', "dbo.Actores_N('APP99', 'C0001', '1')"),
            ('NDQ3908', "dbo.Actores_N('APP101', 'C0001', '1')"),
            ('NDQ3909', "dbo.Actores_N('APP102', 'C0001', '1')"),
            ('NDQ3910', "dbo.Actores_N('APP104', 'C0001', '1')"),
            ('NDQ3911', "dbo.Actores_N('APP106', 'C0001', '1')"),
            ('NDQ3912', "dbo.Actores_N('APP108', 'C0001', '1')"),
            ('NDQ3913', "dbo.Actores_N('APP100', 'C0001', '1')"),
            ('NDQ3914', "dbo.Actores_N('APP103', 'C0001', '1')"),
            ('NDQ3915', "dbo.Actores_N('APP105', 'C0001', '1')"),
            ('NDQ3916', "dbo.Actores_N('APP111', 'C0001', '1')"),
            ('NDQ3917', "dbo.Actores_N('APP119', 'C0001', '1')"),
            ('NDQ3918', "dbo.Actores_N('APP121', 'C0001', '1')"),
            ('NDQ3919', "dbo.Actores_N('APP123', 'C0001', '1')"),
            ('NDQ3920', "dbo.Actores_N('APP136', 'C0001', '1')"),
            ('NDQ3921', "dbo.Actores_N('APP139', 'C0001', '1')"),
            ('NDQ3922', "dbo.Actores_N('APP140', 'C0001', '1')"),
            ('NDQ3923', "dbo.Actores_N('APP141', 'C0001', '1')"),
            ('NDQ3924', "dbo.Actores_N('APP142', 'C0001', '1')"),
            ('NDQ3925', "dbo.Actores_N('APP143', 'C0001', '1')"),
            ('NDQ3926', "dbo.Actores_N('APP144', 'C0001', '1')"),
            ('NDQ3927', "dbo.Actores_N('APP145', 'C0001', '1')"),
            ('NDQ3928', "dbo.Actores_N('APP146', 'C0001', '1')"),
            ('NDQ3929', "dbo.Actores_N('APP150', 'C0001', '1')"),
            ('NDQ3930', "dbo.Actores_N('APP163', 'C0001', '1')"),
            ('NDQ3931', "dbo.Actores_N('APP165', 'C0001', '1')"),
            ('NDQ3932', "dbo.Actores_N('APP166', 'C0001', '1')"),
            ('NDQ3933', "dbo.Actores_N('APP168', 'C0001', '1')"),
            ('NDQ3934', "dbo.Actores_Cap('APP91', 'C0001', '1')"),
            ('NDQ3935', "dbo.Actores_Cap('APP92', 'C0001', '1')"),
            ('NDQ3936', "dbo.Actores_Cap('APP93', 'C0001', '1')"),
            ('NDQ3937', "dbo.Actores_Cap('APP94', 'C0001', '1')"),
            ('NDQ3938', "dbo.Actores_Cap('APP95', 'C0001', '1')"),
            ('NDQ3939', "dbo.Actores_Cap('APP96', 'C0001', '1')"),
            ('NDQ3940', "dbo.Actores_Cap('APP98', 'C0001', '1')"),
            ('NDQ3941', "dbo.Actores_Cap('APP99', 'C0001', '1')"),
            ('NDQ3942', "dbo.Actores_Cap('APP101', 'C0001', '1')"),
            ('NDQ3943', "dbo.Actores_Cap('APP102', 'C0001', '1')"),
            ('NDQ3944', "dbo.Actores_Cap('APP104', 'C0001', '1')"),
            ('NDQ3945', "dbo.Actores_Cap('APP106', 'C0001', '1')"),
            ('NDQ3946', "dbo.Actores_Cap('APP108', 'C0001', '1')"),
            ('NDQ3947', "dbo.Actores_Cap('APP100', 'C0001', '1')"),
            ('NDQ3948', "dbo.Actores_Cap('APP103', 'C0001', '1')"),
            ('NDQ3949', "dbo.Actores_Cap('APP105', 'C0001', '1')"),
            ('NDQ3950', "dbo.Actores_Cap('APP111', 'C0001', '1')"),
            ('NDQ3951', "dbo.Actores_Cap('APP119', 'C0001', '1')"),
            ('NDQ3952', "dbo.Actores_Cap('APP121', 'C0001', '1')"),
            ('NDQ3953', "dbo.Actores_Cap('APP123', 'C0001', '1')"),
            ('NDQ3954', "dbo.Actores_Cap('APP136', 'C0001', '1')"),
            ('NDQ3955', "dbo.Actores_Cap('APP139', 'C0001', '1')"),
            ('NDQ3956', "dbo.Actores_Cap('APP140', 'C0001', '1')"),
            ('NDQ3957', "dbo.Actores_Cap('APP141', 'C0001', '1')"),
            ('NDQ3958', "dbo.Actores_Cap('APP142', 'C0001', '1')"),
            ('NDQ3959', "dbo.Actores_Cap('APP143', 'C0001', '1')"),
            ('NDQ3960', "dbo.Actores_Cap('APP144', 'C0001', '1')"),
            ('NDQ3961', "dbo.Actores_Cap('APP145', 'C0001', '1')"),
            ('NDQ3962', "dbo.Actores_Cap('APP146', 'C0001', '1')"),
            ('NDQ3963', "dbo.Actores_Cap('APP150', 'C0001', '1')"),
            ('NDQ3964', "dbo.Actores_Cap('APP163', 'C0001', '1')"),
            ('NDQ3965', "dbo.Actores_Cap('APP165', 'C0001', '1')"),
            ('NDQ3966', "dbo.Actores_Cap('APP166', 'C0001', '1')"),
            ('NDQ3967', "dbo.Actores_Cap('APP168', 'C0001', '1')"),
            ('NDQ3968', "dbo.Actores_N('APP91', 'C0002', '1')"),
            ('NDQ3969', "dbo.Actores_N('APP92', 'C0002', '1')"),
            ('NDQ3970', "dbo.Actores_N('APP93', 'C0002', '1')"),
            ('NDQ3971', "dbo.Actores_N('APP94', 'C0002', '1')"),
            ('NDQ3972', "dbo.Actores_N('APP95', 'C0002', '1')"),
            ('NDQ3973', "dbo.Actores_N('APP96', 'C0002', '1')"),
            ('NDQ3974', "dbo.Actores_N('APP98', 'C0002', '1')"),
            ('NDQ3975', "dbo.Actores_N('APP99', 'C0002', '1')"),
            ('NDQ3976', "dbo.Actores_N('APP101', 'C0002', '1')"),
            ('NDQ3977', "dbo.Actores_N('APP102', 'C0002', '1')"),
            ('NDQ3978', "dbo.Actores_N('APP104', 'C0002', '1')"),
            ('NDQ3979', "dbo.Actores_N('APP106', 'C0002', '1')"),
            ('NDQ3980', "dbo.Actores_N('APP108', 'C0002', '1')"),
            ('NDQ3981', "dbo.Actores_N('APP100', 'C0002', '1')"),
            ('NDQ3982', "dbo.Actores_N('APP103', 'C0002', '1')"),
            ('NDQ3983', "dbo.Actores_N('APP105', 'C0002', '1')"),
            ('NDQ3984', "dbo.Actores_N('APP111', 'C0002', '1')"),
            ('NDQ3985', "dbo.Actores_N('APP119', 'C0002', '1')"),
            ('NDQ3986', "dbo.Actores_N('APP121', 'C0002', '1')"),
            ('NDQ3987', "dbo.Actores_N('APP123', 'C0002', '1')"),
            ('NDQ3988', "dbo.Actores_N('APP136', 'C0002', '1')"),
            ('NDQ3989', "dbo.Actores_N('APP139', 'C0002', '1')"),
            ('NDQ3990', "dbo.Actores_N('APP140', 'C0002', '1')"),
            ('NDQ3991', "dbo.Actores_N('APP141', 'C0002', '1')"),
            ('NDQ3992', "dbo.Actores_N('APP142', 'C0002', '1')"),
            ('NDQ3993', "dbo.Actores_N('APP143', 'C0002', '1')"),
            ('NDQ3994', "dbo.Actores_N('APP144', 'C0002', '1')"),
            ('NDQ3995', "dbo.Actores_N('APP145', 'C0002', '1')"),
            ('NDQ3996', "dbo.Actores_N('APP146', 'C0002', '1')"),
            ('NDQ3997', "dbo.Actores_N('APP150', 'C0002', '1')"),
            ('NDQ3998', "dbo.Actores_N('APP163', 'C0002', '1')"),
            ('NDQ3999', "dbo.Actores_N('APP165', 'C0002', '1')"),
            ('NDQ4000', "dbo.Actores_N('APP166', 'C0002', '1')"),
            ('NDQ4001', "dbo.Actores_N('APP168', 'C0002', '1')"),
            ('NDQ4002', "dbo.Actores_Cap('APP91', 'C0002', '1')"),
            ('NDQ4003', "dbo.Actores_Cap('APP92', 'C0002', '1')"),
            ('NDQ4004', "dbo.Actores_Cap('APP93', 'C0002', '1')"),
            ('NDQ4005', "dbo.Actores_Cap('APP94', 'C0002', '1')"),
            ('NDQ4006', "dbo.Actores_Cap('APP95', 'C0002', '1')"),
            ('NDQ4007', "dbo.Actores_Cap('APP96', 'C0002', '1')"),
            ('NDQ4008', "dbo.Actores_Cap('APP98', 'C0002', '1')"),
            ('NDQ4009', "dbo.Actores_Cap('APP99', 'C0002', '1')"),
            ('NDQ4010', "dbo.Actores_Cap('APP101', 'C0002', '1')"),
            ('NDQ4011', "dbo.Actores_Cap('APP102', 'C0002', '1')"),
            ('NDQ4012', "dbo.Actores_Cap('APP104', 'C0002', '1')"),
            ('NDQ4013', "dbo.Actores_Cap('APP106', 'C0002', '1')"),
            ('NDQ4014', "dbo.Actores_Cap('APP108', 'C0002', '1')"),
            ('NDQ4015', "dbo.Actores_Cap('APP100', 'C0002', '1')"),
            ('NDQ4016', "dbo.Actores_Cap('APP103', 'C0002', '1')"),
            ('NDQ4017', "dbo.Actores_Cap('APP105', 'C0002', '1')"),
            ('NDQ4018', "dbo.Actores_Cap('APP111', 'C0002', '1')"),
            ('NDQ4019', "dbo.Actores_Cap('APP119', 'C0002', '1')"),
            ('NDQ4020', "dbo.Actores_Cap('APP121', 'C0002', '1')"),
            ('NDQ4021', "dbo.Actores_Cap('APP123', 'C0002', '1')"),
            ('NDQ4022', "dbo.Actores_Cap('APP136', 'C0002', '1')"),
            ('NDQ4023', "dbo.Actores_Cap('APP139', 'C0002', '1')"),
            ('NDQ4024', "dbo.Actores_Cap('APP140', 'C0002', '1')"),
            ('NDQ4025', "dbo.Actores_Cap('APP141', 'C0002', '1')"),
            ('NDQ4026', "dbo.Actores_Cap('APP142', 'C0002', '1')"),
            ('NDQ4027', "dbo.Actores_Cap('APP143', 'C0002', '1')"),
            ('NDQ4028', "dbo.Actores_Cap('APP144', 'C0002', '1')"),
            ('NDQ4029', "dbo.Actores_Cap('APP145', 'C0002', '1')"),
            ('NDQ4030', "dbo.Actores_Cap('APP146', 'C0002', '1')"),
            ('NDQ4031', "dbo.Actores_Cap('APP150', 'C0002', '1')"),
            ('NDQ4032', "dbo.Actores_Cap('APP163', 'C0002', '1')"),
            ('NDQ4033', "dbo.Actores_Cap('APP165', 'C0002', '1')"),
            ('NDQ4034', "dbo.Actores_Cap('APP166', 'C0002', '1')"),
            ('NDQ4035', "dbo.Actores_Cap('APP168', 'C0002', '1')"),
            ('NDQ4036', "dbo.Actores_N('APP91', 'C0003', '1')"),
            ('NDQ4037', "dbo.Actores_N('APP92', 'C0003', '1')"),
            ('NDQ4038', "dbo.Actores_N('APP93', 'C0003', '1')"),
            ('NDQ4039', "dbo.Actores_N('APP94', 'C0003', '1')"),
            ('NDQ4040', "dbo.Actores_N('APP95', 'C0003', '1')"),
            ('NDQ4041', "dbo.Actores_N('APP96', 'C0003', '1')"),
            ('NDQ4042', "dbo.Actores_N('APP98', 'C0003', '1')"),
            ('NDQ4043', "dbo.Actores_N('APP99', 'C0003', '1')"),
            ('NDQ4044', "dbo.Actores_N('APP101', 'C0003', '1')"),
            ('NDQ4045', "dbo.Actores_N('APP102', 'C0003', '1')"),
            ('NDQ4046', "dbo.Actores_N('APP104', 'C0003', '1')"),
            ('NDQ4047', "dbo.Actores_N('APP106', 'C0003', '1')"),
            ('NDQ4048', "dbo.Actores_N('APP108', 'C0003', '1')"),
            ('NDQ4049', "dbo.Actores_N('APP100', 'C0003', '1')"),
            ('NDQ4050', "dbo.Actores_N('APP103', 'C0003', '1')"),
            ('NDQ4051', "dbo.Actores_N('APP105', 'C0003', '1')"),
            ('NDQ4052', "dbo.Actores_N('APP111', 'C0003', '1')"),
            ('NDQ4053', "dbo.Actores_N('APP119', 'C0003', '1')"),
            ('NDQ4054', "dbo.Actores_N('APP121', 'C0003', '1')"),
            ('NDQ4055', "dbo.Actores_N('APP123', 'C0003', '1')"),
            ('NDQ4056', "dbo.Actores_N('APP136', 'C0003', '1')"),
            ('NDQ4057', "dbo.Actores_N('APP139', 'C0003', '1')"),
            ('NDQ4058', "dbo.Actores_N('APP140', 'C0003', '1')"),
            ('NDQ4059', "dbo.Actores_N('APP141', 'C0003', '1')"),
            ('NDQ4060', "dbo.Actores_N('APP142', 'C0003', '1')"),
            ('NDQ4061', "dbo.Actores_N('APP143', 'C0003', '1')"),
            ('NDQ4062', "dbo.Actores_N('APP144', 'C0003', '1')"),
            ('NDQ4063', "dbo.Actores_N('APP145', 'C0003', '1')"),
            ('NDQ4064', "dbo.Actores_N('APP146', 'C0003', '1')"),
            ('NDQ4065', "dbo.Actores_N('APP150', 'C0003', '1')"),
            ('NDQ4066', "dbo.Actores_N('APP163', 'C0003', '1')"),
            ('NDQ4067', "dbo.Actores_N('APP165', 'C0003', '1')"),
            ('NDQ4068', "dbo.Actores_N('APP166', 'C0003', '1')"),
            ('NDQ4069', "dbo.Actores_N('APP168', 'C0003', '1')"),
            ('NDQ4070', "dbo.Actores_Cap('APP91', 'C0003', '1')"),
            ('NDQ4071', "dbo.Actores_Cap('APP92', 'C0003', '1')"),
            ('NDQ4072', "dbo.Actores_Cap('APP93', 'C0003', '1')"),
            ('NDQ4073', "dbo.Actores_Cap('APP94', 'C0003', '1')"),
            ('NDQ4074', "dbo.Actores_Cap('APP95', 'C0003', '1')"),
            ('NDQ4075', "dbo.Actores_Cap('APP96', 'C0003', '1')"),
            ('NDQ4076', "dbo.Actores_Cap('APP98', 'C0003', '1')"),
            ('NDQ4077', "dbo.Actores_Cap('APP99', 'C0003', '1')"),
            ('NDQ4078', "dbo.Actores_Cap('APP101', 'C0003', '1')"),
            ('NDQ4079', "dbo.Actores_Cap('APP102', 'C0003', '1')"),
            ('NDQ4080', "dbo.Actores_Cap('APP104', 'C0003', '1')"),
            ('NDQ4081', "dbo.Actores_Cap('APP106', 'C0003', '1')"),
            ('NDQ4082', "dbo.Actores_Cap('APP108', 'C0003', '1')"),
            ('NDQ4083', "dbo.Actores_Cap('APP100', 'C0003', '1')"),
            ('NDQ4084', "dbo.Actores_Cap('APP103', 'C0003', '1')"),
            ('NDQ4085', "dbo.Actores_Cap('APP105', 'C0003', '1')"),
            ('NDQ4086', "dbo.Actores_Cap('APP111', 'C0003', '1')"),
            ('NDQ4087', "dbo.Actores_Cap('APP119', 'C0003', '1')"),
            ('NDQ4088', "dbo.Actores_Cap('APP121', 'C0003', '1')"),
            ('NDQ4089', "dbo.Actores_Cap('APP123', 'C0003', '1')"),
            ('NDQ4090', "dbo.Actores_Cap('APP136', 'C0003', '1')"),
            ('NDQ4091', "dbo.Actores_Cap('APP139', 'C0003', '1')"),
            ('NDQ4092', "dbo.Actores_Cap('APP140', 'C0003', '1')"),
            ('NDQ4093', "dbo.Actores_Cap('APP141', 'C0003', '1')"),
            ('NDQ4094', "dbo.Actores_Cap('APP142', 'C0003', '1')"),
            ('NDQ4095', "dbo.Actores_Cap('APP143', 'C0003', '1')"),
            ('NDQ4096', "dbo.Actores_Cap('APP144', 'C0003', '1')"),
            ('NDQ4097', "dbo.Actores_Cap('APP145', 'C0003', '1')"),
            ('NDQ4098', "dbo.Actores_Cap('APP146', 'C0003', '1')"),
            ('NDQ4099', "dbo.Actores_Cap('APP150', 'C0003', '1')"),
            ('NDQ4100', "dbo.Actores_Cap('APP163', 'C0003', '1')"),
            ('NDQ4101', "dbo.Actores_Cap('APP165', 'C0003', '1')"),
            ('NDQ4102', "dbo.Actores_Cap('APP166', 'C0003', '1')"),
            ('NDQ4103', "dbo.Actores_Cap('APP168', 'C0003', '1')"),
            ('NDQ4104', "dbo.Actores_N('APP91', 'C0004', '1')"),
            ('NDQ4105', "dbo.Actores_N('APP92', 'C0004', '1')"),
            ('NDQ4106', "dbo.Actores_N('APP93', 'C0004', '1')"),
            ('NDQ4107', "dbo.Actores_N('APP94', 'C0004', '1')"),
            ('NDQ4108', "dbo.Actores_N('APP95', 'C0004', '1')"),
            ('NDQ4109', "dbo.Actores_N('APP96', 'C0004', '1')"),
            ('NDQ4110', "dbo.Actores_N('APP98', 'C0004', '1')"),
            ('NDQ4111', "dbo.Actores_N('APP99', 'C0004', '1')"),
            ('NDQ4112', "dbo.Actores_N('APP101', 'C0004', '1')"),
            ('NDQ4113', "dbo.Actores_N('APP102', 'C0004', '1')"),
            ('NDQ4114', "dbo.Actores_N('APP104', 'C0004', '1')"),
            ('NDQ4115', "dbo.Actores_N('APP106', 'C0004', '1')"),
            ('NDQ4116', "dbo.Actores_N('APP108', 'C0004', '1')"),
            ('NDQ4117', "dbo.Actores_N('APP100', 'C0004', '1')"),
            ('NDQ4118', "dbo.Actores_N('APP103', 'C0004', '1')"),
            ('NDQ4119', "dbo.Actores_N('APP105', 'C0004', '1')"),
            ('NDQ4120', "dbo.Actores_N('APP111', 'C0004', '1')"),
            ('NDQ4121', "dbo.Actores_N('APP119', 'C0004', '1')"),
            ('NDQ4122', "dbo.Actores_N('APP121', 'C0004', '1')"),
            ('NDQ4123', "dbo.Actores_N('APP123', 'C0004', '1')"),
            ('NDQ4124', "dbo.Actores_N('APP136', 'C0004', '1')"),
            ('NDQ4125', "dbo.Actores_N('APP139', 'C0004', '1')"),
            ('NDQ4126', "dbo.Actores_N('APP140', 'C0004', '1')"),
            ('NDQ4127', "dbo.Actores_N('APP141', 'C0004', '1')"),
            ('NDQ4128', "dbo.Actores_N('APP142', 'C0004', '1')"),
            ('NDQ4129', "dbo.Actores_N('APP143', 'C0004', '1')"),
            ('NDQ4130', "dbo.Actores_N('APP144', 'C0004', '1')"),
            ('NDQ4131', "dbo.Actores_N('APP145', 'C0004', '1')"),
            ('NDQ4132', "dbo.Actores_N('APP146', 'C0004', '1')"),
            ('NDQ4133', "dbo.Actores_N('APP150', 'C0004', '1')"),
            ('NDQ4134', "dbo.Actores_N('APP163', 'C0004', '1')"),
            ('NDQ4135', "dbo.Actores_N('APP165', 'C0004', '1')"),
            ('NDQ4136', "dbo.Actores_N('APP166', 'C0004', '1')"),
            ('NDQ4137', "dbo.Actores_N('APP168', 'C0004', '1')"),
            ('NDQ4138', "dbo.Actores_Cap('APP91', 'C0004', '1')"),
            ('NDQ4139', "dbo.Actores_Cap('APP92', 'C0004', '1')"),
            ('NDQ4140', "dbo.Actores_Cap('APP93', 'C0004', '1')"),
            ('NDQ4141', "dbo.Actores_Cap('APP94', 'C0004', '1')"),
            ('NDQ4142', "dbo.Actores_Cap('APP95', 'C0004', '1')"),
            ('NDQ4143', "dbo.Actores_Cap('APP96', 'C0004', '1')"),
            ('NDQ4144', "dbo.Actores_Cap('APP98', 'C0004', '1')"),
            ('NDQ4145', "dbo.Actores_Cap('APP99', 'C0004', '1')"),
            ('NDQ4146', "dbo.Actores_Cap('APP101', 'C0004', '1')"),
            ('NDQ4147', "dbo.Actores_Cap('APP102', 'C0004', '1')"),
            ('NDQ4148', "dbo.Actores_Cap('APP104', 'C0004', '1')"),
            ('NDQ4149', "dbo.Actores_Cap('APP106', 'C0004', '1')"),
            ('NDQ4150', "dbo.Actores_Cap('APP108', 'C0004', '1')"),
            ('NDQ4151', "dbo.Actores_Cap('APP100', 'C0004', '1')"),
            ('NDQ4152', "dbo.Actores_Cap('APP103', 'C0004', '1')"),
            ('NDQ4153', "dbo.Actores_Cap('APP105', 'C0004', '1')"),
            ('NDQ4154', "dbo.Actores_Cap('APP111', 'C0004', '1')"),
            ('NDQ4155', "dbo.Actores_Cap('APP119', 'C0004', '1')"),
            ('NDQ4156', "dbo.Actores_Cap('APP121', 'C0004', '1')"),
            ('NDQ4157', "dbo.Actores_Cap('APP123', 'C0004', '1')"),
            ('NDQ4158', "dbo.Actores_Cap('APP136', 'C0004', '1')"),
            ('NDQ4159', "dbo.Actores_Cap('APP139', 'C0004', '1')"),
            ('NDQ4160', "dbo.Actores_Cap('APP140', 'C0004', '1')"),
            ('NDQ4161', "dbo.Actores_Cap('APP141', 'C0004', '1')"),
            ('NDQ4162', "dbo.Actores_Cap('APP142', 'C0004', '1')"),
            ('NDQ4163', "dbo.Actores_Cap('APP143', 'C0004', '1')"),
            ('NDQ4164', "dbo.Actores_Cap('APP144', 'C0004', '1')"),
            ('NDQ4165', "dbo.Actores_Cap('APP145', 'C0004', '1')"),
            ('NDQ4166', "dbo.Actores_Cap('APP146', 'C0004', '1')"),
            ('NDQ4167', "dbo.Actores_Cap('APP150', 'C0004', '1')"),
            ('NDQ4168', "dbo.Actores_Cap('APP163', 'C0004', '1')"),
            ('NDQ4169', "dbo.Actores_Cap('APP165', 'C0004', '1')"),
            ('NDQ4170', "dbo.Actores_Cap('APP166', 'C0004', '1')"),
            ('NDQ4171', "dbo.Actores_Cap('APP168', 'C0004', '1')"),
            ('NDQ4172', "dbo.Actores_N('APP91', 'C0005', '1')"),
            ('NDQ4173', "dbo.Actores_N('APP92', 'C0005', '1')"),
            ('NDQ4174', "dbo.Actores_N('APP93', 'C0005', '1')"),
            ('NDQ4175', "dbo.Actores_N('APP94', 'C0005', '1')"),
            ('NDQ4176', "dbo.Actores_N('APP95', 'C0005', '1')"),
            ('NDQ4177', "dbo.Actores_N('APP96', 'C0005', '1')"),
            ('NDQ4178', "dbo.Actores_N('APP98', 'C0005', '1')"),
            ('NDQ4179', "dbo.Actores_N('APP99', 'C0005', '1')"),
            ('NDQ4180', "dbo.Actores_N('APP101', 'C0005', '1')"),
            ('NDQ4181', "dbo.Actores_N('APP102', 'C0005', '1')"),
            ('NDQ4182', "dbo.Actores_N('APP104', 'C0005', '1')"),
            ('NDQ4183', "dbo.Actores_N('APP106', 'C0005', '1')"),
            ('NDQ4184', "dbo.Actores_N('APP108', 'C0005', '1')"),
            ('NDQ4185', "dbo.Actores_N('APP100', 'C0005', '1')"),
            ('NDQ4186', "dbo.Actores_N('APP103', 'C0005', '1')"),
            ('NDQ4187', "dbo.Actores_N('APP105', 'C0005', '1')"),
            ('NDQ4188', "dbo.Actores_N('APP111', 'C0005', '1')"),
            ('NDQ4189', "dbo.Actores_N('APP119', 'C0005', '1')"),
            ('NDQ4190', "dbo.Actores_N('APP121', 'C0005', '1')"),
            ('NDQ4191', "dbo.Actores_N('APP123', 'C0005', '1')"),
            ('NDQ4192', "dbo.Actores_N('APP136', 'C0005', '1')"),
            ('NDQ4193', "dbo.Actores_N('APP139', 'C0005', '1')"),
            ('NDQ4194', "dbo.Actores_N('APP140', 'C0005', '1')"),
            ('NDQ4195', "dbo.Actores_N('APP141', 'C0005', '1')"),
            ('NDQ4196', "dbo.Actores_N('APP142', 'C0005', '1')"),
            ('NDQ4197', "dbo.Actores_N('APP143', 'C0005', '1')"),
            ('NDQ4198', "dbo.Actores_N('APP144', 'C0005', '1')"),
            ('NDQ4199', "dbo.Actores_N('APP145', 'C0005', '1')"),
            ('NDQ4200', "dbo.Actores_N('APP146', 'C0005', '1')"),
            ('NDQ4201', "dbo.Actores_N('APP150', 'C0005', '1')"),
            ('NDQ4202', "dbo.Actores_N('APP163', 'C0005', '1')"),
            ('NDQ4203', "dbo.Actores_N('APP165', 'C0005', '1')"),
            ('NDQ4204', "dbo.Actores_N('APP166', 'C0005', '1')"),
            ('NDQ4205', "dbo.Actores_N('APP168', 'C0005', '1')"),
            ('NDQ4206', "dbo.Actores_Cap('APP91', 'C0005', '1')"),
            ('NDQ4207', "dbo.Actores_Cap('APP92', 'C0005', '1')"),
            ('NDQ4208', "dbo.Actores_Cap('APP93', 'C0005', '1')"),
            ('NDQ4209', "dbo.Actores_Cap('APP94', 'C0005', '1')"),
            ('NDQ4210', "dbo.Actores_Cap('APP95', 'C0005', '1')"),
            ('NDQ4211', "dbo.Actores_Cap('APP96', 'C0005', '1')"),
            ('NDQ4212', "dbo.Actores_Cap('APP98', 'C0005', '1')"),
            ('NDQ4213', "dbo.Actores_Cap('APP99', 'C0005', '1')"),
            ('NDQ4214', "dbo.Actores_Cap('APP101', 'C0005', '1')"),
            ('NDQ4215', "dbo.Actores_Cap('APP102', 'C0005', '1')"),
            ('NDQ4216', "dbo.Actores_Cap('APP104', 'C0005', '1')"),
            ('NDQ4217', "dbo.Actores_Cap('APP106', 'C0005', '1')"),
            ('NDQ4218', "dbo.Actores_Cap('APP108', 'C0005', '1')"),
            ('NDQ4219', "dbo.Actores_Cap('APP100', 'C0005', '1')"),
            ('NDQ4220', "dbo.Actores_Cap('APP103', 'C0005', '1')"),
            ('NDQ4221', "dbo.Actores_Cap('APP105', 'C0005', '1')"),
            ('NDQ4222', "dbo.Actores_Cap('APP111', 'C0005', '1')"),
            ('NDQ4223', "dbo.Actores_Cap('APP119', 'C0005', '1')"),
            ('NDQ4224', "dbo.Actores_Cap('APP121', 'C0005', '1')"),
            ('NDQ4225', "dbo.Actores_Cap('APP123', 'C0005', '1')"),
            ('NDQ4226', "dbo.Actores_Cap('APP136', 'C0005', '1')"),
            ('NDQ4227', "dbo.Actores_Cap('APP139', 'C0005', '1')"),
            ('NDQ4228', "dbo.Actores_Cap('APP140', 'C0005', '1')"),
            ('NDQ4229', "dbo.Actores_Cap('APP141', 'C0005', '1')"),
            ('NDQ4230', "dbo.Actores_Cap('APP142', 'C0005', '1')"),
            ('NDQ4231', "dbo.Actores_Cap('APP143', 'C0005', '1')"),
            ('NDQ4232', "dbo.Actores_Cap('APP144', 'C0005', '1')"),
            ('NDQ4233', "dbo.Actores_Cap('APP145', 'C0005', '1')"),
            ('NDQ4234', "dbo.Actores_Cap('APP146', 'C0005', '1')"),
            ('NDQ4235', "dbo.Actores_Cap('APP150', 'C0005', '1')"),
            ('NDQ4236', "dbo.Actores_Cap('APP163', 'C0005', '1')"),
            ('NDQ4237', "dbo.Actores_Cap('APP165', 'C0005', '1')"),
            ('NDQ4238', "dbo.Actores_Cap('APP166', 'C0005', '1')"),
            ('NDQ4239', "dbo.Actores_Cap('APP168', 'C0005', '1')"),
            ('NDQ4240', "dbo.Actores_N('APP91', 'C0006', '1')"),
            ('NDQ4241', "dbo.Actores_N('APP92', 'C0006', '1')"),
            ('NDQ4242', "dbo.Actores_N('APP93', 'C0006', '1')"),
            ('NDQ4243', "dbo.Actores_N('APP94', 'C0006', '1')"),
            ('NDQ4244', "dbo.Actores_N('APP95', 'C0006', '1')"),
            ('NDQ4245', "dbo.Actores_N('APP96', 'C0006', '1')"),
            ('NDQ4246', "dbo.Actores_N('APP98', 'C0006', '1')"),
            ('NDQ4247', "dbo.Actores_N('APP99', 'C0006', '1')"),
            ('NDQ4248', "dbo.Actores_N('APP101', 'C0006', '1')"),
            ('NDQ4249', "dbo.Actores_N('APP102', 'C0006', '1')"),
            ('NDQ4250', "dbo.Actores_N('APP104', 'C0006', '1')"),
            ('NDQ4251', "dbo.Actores_N('APP106', 'C0006', '1')"),
            ('NDQ4252', "dbo.Actores_N('APP108', 'C0006', '1')"),
            ('NDQ4253', "dbo.Actores_N('APP100', 'C0006', '1')"),
            ('NDQ4254', "dbo.Actores_N('APP103', 'C0006', '1')"),
            ('NDQ4255', "dbo.Actores_N('APP105', 'C0006', '1')"),
            ('NDQ4256', "dbo.Actores_N('APP111', 'C0006', '1')"),
            ('NDQ4257', "dbo.Actores_N('APP119', 'C0006', '1')"),
            ('NDQ4258', "dbo.Actores_N('APP121', 'C0006', '1')"),
            ('NDQ4259', "dbo.Actores_N('APP123', 'C0006', '1')"),
            ('NDQ4260', "dbo.Actores_N('APP136', 'C0006', '1')"),
            ('NDQ4261', "dbo.Actores_N('APP139', 'C0006', '1')"),
            ('NDQ4262', "dbo.Actores_N('APP140', 'C0006', '1')"),
            ('NDQ4263', "dbo.Actores_N('APP141', 'C0006', '1')"),
            ('NDQ4264', "dbo.Actores_N('APP142', 'C0006', '1')"),
            ('NDQ4265', "dbo.Actores_N('APP143', 'C0006', '1')"),
            ('NDQ4266', "dbo.Actores_N('APP144', 'C0006', '1')"),
            ('NDQ4267', "dbo.Actores_N('APP145', 'C0006', '1')"),
            ('NDQ4268', "dbo.Actores_N('APP146', 'C0006', '1')"),
            ('NDQ4269', "dbo.Actores_N('APP150', 'C0006', '1')"),
            ('NDQ4270', "dbo.Actores_N('APP163', 'C0006', '1')"),
            ('NDQ4271', "dbo.Actores_N('APP165', 'C0006', '1')"),
            ('NDQ4272', "dbo.Actores_N('APP166', 'C0006', '1')"),
            ('NDQ4273', "dbo.Actores_N('APP168', 'C0006', '1')"),
            ('NDQ4274', "dbo.Actores_Cap('APP91', 'C0006', '1')"),
            ('NDQ4275', "dbo.Actores_Cap('APP92', 'C0006', '1')"),
            ('NDQ4276', "dbo.Actores_Cap('APP93', 'C0006', '1')"),
            ('NDQ4277', "dbo.Actores_Cap('APP94', 'C0006', '1')"),
            ('NDQ4278', "dbo.Actores_Cap('APP95', 'C0006', '1')"),
            ('NDQ4279', "dbo.Actores_Cap('APP96', 'C0006', '1')"),
            ('NDQ4280', "dbo.Actores_Cap('APP98', 'C0006', '1')"),
            ('NDQ4281', "dbo.Actores_Cap('APP99', 'C0006', '1')"),
            ('NDQ4282', "dbo.Actores_Cap('APP101', 'C0006', '1')"),
            ('NDQ4283', "dbo.Actores_Cap('APP102', 'C0006', '1')"),
            ('NDQ4284', "dbo.Actores_Cap('APP104', 'C0006', '1')"),
            ('NDQ4285', "dbo.Actores_Cap('APP106', 'C0006', '1')"),
            ('NDQ4286', "dbo.Actores_Cap('APP108', 'C0006', '1')"),
            ('NDQ4287', "dbo.Actores_Cap('APP100', 'C0006', '1')"),
            ('NDQ4288', "dbo.Actores_Cap('APP103', 'C0006', '1')"),
            ('NDQ4289', "dbo.Actores_Cap('APP105', 'C0006', '1')"),
            ('NDQ4290', "dbo.Actores_Cap('APP111', 'C0006', '1')"),
            ('NDQ4291', "dbo.Actores_Cap('APP119', 'C0006', '1')"),
            ('NDQ4292', "dbo.Actores_Cap('APP121', 'C0006', '1')"),
            ('NDQ4293', "dbo.Actores_Cap('APP123', 'C0006', '1')"),
            ('NDQ4294', "dbo.Actores_Cap('APP136', 'C0006', '1')"),
            ('NDQ4295', "dbo.Actores_Cap('APP139', 'C0006', '1')"),
            ('NDQ4296', "dbo.Actores_Cap('APP140', 'C0006', '1')"),
            ('NDQ4297', "dbo.Actores_Cap('APP141', 'C0006', '1')"),
            ('NDQ4298', "dbo.Actores_Cap('APP142', 'C0006', '1')"),
            ('NDQ4299', "dbo.Actores_Cap('APP143', 'C0006', '1')"),
            ('NDQ4300', "dbo.Actores_Cap('APP144', 'C0006', '1')"),
            ('NDQ4301', "dbo.Actores_Cap('APP145', 'C0006', '1')"),
            ('NDQ4302', "dbo.Actores_Cap('APP146', 'C0006', '1')"),
            ('NDQ4303', "dbo.Actores_Cap('APP150', 'C0006', '1')"),
            ('NDQ4304', "dbo.Actores_Cap('APP163', 'C0006', '1')"),
            ('NDQ4305', "dbo.Actores_Cap('APP165', 'C0006', '1')"),
            ('NDQ4306', "dbo.Actores_Cap('APP166', 'C0006', '1')"),
            ('NDQ4307', "dbo.Actores_Cap('APP168', 'C0006', '1')"),
            ('NDQ4308', "dbo.Actores_N('APP91', 'C0008', '1')"),
            ('NDQ4309', "dbo.Actores_N('APP92', 'C0008', '1')"),
            ('NDQ4310', "dbo.Actores_N('APP93', 'C0008', '1')"),
            ('NDQ4311', "dbo.Actores_N('APP94', 'C0008', '1')"),
            ('NDQ4312', "dbo.Actores_N('APP95', 'C0008', '1')"),
            ('NDQ4313', "dbo.Actores_N('APP96', 'C0008', '1')"),
            ('NDQ4314', "dbo.Actores_N('APP98', 'C0008', '1')"),
            ('NDQ4315', "dbo.Actores_N('APP99', 'C0008', '1')"),
            ('NDQ4316', "dbo.Actores_N('APP101', 'C0008', '1')"),
            ('NDQ4317', "dbo.Actores_N('APP102', 'C0008', '1')"),
            ('NDQ4318', "dbo.Actores_N('APP104', 'C0008', '1')"),
            ('NDQ4319', "dbo.Actores_N('APP106', 'C0008', '1')"),
            ('NDQ4320', "dbo.Actores_N('APP108', 'C0008', '1')"),
            ('NDQ4321', "dbo.Actores_N('APP100', 'C0008', '1')"),
            ('NDQ4322', "dbo.Actores_N('APP103', 'C0008', '1')"),
            ('NDQ4323', "dbo.Actores_N('APP105', 'C0008', '1')"),
            ('NDQ4324', "dbo.Actores_N('APP111', 'C0008', '1')"),
            ('NDQ4325', "dbo.Actores_N('APP119', 'C0008', '1')"),
            ('NDQ4326', "dbo.Actores_N('APP121', 'C0008', '1')"),
            ('NDQ4327', "dbo.Actores_N('APP123', 'C0008', '1')"),
            ('NDQ4328', "dbo.Actores_N('APP136', 'C0008', '1')"),
            ('NDQ4329', "dbo.Actores_N('APP139', 'C0008', '1')"),
            ('NDQ4330', "dbo.Actores_N('APP140', 'C0008', '1')"),
            ('NDQ4331', "dbo.Actores_N('APP141', 'C0008', '1')"),
            ('NDQ4332', "dbo.Actores_N('APP142', 'C0008', '1')"),
            ('NDQ4333', "dbo.Actores_N('APP143', 'C0008', '1')"),
            ('NDQ4334', "dbo.Actores_N('APP144', 'C0008', '1')"),
            ('NDQ4335', "dbo.Actores_N('APP145', 'C0008', '1')"),
            ('NDQ4336', "dbo.Actores_N('APP146', 'C0008', '1')"),
            ('NDQ4337', "dbo.Actores_N('APP150', 'C0008', '1')"),
            ('NDQ4338', "dbo.Actores_N('APP163', 'C0008', '1')"),
            ('NDQ4339', "dbo.Actores_N('APP165', 'C0008', '1')"),
            ('NDQ4340', "dbo.Actores_N('APP166', 'C0008', '1')"),
            ('NDQ4341', "dbo.Actores_N('APP168', 'C0008', '1')"),
            ('NDQ4342', "dbo.Actores_Cap('APP91', 'C0008', '1')"),
            ('NDQ4343', "dbo.Actores_Cap('APP92', 'C0008', '1')"),
            ('NDQ4344', "dbo.Actores_Cap('APP93', 'C0008', '1')"),
            ('NDQ4345', "dbo.Actores_Cap('APP94', 'C0008', '1')"),
            ('NDQ4346', "dbo.Actores_Cap('APP95', 'C0008', '1')"),
            ('NDQ4347', "dbo.Actores_Cap('APP96', 'C0008', '1')"),
            ('NDQ4348', "dbo.Actores_Cap('APP98', 'C0008', '1')"),
            ('NDQ4349', "dbo.Actores_Cap('APP99', 'C0008', '1')"),
            ('NDQ4350', "dbo.Actores_Cap('APP101', 'C0008', '1')"),
            ('NDQ4351', "dbo.Actores_Cap('APP102', 'C0008', '1')"),
            ('NDQ4352', "dbo.Actores_Cap('APP104', 'C0008', '1')"),
            ('NDQ4353', "dbo.Actores_Cap('APP106', 'C0008', '1')"),
            ('NDQ4354', "dbo.Actores_Cap('APP108', 'C0008', '1')"),
            ('NDQ4355', "dbo.Actores_Cap('APP100', 'C0008', '1')"),
            ('NDQ4356', "dbo.Actores_Cap('APP103', 'C0008', '1')"),
            ('NDQ4357', "dbo.Actores_Cap('APP105', 'C0008', '1')"),
            ('NDQ4358', "dbo.Actores_Cap('APP111', 'C0008', '1')"),
            ('NDQ4359', "dbo.Actores_Cap('APP119', 'C0008', '1')"),
            ('NDQ4360', "dbo.Actores_Cap('APP121', 'C0008', '1')"),
            ('NDQ4361', "dbo.Actores_Cap('APP123', 'C0008', '1')"),
            ('NDQ4362', "dbo.Actores_Cap('APP136', 'C0008', '1')"),
            ('NDQ4363', "dbo.Actores_Cap('APP139', 'C0008', '1')"),
            ('NDQ4364', "dbo.Actores_Cap('APP140', 'C0008', '1')"),
            ('NDQ4365', "dbo.Actores_Cap('APP141', 'C0008', '1')"),
            ('NDQ4366', "dbo.Actores_Cap('APP142', 'C0008', '1')"),
            ('NDQ4367', "dbo.Actores_Cap('APP143', 'C0008', '1')"),
            ('NDQ4368', "dbo.Actores_Cap('APP144', 'C0008', '1')"),
            ('NDQ4369', "dbo.Actores_Cap('APP145', 'C0008', '1')"),
            ('NDQ4370', "dbo.Actores_Cap('APP146', 'C0008', '1')"),
            ('NDQ4371', "dbo.Actores_Cap('APP150', 'C0008', '1')"),
            ('NDQ4372', "dbo.Actores_Cap('APP163', 'C0008', '1')"),
            ('NDQ4373', "dbo.Actores_Cap('APP165', 'C0008', '1')"),
            ('NDQ4374', "dbo.Actores_Cap('APP166', 'C0008', '1')"),
            ('NDQ4375', "dbo.Actores_Cap('APP168', 'C0008', '1')"),
            ('NDQ4376', "dbo.Actores_N('APP91', 'C0009', '1')"),
            ('NDQ4377', "dbo.Actores_N('APP92', 'C0009', '1')"),
            ('NDQ4378', "dbo.Actores_N('APP93', 'C0009', '1')"),
            ('NDQ4379', "dbo.Actores_N('APP94', 'C0009', '1')"),
            ('NDQ4380', "dbo.Actores_N('APP95', 'C0009', '1')"),
            ('NDQ4381', "dbo.Actores_N('APP96', 'C0009', '1')"),
            ('NDQ4382', "dbo.Actores_N('APP98', 'C0009', '1')"),
            ('NDQ4383', "dbo.Actores_N('APP99', 'C0009', '1')"),
            ('NDQ4384', "dbo.Actores_N('APP101', 'C0009', '1')"),
            ('NDQ4385', "dbo.Actores_N('APP102', 'C0009', '1')"),
            ('NDQ4386', "dbo.Actores_N('APP104', 'C0009', '1')"),
            ('NDQ4387', "dbo.Actores_N('APP106', 'C0009', '1')"),
            ('NDQ4388', "dbo.Actores_N('APP108', 'C0009', '1')"),
            ('NDQ4389', "dbo.Actores_N('APP100', 'C0009', '1')"),
            ('NDQ4390', "dbo.Actores_N('APP103', 'C0009', '1')"),
            ('NDQ4391', "dbo.Actores_N('APP105', 'C0009', '1')"),
            ('NDQ4392', "dbo.Actores_N('APP111', 'C0009', '1')"),
            ('NDQ4393', "dbo.Actores_N('APP119', 'C0009', '1')"),
            ('NDQ4394', "dbo.Actores_N('APP121', 'C0009', '1')"),
            ('NDQ4395', "dbo.Actores_N('APP123', 'C0009', '1')"),
            ('NDQ4396', "dbo.Actores_N('APP136', 'C0009', '1')"),
            ('NDQ4397', "dbo.Actores_N('APP139', 'C0009', '1')"),
            ('NDQ4398', "dbo.Actores_N('APP140', 'C0009', '1')"),
            ('NDQ4399', "dbo.Actores_N('APP141', 'C0009', '1')"),
            ('NDQ4400', "dbo.Actores_N('APP142', 'C0009', '1')"),
            ('NDQ4401', "dbo.Actores_N('APP143', 'C0009', '1')"),
            ('NDQ4402', "dbo.Actores_N('APP144', 'C0009', '1')"),
            ('NDQ4403', "dbo.Actores_N('APP145', 'C0009', '1')"),
            ('NDQ4404', "dbo.Actores_N('APP146', 'C0009', '1')"),
            ('NDQ4405', "dbo.Actores_N('APP150', 'C0009', '1')"),
            ('NDQ4406', "dbo.Actores_N('APP163', 'C0009', '1')"),
            ('NDQ4407', "dbo.Actores_N('APP165', 'C0009', '1')"),
            ('NDQ4408', "dbo.Actores_N('APP166', 'C0009', '1')"),
            ('NDQ4409', "dbo.Actores_N('APP168', 'C0009', '1')"),
            ('NDQ4410', "dbo.Actores_Cap('APP91', 'C0009', '1')"),
            ('NDQ4411', "dbo.Actores_Cap('APP92', 'C0009', '1')"),
            ('NDQ4412', "dbo.Actores_Cap('APP93', 'C0009', '1')"),
            ('NDQ4413', "dbo.Actores_Cap('APP94', 'C0009', '1')"),
            ('NDQ4414', "dbo.Actores_Cap('APP95', 'C0009', '1')"),
            ('NDQ4415', "dbo.Actores_Cap('APP96', 'C0009', '1')"),
            ('NDQ4416', "dbo.Actores_Cap('APP98', 'C0009', '1')"),
            ('NDQ4417', "dbo.Actores_Cap('APP99', 'C0009', '1')"),
            ('NDQ4418', "dbo.Actores_Cap('APP101', 'C0009', '1')"),
            ('NDQ4419', "dbo.Actores_Cap('APP102', 'C0009', '1')"),
            ('NDQ4420', "dbo.Actores_Cap('APP104', 'C0009', '1')"),
            ('NDQ4421', "dbo.Actores_Cap('APP106', 'C0009', '1')"),
            ('NDQ4422', "dbo.Actores_Cap('APP108', 'C0009', '1')"),
            ('NDQ4423', "dbo.Actores_Cap('APP100', 'C0009', '1')"),
            ('NDQ4424', "dbo.Actores_Cap('APP103', 'C0009', '1')"),
            ('NDQ4425', "dbo.Actores_Cap('APP105', 'C0009', '1')"),
            ('NDQ4426', "dbo.Actores_Cap('APP111', 'C0009', '1')"),
            ('NDQ4427', "dbo.Actores_Cap('APP119', 'C0009', '1')"),
            ('NDQ4428', "dbo.Actores_Cap('APP121', 'C0009', '1')"),
            ('NDQ4429', "dbo.Actores_Cap('APP123', 'C0009', '1')"),
            ('NDQ4430', "dbo.Actores_Cap('APP136', 'C0009', '1')"),
            ('NDQ4431', "dbo.Actores_Cap('APP139', 'C0009', '1')"),
            ('NDQ4432', "dbo.Actores_Cap('APP140', 'C0009', '1')"),
            ('NDQ4433', "dbo.Actores_Cap('APP141', 'C0009', '1')"),
            ('NDQ4434', "dbo.Actores_Cap('APP142', 'C0009', '1')"),
            ('NDQ4435', "dbo.Actores_Cap('APP143', 'C0009', '1')"),
            ('NDQ4436', "dbo.Actores_Cap('APP144', 'C0009', '1')"),
            ('NDQ4437', "dbo.Actores_Cap('APP145', 'C0009', '1')"),
            ('NDQ4438', "dbo.Actores_Cap('APP146', 'C0009', '1')"),
            ('NDQ4439', "dbo.Actores_Cap('APP150', 'C0009', '1')"),
            ('NDQ4440', "dbo.Actores_Cap('APP163', 'C0009', '1')"),
            ('NDQ4441', "dbo.Actores_Cap('APP165', 'C0009', '1')"),
            ('NDQ4442', "dbo.Actores_Cap('APP166', 'C0009', '1')"),
            ('NDQ4443', "dbo.Actores_Cap('APP168', 'C0009', '1')"),
            ('NDQ4444', "dbo.Actores_N('APP91', 'C0010', '1')"),
            ('NDQ4445', "dbo.Actores_N('APP92', 'C0010', '1')"),
            ('NDQ4446', "dbo.Actores_N('APP93', 'C0010', '1')"),
            ('NDQ4447', "dbo.Actores_N('APP94', 'C0010', '1')"),
            ('NDQ4448', "dbo.Actores_N('APP95', 'C0010', '1')"),
            ('NDQ4449', "dbo.Actores_N('APP96', 'C0010', '1')"),
            ('NDQ4450', "dbo.Actores_N('APP98', 'C0010', '1')"),
            ('NDQ4451', "dbo.Actores_N('APP99', 'C0010', '1')"),
            ('NDQ4452', "dbo.Actores_N('APP101', 'C0010', '1')"),
            ('NDQ4453', "dbo.Actores_N('APP102', 'C0010', '1')"),
            ('NDQ4454', "dbo.Actores_N('APP104', 'C0010', '1')"),
            ('NDQ4455', "dbo.Actores_N('APP106', 'C0010', '1')"),
            ('NDQ4456', "dbo.Actores_N('APP108', 'C0010', '1')"),
            ('NDQ4457', "dbo.Actores_N('APP100', 'C0010', '1')"),
            ('NDQ4458', "dbo.Actores_N('APP103', 'C0010', '1')"),
            ('NDQ4459', "dbo.Actores_N('APP105', 'C0010', '1')"),
            ('NDQ4460', "dbo.Actores_N('APP111', 'C0010', '1')"),
            ('NDQ4461', "dbo.Actores_N('APP119', 'C0010', '1')"),
            ('NDQ4462', "dbo.Actores_N('APP121', 'C0010', '1')"),
            ('NDQ4463', "dbo.Actores_N('APP123', 'C0010', '1')"),
            ('NDQ4464', "dbo.Actores_N('APP136', 'C0010', '1')"),
            ('NDQ4465', "dbo.Actores_N('APP139', 'C0010', '1')"),
            ('NDQ4466', "dbo.Actores_N('APP140', 'C0010', '1')"),
            ('NDQ4467', "dbo.Actores_N('APP141', 'C0010', '1')"),
            ('NDQ4468', "dbo.Actores_N('APP142', 'C0010', '1')"),
            ('NDQ4469', "dbo.Actores_N('APP143', 'C0010', '1')"),
            ('NDQ4470', "dbo.Actores_N('APP144', 'C0010', '1')"),
            ('NDQ4471', "dbo.Actores_N('APP145', 'C0010', '1')"),
            ('NDQ4472', "dbo.Actores_N('APP146', 'C0010', '1')"),
            ('NDQ4473', "dbo.Actores_N('APP150', 'C0010', '1')"),
            ('NDQ4474', "dbo.Actores_N('APP163', 'C0010', '1')"),
            ('NDQ4475', "dbo.Actores_N('APP165', 'C0010', '1')"),
            ('NDQ4476', "dbo.Actores_N('APP166', 'C0010', '1')"),
            ('NDQ4477', "dbo.Actores_N('APP168', 'C0010', '1')"),
            ('NDQ4478', "dbo.Actores_Cap('APP91', 'C0010', '1')"),
            ('NDQ4479', "dbo.Actores_Cap('APP92', 'C0010', '1')"),
            ('NDQ4480', "dbo.Actores_Cap('APP93', 'C0010', '1')"),
            ('NDQ4481', "dbo.Actores_Cap('APP94', 'C0010', '1')"),
            ('NDQ4482', "dbo.Actores_Cap('APP95', 'C0010', '1')"),
            ('NDQ4483', "dbo.Actores_Cap('APP96', 'C0010', '1')"),
            ('NDQ4484', "dbo.Actores_Cap('APP98', 'C0010', '1')"),
            ('NDQ4485', "dbo.Actores_Cap('APP99', 'C0010', '1')"),
            ('NDQ4486', "dbo.Actores_Cap('APP101', 'C0010', '1')"),
            ('NDQ4487', "dbo.Actores_Cap('APP102', 'C0010', '1')"),
            ('NDQ4488', "dbo.Actores_Cap('APP104', 'C0010', '1')"),
            ('NDQ4489', "dbo.Actores_Cap('APP106', 'C0010', '1')"),
            ('NDQ4490', "dbo.Actores_Cap('APP108', 'C0010', '1')"),
            ('NDQ4491', "dbo.Actores_Cap('APP100', 'C0010', '1')"),
            ('NDQ4492', "dbo.Actores_Cap('APP103', 'C0010', '1')"),
            ('NDQ4493', "dbo.Actores_Cap('APP105', 'C0010', '1')"),
            ('NDQ4494', "dbo.Actores_Cap('APP111', 'C0010', '1')"),
            ('NDQ4495', "dbo.Actores_Cap('APP119', 'C0010', '1')"),
            ('NDQ4496', "dbo.Actores_Cap('APP121', 'C0010', '1')"),
            ('NDQ4497', "dbo.Actores_Cap('APP123', 'C0010', '1')"),
            ('NDQ4498', "dbo.Actores_Cap('APP136', 'C0010', '1')"),
            ('NDQ4499', "dbo.Actores_Cap('APP139', 'C0010', '1')"),
            ('NDQ4500', "dbo.Actores_Cap('APP140', 'C0010', '1')"),
            ('NDQ4501', "dbo.Actores_Cap('APP141', 'C0010', '1')"),
            ('NDQ4502', "dbo.Actores_Cap('APP142', 'C0010', '1')"),
            ('NDQ4503', "dbo.Actores_Cap('APP143', 'C0010', '1')"),
            ('NDQ4504', "dbo.Actores_Cap('APP144', 'C0010', '1')"),
            ('NDQ4505', "dbo.Actores_Cap('APP145', 'C0010', '1')"),
            ('NDQ4506', "dbo.Actores_Cap('APP146', 'C0010', '1')"),
            ('NDQ4507', "dbo.Actores_Cap('APP150', 'C0010', '1')"),
            ('NDQ4508', "dbo.Actores_Cap('APP163', 'C0010', '1')"),
            ('NDQ4509', "dbo.Actores_Cap('APP165', 'C0010', '1')"),
            ('NDQ4510', "dbo.Actores_Cap('APP166', 'C0010', '1')"),
            ('NDQ4511', "dbo.Actores_Cap('APP168', 'C0010', '1')"),
            ('NDQ4512', "dbo.Actores_N('APP91', 'C0012', '1')"),
            ('NDQ4513', "dbo.Actores_N('APP92', 'C0012', '1')"),
            ('NDQ4514', "dbo.Actores_N('APP93', 'C0012', '1')"),
            ('NDQ4515', "dbo.Actores_N('APP94', 'C0012', '1')"),
            ('NDQ4516', "dbo.Actores_N('APP95', 'C0012', '1')"),
            ('NDQ4517', "dbo.Actores_N('APP96', 'C0012', '1')"),
            ('NDQ4518', "dbo.Actores_N('APP98', 'C0012', '1')"),
            ('NDQ4519', "dbo.Actores_N('APP99', 'C0012', '1')"),
            ('NDQ4520', "dbo.Actores_N('APP101', 'C0012', '1')"),
            ('NDQ4521', "dbo.Actores_N('APP102', 'C0012', '1')"),
            ('NDQ4522', "dbo.Actores_N('APP104', 'C0012', '1')"),
            ('NDQ4523', "dbo.Actores_N('APP106', 'C0012', '1')"),
            ('NDQ4524', "dbo.Actores_N('APP108', 'C0012', '1')"),
            ('NDQ4525', "dbo.Actores_N('APP100', 'C0012', '1')"),
            ('NDQ4526', "dbo.Actores_N('APP103', 'C0012', '1')"),
            ('NDQ4527', "dbo.Actores_N('APP105', 'C0012', '1')"),
            ('NDQ4528', "dbo.Actores_N('APP111', 'C0012', '1')"),
            ('NDQ4529', "dbo.Actores_N('APP119', 'C0012', '1')"),
            ('NDQ4530', "dbo.Actores_N('APP121', 'C0012', '1')"),
            ('NDQ4531', "dbo.Actores_N('APP123', 'C0012', '1')"),
            ('NDQ4532', "dbo.Actores_N('APP136', 'C0012', '1')"),
            ('NDQ4533', "dbo.Actores_N('APP139', 'C0012', '1')"),
            ('NDQ4534', "dbo.Actores_N('APP140', 'C0012', '1')"),
            ('NDQ4535', "dbo.Actores_N('APP141', 'C0012', '1')"),
            ('NDQ4536', "dbo.Actores_N('APP142', 'C0012', '1')"),
            ('NDQ4537', "dbo.Actores_N('APP143', 'C0012', '1')"),
            ('NDQ4538', "dbo.Actores_N('APP144', 'C0012', '1')"),
            ('NDQ4539', "dbo.Actores_N('APP145', 'C0012', '1')"),
            ('NDQ4540', "dbo.Actores_N('APP146', 'C0012', '1')"),
            ('NDQ4541', "dbo.Actores_N('APP150', 'C0012', '1')"),
            ('NDQ4542', "dbo.Actores_N('APP163', 'C0012', '1')"),
            ('NDQ4543', "dbo.Actores_N('APP165', 'C0012', '1')"),
            ('NDQ4544', "dbo.Actores_N('APP166', 'C0012', '1')"),
            ('NDQ4545', "dbo.Actores_N('APP168', 'C0012', '1')"),
            ('NDQ4546', "dbo.Actores_Cap('APP91', 'C0012', '1')"),
            ('NDQ4547', "dbo.Actores_Cap('APP92', 'C0012', '1')"),
            ('NDQ4548', "dbo.Actores_Cap('APP93', 'C0012', '1')"),
            ('NDQ4549', "dbo.Actores_Cap('APP94', 'C0012', '1')"),
            ('NDQ4550', "dbo.Actores_Cap('APP95', 'C0012', '1')"),
            ('NDQ4551', "dbo.Actores_Cap('APP96', 'C0012', '1')"),
            ('NDQ4552', "dbo.Actores_Cap('APP98', 'C0012', '1')"),
            ('NDQ4553', "dbo.Actores_Cap('APP99', 'C0012', '1')"),
            ('NDQ4554', "dbo.Actores_Cap('APP101', 'C0012', '1')"),
            ('NDQ4555', "dbo.Actores_Cap('APP102', 'C0012', '1')"),
            ('NDQ4556', "dbo.Actores_Cap('APP104', 'C0012', '1')"),
            ('NDQ4557', "dbo.Actores_Cap('APP106', 'C0012', '1')"),
            ('NDQ4558', "dbo.Actores_Cap('APP108', 'C0012', '1')"),
            ('NDQ4559', "dbo.Actores_Cap('APP100', 'C0012', '1')"),
            ('NDQ4560', "dbo.Actores_Cap('APP103', 'C0012', '1')"),
            ('NDQ4561', "dbo.Actores_Cap('APP105', 'C0012', '1')"),
            ('NDQ4562', "dbo.Actores_Cap('APP111', 'C0012', '1')"),
            ('NDQ4563', "dbo.Actores_Cap('APP119', 'C0012', '1')"),
            ('NDQ4564', "dbo.Actores_Cap('APP121', 'C0012', '1')"),
            ('NDQ4565', "dbo.Actores_Cap('APP123', 'C0012', '1')"),
            ('NDQ4566', "dbo.Actores_Cap('APP136', 'C0012', '1')"),
            ('NDQ4567', "dbo.Actores_Cap('APP139', 'C0012', '1')"),
            ('NDQ4568', "dbo.Actores_Cap('APP140', 'C0012', '1')"),
            ('NDQ4569', "dbo.Actores_Cap('APP141', 'C0012', '1')"),
            ('NDQ4570', "dbo.Actores_Cap('APP142', 'C0012', '1')"),
            ('NDQ4571', "dbo.Actores_Cap('APP143', 'C0012', '1')"),
            ('NDQ4572', "dbo.Actores_Cap('APP144', 'C0012', '1')"),
            ('NDQ4573', "dbo.Actores_Cap('APP145', 'C0012', '1')"),
            ('NDQ4574', "dbo.Actores_Cap('APP146', 'C0012', '1')"),
            ('NDQ4575', "dbo.Actores_Cap('APP150', 'C0012', '1')"),
            ('NDQ4576', "dbo.Actores_Cap('APP163', 'C0012', '1')"),
            ('NDQ4577', "dbo.Actores_Cap('APP165', 'C0012', '1')"),
            ('NDQ4578', "dbo.Actores_Cap('APP166', 'C0012', '1')"),
            ('NDQ4579', "dbo.Actores_Cap('APP168', 'C0012', '1')"),
            ('NDQ4580', "dbo.Actores_N('APP91', 'C3121', '1')"),
            ('NDQ4581', "dbo.Actores_N('APP92', 'C3121', '1')"),
            ('NDQ4582', "dbo.Actores_N('APP93', 'C3121', '1')"),
            ('NDQ4583', "dbo.Actores_N('APP94', 'C3121', '1')"),
            ('NDQ4584', "dbo.Actores_N('APP95', 'C3121', '1')"),
            ('NDQ4585', "dbo.Actores_N('APP96', 'C3121', '1')"),
            ('NDQ4586', "dbo.Actores_N('APP98', 'C3121', '1')"),
            ('NDQ4587', "dbo.Actores_N('APP99', 'C3121', '1')"),
            ('NDQ4588', "dbo.Actores_N('APP101', 'C3121', '1')"),
            ('NDQ4589', "dbo.Actores_N('APP102', 'C3121', '1')"),
            ('NDQ4590', "dbo.Actores_N('APP104', 'C3121', '1')"),
            ('NDQ4591', "dbo.Actores_N('APP106', 'C3121', '1')"),
            ('NDQ4592', "dbo.Actores_N('APP108', 'C3121', '1')"),
            ('NDQ4593', "dbo.Actores_N('APP100', 'C3121', '1')"),
            ('NDQ4594', "dbo.Actores_N('APP103', 'C3121', '1')"),
            ('NDQ4595', "dbo.Actores_N('APP105', 'C3121', '1')"),
            ('NDQ4596', "dbo.Actores_N('APP111', 'C3121', '1')"),
            ('NDQ4597', "dbo.Actores_N('APP119', 'C3121', '1')"),
            ('NDQ4598', "dbo.Actores_N('APP121', 'C3121', '1')"),
            ('NDQ4599', "dbo.Actores_N('APP123', 'C3121', '1')"),
            ('NDQ4600', "dbo.Actores_N('APP136', 'C3121', '1')"),
            ('NDQ4601', "dbo.Actores_N('APP139', 'C3121', '1')"),
            ('NDQ4602', "dbo.Actores_N('APP140', 'C3121', '1')"),
            ('NDQ4603', "dbo.Actores_N('APP141', 'C3121', '1')"),
            ('NDQ4604', "dbo.Actores_N('APP142', 'C3121', '1')"),
            ('NDQ4605', "dbo.Actores_N('APP143', 'C3121', '1')"),
            ('NDQ4606', "dbo.Actores_N('APP144', 'C3121', '1')"),
            ('NDQ4607', "dbo.Actores_N('APP145', 'C3121', '1')"),
            ('NDQ4608', "dbo.Actores_N('APP146', 'C3121', '1')"),
            ('NDQ4609', "dbo.Actores_N('APP150', 'C3121', '1')"),
            ('NDQ4610', "dbo.Actores_N('APP163', 'C3121', '1')"),
            ('NDQ4611', "dbo.Actores_N('APP165', 'C3121', '1')"),
            ('NDQ4612', "dbo.Actores_N('APP166', 'C3121', '1')"),
            ('NDQ4613', "dbo.Actores_N('APP168', 'C3121', '1')"),
            ('NDQ4614', "dbo.Actores_Cap('APP91', 'C3121', '1')"),
            ('NDQ4615', "dbo.Actores_Cap('APP92', 'C3121', '1')"),
            ('NDQ4616', "dbo.Actores_Cap('APP93', 'C3121', '1')"),
            ('NDQ4617', "dbo.Actores_Cap('APP94', 'C3121', '1')"),
            ('NDQ4618', "dbo.Actores_Cap('APP95', 'C3121', '1')"),
            ('NDQ4619', "dbo.Actores_Cap('APP96', 'C3121', '1')"),
            ('NDQ4620', "dbo.Actores_Cap('APP98', 'C3121', '1')"),
            ('NDQ4621', "dbo.Actores_Cap('APP99', 'C3121', '1')"),
            ('NDQ4622', "dbo.Actores_Cap('APP101', 'C3121', '1')"),
            ('NDQ4623', "dbo.Actores_Cap('APP102', 'C3121', '1')"),
            ('NDQ4624', "dbo.Actores_Cap('APP104', 'C3121', '1')"),
            ('NDQ4625', "dbo.Actores_Cap('APP106', 'C3121', '1')"),
            ('NDQ4626', "dbo.Actores_Cap('APP108', 'C3121', '1')"),
            ('NDQ4627', "dbo.Actores_Cap('APP100', 'C3121', '1')"),
            ('NDQ4628', "dbo.Actores_Cap('APP103', 'C3121', '1')"),
            ('NDQ4629', "dbo.Actores_Cap('APP105', 'C3121', '1')"),
            ('NDQ4630', "dbo.Actores_Cap('APP111', 'C3121', '1')"),
            ('NDQ4631', "dbo.Actores_Cap('APP119', 'C3121', '1')"),
            ('NDQ4632', "dbo.Actores_Cap('APP121', 'C3121', '1')"),
            ('NDQ4633', "dbo.Actores_Cap('APP123', 'C3121', '1')"),
            ('NDQ4634', "dbo.Actores_Cap('APP136', 'C3121', '1')"),
            ('NDQ4635', "dbo.Actores_Cap('APP139', 'C3121', '1')"),
            ('NDQ4636', "dbo.Actores_Cap('APP140', 'C3121', '1')"),
            ('NDQ4637', "dbo.Actores_Cap('APP141', 'C3121', '1')"),
            ('NDQ4638', "dbo.Actores_Cap('APP142', 'C3121', '1')"),
            ('NDQ4639', "dbo.Actores_Cap('APP143', 'C3121', '1')"),
            ('NDQ4640', "dbo.Actores_Cap('APP144', 'C3121', '1')"),
            ('NDQ4641', "dbo.Actores_Cap('APP145', 'C3121', '1')"),
            ('NDQ4642', "dbo.Actores_Cap('APP146', 'C3121', '1')"),
            ('NDQ4643', "dbo.Actores_Cap('APP150', 'C3121', '1')"),
            ('NDQ4644', "dbo.Actores_Cap('APP163', 'C3121', '1')"),
            ('NDQ4645', "dbo.Actores_Cap('APP165', 'C3121', '1')"),
            ('NDQ4646', "dbo.Actores_Cap('APP166', 'C3121', '1')"),
            ('NDQ4647', "dbo.Actores_Cap('APP168', 'C3121', '1')"),
            ('NDQ4648', "dbo.Actores_N('APP91', 'C3141', '1')"),
            ('NDQ4649', "dbo.Actores_N('APP92', 'C3141', '1')"),
            ('NDQ4650', "dbo.Actores_N('APP93', 'C3141', '1')"),
            ('NDQ4651', "dbo.Actores_N('APP94', 'C3141', '1')"),
            ('NDQ4652', "dbo.Actores_N('APP95', 'C3141', '1')"),
            ('NDQ4653', "dbo.Actores_N('APP96', 'C3141', '1')"),
            ('NDQ4654', "dbo.Actores_N('APP98', 'C3141', '1')"),
            ('NDQ4655', "dbo.Actores_N('APP99', 'C3141', '1')"),
            ('NDQ4656', "dbo.Actores_N('APP101', 'C3141', '1')"),
            ('NDQ4657', "dbo.Actores_N('APP102', 'C3141', '1')"),
            ('NDQ4658', "dbo.Actores_N('APP104', 'C3141', '1')"),
            ('NDQ4659', "dbo.Actores_N('APP106', 'C3141', '1')"),
            ('NDQ4660', "dbo.Actores_N('APP108', 'C3141', '1')"),
            ('NDQ4661', "dbo.Actores_N('APP100', 'C3141', '1')"),
            ('NDQ4662', "dbo.Actores_N('APP103', 'C3141', '1')"),
            ('NDQ4663', "dbo.Actores_N('APP105', 'C3141', '1')"),
            ('NDQ4664', "dbo.Actores_N('APP111', 'C3141', '1')"),
            ('NDQ4665', "dbo.Actores_N('APP119', 'C3141', '1')"),
            ('NDQ4666', "dbo.Actores_N('APP121', 'C3141', '1')"),
            ('NDQ4667', "dbo.Actores_N('APP123', 'C3141', '1')"),
            ('NDQ4668', "dbo.Actores_N('APP136', 'C3141', '1')"),
            ('NDQ4669', "dbo.Actores_N('APP139', 'C3141', '1')"),
            ('NDQ4670', "dbo.Actores_N('APP140', 'C3141', '1')"),
            ('NDQ4671', "dbo.Actores_N('APP141', 'C3141', '1')"),
            ('NDQ4672', "dbo.Actores_N('APP142', 'C3141', '1')"),
            ('NDQ4673', "dbo.Actores_N('APP143', 'C3141', '1')"),
            ('NDQ4674', "dbo.Actores_N('APP144', 'C3141', '1')"),
            ('NDQ4675', "dbo.Actores_N('APP145', 'C3141', '1')"),
            ('NDQ4676', "dbo.Actores_N('APP146', 'C3141', '1')"),
            ('NDQ4677', "dbo.Actores_N('APP150', 'C3141', '1')"),
            ('NDQ4678', "dbo.Actores_N('APP163', 'C3141', '1')"),
            ('NDQ4679', "dbo.Actores_N('APP165', 'C3141', '1')"),
            ('NDQ4680', "dbo.Actores_N('APP166', 'C3141', '1')"),
            ('NDQ4681', "dbo.Actores_N('APP168', 'C3141', '1')"),
            ('NDQ4682', "dbo.Actores_Cap('APP91', 'C3141', '1')"),
            ('NDQ4683', "dbo.Actores_Cap('APP92', 'C3141', '1')"),
            ('NDQ4684', "dbo.Actores_Cap('APP93', 'C3141', '1')"),
            ('NDQ4685', "dbo.Actores_Cap('APP94', 'C3141', '1')"),
            ('NDQ4686', "dbo.Actores_Cap('APP95', 'C3141', '1')"),
            ('NDQ4687', "dbo.Actores_Cap('APP96', 'C3141', '1')"),
            ('NDQ4688', "dbo.Actores_Cap('APP98', 'C3141', '1')"),
            ('NDQ4689', "dbo.Actores_Cap('APP99', 'C3141', '1')"),
            ('NDQ4690', "dbo.Actores_Cap('APP101', 'C3141', '1')"),
            ('NDQ4691', "dbo.Actores_Cap('APP102', 'C3141', '1')"),
            ('NDQ4692', "dbo.Actores_Cap('APP104', 'C3141', '1')"),
            ('NDQ4693', "dbo.Actores_Cap('APP106', 'C3141', '1')"),
            ('NDQ4694', "dbo.Actores_Cap('APP108', 'C3141', '1')"),
            ('NDQ4695', "dbo.Actores_Cap('APP100', 'C3141', '1')"),
            ('NDQ4696', "dbo.Actores_Cap('APP103', 'C3141', '1')"),
            ('NDQ4697', "dbo.Actores_Cap('APP105', 'C3141', '1')"),
            ('NDQ4698', "dbo.Actores_Cap('APP111', 'C3141', '1')"),
            ('NDQ4699', "dbo.Actores_Cap('APP119', 'C3141', '1')"),
            ('NDQ4700', "dbo.Actores_Cap('APP121', 'C3141', '1')"),
            ('NDQ4701', "dbo.Actores_Cap('APP123', 'C3141', '1')"),
            ('NDQ4702', "dbo.Actores_Cap('APP136', 'C3141', '1')"),
            ('NDQ4703', "dbo.Actores_Cap('APP139', 'C3141', '1')"),
            ('NDQ4704', "dbo.Actores_Cap('APP140', 'C3141', '1')"),
            ('NDQ4705', "dbo.Actores_Cap('APP141', 'C3141', '1')"),
            ('NDQ4706', "dbo.Actores_Cap('APP142', 'C3141', '1')"),
            ('NDQ4707', "dbo.Actores_Cap('APP143', 'C3141', '1')"),
            ('NDQ4708', "dbo.Actores_Cap('APP144', 'C3141', '1')"),
            ('NDQ4709', "dbo.Actores_Cap('APP145', 'C3141', '1')"),
            ('NDQ4710', "dbo.Actores_Cap('APP146', 'C3141', '1')"),
            ('NDQ4711', "dbo.Actores_Cap('APP150', 'C3141', '1')"),
            ('NDQ4712', "dbo.Actores_Cap('APP163', 'C3141', '1')"),
            ('NDQ4713', "dbo.Actores_Cap('APP165', 'C3141', '1')"),
            ('NDQ4714', "dbo.Actores_Cap('APP166', 'C3141', '1')"),
            ('NDQ4715', "dbo.Actores_Cap('APP168', 'C3141', '1')"),
            ('NDQ4716', "dbo.Actores_N('APP91', 'C1042', '1')"),
            ('NDQ4717', "dbo.Actores_N('APP92', 'C1042', '1')"),
            ('NDQ4718', "dbo.Actores_N('APP93', 'C1042', '1')"),
            ('NDQ4719', "dbo.Actores_N('APP94', 'C1042', '1')"),
            ('NDQ4720', "dbo.Actores_N('APP95', 'C1042', '1')"),
            ('NDQ4721', "dbo.Actores_N('APP96', 'C1042', '1')"),
            ('NDQ4722', "dbo.Actores_N('APP98', 'C1042', '1')"),
            ('NDQ4723', "dbo.Actores_N('APP99', 'C1042', '1')"),
            ('NDQ4724', "dbo.Actores_N('APP101', 'C1042', '1')"),
            ('NDQ4725', "dbo.Actores_N('APP102', 'C1042', '1')"),
            ('NDQ4726', "dbo.Actores_N('APP104', 'C1042', '1')"),
            ('NDQ4727', "dbo.Actores_N('APP106', 'C1042', '1')"),
            ('NDQ4728', "dbo.Actores_N('APP108', 'C1042', '1')"),
            ('NDQ4729', "dbo.Actores_N('APP100', 'C1042', '1')"),
            ('NDQ4730', "dbo.Actores_N('APP103', 'C1042', '1')"),
            ('NDQ4731', "dbo.Actores_N('APP105', 'C1042', '1')"),
            ('NDQ4732', "dbo.Actores_N('APP111', 'C1042', '1')"),
            ('NDQ4733', "dbo.Actores_N('APP119', 'C1042', '1')"),
            ('NDQ4734', "dbo.Actores_N('APP121', 'C1042', '1')"),
            ('NDQ4735', "dbo.Actores_N('APP123', 'C1042', '1')"),
            ('NDQ4736', "dbo.Actores_N('APP136', 'C1042', '1')"),
            ('NDQ4737', "dbo.Actores_N('APP139', 'C1042', '1')"),
            ('NDQ4738', "dbo.Actores_N('APP140', 'C1042', '1')"),
            ('NDQ4739', "dbo.Actores_N('APP141', 'C1042', '1')"),
            ('NDQ4740', "dbo.Actores_N('APP142', 'C1042', '1')"),
            ('NDQ4741', "dbo.Actores_N('APP143', 'C1042', '1')"),
            ('NDQ4742', "dbo.Actores_N('APP144', 'C1042', '1')"),
            ('NDQ4743', "dbo.Actores_N('APP145', 'C1042', '1')"),
            ('NDQ4744', "dbo.Actores_N('APP146', 'C1042', '1')"),
            ('NDQ4745', "dbo.Actores_N('APP150', 'C1042', '1')"),
            ('NDQ4746', "dbo.Actores_N('APP163', 'C1042', '1')"),
            ('NDQ4747', "dbo.Actores_N('APP165', 'C1042', '1')"),
            ('NDQ4748', "dbo.Actores_N('APP166', 'C1042', '1')"),
            ('NDQ4749', "dbo.Actores_N('APP168', 'C1042', '1')"),
            ('NDQ4750', "dbo.Actores_Cap('APP91', 'C1042', '1')"),
            ('NDQ4751', "dbo.Actores_Cap('APP92', 'C1042', '1')"),
            ('NDQ4752', "dbo.Actores_Cap('APP93', 'C1042', '1')"),
            ('NDQ4753', "dbo.Actores_Cap('APP94', 'C1042', '1')"),
            ('NDQ4754', "dbo.Actores_Cap('APP95', 'C1042', '1')"),
            ('NDQ4755', "dbo.Actores_Cap('APP96', 'C1042', '1')"),
            ('NDQ4756', "dbo.Actores_Cap('APP98', 'C1042', '1')"),
            ('NDQ4757', "dbo.Actores_Cap('APP99', 'C1042', '1')"),
            ('NDQ4758', "dbo.Actores_Cap('APP101', 'C1042', '1')"),
            ('NDQ4759', "dbo.Actores_Cap('APP102', 'C1042', '1')"),
            ('NDQ4760', "dbo.Actores_Cap('APP104', 'C1042', '1')"),
            ('NDQ4761', "dbo.Actores_Cap('APP106', 'C1042', '1')"),
            ('NDQ4762', "dbo.Actores_Cap('APP108', 'C1042', '1')"),
            ('NDQ4763', "dbo.Actores_Cap('APP100', 'C1042', '1')"),
            ('NDQ4764', "dbo.Actores_Cap('APP103', 'C1042', '1')"),
            ('NDQ4765', "dbo.Actores_Cap('APP105', 'C1042', '1')"),
            ('NDQ4766', "dbo.Actores_Cap('APP111', 'C1042', '1')"),
            ('NDQ4767', "dbo.Actores_Cap('APP119', 'C1042', '1')"),
            ('NDQ4768', "dbo.Actores_Cap('APP121', 'C1042', '1')"),
            ('NDQ4769', "dbo.Actores_Cap('APP123', 'C1042', '1')"),
            ('NDQ4770', "dbo.Actores_Cap('APP136', 'C1042', '1')"),
            ('NDQ4771', "dbo.Actores_Cap('APP139', 'C1042', '1')"),
            ('NDQ4772', "dbo.Actores_Cap('APP140', 'C1042', '1')"),
            ('NDQ4773', "dbo.Actores_Cap('APP141', 'C1042', '1')"),
            ('NDQ4774', "dbo.Actores_Cap('APP142', 'C1042', '1')"),
            ('NDQ4775', "dbo.Actores_Cap('APP143', 'C1042', '1')"),
            ('NDQ4776', "dbo.Actores_Cap('APP144', 'C1042', '1')"),
            ('NDQ4777', "dbo.Actores_Cap('APP145', 'C1042', '1')"),
            ('NDQ4778', "dbo.Actores_Cap('APP146', 'C1042', '1')"),
            ('NDQ4779', "dbo.Actores_Cap('APP150', 'C1042', '1')"),
            ('NDQ4780', "dbo.Actores_Cap('APP163', 'C1042', '1')"),
            ('NDQ4781', "dbo.Actores_Cap('APP165', 'C1042', '1')"),
            ('NDQ4782', "dbo.Actores_Cap('APP166', 'C1042', '1')"),
            ('NDQ4783', "dbo.Actores_Cap('APP168', 'C1042', '1')")

        

        ],

        "FACT_DISC_SNAPSHOT_ACTORES_BL2": [

            ('NDQ4784', "dbo.Actores_N('APP91', 'C0001', '2')"),
            ('NDQ4785', "dbo.Actores_N('APP92', 'C0001', '2')"),
            ('NDQ4786', "dbo.Actores_N('APP93', 'C0001', '2')"),
            ('NDQ4787', "dbo.Actores_N('APP94', 'C0001', '2')"),
            ('NDQ4788', "dbo.Actores_N('APP95', 'C0001', '2')"),
            ('NDQ4789', "dbo.Actores_N('APP96', 'C0001', '2')"),
            ('NDQ4790', "dbo.Actores_N('APP98', 'C0001', '2')"),
            ('NDQ4791', "dbo.Actores_N('APP99', 'C0001', '2')"),
            ('NDQ4792', "dbo.Actores_N('APP101', 'C0001', '2')"),
            ('NDQ4793', "dbo.Actores_N('APP102', 'C0001', '2')"),
            ('NDQ4794', "dbo.Actores_N('APP104', 'C0001', '2')"),
            ('NDQ4795', "dbo.Actores_N('APP106', 'C0001', '2')"),
            ('NDQ4796', "dbo.Actores_N('APP108', 'C0001', '2')"),
            ('NDQ4797', "dbo.Actores_N('APP100', 'C0001', '2')"),
            ('NDQ4798', "dbo.Actores_N('APP103', 'C0001', '2')"),
            ('NDQ4799', "dbo.Actores_N('APP105', 'C0001', '2')"),
            ('NDQ4800', "dbo.Actores_N('APP111', 'C0001', '2')"),
            ('NDQ4801', "dbo.Actores_N('APP119', 'C0001', '2')"),
            ('NDQ4802', "dbo.Actores_N('APP121', 'C0001', '2')"),
            ('NDQ4803', "dbo.Actores_N('APP123', 'C0001', '2')"),
            ('NDQ4804', "dbo.Actores_N('APP136', 'C0001', '2')"),
            ('NDQ4805', "dbo.Actores_N('APP139', 'C0001', '2')"),
            ('NDQ4806', "dbo.Actores_N('APP140', 'C0001', '2')"),
            ('NDQ4807', "dbo.Actores_N('APP141', 'C0001', '2')"),
            ('NDQ4808', "dbo.Actores_N('APP142', 'C0001', '2')"),
            ('NDQ4809', "dbo.Actores_N('APP143', 'C0001', '2')"),
            ('NDQ4810', "dbo.Actores_N('APP144', 'C0001', '2')"),
            ('NDQ4811', "dbo.Actores_N('APP145', 'C0001', '2')"),
            ('NDQ4812', "dbo.Actores_N('APP146', 'C0001', '2')"),
            ('NDQ4813', "dbo.Actores_N('APP150', 'C0001', '2')"),
            ('NDQ4814', "dbo.Actores_N('APP163', 'C0001', '2')"),
            ('NDQ4815', "dbo.Actores_N('APP165', 'C0001', '2')"),
            ('NDQ4816', "dbo.Actores_N('APP166', 'C0001', '2')"),
            ('NDQ4817', "dbo.Actores_N('APP168', 'C0001', '2')"),
            ('NDQ4818', "dbo.Actores_Cap('APP91', 'C0001', '2')"),
            ('NDQ4819', "dbo.Actores_Cap('APP92', 'C0001', '2')"),
            ('NDQ4820', "dbo.Actores_Cap('APP93', 'C0001', '2')"),
            ('NDQ4821', "dbo.Actores_Cap('APP94', 'C0001', '2')"),
            ('NDQ4822', "dbo.Actores_Cap('APP95', 'C0001', '2')"),
            ('NDQ4823', "dbo.Actores_Cap('APP96', 'C0001', '2')"),
            ('NDQ4824', "dbo.Actores_Cap('APP98', 'C0001', '2')"),
            ('NDQ4825', "dbo.Actores_Cap('APP99', 'C0001', '2')"),
            ('NDQ4826', "dbo.Actores_Cap('APP101', 'C0001', '2')"),
            ('NDQ4827', "dbo.Actores_Cap('APP102', 'C0001', '2')"),
            ('NDQ4828', "dbo.Actores_Cap('APP104', 'C0001', '2')"),
            ('NDQ4829', "dbo.Actores_Cap('APP106', 'C0001', '2')"),
            ('NDQ4830', "dbo.Actores_Cap('APP108', 'C0001', '2')"),
            ('NDQ4831', "dbo.Actores_Cap('APP100', 'C0001', '2')"),
            ('NDQ4832', "dbo.Actores_Cap('APP103', 'C0001', '2')"),
            ('NDQ4833', "dbo.Actores_Cap('APP105', 'C0001', '2')"),
            ('NDQ4834', "dbo.Actores_Cap('APP111', 'C0001', '2')"),
            ('NDQ4835', "dbo.Actores_Cap('APP119', 'C0001', '2')"),
            ('NDQ4836', "dbo.Actores_Cap('APP121', 'C0001', '2')"),
            ('NDQ4837', "dbo.Actores_Cap('APP123', 'C0001', '2')"),
            ('NDQ4838', "dbo.Actores_Cap('APP136', 'C0001', '2')"),
            ('NDQ4839', "dbo.Actores_Cap('APP139', 'C0001', '2')"),
            ('NDQ4840', "dbo.Actores_Cap('APP140', 'C0001', '2')"),
            ('NDQ4841', "dbo.Actores_Cap('APP141', 'C0001', '2')"),
            ('NDQ4842', "dbo.Actores_Cap('APP142', 'C0001', '2')"),
            ('NDQ4843', "dbo.Actores_Cap('APP143', 'C0001', '2')"),
            ('NDQ4844', "dbo.Actores_Cap('APP144', 'C0001', '2')"),
            ('NDQ4845', "dbo.Actores_Cap('APP145', 'C0001', '2')"),
            ('NDQ4846', "dbo.Actores_Cap('APP146', 'C0001', '2')"),
            ('NDQ4847', "dbo.Actores_Cap('APP150', 'C0001', '2')"),
            ('NDQ4848', "dbo.Actores_Cap('APP163', 'C0001', '2')"),
            ('NDQ4849', "dbo.Actores_Cap('APP165', 'C0001', '2')"),
            ('NDQ4850', "dbo.Actores_Cap('APP166', 'C0001', '2')"),
            ('NDQ4851', "dbo.Actores_Cap('APP168', 'C0001', '2')"),
            ('NDQ4852', "dbo.Actores_N('APP91', 'C0002', '2')"),
            ('NDQ4853', "dbo.Actores_N('APP92', 'C0002', '2')"),
            ('NDQ4854', "dbo.Actores_N('APP93', 'C0002', '2')"),
            ('NDQ4855', "dbo.Actores_N('APP94', 'C0002', '2')"),
            ('NDQ4856', "dbo.Actores_N('APP95', 'C0002', '2')"),
            ('NDQ4857', "dbo.Actores_N('APP96', 'C0002', '2')"),
            ('NDQ4858', "dbo.Actores_N('APP98', 'C0002', '2')"),
            ('NDQ4859', "dbo.Actores_N('APP99', 'C0002', '2')"),
            ('NDQ4860', "dbo.Actores_N('APP101', 'C0002', '2')"),
            ('NDQ4861', "dbo.Actores_N('APP102', 'C0002', '2')"),
            ('NDQ4862', "dbo.Actores_N('APP104', 'C0002', '2')"),
            ('NDQ4863', "dbo.Actores_N('APP106', 'C0002', '2')"),
            ('NDQ4864', "dbo.Actores_N('APP108', 'C0002', '2')"),
            ('NDQ4865', "dbo.Actores_N('APP100', 'C0002', '2')"),
            ('NDQ4866', "dbo.Actores_N('APP103', 'C0002', '2')"),
            ('NDQ4867', "dbo.Actores_N('APP105', 'C0002', '2')"),
            ('NDQ4868', "dbo.Actores_N('APP111', 'C0002', '2')"),
            ('NDQ4869', "dbo.Actores_N('APP119', 'C0002', '2')"),
            ('NDQ4870', "dbo.Actores_N('APP121', 'C0002', '2')"),
            ('NDQ4871', "dbo.Actores_N('APP123', 'C0002', '2')"),
            ('NDQ4872', "dbo.Actores_N('APP136', 'C0002', '2')"),
            ('NDQ4873', "dbo.Actores_N('APP139', 'C0002', '2')"),
            ('NDQ4874', "dbo.Actores_N('APP140', 'C0002', '2')"),
            ('NDQ4875', "dbo.Actores_N('APP141', 'C0002', '2')"),
            ('NDQ4876', "dbo.Actores_N('APP142', 'C0002', '2')"),
            ('NDQ4877', "dbo.Actores_N('APP143', 'C0002', '2')"),
            ('NDQ4878', "dbo.Actores_N('APP144', 'C0002', '2')"),
            ('NDQ4879', "dbo.Actores_N('APP145', 'C0002', '2')"),
            ('NDQ4880', "dbo.Actores_N('APP146', 'C0002', '2')"),
            ('NDQ4881', "dbo.Actores_N('APP150', 'C0002', '2')"),
            ('NDQ4882', "dbo.Actores_N('APP163', 'C0002', '2')"),
            ('NDQ4883', "dbo.Actores_N('APP165', 'C0002', '2')"),
            ('NDQ4884', "dbo.Actores_N('APP166', 'C0002', '2')"),
            ('NDQ4885', "dbo.Actores_N('APP168', 'C0002', '2')"),
            ('NDQ4886', "dbo.Actores_Cap('APP91', 'C0002', '2')"),
            ('NDQ4887', "dbo.Actores_Cap('APP92', 'C0002', '2')"),
            ('NDQ4888', "dbo.Actores_Cap('APP93', 'C0002', '2')"),
            ('NDQ4889', "dbo.Actores_Cap('APP94', 'C0002', '2')"),
            ('NDQ4890', "dbo.Actores_Cap('APP95', 'C0002', '2')"),
            ('NDQ4891', "dbo.Actores_Cap('APP96', 'C0002', '2')"),
            ('NDQ4892', "dbo.Actores_Cap('APP98', 'C0002', '2')"),
            ('NDQ4893', "dbo.Actores_Cap('APP99', 'C0002', '2')"),
            ('NDQ4894', "dbo.Actores_Cap('APP101', 'C0002', '2')"),
            ('NDQ4895', "dbo.Actores_Cap('APP102', 'C0002', '2')"),
            ('NDQ4896', "dbo.Actores_Cap('APP104', 'C0002', '2')"),
            ('NDQ4897', "dbo.Actores_Cap('APP106', 'C0002', '2')"),
            ('NDQ4898', "dbo.Actores_Cap('APP108', 'C0002', '2')"),
            ('NDQ4899', "dbo.Actores_Cap('APP100', 'C0002', '2')"),
            ('NDQ4900', "dbo.Actores_Cap('APP103', 'C0002', '2')"),
            ('NDQ4901', "dbo.Actores_Cap('APP105', 'C0002', '2')"),
            ('NDQ4902', "dbo.Actores_Cap('APP111', 'C0002', '2')"),
            ('NDQ4903', "dbo.Actores_Cap('APP119', 'C0002', '2')"),
            ('NDQ4904', "dbo.Actores_Cap('APP121', 'C0002', '2')"),
            ('NDQ4905', "dbo.Actores_Cap('APP123', 'C0002', '2')"),
            ('NDQ4906', "dbo.Actores_Cap('APP136', 'C0002', '2')"),
            ('NDQ4907', "dbo.Actores_Cap('APP139', 'C0002', '2')"),
            ('NDQ4908', "dbo.Actores_Cap('APP140', 'C0002', '2')"),
            ('NDQ4909', "dbo.Actores_Cap('APP141', 'C0002', '2')"),
            ('NDQ4910', "dbo.Actores_Cap('APP142', 'C0002', '2')"),
            ('NDQ4911', "dbo.Actores_Cap('APP143', 'C0002', '2')"),
            ('NDQ4912', "dbo.Actores_Cap('APP144', 'C0002', '2')"),
            ('NDQ4913', "dbo.Actores_Cap('APP145', 'C0002', '2')"),
            ('NDQ4914', "dbo.Actores_Cap('APP146', 'C0002', '2')"),
            ('NDQ4915', "dbo.Actores_Cap('APP150', 'C0002', '2')"),
            ('NDQ4916', "dbo.Actores_Cap('APP163', 'C0002', '2')"),
            ('NDQ4917', "dbo.Actores_Cap('APP165', 'C0002', '2')"),
            ('NDQ4918', "dbo.Actores_Cap('APP166', 'C0002', '2')"),
            ('NDQ4919', "dbo.Actores_Cap('APP168', 'C0002', '2')"),
            ('NDQ4920', "dbo.Actores_N('APP91', 'C0003', '2')"),
            ('NDQ4921', "dbo.Actores_N('APP92', 'C0003', '2')"),
            ('NDQ4922', "dbo.Actores_N('APP93', 'C0003', '2')"),
            ('NDQ4923', "dbo.Actores_N('APP94', 'C0003', '2')"),
            ('NDQ4924', "dbo.Actores_N('APP95', 'C0003', '2')"),
            ('NDQ4925', "dbo.Actores_N('APP96', 'C0003', '2')"),
            ('NDQ4926', "dbo.Actores_N('APP98', 'C0003', '2')"),
            ('NDQ4927', "dbo.Actores_N('APP99', 'C0003', '2')"),
            ('NDQ4928', "dbo.Actores_N('APP101', 'C0003', '2')"),
            ('NDQ4929', "dbo.Actores_N('APP102', 'C0003', '2')"),
            ('NDQ4930', "dbo.Actores_N('APP104', 'C0003', '2')"),
            ('NDQ4931', "dbo.Actores_N('APP106', 'C0003', '2')"),
            ('NDQ4932', "dbo.Actores_N('APP108', 'C0003', '2')"),
            ('NDQ4933', "dbo.Actores_N('APP100', 'C0003', '2')"),
            ('NDQ4934', "dbo.Actores_N('APP103', 'C0003', '2')"),
            ('NDQ4935', "dbo.Actores_N('APP105', 'C0003', '2')"),
            ('NDQ4936', "dbo.Actores_N('APP111', 'C0003', '2')"),
            ('NDQ4937', "dbo.Actores_N('APP119', 'C0003', '2')"),
            ('NDQ4938', "dbo.Actores_N('APP121', 'C0003', '2')"),
            ('NDQ4939', "dbo.Actores_N('APP123', 'C0003', '2')"),
            ('NDQ4940', "dbo.Actores_N('APP136', 'C0003', '2')"),
            ('NDQ4941', "dbo.Actores_N('APP139', 'C0003', '2')"),
            ('NDQ4942', "dbo.Actores_N('APP140', 'C0003', '2')"),
            ('NDQ4943', "dbo.Actores_N('APP141', 'C0003', '2')"),
            ('NDQ4944', "dbo.Actores_N('APP142', 'C0003', '2')"),
            ('NDQ4945', "dbo.Actores_N('APP143', 'C0003', '2')"),
            ('NDQ4946', "dbo.Actores_N('APP144', 'C0003', '2')"),
            ('NDQ4947', "dbo.Actores_N('APP145', 'C0003', '2')"),
            ('NDQ4948', "dbo.Actores_N('APP146', 'C0003', '2')"),
            ('NDQ4949', "dbo.Actores_N('APP150', 'C0003', '2')"),
            ('NDQ4950', "dbo.Actores_N('APP163', 'C0003', '2')"),
            ('NDQ4951', "dbo.Actores_N('APP165', 'C0003', '2')"),
            ('NDQ4952', "dbo.Actores_N('APP166', 'C0003', '2')"),
            ('NDQ4953', "dbo.Actores_N('APP168', 'C0003', '2')"),
            ('NDQ4954', "dbo.Actores_Cap('APP91', 'C0003', '2')"),
            ('NDQ4955', "dbo.Actores_Cap('APP92', 'C0003', '2')"),
            ('NDQ4956', "dbo.Actores_Cap('APP93', 'C0003', '2')"),
            ('NDQ4957', "dbo.Actores_Cap('APP94', 'C0003', '2')"),
            ('NDQ4958', "dbo.Actores_Cap('APP95', 'C0003', '2')"),
            ('NDQ4959', "dbo.Actores_Cap('APP96', 'C0003', '2')"),
            ('NDQ4960', "dbo.Actores_Cap('APP98', 'C0003', '2')"),
            ('NDQ4961', "dbo.Actores_Cap('APP99', 'C0003', '2')"),
            ('NDQ4962', "dbo.Actores_Cap('APP101', 'C0003', '2')"),
            ('NDQ4963', "dbo.Actores_Cap('APP102', 'C0003', '2')"),
            ('NDQ4964', "dbo.Actores_Cap('APP104', 'C0003', '2')"),
            ('NDQ4965', "dbo.Actores_Cap('APP106', 'C0003', '2')"),
            ('NDQ4966', "dbo.Actores_Cap('APP108', 'C0003', '2')"),
            ('NDQ4967', "dbo.Actores_Cap('APP100', 'C0003', '2')"),
            ('NDQ4968', "dbo.Actores_Cap('APP103', 'C0003', '2')"),
            ('NDQ4969', "dbo.Actores_Cap('APP105', 'C0003', '2')"),
            ('NDQ4970', "dbo.Actores_Cap('APP111', 'C0003', '2')"),
            ('NDQ4971', "dbo.Actores_Cap('APP119', 'C0003', '2')"),
            ('NDQ4972', "dbo.Actores_Cap('APP121', 'C0003', '2')"),
            ('NDQ4973', "dbo.Actores_Cap('APP123', 'C0003', '2')"),
            ('NDQ4974', "dbo.Actores_Cap('APP136', 'C0003', '2')"),
            ('NDQ4975', "dbo.Actores_Cap('APP139', 'C0003', '2')"),
            ('NDQ4976', "dbo.Actores_Cap('APP140', 'C0003', '2')"),
            ('NDQ4977', "dbo.Actores_Cap('APP141', 'C0003', '2')"),
            ('NDQ4978', "dbo.Actores_Cap('APP142', 'C0003', '2')"),
            ('NDQ4979', "dbo.Actores_Cap('APP143', 'C0003', '2')"),
            ('NDQ4980', "dbo.Actores_Cap('APP144', 'C0003', '2')"),
            ('NDQ4981', "dbo.Actores_Cap('APP145', 'C0003', '2')"),
            ('NDQ4982', "dbo.Actores_Cap('APP146', 'C0003', '2')"),
            ('NDQ4983', "dbo.Actores_Cap('APP150', 'C0003', '2')"),
            ('NDQ4984', "dbo.Actores_Cap('APP163', 'C0003', '2')"),
            ('NDQ4985', "dbo.Actores_Cap('APP165', 'C0003', '2')"),
            ('NDQ4986', "dbo.Actores_Cap('APP166', 'C0003', '2')"),
            ('NDQ4987', "dbo.Actores_Cap('APP168', 'C0003', '2')"),
            ('NDQ4988', "dbo.Actores_N('APP91', 'C0004', '2')"),
            ('NDQ4989', "dbo.Actores_N('APP92', 'C0004', '2')"),
            ('NDQ4990', "dbo.Actores_N('APP93', 'C0004', '2')"),
            ('NDQ4991', "dbo.Actores_N('APP94', 'C0004', '2')"),
            ('NDQ4992', "dbo.Actores_N('APP95', 'C0004', '2')"),
            ('NDQ4993', "dbo.Actores_N('APP96', 'C0004', '2')"),
            ('NDQ4994', "dbo.Actores_N('APP98', 'C0004', '2')"),
            ('NDQ4995', "dbo.Actores_N('APP99', 'C0004', '2')"),
            ('NDQ4996', "dbo.Actores_N('APP101', 'C0004', '2')"),
            ('NDQ4997', "dbo.Actores_N('APP102', 'C0004', '2')"),
            ('NDQ4998', "dbo.Actores_N('APP104', 'C0004', '2')"),
            ('NDQ4999', "dbo.Actores_N('APP106', 'C0004', '2')"),
            ('NDQ5000', "dbo.Actores_N('APP108', 'C0004', '2')"),
            ('NDQ5001', "dbo.Actores_N('APP100', 'C0004', '2')"),
            ('NDQ5002', "dbo.Actores_N('APP103', 'C0004', '2')"),
            ('NDQ5003', "dbo.Actores_N('APP105', 'C0004', '2')"),
            ('NDQ5004', "dbo.Actores_N('APP111', 'C0004', '2')"),
            ('NDQ5005', "dbo.Actores_N('APP119', 'C0004', '2')"),
            ('NDQ5006', "dbo.Actores_N('APP121', 'C0004', '2')"),
            ('NDQ5007', "dbo.Actores_N('APP123', 'C0004', '2')"),
            ('NDQ5008', "dbo.Actores_N('APP136', 'C0004', '2')"),
            ('NDQ5009', "dbo.Actores_N('APP139', 'C0004', '2')"),
            ('NDQ5010', "dbo.Actores_N('APP140', 'C0004', '2')"),
            ('NDQ5011', "dbo.Actores_N('APP141', 'C0004', '2')"),
            ('NDQ5012', "dbo.Actores_N('APP142', 'C0004', '2')"),
            ('NDQ5013', "dbo.Actores_N('APP143', 'C0004', '2')"),
            ('NDQ5014', "dbo.Actores_N('APP144', 'C0004', '2')"),
            ('NDQ5015', "dbo.Actores_N('APP145', 'C0004', '2')"),
            ('NDQ5016', "dbo.Actores_N('APP146', 'C0004', '2')"),
            ('NDQ5017', "dbo.Actores_N('APP150', 'C0004', '2')"),
            ('NDQ5018', "dbo.Actores_N('APP163', 'C0004', '2')"),
            ('NDQ5019', "dbo.Actores_N('APP165', 'C0004', '2')"),
            ('NDQ5020', "dbo.Actores_N('APP166', 'C0004', '2')"),
            ('NDQ5021', "dbo.Actores_N('APP168', 'C0004', '2')"),
            ('NDQ5022', "dbo.Actores_Cap('APP91', 'C0004', '2')"),
            ('NDQ5023', "dbo.Actores_Cap('APP92', 'C0004', '2')"),
            ('NDQ5024', "dbo.Actores_Cap('APP93', 'C0004', '2')"),
            ('NDQ5025', "dbo.Actores_Cap('APP94', 'C0004', '2')"),
            ('NDQ5026', "dbo.Actores_Cap('APP95', 'C0004', '2')"),
            ('NDQ5027', "dbo.Actores_Cap('APP96', 'C0004', '2')"),
            ('NDQ5028', "dbo.Actores_Cap('APP98', 'C0004', '2')"),
            ('NDQ5029', "dbo.Actores_Cap('APP99', 'C0004', '2')"),
            ('NDQ5030', "dbo.Actores_Cap('APP101', 'C0004', '2')"),
            ('NDQ5031', "dbo.Actores_Cap('APP102', 'C0004', '2')"),
            ('NDQ5032', "dbo.Actores_Cap('APP104', 'C0004', '2')"),
            ('NDQ5033', "dbo.Actores_Cap('APP106', 'C0004', '2')"),
            ('NDQ5034', "dbo.Actores_Cap('APP108', 'C0004', '2')"),
            ('NDQ5035', "dbo.Actores_Cap('APP100', 'C0004', '2')"),
            ('NDQ5036', "dbo.Actores_Cap('APP103', 'C0004', '2')"),
            ('NDQ5037', "dbo.Actores_Cap('APP105', 'C0004', '2')"),
            ('NDQ5038', "dbo.Actores_Cap('APP111', 'C0004', '2')"),
            ('NDQ5039', "dbo.Actores_Cap('APP119', 'C0004', '2')"),
            ('NDQ5040', "dbo.Actores_Cap('APP121', 'C0004', '2')"),
            ('NDQ5041', "dbo.Actores_Cap('APP123', 'C0004', '2')"),
            ('NDQ5042', "dbo.Actores_Cap('APP136', 'C0004', '2')"),
            ('NDQ5043', "dbo.Actores_Cap('APP139', 'C0004', '2')"),
            ('NDQ5044', "dbo.Actores_Cap('APP140', 'C0004', '2')"),
            ('NDQ5045', "dbo.Actores_Cap('APP141', 'C0004', '2')"),
            ('NDQ5046', "dbo.Actores_Cap('APP142', 'C0004', '2')"),
            ('NDQ5047', "dbo.Actores_Cap('APP143', 'C0004', '2')"),
            ('NDQ5048', "dbo.Actores_Cap('APP144', 'C0004', '2')"),
            ('NDQ5049', "dbo.Actores_Cap('APP145', 'C0004', '2')"),
            ('NDQ5050', "dbo.Actores_Cap('APP146', 'C0004', '2')"),
            ('NDQ5051', "dbo.Actores_Cap('APP150', 'C0004', '2')"),
            ('NDQ5052', "dbo.Actores_Cap('APP163', 'C0004', '2')"),
            ('NDQ5053', "dbo.Actores_Cap('APP165', 'C0004', '2')"),
            ('NDQ5054', "dbo.Actores_Cap('APP166', 'C0004', '2')"),
            ('NDQ5055', "dbo.Actores_Cap('APP168', 'C0004', '2')"),
            ('NDQ5056', "dbo.Actores_N('APP91', 'C0005', '2')"),
            ('NDQ5057', "dbo.Actores_N('APP92', 'C0005', '2')"),
            ('NDQ5058', "dbo.Actores_N('APP93', 'C0005', '2')"),
            ('NDQ5059', "dbo.Actores_N('APP94', 'C0005', '2')"),
            ('NDQ5060', "dbo.Actores_N('APP95', 'C0005', '2')"),
            ('NDQ5061', "dbo.Actores_N('APP96', 'C0005', '2')"),
            ('NDQ5062', "dbo.Actores_N('APP98', 'C0005', '2')"),
            ('NDQ5063', "dbo.Actores_N('APP99', 'C0005', '2')"),
            ('NDQ5064', "dbo.Actores_N('APP101', 'C0005', '2')"),
            ('NDQ5065', "dbo.Actores_N('APP102', 'C0005', '2')"),
            ('NDQ5066', "dbo.Actores_N('APP104', 'C0005', '2')"),
            ('NDQ5067', "dbo.Actores_N('APP106', 'C0005', '2')"),
            ('NDQ5068', "dbo.Actores_N('APP108', 'C0005', '2')"),
            ('NDQ5069', "dbo.Actores_N('APP100', 'C0005', '2')"),
            ('NDQ5070', "dbo.Actores_N('APP103', 'C0005', '2')"),
            ('NDQ5071', "dbo.Actores_N('APP105', 'C0005', '2')"),
            ('NDQ5072', "dbo.Actores_N('APP111', 'C0005', '2')"),
            ('NDQ5073', "dbo.Actores_N('APP119', 'C0005', '2')"),
            ('NDQ5074', "dbo.Actores_N('APP121', 'C0005', '2')"),
            ('NDQ5075', "dbo.Actores_N('APP123', 'C0005', '2')"),
            ('NDQ5076', "dbo.Actores_N('APP136', 'C0005', '2')"),
            ('NDQ5077', "dbo.Actores_N('APP139', 'C0005', '2')"),
            ('NDQ5078', "dbo.Actores_N('APP140', 'C0005', '2')"),
            ('NDQ5079', "dbo.Actores_N('APP141', 'C0005', '2')"),
            ('NDQ5080', "dbo.Actores_N('APP142', 'C0005', '2')"),
            ('NDQ5081', "dbo.Actores_N('APP143', 'C0005', '2')"),
            ('NDQ5082', "dbo.Actores_N('APP144', 'C0005', '2')"),
            ('NDQ5083', "dbo.Actores_N('APP145', 'C0005', '2')"),
            ('NDQ5084', "dbo.Actores_N('APP146', 'C0005', '2')"),
            ('NDQ5085', "dbo.Actores_N('APP150', 'C0005', '2')"),
            ('NDQ5086', "dbo.Actores_N('APP163', 'C0005', '2')"),
            ('NDQ5087', "dbo.Actores_N('APP165', 'C0005', '2')"),
            ('NDQ5088', "dbo.Actores_N('APP166', 'C0005', '2')"),
            ('NDQ5089', "dbo.Actores_N('APP168', 'C0005', '2')"),
            ('NDQ5090', "dbo.Actores_Cap('APP91', 'C0005', '2')"),
            ('NDQ5091', "dbo.Actores_Cap('APP92', 'C0005', '2')"),
            ('NDQ5092', "dbo.Actores_Cap('APP93', 'C0005', '2')"),
            ('NDQ5093', "dbo.Actores_Cap('APP94', 'C0005', '2')"),
            ('NDQ5094', "dbo.Actores_Cap('APP95', 'C0005', '2')"),
            ('NDQ5095', "dbo.Actores_Cap('APP96', 'C0005', '2')"),
            ('NDQ5096', "dbo.Actores_Cap('APP98', 'C0005', '2')"),
            ('NDQ5097', "dbo.Actores_Cap('APP99', 'C0005', '2')"),
            ('NDQ5098', "dbo.Actores_Cap('APP101', 'C0005', '2')"),
            ('NDQ5099', "dbo.Actores_Cap('APP102', 'C0005', '2')"),
            ('NDQ5100', "dbo.Actores_Cap('APP104', 'C0005', '2')"),
            ('NDQ5101', "dbo.Actores_Cap('APP106', 'C0005', '2')"),
            ('NDQ5102', "dbo.Actores_Cap('APP108', 'C0005', '2')"),
            ('NDQ5103', "dbo.Actores_Cap('APP100', 'C0005', '2')"),
            ('NDQ5104', "dbo.Actores_Cap('APP103', 'C0005', '2')"),
            ('NDQ5105', "dbo.Actores_Cap('APP105', 'C0005', '2')"),
            ('NDQ5106', "dbo.Actores_Cap('APP111', 'C0005', '2')"),
            ('NDQ5107', "dbo.Actores_Cap('APP119', 'C0005', '2')"),
            ('NDQ5108', "dbo.Actores_Cap('APP121', 'C0005', '2')"),
            ('NDQ5109', "dbo.Actores_Cap('APP123', 'C0005', '2')"),
            ('NDQ5110', "dbo.Actores_Cap('APP136', 'C0005', '2')"),
            ('NDQ5111', "dbo.Actores_Cap('APP139', 'C0005', '2')"),
            ('NDQ5112', "dbo.Actores_Cap('APP140', 'C0005', '2')"),
            ('NDQ5113', "dbo.Actores_Cap('APP141', 'C0005', '2')"),
            ('NDQ5114', "dbo.Actores_Cap('APP142', 'C0005', '2')"),
            ('NDQ5115', "dbo.Actores_Cap('APP143', 'C0005', '2')"),
            ('NDQ5116', "dbo.Actores_Cap('APP144', 'C0005', '2')"),
            ('NDQ5117', "dbo.Actores_Cap('APP145', 'C0005', '2')"),
            ('NDQ5118', "dbo.Actores_Cap('APP146', 'C0005', '2')"),
            ('NDQ5119', "dbo.Actores_Cap('APP150', 'C0005', '2')"),
            ('NDQ5120', "dbo.Actores_Cap('APP163', 'C0005', '2')"),
            ('NDQ5121', "dbo.Actores_Cap('APP165', 'C0005', '2')"),
            ('NDQ5122', "dbo.Actores_Cap('APP166', 'C0005', '2')"),
            ('NDQ5123', "dbo.Actores_Cap('APP168', 'C0005', '2')"),
            ('NDQ5124', "dbo.Actores_N('APP91', 'C0006', '2')"),
            ('NDQ5125', "dbo.Actores_N('APP92', 'C0006', '2')"),
            ('NDQ5126', "dbo.Actores_N('APP93', 'C0006', '2')"),
            ('NDQ5127', "dbo.Actores_N('APP94', 'C0006', '2')"),
            ('NDQ5128', "dbo.Actores_N('APP95', 'C0006', '2')"),
            ('NDQ5129', "dbo.Actores_N('APP96', 'C0006', '2')"),
            ('NDQ5130', "dbo.Actores_N('APP98', 'C0006', '2')"),
            ('NDQ5131', "dbo.Actores_N('APP99', 'C0006', '2')"),
            ('NDQ5132', "dbo.Actores_N('APP101', 'C0006', '2')"),
            ('NDQ5133', "dbo.Actores_N('APP102', 'C0006', '2')"),
            ('NDQ5134', "dbo.Actores_N('APP104', 'C0006', '2')"),
            ('NDQ5135', "dbo.Actores_N('APP106', 'C0006', '2')"),
            ('NDQ5136', "dbo.Actores_N('APP108', 'C0006', '2')"),
            ('NDQ5137', "dbo.Actores_N('APP100', 'C0006', '2')"),
            ('NDQ5138', "dbo.Actores_N('APP103', 'C0006', '2')"),
            ('NDQ5139', "dbo.Actores_N('APP105', 'C0006', '2')"),
            ('NDQ5140', "dbo.Actores_N('APP111', 'C0006', '2')"),
            ('NDQ5141', "dbo.Actores_N('APP119', 'C0006', '2')"),
            ('NDQ5142', "dbo.Actores_N('APP121', 'C0006', '2')"),
            ('NDQ5143', "dbo.Actores_N('APP123', 'C0006', '2')"),
            ('NDQ5144', "dbo.Actores_N('APP136', 'C0006', '2')"),
            ('NDQ5145', "dbo.Actores_N('APP139', 'C0006', '2')"),
            ('NDQ5146', "dbo.Actores_N('APP140', 'C0006', '2')"),
            ('NDQ5147', "dbo.Actores_N('APP141', 'C0006', '2')"),
            ('NDQ5148', "dbo.Actores_N('APP142', 'C0006', '2')"),
            ('NDQ5149', "dbo.Actores_N('APP143', 'C0006', '2')"),
            ('NDQ5150', "dbo.Actores_N('APP144', 'C0006', '2')"),
            ('NDQ5151', "dbo.Actores_N('APP145', 'C0006', '2')"),
            ('NDQ5152', "dbo.Actores_N('APP146', 'C0006', '2')"),
            ('NDQ5153', "dbo.Actores_N('APP150', 'C0006', '2')"),
            ('NDQ5154', "dbo.Actores_N('APP163', 'C0006', '2')"),
            ('NDQ5155', "dbo.Actores_N('APP165', 'C0006', '2')"),
            ('NDQ5156', "dbo.Actores_N('APP166', 'C0006', '2')"),
            ('NDQ5157', "dbo.Actores_N('APP168', 'C0006', '2')"),
            ('NDQ5158', "dbo.Actores_Cap('APP91', 'C0006', '2')"),
            ('NDQ5159', "dbo.Actores_Cap('APP92', 'C0006', '2')"),
            ('NDQ5160', "dbo.Actores_Cap('APP93', 'C0006', '2')"),
            ('NDQ5161', "dbo.Actores_Cap('APP94', 'C0006', '2')"),
            ('NDQ5162', "dbo.Actores_Cap('APP95', 'C0006', '2')"),
            ('NDQ5163', "dbo.Actores_Cap('APP96', 'C0006', '2')"),
            ('NDQ5164', "dbo.Actores_Cap('APP98', 'C0006', '2')"),
            ('NDQ5165', "dbo.Actores_Cap('APP99', 'C0006', '2')"),
            ('NDQ5166', "dbo.Actores_Cap('APP101', 'C0006', '2')"),
            ('NDQ5167', "dbo.Actores_Cap('APP102', 'C0006', '2')"),
            ('NDQ5168', "dbo.Actores_Cap('APP104', 'C0006', '2')"),
            ('NDQ5169', "dbo.Actores_Cap('APP106', 'C0006', '2')"),
            ('NDQ5170', "dbo.Actores_Cap('APP108', 'C0006', '2')"),
            ('NDQ5171', "dbo.Actores_Cap('APP100', 'C0006', '2')"),
            ('NDQ5172', "dbo.Actores_Cap('APP103', 'C0006', '2')"),
            ('NDQ5173', "dbo.Actores_Cap('APP105', 'C0006', '2')"),
            ('NDQ5174', "dbo.Actores_Cap('APP111', 'C0006', '2')"),
            ('NDQ5175', "dbo.Actores_Cap('APP119', 'C0006', '2')"),
            ('NDQ5176', "dbo.Actores_Cap('APP121', 'C0006', '2')"),
            ('NDQ5177', "dbo.Actores_Cap('APP123', 'C0006', '2')"),
            ('NDQ5178', "dbo.Actores_Cap('APP136', 'C0006', '2')"),
            ('NDQ5179', "dbo.Actores_Cap('APP139', 'C0006', '2')"),
            ('NDQ5180', "dbo.Actores_Cap('APP140', 'C0006', '2')"),
            ('NDQ5181', "dbo.Actores_Cap('APP141', 'C0006', '2')"),
            ('NDQ5182', "dbo.Actores_Cap('APP142', 'C0006', '2')"),
            ('NDQ5183', "dbo.Actores_Cap('APP143', 'C0006', '2')"),
            ('NDQ5184', "dbo.Actores_Cap('APP144', 'C0006', '2')"),
            ('NDQ5185', "dbo.Actores_Cap('APP145', 'C0006', '2')"),
            ('NDQ5186', "dbo.Actores_Cap('APP146', 'C0006', '2')"),
            ('NDQ5187', "dbo.Actores_Cap('APP150', 'C0006', '2')"),
            ('NDQ5188', "dbo.Actores_Cap('APP163', 'C0006', '2')"),
            ('NDQ5189', "dbo.Actores_Cap('APP165', 'C0006', '2')"),
            ('NDQ5190', "dbo.Actores_Cap('APP166', 'C0006', '2')"),
            ('NDQ5191', "dbo.Actores_Cap('APP168', 'C0006', '2')"),
            ('NDQ5192', "dbo.Actores_N('APP91', 'C0008', '2')"),
            ('NDQ5193', "dbo.Actores_N('APP92', 'C0008', '2')"),
            ('NDQ5194', "dbo.Actores_N('APP93', 'C0008', '2')"),
            ('NDQ5195', "dbo.Actores_N('APP94', 'C0008', '2')"),
            ('NDQ5196', "dbo.Actores_N('APP95', 'C0008', '2')"),
            ('NDQ5197', "dbo.Actores_N('APP96', 'C0008', '2')"),
            ('NDQ5198', "dbo.Actores_N('APP98', 'C0008', '2')"),
            ('NDQ5199', "dbo.Actores_N('APP99', 'C0008', '2')"),
            ('NDQ5200', "dbo.Actores_N('APP101', 'C0008', '2')"),
            ('NDQ5201', "dbo.Actores_N('APP102', 'C0008', '2')"),
            ('NDQ5202', "dbo.Actores_N('APP104', 'C0008', '2')"),
            ('NDQ5203', "dbo.Actores_N('APP106', 'C0008', '2')"),
            ('NDQ5204', "dbo.Actores_N('APP108', 'C0008', '2')"),
            ('NDQ5205', "dbo.Actores_N('APP100', 'C0008', '2')"),
            ('NDQ5206', "dbo.Actores_N('APP103', 'C0008', '2')"),
            ('NDQ5207', "dbo.Actores_N('APP105', 'C0008', '2')"),
            ('NDQ5208', "dbo.Actores_N('APP111', 'C0008', '2')"),
            ('NDQ5209', "dbo.Actores_N('APP119', 'C0008', '2')"),
            ('NDQ5210', "dbo.Actores_N('APP121', 'C0008', '2')"),
            ('NDQ5211', "dbo.Actores_N('APP123', 'C0008', '2')"),
            ('NDQ5212', "dbo.Actores_N('APP136', 'C0008', '2')"),
            ('NDQ5213', "dbo.Actores_N('APP139', 'C0008', '2')"),
            ('NDQ5214', "dbo.Actores_N('APP140', 'C0008', '2')"),
            ('NDQ5215', "dbo.Actores_N('APP141', 'C0008', '2')"),
            ('NDQ5216', "dbo.Actores_N('APP142', 'C0008', '2')"),
            ('NDQ5217', "dbo.Actores_N('APP143', 'C0008', '2')"),
            ('NDQ5218', "dbo.Actores_N('APP144', 'C0008', '2')"),
            ('NDQ5219', "dbo.Actores_N('APP145', 'C0008', '2')"),
            ('NDQ5220', "dbo.Actores_N('APP146', 'C0008', '2')"),
            ('NDQ5221', "dbo.Actores_N('APP150', 'C0008', '2')"),
            ('NDQ5222', "dbo.Actores_N('APP163', 'C0008', '2')"),
            ('NDQ5223', "dbo.Actores_N('APP165', 'C0008', '2')"),
            ('NDQ5224', "dbo.Actores_N('APP166', 'C0008', '2')"),
            ('NDQ5225', "dbo.Actores_N('APP168', 'C0008', '2')"),
            ('NDQ5226', "dbo.Actores_Cap('APP91', 'C0008', '2')"),
            ('NDQ5227', "dbo.Actores_Cap('APP92', 'C0008', '2')"),
            ('NDQ5228', "dbo.Actores_Cap('APP93', 'C0008', '2')"),
            ('NDQ5229', "dbo.Actores_Cap('APP94', 'C0008', '2')"),
            ('NDQ5230', "dbo.Actores_Cap('APP95', 'C0008', '2')"),
            ('NDQ5231', "dbo.Actores_Cap('APP96', 'C0008', '2')"),
            ('NDQ5232', "dbo.Actores_Cap('APP98', 'C0008', '2')"),
            ('NDQ5233', "dbo.Actores_Cap('APP99', 'C0008', '2')"),
            ('NDQ5234', "dbo.Actores_Cap('APP101', 'C0008', '2')"),
            ('NDQ5235', "dbo.Actores_Cap('APP102', 'C0008', '2')"),
            ('NDQ5236', "dbo.Actores_Cap('APP104', 'C0008', '2')"),
            ('NDQ5237', "dbo.Actores_Cap('APP106', 'C0008', '2')"),
            ('NDQ5238', "dbo.Actores_Cap('APP108', 'C0008', '2')"),
            ('NDQ5239', "dbo.Actores_Cap('APP100', 'C0008', '2')"),
            ('NDQ5240', "dbo.Actores_Cap('APP103', 'C0008', '2')"),
            ('NDQ5241', "dbo.Actores_Cap('APP105', 'C0008', '2')"),
            ('NDQ5242', "dbo.Actores_Cap('APP111', 'C0008', '2')"),
            ('NDQ5243', "dbo.Actores_Cap('APP119', 'C0008', '2')"),
            ('NDQ5244', "dbo.Actores_Cap('APP121', 'C0008', '2')"),
            ('NDQ5245', "dbo.Actores_Cap('APP123', 'C0008', '2')"),
            ('NDQ5246', "dbo.Actores_Cap('APP136', 'C0008', '2')"),
            ('NDQ5247', "dbo.Actores_Cap('APP139', 'C0008', '2')"),
            ('NDQ5248', "dbo.Actores_Cap('APP140', 'C0008', '2')"),
            ('NDQ5249', "dbo.Actores_Cap('APP141', 'C0008', '2')"),
            ('NDQ5250', "dbo.Actores_Cap('APP142', 'C0008', '2')"),
            ('NDQ5251', "dbo.Actores_Cap('APP143', 'C0008', '2')"),
            ('NDQ5252', "dbo.Actores_Cap('APP144', 'C0008', '2')"),
            ('NDQ5253', "dbo.Actores_Cap('APP145', 'C0008', '2')"),
            ('NDQ5254', "dbo.Actores_Cap('APP146', 'C0008', '2')"),
            ('NDQ5255', "dbo.Actores_Cap('APP150', 'C0008', '2')"),
            ('NDQ5256', "dbo.Actores_Cap('APP163', 'C0008', '2')"),
            ('NDQ5257', "dbo.Actores_Cap('APP165', 'C0008', '2')"),
            ('NDQ5258', "dbo.Actores_Cap('APP166', 'C0008', '2')"),
            ('NDQ5259', "dbo.Actores_Cap('APP168', 'C0008', '2')"),
            ('NDQ5260', "dbo.Actores_N('APP91', 'C0009', '2')"),
            ('NDQ5261', "dbo.Actores_N('APP92', 'C0009', '2')"),
            ('NDQ5262', "dbo.Actores_N('APP93', 'C0009', '2')"),
            ('NDQ5263', "dbo.Actores_N('APP94', 'C0009', '2')"),
            ('NDQ5264', "dbo.Actores_N('APP95', 'C0009', '2')"),
            ('NDQ5265', "dbo.Actores_N('APP96', 'C0009', '2')"),
            ('NDQ5266', "dbo.Actores_N('APP98', 'C0009', '2')"),
            ('NDQ5267', "dbo.Actores_N('APP99', 'C0009', '2')"),
            ('NDQ5268', "dbo.Actores_N('APP101', 'C0009', '2')"),
            ('NDQ5269', "dbo.Actores_N('APP102', 'C0009', '2')"),
            ('NDQ5270', "dbo.Actores_N('APP104', 'C0009', '2')"),
            ('NDQ5271', "dbo.Actores_N('APP106', 'C0009', '2')"),
            ('NDQ5272', "dbo.Actores_N('APP108', 'C0009', '2')"),
            ('NDQ5273', "dbo.Actores_N('APP100', 'C0009', '2')"),
            ('NDQ5274', "dbo.Actores_N('APP103', 'C0009', '2')"),
            ('NDQ5275', "dbo.Actores_N('APP105', 'C0009', '2')"),
            ('NDQ5276', "dbo.Actores_N('APP111', 'C0009', '2')"),
            ('NDQ5277', "dbo.Actores_N('APP119', 'C0009', '2')"),
            ('NDQ5278', "dbo.Actores_N('APP121', 'C0009', '2')"),
            ('NDQ5279', "dbo.Actores_N('APP123', 'C0009', '2')"),
            ('NDQ5280', "dbo.Actores_N('APP136', 'C0009', '2')"),
            ('NDQ5281', "dbo.Actores_N('APP139', 'C0009', '2')"),
            ('NDQ5282', "dbo.Actores_N('APP140', 'C0009', '2')"),
            ('NDQ5283', "dbo.Actores_N('APP141', 'C0009', '2')"),
            ('NDQ5284', "dbo.Actores_N('APP142', 'C0009', '2')"),
            ('NDQ5285', "dbo.Actores_N('APP143', 'C0009', '2')"),
            ('NDQ5286', "dbo.Actores_N('APP144', 'C0009', '2')"),
            ('NDQ5287', "dbo.Actores_N('APP145', 'C0009', '2')"),
            ('NDQ5288', "dbo.Actores_N('APP146', 'C0009', '2')"),
            ('NDQ5289', "dbo.Actores_N('APP150', 'C0009', '2')"),
            ('NDQ5290', "dbo.Actores_N('APP163', 'C0009', '2')"),
            ('NDQ5291', "dbo.Actores_N('APP165', 'C0009', '2')"),
            ('NDQ5292', "dbo.Actores_N('APP166', 'C0009', '2')"),
            ('NDQ5293', "dbo.Actores_N('APP168', 'C0009', '2')"),
            ('NDQ5294', "dbo.Actores_Cap('APP91', 'C0009', '2')"),
            ('NDQ5295', "dbo.Actores_Cap('APP92', 'C0009', '2')"),
            ('NDQ5296', "dbo.Actores_Cap('APP93', 'C0009', '2')"),
            ('NDQ5297', "dbo.Actores_Cap('APP94', 'C0009', '2')"),
            ('NDQ5298', "dbo.Actores_Cap('APP95', 'C0009', '2')"),
            ('NDQ5299', "dbo.Actores_Cap('APP96', 'C0009', '2')"),
            ('NDQ5300', "dbo.Actores_Cap('APP98', 'C0009', '2')"),
            ('NDQ5301', "dbo.Actores_Cap('APP99', 'C0009', '2')"),
            ('NDQ5302', "dbo.Actores_Cap('APP101', 'C0009', '2')"),
            ('NDQ5303', "dbo.Actores_Cap('APP102', 'C0009', '2')"),
            ('NDQ5304', "dbo.Actores_Cap('APP104', 'C0009', '2')"),
            ('NDQ5305', "dbo.Actores_Cap('APP106', 'C0009', '2')"),
            ('NDQ5306', "dbo.Actores_Cap('APP108', 'C0009', '2')"),
            ('NDQ5307', "dbo.Actores_Cap('APP100', 'C0009', '2')"),
            ('NDQ5308', "dbo.Actores_Cap('APP103', 'C0009', '2')"),
            ('NDQ5309', "dbo.Actores_Cap('APP105', 'C0009', '2')"),
            ('NDQ5310', "dbo.Actores_Cap('APP111', 'C0009', '2')"),
            ('NDQ5311', "dbo.Actores_Cap('APP119', 'C0009', '2')"),
            ('NDQ5312', "dbo.Actores_Cap('APP121', 'C0009', '2')"),
            ('NDQ5313', "dbo.Actores_Cap('APP123', 'C0009', '2')"),
            ('NDQ5314', "dbo.Actores_Cap('APP136', 'C0009', '2')"),
            ('NDQ5315', "dbo.Actores_Cap('APP139', 'C0009', '2')"),
            ('NDQ5316', "dbo.Actores_Cap('APP140', 'C0009', '2')"),
            ('NDQ5317', "dbo.Actores_Cap('APP141', 'C0009', '2')"),
            ('NDQ5318', "dbo.Actores_Cap('APP142', 'C0009', '2')"),
            ('NDQ5319', "dbo.Actores_Cap('APP143', 'C0009', '2')"),
            ('NDQ5320', "dbo.Actores_Cap('APP144', 'C0009', '2')"),
            ('NDQ5321', "dbo.Actores_Cap('APP145', 'C0009', '2')"),
            ('NDQ5322', "dbo.Actores_Cap('APP146', 'C0009', '2')"),
            ('NDQ5323', "dbo.Actores_Cap('APP150', 'C0009', '2')"),
            ('NDQ5324', "dbo.Actores_Cap('APP163', 'C0009', '2')"),
            ('NDQ5325', "dbo.Actores_Cap('APP165', 'C0009', '2')"),
            ('NDQ5326', "dbo.Actores_Cap('APP166', 'C0009', '2')"),
            ('NDQ5327', "dbo.Actores_Cap('APP168', 'C0009', '2')"),
            ('NDQ5328', "dbo.Actores_N('APP91', 'C0010', '2')"),
            ('NDQ5329', "dbo.Actores_N('APP92', 'C0010', '2')"),
            ('NDQ5330', "dbo.Actores_N('APP93', 'C0010', '2')"),
            ('NDQ5331', "dbo.Actores_N('APP94', 'C0010', '2')"),
            ('NDQ5332', "dbo.Actores_N('APP95', 'C0010', '2')"),
            ('NDQ5333', "dbo.Actores_N('APP96', 'C0010', '2')"),
            ('NDQ5334', "dbo.Actores_N('APP98', 'C0010', '2')"),
            ('NDQ5335', "dbo.Actores_N('APP99', 'C0010', '2')"),
            ('NDQ5336', "dbo.Actores_N('APP101', 'C0010', '2')"),
            ('NDQ5337', "dbo.Actores_N('APP102', 'C0010', '2')"),
            ('NDQ5338', "dbo.Actores_N('APP104', 'C0010', '2')"),
            ('NDQ5339', "dbo.Actores_N('APP106', 'C0010', '2')"),
            ('NDQ5340', "dbo.Actores_N('APP108', 'C0010', '2')"),
            ('NDQ5341', "dbo.Actores_N('APP100', 'C0010', '2')"),
            ('NDQ5342', "dbo.Actores_N('APP103', 'C0010', '2')"),
            ('NDQ5343', "dbo.Actores_N('APP105', 'C0010', '2')"),
            ('NDQ5344', "dbo.Actores_N('APP111', 'C0010', '2')"),
            ('NDQ5345', "dbo.Actores_N('APP119', 'C0010', '2')"),
            ('NDQ5346', "dbo.Actores_N('APP121', 'C0010', '2')"),
            ('NDQ5347', "dbo.Actores_N('APP123', 'C0010', '2')"),
            ('NDQ5348', "dbo.Actores_N('APP136', 'C0010', '2')"),
            ('NDQ5349', "dbo.Actores_N('APP139', 'C0010', '2')"),
            ('NDQ5350', "dbo.Actores_N('APP140', 'C0010', '2')"),
            ('NDQ5351', "dbo.Actores_N('APP141', 'C0010', '2')"),
            ('NDQ5352', "dbo.Actores_N('APP142', 'C0010', '2')"),
            ('NDQ5353', "dbo.Actores_N('APP143', 'C0010', '2')"),
            ('NDQ5354', "dbo.Actores_N('APP144', 'C0010', '2')"),
            ('NDQ5355', "dbo.Actores_N('APP145', 'C0010', '2')"),
            ('NDQ5356', "dbo.Actores_N('APP146', 'C0010', '2')"),
            ('NDQ5357', "dbo.Actores_N('APP150', 'C0010', '2')"),
            ('NDQ5358', "dbo.Actores_N('APP163', 'C0010', '2')"),
            ('NDQ5359', "dbo.Actores_N('APP165', 'C0010', '2')"),
            ('NDQ5360', "dbo.Actores_N('APP166', 'C0010', '2')"),
            ('NDQ5361', "dbo.Actores_N('APP168', 'C0010', '2')"),
            ('NDQ5362', "dbo.Actores_Cap('APP91', 'C0010', '2')"),
            ('NDQ5363', "dbo.Actores_Cap('APP92', 'C0010', '2')"),
            ('NDQ5364', "dbo.Actores_Cap('APP93', 'C0010', '2')"),
            ('NDQ5365', "dbo.Actores_Cap('APP94', 'C0010', '2')"),
            ('NDQ5366', "dbo.Actores_Cap('APP95', 'C0010', '2')"),
            ('NDQ5367', "dbo.Actores_Cap('APP96', 'C0010', '2')"),
            ('NDQ5368', "dbo.Actores_Cap('APP98', 'C0010', '2')"),
            ('NDQ5369', "dbo.Actores_Cap('APP99', 'C0010', '2')"),
            ('NDQ5370', "dbo.Actores_Cap('APP101', 'C0010', '2')"),
            ('NDQ5371', "dbo.Actores_Cap('APP102', 'C0010', '2')"),
            ('NDQ5372', "dbo.Actores_Cap('APP104', 'C0010', '2')"),
            ('NDQ5373', "dbo.Actores_Cap('APP106', 'C0010', '2')"),
            ('NDQ5374', "dbo.Actores_Cap('APP108', 'C0010', '2')"),
            ('NDQ5375', "dbo.Actores_Cap('APP100', 'C0010', '2')"),
            ('NDQ5376', "dbo.Actores_Cap('APP103', 'C0010', '2')"),
            ('NDQ5377', "dbo.Actores_Cap('APP105', 'C0010', '2')"),
            ('NDQ5378', "dbo.Actores_Cap('APP111', 'C0010', '2')"),
            ('NDQ5379', "dbo.Actores_Cap('APP119', 'C0010', '2')"),
            ('NDQ5380', "dbo.Actores_Cap('APP121', 'C0010', '2')"),
            ('NDQ5381', "dbo.Actores_Cap('APP123', 'C0010', '2')"),
            ('NDQ5382', "dbo.Actores_Cap('APP136', 'C0010', '2')"),
            ('NDQ5383', "dbo.Actores_Cap('APP139', 'C0010', '2')"),
            ('NDQ5384', "dbo.Actores_Cap('APP140', 'C0010', '2')"),
            ('NDQ5385', "dbo.Actores_Cap('APP141', 'C0010', '2')"),
            ('NDQ5386', "dbo.Actores_Cap('APP142', 'C0010', '2')"),
            ('NDQ5387', "dbo.Actores_Cap('APP143', 'C0010', '2')"),
            ('NDQ5388', "dbo.Actores_Cap('APP144', 'C0010', '2')"),
            ('NDQ5389', "dbo.Actores_Cap('APP145', 'C0010', '2')"),
            ('NDQ5390', "dbo.Actores_Cap('APP146', 'C0010', '2')"),
            ('NDQ5391', "dbo.Actores_Cap('APP150', 'C0010', '2')"),
            ('NDQ5392', "dbo.Actores_Cap('APP163', 'C0010', '2')"),
            ('NDQ5393', "dbo.Actores_Cap('APP165', 'C0010', '2')"),
            ('NDQ5394', "dbo.Actores_Cap('APP166', 'C0010', '2')"),
            ('NDQ5395', "dbo.Actores_Cap('APP168', 'C0010', '2')"),
            ('NDQ5396', "dbo.Actores_N('APP91', 'C0012', '2')"),
            ('NDQ5397', "dbo.Actores_N('APP92', 'C0012', '2')"),
            ('NDQ5398', "dbo.Actores_N('APP93', 'C0012', '2')"),
            ('NDQ5399', "dbo.Actores_N('APP94', 'C0012', '2')"),
            ('NDQ5400', "dbo.Actores_N('APP95', 'C0012', '2')"),
            ('NDQ5401', "dbo.Actores_N('APP96', 'C0012', '2')"),
            ('NDQ5402', "dbo.Actores_N('APP98', 'C0012', '2')"),
            ('NDQ5403', "dbo.Actores_N('APP99', 'C0012', '2')"),
            ('NDQ5404', "dbo.Actores_N('APP101', 'C0012', '2')"),
            ('NDQ5405', "dbo.Actores_N('APP102', 'C0012', '2')"),
            ('NDQ5406', "dbo.Actores_N('APP104', 'C0012', '2')"),
            ('NDQ5407', "dbo.Actores_N('APP106', 'C0012', '2')"),
            ('NDQ5408', "dbo.Actores_N('APP108', 'C0012', '2')"),
            ('NDQ5409', "dbo.Actores_N('APP100', 'C0012', '2')"),
            ('NDQ5410', "dbo.Actores_N('APP103', 'C0012', '2')"),
            ('NDQ5411', "dbo.Actores_N('APP105', 'C0012', '2')"),
            ('NDQ5412', "dbo.Actores_N('APP111', 'C0012', '2')"),
            ('NDQ5413', "dbo.Actores_N('APP119', 'C0012', '2')"),
            ('NDQ5414', "dbo.Actores_N('APP121', 'C0012', '2')"),
            ('NDQ5415', "dbo.Actores_N('APP123', 'C0012', '2')"),
            ('NDQ5416', "dbo.Actores_N('APP136', 'C0012', '2')"),
            ('NDQ5417', "dbo.Actores_N('APP139', 'C0012', '2')"),
            ('NDQ5418', "dbo.Actores_N('APP140', 'C0012', '2')"),
            ('NDQ5419', "dbo.Actores_N('APP141', 'C0012', '2')"),
            ('NDQ5420', "dbo.Actores_N('APP142', 'C0012', '2')"),
            ('NDQ5421', "dbo.Actores_N('APP143', 'C0012', '2')"),
            ('NDQ5422', "dbo.Actores_N('APP144', 'C0012', '2')"),
            ('NDQ5423', "dbo.Actores_N('APP145', 'C0012', '2')"),
            ('NDQ5424', "dbo.Actores_N('APP146', 'C0012', '2')"),
            ('NDQ5425', "dbo.Actores_N('APP150', 'C0012', '2')"),
            ('NDQ5426', "dbo.Actores_N('APP163', 'C0012', '2')"),
            ('NDQ5427', "dbo.Actores_N('APP165', 'C0012', '2')"),
            ('NDQ5428', "dbo.Actores_N('APP166', 'C0012', '2')"),
            ('NDQ5429', "dbo.Actores_N('APP168', 'C0012', '2')"),
            ('NDQ5430', "dbo.Actores_Cap('APP91', 'C0012', '2')"),
            ('NDQ5431', "dbo.Actores_Cap('APP92', 'C0012', '2')"),
            ('NDQ5432', "dbo.Actores_Cap('APP93', 'C0012', '2')"),
            ('NDQ5433', "dbo.Actores_Cap('APP94', 'C0012', '2')"),
            ('NDQ5434', "dbo.Actores_Cap('APP95', 'C0012', '2')"),
            ('NDQ5435', "dbo.Actores_Cap('APP96', 'C0012', '2')"),
            ('NDQ5436', "dbo.Actores_Cap('APP98', 'C0012', '2')"),
            ('NDQ5437', "dbo.Actores_Cap('APP99', 'C0012', '2')"),
            ('NDQ5438', "dbo.Actores_Cap('APP101', 'C0012', '2')"),
            ('NDQ5439', "dbo.Actores_Cap('APP102', 'C0012', '2')"),
            ('NDQ5440', "dbo.Actores_Cap('APP104', 'C0012', '2')"),
            ('NDQ5441', "dbo.Actores_Cap('APP106', 'C0012', '2')"),
            ('NDQ5442', "dbo.Actores_Cap('APP108', 'C0012', '2')"),
            ('NDQ5443', "dbo.Actores_Cap('APP100', 'C0012', '2')"),
            ('NDQ5444', "dbo.Actores_Cap('APP103', 'C0012', '2')"),
            ('NDQ5445', "dbo.Actores_Cap('APP105', 'C0012', '2')"),
            ('NDQ5446', "dbo.Actores_Cap('APP111', 'C0012', '2')"),
            ('NDQ5447', "dbo.Actores_Cap('APP119', 'C0012', '2')"),
            ('NDQ5448', "dbo.Actores_Cap('APP121', 'C0012', '2')"),
            ('NDQ5449', "dbo.Actores_Cap('APP123', 'C0012', '2')"),
            ('NDQ5450', "dbo.Actores_Cap('APP136', 'C0012', '2')"),
            ('NDQ5451', "dbo.Actores_Cap('APP139', 'C0012', '2')"),
            ('NDQ5452', "dbo.Actores_Cap('APP140', 'C0012', '2')"),
            ('NDQ5453', "dbo.Actores_Cap('APP141', 'C0012', '2')"),
            ('NDQ5454', "dbo.Actores_Cap('APP142', 'C0012', '2')"),
            ('NDQ5455', "dbo.Actores_Cap('APP143', 'C0012', '2')"),
            ('NDQ5456', "dbo.Actores_Cap('APP144', 'C0012', '2')"),
            ('NDQ5457', "dbo.Actores_Cap('APP145', 'C0012', '2')"),
            ('NDQ5458', "dbo.Actores_Cap('APP146', 'C0012', '2')"),
            ('NDQ5459', "dbo.Actores_Cap('APP150', 'C0012', '2')"),
            ('NDQ5460', "dbo.Actores_Cap('APP163', 'C0012', '2')"),
            ('NDQ5461', "dbo.Actores_Cap('APP165', 'C0012', '2')"),
            ('NDQ5462', "dbo.Actores_Cap('APP166', 'C0012', '2')"),
            ('NDQ5463', "dbo.Actores_Cap('APP168', 'C0012', '2')"),
            ('NDQ5464', "dbo.Actores_N('APP91', 'C3121', '2')"),
            ('NDQ5465', "dbo.Actores_N('APP92', 'C3121', '2')"),
            ('NDQ5466', "dbo.Actores_N('APP93', 'C3121', '2')"),
            ('NDQ5467', "dbo.Actores_N('APP94', 'C3121', '2')"),
            ('NDQ5468', "dbo.Actores_N('APP95', 'C3121', '2')"),
            ('NDQ5469', "dbo.Actores_N('APP96', 'C3121', '2')"),
            ('NDQ5470', "dbo.Actores_N('APP98', 'C3121', '2')"),
            ('NDQ5471', "dbo.Actores_N('APP99', 'C3121', '2')"),
            ('NDQ5472', "dbo.Actores_N('APP101', 'C3121', '2')"),
            ('NDQ5473', "dbo.Actores_N('APP102', 'C3121', '2')"),
            ('NDQ5474', "dbo.Actores_N('APP104', 'C3121', '2')"),
            ('NDQ5475', "dbo.Actores_N('APP106', 'C3121', '2')"),
            ('NDQ5476', "dbo.Actores_N('APP108', 'C3121', '2')"),
            ('NDQ5477', "dbo.Actores_N('APP100', 'C3121', '2')"),
            ('NDQ5478', "dbo.Actores_N('APP103', 'C3121', '2')"),
            ('NDQ5479', "dbo.Actores_N('APP105', 'C3121', '2')"),
            ('NDQ5480', "dbo.Actores_N('APP111', 'C3121', '2')"),
            ('NDQ5481', "dbo.Actores_N('APP119', 'C3121', '2')"),
            ('NDQ5482', "dbo.Actores_N('APP121', 'C3121', '2')"),
            ('NDQ5483', "dbo.Actores_N('APP123', 'C3121', '2')"),
            ('NDQ5484', "dbo.Actores_N('APP136', 'C3121', '2')"),
            ('NDQ5485', "dbo.Actores_N('APP139', 'C3121', '2')"),
            ('NDQ5486', "dbo.Actores_N('APP140', 'C3121', '2')"),
            ('NDQ5487', "dbo.Actores_N('APP141', 'C3121', '2')"),
            ('NDQ5488', "dbo.Actores_N('APP142', 'C3121', '2')"),
            ('NDQ5489', "dbo.Actores_N('APP143', 'C3121', '2')"),
            ('NDQ5490', "dbo.Actores_N('APP144', 'C3121', '2')"),
            ('NDQ5491', "dbo.Actores_N('APP145', 'C3121', '2')"),
            ('NDQ5492', "dbo.Actores_N('APP146', 'C3121', '2')"),
            ('NDQ5493', "dbo.Actores_N('APP150', 'C3121', '2')"),
            ('NDQ5494', "dbo.Actores_N('APP163', 'C3121', '2')"),
            ('NDQ5495', "dbo.Actores_N('APP165', 'C3121', '2')"),
            ('NDQ5496', "dbo.Actores_N('APP166', 'C3121', '2')"),
            ('NDQ5497', "dbo.Actores_N('APP168', 'C3121', '2')"),
            ('NDQ5498', "dbo.Actores_Cap('APP91', 'C3121', '2')"),
            ('NDQ5499', "dbo.Actores_Cap('APP92', 'C3121', '2')"),
            ('NDQ5500', "dbo.Actores_Cap('APP93', 'C3121', '2')"),
            ('NDQ5501', "dbo.Actores_Cap('APP94', 'C3121', '2')"),
            ('NDQ5502', "dbo.Actores_Cap('APP95', 'C3121', '2')"),
            ('NDQ5503', "dbo.Actores_Cap('APP96', 'C3121', '2')"),
            ('NDQ5504', "dbo.Actores_Cap('APP98', 'C3121', '2')"),
            ('NDQ5505', "dbo.Actores_Cap('APP99', 'C3121', '2')"),
            ('NDQ5506', "dbo.Actores_Cap('APP101', 'C3121', '2')"),
            ('NDQ5507', "dbo.Actores_Cap('APP102', 'C3121', '2')"),
            ('NDQ5508', "dbo.Actores_Cap('APP104', 'C3121', '2')"),
            ('NDQ5509', "dbo.Actores_Cap('APP106', 'C3121', '2')"),
            ('NDQ5510', "dbo.Actores_Cap('APP108', 'C3121', '2')"),
            ('NDQ5511', "dbo.Actores_Cap('APP100', 'C3121', '2')"),
            ('NDQ5512', "dbo.Actores_Cap('APP103', 'C3121', '2')"),
            ('NDQ5513', "dbo.Actores_Cap('APP105', 'C3121', '2')"),
            ('NDQ5514', "dbo.Actores_Cap('APP111', 'C3121', '2')"),
            ('NDQ5515', "dbo.Actores_Cap('APP119', 'C3121', '2')"),
            ('NDQ5516', "dbo.Actores_Cap('APP121', 'C3121', '2')"),
            ('NDQ5517', "dbo.Actores_Cap('APP123', 'C3121', '2')"),
            ('NDQ5518', "dbo.Actores_Cap('APP136', 'C3121', '2')"),
            ('NDQ5519', "dbo.Actores_Cap('APP139', 'C3121', '2')"),
            ('NDQ5520', "dbo.Actores_Cap('APP140', 'C3121', '2')"),
            ('NDQ5521', "dbo.Actores_Cap('APP141', 'C3121', '2')"),
            ('NDQ5522', "dbo.Actores_Cap('APP142', 'C3121', '2')"),
            ('NDQ5523', "dbo.Actores_Cap('APP143', 'C3121', '2')"),
            ('NDQ5524', "dbo.Actores_Cap('APP144', 'C3121', '2')"),
            ('NDQ5525', "dbo.Actores_Cap('APP145', 'C3121', '2')"),
            ('NDQ5526', "dbo.Actores_Cap('APP146', 'C3121', '2')"),
            ('NDQ5527', "dbo.Actores_Cap('APP150', 'C3121', '2')"),
            ('NDQ5528', "dbo.Actores_Cap('APP163', 'C3121', '2')"),
            ('NDQ5529', "dbo.Actores_Cap('APP165', 'C3121', '2')"),
            ('NDQ5530', "dbo.Actores_Cap('APP166', 'C3121', '2')"),
            ('NDQ5531', "dbo.Actores_Cap('APP168', 'C3121', '2')"),
            ('NDQ5532', "dbo.Actores_N('APP91', 'C3141', '2')"),
            ('NDQ5533', "dbo.Actores_N('APP92', 'C3141', '2')"),
            ('NDQ5534', "dbo.Actores_N('APP93', 'C3141', '2')"),
            ('NDQ5535', "dbo.Actores_N('APP94', 'C3141', '2')"),
            ('NDQ5536', "dbo.Actores_N('APP95', 'C3141', '2')"),
            ('NDQ5537', "dbo.Actores_N('APP96', 'C3141', '2')"),
            ('NDQ5538', "dbo.Actores_N('APP98', 'C3141', '2')"),
            ('NDQ5539', "dbo.Actores_N('APP99', 'C3141', '2')"),
            ('NDQ5540', "dbo.Actores_N('APP101', 'C3141', '2')"),
            ('NDQ5541', "dbo.Actores_N('APP102', 'C3141', '2')"),
            ('NDQ5542', "dbo.Actores_N('APP104', 'C3141', '2')"),
            ('NDQ5543', "dbo.Actores_N('APP106', 'C3141', '2')"),
            ('NDQ5544', "dbo.Actores_N('APP108', 'C3141', '2')"),
            ('NDQ5545', "dbo.Actores_N('APP100', 'C3141', '2')"),
            ('NDQ5546', "dbo.Actores_N('APP103', 'C3141', '2')"),
            ('NDQ5547', "dbo.Actores_N('APP105', 'C3141', '2')"),
            ('NDQ5548', "dbo.Actores_N('APP111', 'C3141', '2')"),
            ('NDQ5549', "dbo.Actores_N('APP119', 'C3141', '2')"),
            ('NDQ5550', "dbo.Actores_N('APP121', 'C3141', '2')"),
            ('NDQ5551', "dbo.Actores_N('APP123', 'C3141', '2')"),
            ('NDQ5552', "dbo.Actores_N('APP136', 'C3141', '2')"),
            ('NDQ5553', "dbo.Actores_N('APP139', 'C3141', '2')"),
            ('NDQ5554', "dbo.Actores_N('APP140', 'C3141', '2')"),
            ('NDQ5555', "dbo.Actores_N('APP141', 'C3141', '2')"),
            ('NDQ5556', "dbo.Actores_N('APP142', 'C3141', '2')"),
            ('NDQ5557', "dbo.Actores_N('APP143', 'C3141', '2')"),
            ('NDQ5558', "dbo.Actores_N('APP144', 'C3141', '2')"),
            ('NDQ5559', "dbo.Actores_N('APP145', 'C3141', '2')"),
            ('NDQ5560', "dbo.Actores_N('APP146', 'C3141', '2')"),
            ('NDQ5561', "dbo.Actores_N('APP150', 'C3141', '2')"),
            ('NDQ5562', "dbo.Actores_N('APP163', 'C3141', '2')"),
            ('NDQ5563', "dbo.Actores_N('APP165', 'C3141', '2')"),
            ('NDQ5564', "dbo.Actores_N('APP166', 'C3141', '2')"),
            ('NDQ5565', "dbo.Actores_N('APP168', 'C3141', '2')"),
            ('NDQ5566', "dbo.Actores_Cap('APP91', 'C3141', '2')"),
            ('NDQ5567', "dbo.Actores_Cap('APP92', 'C3141', '2')"),
            ('NDQ5568', "dbo.Actores_Cap('APP93', 'C3141', '2')"),
            ('NDQ5569', "dbo.Actores_Cap('APP94', 'C3141', '2')"),
            ('NDQ5570', "dbo.Actores_Cap('APP95', 'C3141', '2')"),
            ('NDQ5571', "dbo.Actores_Cap('APP96', 'C3141', '2')"),
            ('NDQ5572', "dbo.Actores_Cap('APP98', 'C3141', '2')"),
            ('NDQ5573', "dbo.Actores_Cap('APP99', 'C3141', '2')"),
            ('NDQ5574', "dbo.Actores_Cap('APP101', 'C3141', '2')"),
            ('NDQ5575', "dbo.Actores_Cap('APP102', 'C3141', '2')"),
            ('NDQ5576', "dbo.Actores_Cap('APP104', 'C3141', '2')"),
            ('NDQ5577', "dbo.Actores_Cap('APP106', 'C3141', '2')"),
            ('NDQ5578', "dbo.Actores_Cap('APP108', 'C3141', '2')"),
            ('NDQ5579', "dbo.Actores_Cap('APP100', 'C3141', '2')"),
            ('NDQ5580', "dbo.Actores_Cap('APP103', 'C3141', '2')"),
            ('NDQ5581', "dbo.Actores_Cap('APP105', 'C3141', '2')"),
            ('NDQ5582', "dbo.Actores_Cap('APP111', 'C3141', '2')"),
            ('NDQ5583', "dbo.Actores_Cap('APP119', 'C3141', '2')"),
            ('NDQ5584', "dbo.Actores_Cap('APP121', 'C3141', '2')"),
            ('NDQ5585', "dbo.Actores_Cap('APP123', 'C3141', '2')"),
            ('NDQ5586', "dbo.Actores_Cap('APP136', 'C3141', '2')"),
            ('NDQ5587', "dbo.Actores_Cap('APP139', 'C3141', '2')"),
            ('NDQ5588', "dbo.Actores_Cap('APP140', 'C3141', '2')"),
            ('NDQ5589', "dbo.Actores_Cap('APP141', 'C3141', '2')"),
            ('NDQ5590', "dbo.Actores_Cap('APP142', 'C3141', '2')"),
            ('NDQ5591', "dbo.Actores_Cap('APP143', 'C3141', '2')"),
            ('NDQ5592', "dbo.Actores_Cap('APP144', 'C3141', '2')"),
            ('NDQ5593', "dbo.Actores_Cap('APP145', 'C3141', '2')"),
            ('NDQ5594', "dbo.Actores_Cap('APP146', 'C3141', '2')"),
            ('NDQ5595', "dbo.Actores_Cap('APP150', 'C3141', '2')"),
            ('NDQ5596', "dbo.Actores_Cap('APP163', 'C3141', '2')"),
            ('NDQ5597', "dbo.Actores_Cap('APP165', 'C3141', '2')"),
            ('NDQ5598', "dbo.Actores_Cap('APP166', 'C3141', '2')"),
            ('NDQ5599', "dbo.Actores_Cap('APP168', 'C3141', '2')"),
            ('NDQ5600', "dbo.Actores_N('APP91', 'C1042', '2')"),
            ('NDQ5601', "dbo.Actores_N('APP92', 'C1042', '2')"),
            ('NDQ5602', "dbo.Actores_N('APP93', 'C1042', '2')"),
            ('NDQ5603', "dbo.Actores_N('APP94', 'C1042', '2')"),
            ('NDQ5604', "dbo.Actores_N('APP95', 'C1042', '2')"),
            ('NDQ5605', "dbo.Actores_N('APP96', 'C1042', '2')"),
            ('NDQ5606', "dbo.Actores_N('APP98', 'C1042', '2')"),
            ('NDQ5607', "dbo.Actores_N('APP99', 'C1042', '2')"),
            ('NDQ5608', "dbo.Actores_N('APP101', 'C1042', '2')"),
            ('NDQ5609', "dbo.Actores_N('APP102', 'C1042', '2')"),
            ('NDQ5610', "dbo.Actores_N('APP104', 'C1042', '2')"),
            ('NDQ5611', "dbo.Actores_N('APP106', 'C1042', '2')"),
            ('NDQ5612', "dbo.Actores_N('APP108', 'C1042', '2')"),
            ('NDQ5613', "dbo.Actores_N('APP100', 'C1042', '2')"),
            ('NDQ5614', "dbo.Actores_N('APP103', 'C1042', '2')"),
            ('NDQ5615', "dbo.Actores_N('APP105', 'C1042', '2')"),
            ('NDQ5616', "dbo.Actores_N('APP111', 'C1042', '2')"),
            ('NDQ5617', "dbo.Actores_N('APP119', 'C1042', '2')"),
            ('NDQ5618', "dbo.Actores_N('APP121', 'C1042', '2')"),
            ('NDQ5619', "dbo.Actores_N('APP123', 'C1042', '2')"),
            ('NDQ5620', "dbo.Actores_N('APP136', 'C1042', '2')"),
            ('NDQ5621', "dbo.Actores_N('APP139', 'C1042', '2')"),
            ('NDQ5622', "dbo.Actores_N('APP140', 'C1042', '2')"),
            ('NDQ5623', "dbo.Actores_N('APP141', 'C1042', '2')"),
            ('NDQ5624', "dbo.Actores_N('APP142', 'C1042', '2')"),
            ('NDQ5625', "dbo.Actores_N('APP143', 'C1042', '2')"),
            ('NDQ5626', "dbo.Actores_N('APP144', 'C1042', '2')"),
            ('NDQ5627', "dbo.Actores_N('APP145', 'C1042', '2')"),
            ('NDQ5628', "dbo.Actores_N('APP146', 'C1042', '2')"),
            ('NDQ5629', "dbo.Actores_N('APP150', 'C1042', '2')"),
            ('NDQ5630', "dbo.Actores_N('APP163', 'C1042', '2')"),
            ('NDQ5631', "dbo.Actores_N('APP165', 'C1042', '2')"),
            ('NDQ5632', "dbo.Actores_N('APP166', 'C1042', '2')"),
            ('NDQ5633', "dbo.Actores_N('APP168', 'C1042', '2')"),
            ('NDQ5634', "dbo.Actores_Cap('APP91', 'C1042', '2')"),
            ('NDQ5635', "dbo.Actores_Cap('APP92', 'C1042', '2')"),
            ('NDQ5636', "dbo.Actores_Cap('APP93', 'C1042', '2')"),
            ('NDQ5637', "dbo.Actores_Cap('APP94', 'C1042', '2')"),
            ('NDQ5638', "dbo.Actores_Cap('APP95', 'C1042', '2')"),
            ('NDQ5639', "dbo.Actores_Cap('APP96', 'C1042', '2')"),
            ('NDQ5640', "dbo.Actores_Cap('APP98', 'C1042', '2')"),
            ('NDQ5641', "dbo.Actores_Cap('APP99', 'C1042', '2')"),
            ('NDQ5642', "dbo.Actores_Cap('APP101', 'C1042', '2')"),
            ('NDQ5643', "dbo.Actores_Cap('APP102', 'C1042', '2')"),
            ('NDQ5644', "dbo.Actores_Cap('APP104', 'C1042', '2')"),
            ('NDQ5645', "dbo.Actores_Cap('APP106', 'C1042', '2')"),
            ('NDQ5646', "dbo.Actores_Cap('APP108', 'C1042', '2')"),
            ('NDQ5647', "dbo.Actores_Cap('APP100', 'C1042', '2')"),
            ('NDQ5648', "dbo.Actores_Cap('APP103', 'C1042', '2')"),
            ('NDQ5649', "dbo.Actores_Cap('APP105', 'C1042', '2')"),
            ('NDQ5650', "dbo.Actores_Cap('APP111', 'C1042', '2')"),
            ('NDQ5651', "dbo.Actores_Cap('APP119', 'C1042', '2')"),
            ('NDQ5652', "dbo.Actores_Cap('APP121', 'C1042', '2')"),
            ('NDQ5653', "dbo.Actores_Cap('APP123', 'C1042', '2')"),
            ('NDQ5654', "dbo.Actores_Cap('APP136', 'C1042', '2')"),
            ('NDQ5655', "dbo.Actores_Cap('APP139', 'C1042', '2')"),
            ('NDQ5656', "dbo.Actores_Cap('APP140', 'C1042', '2')"),
            ('NDQ5657', "dbo.Actores_Cap('APP141', 'C1042', '2')"),
            ('NDQ5658', "dbo.Actores_Cap('APP142', 'C1042', '2')"),
            ('NDQ5659', "dbo.Actores_Cap('APP143', 'C1042', '2')"),
            ('NDQ5660', "dbo.Actores_Cap('APP144', 'C1042', '2')"),
            ('NDQ5661', "dbo.Actores_Cap('APP145', 'C1042', '2')"),
            ('NDQ5662', "dbo.Actores_Cap('APP146', 'C1042', '2')"),
            ('NDQ5663', "dbo.Actores_Cap('APP150', 'C1042', '2')"),
            ('NDQ5664', "dbo.Actores_Cap('APP163', 'C1042', '2')"),
            ('NDQ5665', "dbo.Actores_Cap('APP165', 'C1042', '2')"),
            ('NDQ5666', "dbo.Actores_Cap('APP166', 'C1042', '2')"),
            ('NDQ5667', "dbo.Actores_Cap('APP168', 'C1042', '2')"),

        ]



    },
    "INDICADORESMULTIPLE": {
        "FACT_DISC_SNAPSHOT_MULTIPLES": [
            (
                '"0d-11A":"NDQ119", "12A-17A":"NDQ120", "18A-29A":"NDQ121", "30A-59A":"NDQ122", "60A+":"NDQ123"',
                "dbo.Multiples_ConCert('fisico', 'sensorial', 'N,R')"
            ),
            (
                '"0d-11A":"NDQ124", "12A-17A":"NDQ125", "18A-29A":"NDQ126", "30A-59A":"NDQ127", "60A+":"NDQ128"',
                "dbo.Multiples_ConCert('sensorial', 'físico', 'N,R')"
            ),
            (
                '"0d-11A":"NDQ129", "12A-17A":"NDQ130", "18A-29A":"NDQ131", "30A-59A":"NDQ132", "60A+":"NDQ133"',
                "dbo.Multiples_ConCert('fisico', 'mental', 'N,R')"
            ),
            (
                '"0d-11A":"NDQ134", "12A-17A":"NDQ135", "18A-29A":"NDQ136", "30A-59A":"NDQ137", "60A+":"NDQ138"',
                "dbo.Multiples_ConCert('mental', 'físico', 'N,R')"
            ),
            (
                '"0d-11A":"NDQ139", "12A-17A":"NDQ140", "18A-29A":"NDQ141", "30A-59A":"NDQ142", "60A+":"NDQ143"',
                "dbo.Multiples_ConCert('sensorial', 'mental', 'N,R')"
            ),
            (
                '"0d-11A":"NDQ144", "12A-17A":"NDQ145", "18A-29A":"NDQ146", "30A-59A":"NDQ147", "60A+":"NDQ148"',
                "dbo.Multiples_ConCert('mental', 'sensorial', 'N,R')"
            ),
            (
                '"0d-11A":"NDQ149", "12A-17A":"NDQ150", "18A-29A":"NDQ151", "30A-59A":"NDQ152", "60A+":"NDQ153"',
                "dbo.Multiples_Triple_ConCert('N,R')"
            ),
            (
                '"0d-11A":"NDQ154", "12A-17A":"NDQ155", "18A-29A":"NDQ156", "30A-59A":"NDQ157", "60A+":"NDQ158"',
                "dbo.Multiples_SinCert('fisico', 'sensorial', 'N,R')"
            ),
            (
                '"0d-11A":"NDQ159", "12A-17A":"NDQ160", "18A-29A":"NDQ161", "30A-59A":"NDQ162", "60A+":"NDQ163"',
                "dbo.Multiples_SinCert('sensorial', 'físico', 'N,R')"
            ),
            (
                '"0d-11A":"NDQ164", "12A-17A":"NDQ165", "18A-29A":"NDQ166", "30A-59A":"NDQ167", "60A+":"NDQ168"',
                "dbo.Multiples_SinCert('fisico', 'mental', 'N,R')"
            ),
            (
                '"0d-11A":"NDQ169", "12A-17A":"NDQ170", "18A-29A":"NDQ171", "30A-59A":"NDQ172", "60A+":"NDQ173"',
                "dbo.Multiples_SinCert('mental', 'físico', 'N,R')"
            ),
            (
                '"0d-11A":"NDQ174", "12A-17A":"NDQ175", "18A-29A":"NDQ176", "30A-59A":"NDQ177", "60A+":"NDQ178"',
                "dbo.Multiples_SinCert('sensorial', 'mental', 'N,R')"
            ),
            (
                '"0d-11A":"NDQ179", "12A-17A":"NDQ180", "18A-29A":"NDQ181", "30A-59A":"NDQ182", "60A+":"NDQ183"',
                "dbo.Multiples_SinCert('mental', 'sensorial', 'N,R')"
            ),
            (
                '"0d-11A":"NDQ184", "12A-17A":"NDQ185", "18A-29A":"NDQ186", "30A-59A":"NDQ187", "60A+":"NDQ188"',
                "dbo.Multiples_Triple_SinCert('N,R')"
            ),
            (
                '"0d-11A":"NDQ189", "12A-17A":"NDQ190", "18A-29A":"NDQ191", "30A-59A":"NDQ192", "60A+":"NDQ193"',
                "dbo.Multiples_EnRiesgo('fisico', 'sensorial', 'N,R')"
            ),
            (
                '"0d-11A":"NDQ194", "12A-17A":"NDQ195", "18A-29A":"NDQ196", "30A-59A":"NDQ197", "60A+":"NDQ198"',
                "dbo.Multiples_EnRiesgo('sensorial', 'físico', 'N,R')"
            ),
            (
                '"0d-11A":"NDQ199", "12A-17A":"NDQ200", "18A-29A":"NDQ201", "30A-59A":"NDQ202", "60A+":"NDQ203"',
                "dbo.Multiples_EnRiesgo('fisico', 'mental', 'N,R')"
            ),
            (
                '"0d-11A":"NDQ204", "12A-17A":"NDQ205", "18A-29A":"NDQ206", "30A-59A":"NDQ207", "60A+":"NDQ208"',
                "dbo.Multiples_EnRiesgo('mental', 'físico', 'N,R')"
            ),
            (
                '"0d-11A":"NDQ209", "12A-17A":"NDQ210", "18A-29A":"NDQ211", "30A-59A":"NDQ212", "60A+":"NDQ213"',
                "dbo.Multiples_EnRiesgo('sensorial', 'mental', 'N,R')"
            ),
            (
                '"0d-11A":"NDQ214", "12A-17A":"NDQ215", "18A-29A":"NDQ216", "30A-59A":"NDQ217", "60A+":"NDQ218"',
                "dbo.Multiples_EnRiesgo('mental', 'sensorial', 'N,R')"
            ),
            (
                '"0d-11A":"NDQ219", "12A-17A":"NDQ220", "18A-29A":"NDQ221", "30A-59A":"NDQ222", "60A+":"NDQ223"',
                "dbo.Multiples_Triple_EnRiesgo('N,R')"
            ),
            (
                '"0d-11A":"NDQ224", "12A-17A":"NDQ225", "18A-29A":"NDQ226", "30A-59A":"NDQ227", "60A+":"NDQ228"',
                "dbo.Multiples_ConCert('fisico', 'sensorial', 'N,C,R')"
            ),
            (
                '"0d-11A":"NDQ229", "12A-17A":"NDQ230", "18A-29A":"NDQ231", "30A-59A":"NDQ232", "60A+":"NDQ233"',
                "dbo.Multiples_ConCert('sensorial', 'físico', 'N,C,R')"
            ),
            (
                '"0d-11A":"NDQ234", "12A-17A":"NDQ235", "18A-29A":"NDQ236", "30A-59A":"NDQ237", "60A+":"NDQ238"',
                "dbo.Multiples_ConCert('fisico', 'mental', 'N,C,R')"
            ),
            (
                '"0d-11A":"NDQ239", "12A-17A":"NDQ240", "18A-29A":"NDQ241", "30A-59A":"NDQ242", "60A+":"NDQ243"',
                "dbo.Multiples_ConCert('mental', 'físico', 'N,C,R')"
            ),
            (
                '"0d-11A":"NDQ244", "12A-17A":"NDQ245", "18A-29A":"NDQ246", "30A-59A":"NDQ247", "60A+":"NDQ248"',
                "dbo.Multiples_ConCert('sensorial', 'mental', 'N,C,R')"
            ),
            (
                '"0d-11A":"NDQ249", "12A-17A":"NDQ250", "18A-29A":"NDQ251", "30A-59A":"NDQ252", "60A+":"NDQ253"',
                "dbo.Multiples_ConCert('mental', 'sensorial', 'N,C,R')"
            ),
            (
                '"0d-11A":"NDQ254", "12A-17A":"NDQ255", "18A-29A":"NDQ256", "30A-59A":"NDQ257", "60A+":"NDQ258"',
                "dbo.Multiples_Triple_ConCert('N,C,R')"
            ),
            (
                '"0d-11A":"NDQ259", "12A-17A":"NDQ260", "18A-29A":"NDQ261", "30A-59A":"NDQ262", "60A+":"NDQ263"',
                "dbo.Multiples_SinCert('fisico', 'sensorial', 'N,C,R')"
            ),
            (
                '"0d-11A":"NDQ264", "12A-17A":"NDQ265", "18A-29A":"NDQ266", "30A-59A":"NDQ267", "60A+":"NDQ268"',
                "dbo.Multiples_SinCert('sensorial', 'físico', 'N,C,R')"
            ),
            (
                '"0d-11A":"NDQ269", "12A-17A":"NDQ270", "18A-29A":"NDQ271", "30A-59A":"NDQ272", "60A+":"NDQ273"',
                "dbo.Multiples_SinCert('fisico', 'mental', 'N,C,R')"
            ),
            (
                '"0d-11A":"NDQ274", "12A-17A":"NDQ275", "18A-29A":"NDQ276", "30A-59A":"NDQ277", "60A+":"NDQ278"',
                "dbo.Multiples_SinCert('mental', 'físico', 'N,C,R')"
            ),
            (
                '"0d-11A":"NDQ279", "12A-17A":"NDQ280", "18A-29A":"NDQ281", "30A-59A":"NDQ282", "60A+":"NDQ283"',
                "dbo.Multiples_SinCert('sensorial', 'mental', 'N,C,R')"
            ),
            (
                '"0d-11A":"NDQ284", "12A-17A":"NDQ285", "18A-29A":"NDQ286", "30A-59A":"NDQ287", "60A+":"NDQ288"',
                "dbo.Multiples_SinCert('mental', 'sensorial', 'N,C,R')"
            ),
            (
                '"0d-11A":"NDQ289", "12A-17A":"NDQ290", "18A-29A":"NDQ291", "30A-59A":"NDQ292", "60A+":"NDQ293"',
                "dbo.Multiples_Triple_SinCert('N,C,R')"
            ),
            (
                '"0d-11A":"NDQ294", "12A-17A":"NDQ295", "18A-29A":"NDQ296", "30A-59A":"NDQ297", "60A+":"NDQ298"',
                "dbo.Multiples_EnRiesgo('fisico', 'sensorial', 'N,C,R')"
            ),
            (
                '"0d-11A":"NDQ299", "12A-17A":"NDQ300", "18A-29A":"NDQ301", "30A-59A":"NDQ302", "60A+":"NDQ303"',
                "dbo.Multiples_EnRiesgo('sensorial', 'físico', 'N,C,R')"
            ),
            (
                '"0d-11A":"NDQ304", "12A-17A":"NDQ305", "18A-29A":"NDQ306", "30A-59A":"NDQ307", "60A+":"NDQ308"',
                "dbo.Multiples_EnRiesgo('fisico', 'mental', 'N,C,R')"
            ),
            (
                '"0d-11A":"NDQ309", "12A-17A":"NDQ310", "18A-29A":"NDQ311", "30A-59A":"NDQ312", "60A+":"NDQ313"',
                "dbo.Multiples_EnRiesgo('mental', 'físico', 'N,C,R')"
            ),
            (
                '"0d-11A":"NDQ314", "12A-17A":"NDQ315", "18A-29A":"NDQ316", "30A-59A":"NDQ317", "60A+":"NDQ318"',
                "dbo.Multiples_EnRiesgo('sensorial', 'mental', 'N,C,R')"
            ),
            (
                '"0d-11A":"NDQ319", "12A-17A":"NDQ320", "18A-29A":"NDQ321", "30A-59A":"NDQ322", "60A+":"NDQ323"',
                "dbo.Multiples_EnRiesgo('mental', 'sensorial', 'N,C,R')"
            ),
            (
                '"0d-11A":"NDQ324", "12A-17A":"NDQ325", "18A-29A":"NDQ326", "30A-59A":"NDQ327", "60A+":"NDQ328"',
                "dbo.Multiples_Triple_EnRiesgo('N,C,R')"
            ),



        ],
        "FACT_DISC_SNAPSHOT_GRUPALES": [
            (
                '"0d-11A":"NDQ329", "12A-17A":"NDQ330", "18A-29A":"NDQ331", "30A-59A":"NDQ332", "60A+":"NDQ333"',
                "dbo.Grupal_ConCert('1', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ334", "12A-17A":"NDQ335", "18A-29A":"NDQ336", "30A-59A":"NDQ337", "60A+":"NDQ338"',
                "dbo.Grupal_ConCert('2', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ339", "12A-17A":"NDQ340", "18A-29A":"NDQ341", "30A-59A":"NDQ342", "60A+":"NDQ343"',
                "dbo.Grupal_ConCert('3', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ344", "12A-17A":"NDQ345", "18A-29A":"NDQ346", "30A-59A":"NDQ347", "60A+":"NDQ348"',
                "dbo.Grupal_ConCert('4', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ349", "12A-17A":"NDQ350", "18A-29A":"NDQ351", "30A-59A":"NDQ352", "60A+":"NDQ353"',
                "dbo.Grupal_ConCert('5', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ354", "12A-17A":"NDQ355", "18A-29A":"NDQ356", "30A-59A":"NDQ357", "60A+":"NDQ358"',
                "dbo.Grupal_ConCert('6', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ359", "12A-17A":"NDQ360", "18A-29A":"NDQ361", "30A-59A":"NDQ362", "60A+":"NDQ363"',
                "dbo.Grupal_SinCert('1', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ364", "12A-17A":"NDQ365", "18A-29A":"NDQ366", "30A-59A":"NDQ367", "60A+":"NDQ368"',
                "dbo.Grupal_SinCert('2', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ369", "12A-17A":"NDQ370", "18A-29A":"NDQ371", "30A-59A":"NDQ372", "60A+":"NDQ373"',
                "dbo.Grupal_SinCert('3', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ374", "12A-17A":"NDQ375", "18A-29A":"NDQ376", "30A-59A":"NDQ377", "60A+":"NDQ378"',
                "dbo.Grupal_SinCert('4', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ379", "12A-17A":"NDQ380", "18A-29A":"NDQ381", "30A-59A":"NDQ382", "60A+":"NDQ383"',
                "dbo.Grupal_SinCert('5', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ384", "12A-17A":"NDQ385", "18A-29A":"NDQ386", "30A-59A":"NDQ387", "60A+":"NDQ388"',
                "dbo.Grupal_SinCert('6', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ389", "12A-17A":"NDQ390", "18A-29A":"NDQ391", "30A-59A":"NDQ392", "60A+":"NDQ393"',
                "dbo.Grupal_EnRiesgo('1', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ394", "12A-17A":"NDQ395", "18A-29A":"NDQ396", "30A-59A":"NDQ397", "60A+":"NDQ398"',
                "dbo.Grupal_EnRiesgo('2', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ399", "12A-17A":"NDQ400", "18A-29A":"NDQ401", "30A-59A":"NDQ402", "60A+":"NDQ403"',
                "dbo.Grupal_EnRiesgo('3', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ404", "12A-17A":"NDQ405", "18A-29A":"NDQ406", "30A-59A":"NDQ407", "60A+":"NDQ408"',
                "dbo.Grupal_EnRiesgo('4', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ409", "12A-17A":"NDQ410", "18A-29A":"NDQ411", "30A-59A":"NDQ412", "60A+":"NDQ413"',
                "dbo.Grupal_EnRiesgo('5', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ414", "12A-17A":"NDQ415", "18A-29A":"NDQ416", "30A-59A":"NDQ417", "60A+":"NDQ418"',
                "dbo.Grupal_EnRiesgo('6', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ419", "12A-17A":"NDQ420", "18A-29A":"NDQ421", "30A-59A":"NDQ422", "60A+":"NDQ423"',
                "dbo.Grupal_ConCert('1', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ424", "12A-17A":"NDQ425", "18A-29A":"NDQ426", "30A-59A":"NDQ427", "60A+":"NDQ428"',
                "dbo.Grupal_ConCert('2', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ429", "12A-17A":"NDQ430", "18A-29A":"NDQ431", "30A-59A":"NDQ432", "60A+":"NDQ433"',
                "dbo.Grupal_ConCert('3', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ434", "12A-17A":"NDQ435", "18A-29A":"NDQ436", "30A-59A":"NDQ437", "60A+":"NDQ438"',
                "dbo.Grupal_ConCert('4', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ439", "12A-17A":"NDQ440", "18A-29A":"NDQ441", "30A-59A":"NDQ442", "60A+":"NDQ443"',
                "dbo.Grupal_ConCert('5', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ444", "12A-17A":"NDQ445", "18A-29A":"NDQ446", "30A-59A":"NDQ447", "60A+":"NDQ448"',
                "dbo.Grupal_ConCert('6', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ449", "12A-17A":"NDQ450", "18A-29A":"NDQ451", "30A-59A":"NDQ452", "60A+":"NDQ453"',
                "dbo.Grupal_SinCert('1', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ454", "12A-17A":"NDQ455", "18A-29A":"NDQ456", "30A-59A":"NDQ457", "60A+":"NDQ458"',
                "dbo.Grupal_SinCert('2', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ459", "12A-17A":"NDQ460", "18A-29A":"NDQ461", "30A-59A":"NDQ462", "60A+":"NDQ463"',
                "dbo.Grupal_SinCert('3', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ464", "12A-17A":"NDQ465", "18A-29A":"NDQ466", "30A-59A":"NDQ467", "60A+":"NDQ468"',
                "dbo.Grupal_SinCert('4', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ469", "12A-17A":"NDQ470", "18A-29A":"NDQ471", "30A-59A":"NDQ472", "60A+":"NDQ473"',
                "dbo.Grupal_SinCert('5', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ474", "12A-17A":"NDQ475", "18A-29A":"NDQ476", "30A-59A":"NDQ477", "60A+":"NDQ478"',
                "dbo.Grupal_SinCert('6', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ479", "12A-17A":"NDQ480", "18A-29A":"NDQ481", "30A-59A":"NDQ482", "60A+":"NDQ483"',
                "dbo.Grupal_EnRiesgo('1', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ484", "12A-17A":"NDQ485", "18A-29A":"NDQ486", "30A-59A":"NDQ487", "60A+":"NDQ488"',
                "dbo.Grupal_EnRiesgo('2', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ489", "12A-17A":"NDQ490", "18A-29A":"NDQ491", "30A-59A":"NDQ492", "60A+":"NDQ493"',
                "dbo.Grupal_EnRiesgo('3', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ494", "12A-17A":"NDQ495", "18A-29A":"NDQ496", "30A-59A":"NDQ497", "60A+":"NDQ498"',
                "dbo.Grupal_EnRiesgo('4', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ499", "12A-17A":"NDQ500", "18A-29A":"NDQ501", "30A-59A":"NDQ502", "60A+":"NDQ503"',
                "dbo.Grupal_EnRiesgo('5', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ504", "12A-17A":"NDQ505", "18A-29A":"NDQ506", "30A-59A":"NDQ507", "60A+":"NDQ508"',
                "dbo.Grupal_EnRiesgo('6', 'N,C,R');"
            ),



        ],
        "FACT_DISC_SNAPSHOT_AYUDATECN": [
            (
                '"0d-11A":"NDQ509", "12A-17A":"NDQ510", "18A-29A":"NDQ511", "30A-59A":"NDQ512", "60A+":"NDQ513"',
                "dbo.AyudaTecn_ConCert('fisico','99201,99201.01,99201.02,99202,99203,99204','1','N,R');"
            ),
            (
                '"0d-11A":"NDQ514", "12A-17A":"NDQ515", "18A-29A":"NDQ516", "30A-59A":"NDQ517", "60A+":"NDQ518"',
                "dbo.AyudaTecn_ConCert('sensorial','99201,99201.01,99201.02,99202,99203,99204','1','N,R');"
            ),
            (
                '"0d-11A":"NDQ519", "12A-17A":"NDQ520", "18A-29A":"NDQ521", "30A-59A":"NDQ522", "60A+":"NDQ523"',
                "dbo.AyudaTecn_ConCert('mental','99201,99201.01,99201.02,99202,99203,99204','1','N,R');"
            ),
            (
                '"0d-11A":"NDQ524", "12A-17A":"NDQ525", "18A-29A":"NDQ526", "30A-59A":"NDQ527", "60A+":"NDQ528"',
                "dbo.AyudaTecn_ConCert('fisico','97762,97703','2','N,R');"
            ),
            (
                '"0d-11A":"NDQ529", "12A-17A":"NDQ530", "18A-29A":"NDQ531", "30A-59A":"NDQ532", "60A+":"NDQ533"',
                "dbo.AyudaTecn_ConCert('sensorial','97762,97703','2','N,R');"
            ),
            (
                '"0d-11A":"NDQ534", "12A-17A":"NDQ535", "18A-29A":"NDQ536", "30A-59A":"NDQ537", "60A+":"NDQ538"',
                "dbo.AyudaTecn_ConCert('mental','97762,97703','2','N,R');"
            ),
            (
                '"0d-11A":"NDQ539", "12A-17A":"NDQ540", "18A-29A":"NDQ541", "30A-59A":"NDQ542", "60A+":"NDQ543"',
                "dbo.AyudaTecn_SinCert('fisico','99201,99201.01,99201.02,99202,99203,99204','1','N,R');"
            ),
            (
                '"0d-11A":"NDQ544", "12A-17A":"NDQ545", "18A-29A":"NDQ546", "30A-59A":"NDQ547", "60A+":"NDQ548"',
                "dbo.AyudaTecn_SinCert('sensorial','99201,99201.01,99201.02,99202,99203,99204','1','N,R');"
            ),
            (
                '"0d-11A":"NDQ549", "12A-17A":"NDQ550", "18A-29A":"NDQ551", "30A-59A":"NDQ552", "60A+":"NDQ553"',
                "dbo.AyudaTecn_SinCert('mental','99201,99201.01,99201.02,99202,99203,99204','1','N,R');"
            ),
            (
                '"0d-11A":"NDQ554", "12A-17A":"NDQ555", "18A-29A":"NDQ556", "30A-59A":"NDQ557", "60A+":"NDQ558"',
                "dbo.AyudaTecn_SinCert('fisico','97762,97703','2','N,R');"
            ),
            (
                '"0d-11A":"NDQ559", "12A-17A":"NDQ560", "18A-29A":"NDQ561", "30A-59A":"NDQ562", "60A+":"NDQ563"',
                "dbo.AyudaTecn_SinCert('sensorial','97762,97703','2','N,R');"
            ),
            (
                '"0d-11A":"NDQ564", "12A-17A":"NDQ565", "18A-29A":"NDQ566", "30A-59A":"NDQ567", "60A+":"NDQ568"',
                "dbo.AyudaTecn_SinCert('mental','97762,97703','2','N,R');"
            ),
            (
                '"0d-11A":"NDQ569", "12A-17A":"NDQ570", "18A-29A":"NDQ571", "30A-59A":"NDQ572", "60A+":"NDQ573"',
                "dbo.AyudaTecn_EnRiesgo('fisico','99201,99201.01,99201.02,99202,99203,99204','1','N,R');"
            ),
            (
                '"0d-11A":"NDQ574", "12A-17A":"NDQ575", "18A-29A":"NDQ576", "30A-59A":"NDQ577", "60A+":"NDQ578"',
                "dbo.AyudaTecn_EnRiesgo('sensorial','99201,99201.01,99201.02,99202,99203,99204','1','N,R');"
            ),
            (
                '"0d-11A":"NDQ579", "12A-17A":"NDQ580", "18A-29A":"NDQ581", "30A-59A":"NDQ582", "60A+":"NDQ583"',
                "dbo.AyudaTecn_EnRiesgo('mental','99201,99201.01,99201.02,99202,99203,99204','1','N,R');"
            ),
            (
                '"0d-11A":"NDQ584", "12A-17A":"NDQ585", "18A-29A":"NDQ586", "30A-59A":"NDQ587", "60A+":"NDQ588"',
                "dbo.AyudaTecn_EnRiesgo('fisico','97762,97703','2','N,R');"
            ),
            (
                '"0d-11A":"NDQ589", "12A-17A":"NDQ590", "18A-29A":"NDQ591", "30A-59A":"NDQ592", "60A+":"NDQ593"',
                "dbo.AyudaTecn_EnRiesgo('sensorial','97762,97703','2','N,R');"
            ),
            (
                '"0d-11A":"NDQ594", "12A-17A":"NDQ595", "18A-29A":"NDQ596", "30A-59A":"NDQ597", "60A+":"NDQ598"',
                "dbo.AyudaTecn_EnRiesgo('mental','97762,97703','2','N,R');"
            ),
            (
                '"0d-11A":"NDQ599", "12A-17A":"NDQ600", "18A-29A":"NDQ601", "30A-59A":"NDQ602", "60A+":"NDQ603"',
                "dbo.AyudaTecn_ConCert('fisico','99201,99201.01,99201.02,99202,99203,99204','1','N,C,R');"
            ),
            (
                '"0d-11A":"NDQ604", "12A-17A":"NDQ605", "18A-29A":"NDQ606", "30A-59A":"NDQ607", "60A+":"NDQ608"',
                "dbo.AyudaTecn_ConCert('sensorial','99201,99201.01,99201.02,99202,99203,99204','1','N,C,R');"
            ),
            (
                '"0d-11A":"NDQ609", "12A-17A":"NDQ610", "18A-29A":"NDQ611", "30A-59A":"NDQ612", "60A+":"NDQ613"',
                "dbo.AyudaTecn_ConCert('mental','99201,99201.01,99201.02,99202,99203,99204','1','N,C,R');"
            ),
            (
                '"0d-11A":"NDQ614", "12A-17A":"NDQ615", "18A-29A":"NDQ616", "30A-59A":"NDQ617", "60A+":"NDQ618"',
                "dbo.AyudaTecn_ConCert('fisico','97762,97703','2','N,C,R');"
            ),
            (
                '"0d-11A":"NDQ619", "12A-17A":"NDQ620", "18A-29A":"NDQ621", "30A-59A":"NDQ622", "60A+":"NDQ623"',
                "dbo.AyudaTecn_ConCert('sensorial','97762,97703','2','N,C,R');"
            ),
            (
                '"0d-11A":"NDQ624", "12A-17A":"NDQ625", "18A-29A":"NDQ626", "30A-59A":"NDQ627", "60A+":"NDQ628"',
                "dbo.AyudaTecn_ConCert('mental','97762,97703','2','N,C,R');"
            ),
            (
                '"0d-11A":"NDQ629", "12A-17A":"NDQ630", "18A-29A":"NDQ631", "30A-59A":"NDQ632", "60A+":"NDQ633"',
                "dbo.AyudaTecn_SinCert('fisico','99201,99201.01,99201.02,99202,99203,99204','1','N,C,R');"
            ),
            (
                '"0d-11A":"NDQ634", "12A-17A":"NDQ635", "18A-29A":"NDQ636", "30A-59A":"NDQ637", "60A+":"NDQ638"',
                "dbo.AyudaTecn_SinCert('sensorial','99201,99201.01,99201.02,99202,99203,99204','1','N,C,R');"
            ),
            (
                '"0d-11A":"NDQ639", "12A-17A":"NDQ640", "18A-29A":"NDQ641", "30A-59A":"NDQ642", "60A+":"NDQ643"',
                "dbo.AyudaTecn_SinCert('mental','99201,99201.01,99201.02,99202,99203,99204','1','N,C,R');"
            ),
            (
                '"0d-11A":"NDQ644", "12A-17A":"NDQ645", "18A-29A":"NDQ646", "30A-59A":"NDQ647", "60A+":"NDQ648"',
                "dbo.AyudaTecn_SinCert('fisico','97762,97703','2','N,C,R');"
            ),
            (
                '"0d-11A":"NDQ649", "12A-17A":"NDQ650", "18A-29A":"NDQ651", "30A-59A":"NDQ652", "60A+":"NDQ653"',
                "dbo.AyudaTecn_SinCert('sensorial','97762,97703','2','N,C,R');"
            ),
            (
                '"0d-11A":"NDQ654", "12A-17A":"NDQ655", "18A-29A":"NDQ656", "30A-59A":"NDQ657", "60A+":"NDQ658"',
                "dbo.AyudaTecn_SinCert('mental','97762,97703','2','N,C,R');"
            ),
            (
                '"0d-11A":"NDQ659", "12A-17A":"NDQ660", "18A-29A":"NDQ661", "30A-59A":"NDQ662", "60A+":"NDQ663"',
                "dbo.AyudaTecn_EnRiesgo('fisico','99201,99201.01,99201.02,99202,99203,99204','1','N,C,R');"
            ),
            (
                '"0d-11A":"NDQ664", "12A-17A":"NDQ665", "18A-29A":"NDQ666", "30A-59A":"NDQ667", "60A+":"NDQ668"',
                "dbo.AyudaTecn_EnRiesgo('sensorial','99201,99201.01,99201.02,99202,99203,99204','1','N,C,R');"
            ),
            (
                '"0d-11A":"NDQ669", "12A-17A":"NDQ670", "18A-29A":"NDQ671", "30A-59A":"NDQ672", "60A+":"NDQ673"',
                "dbo.AyudaTecn_EnRiesgo('mental','99201,99201.01,99201.02,99202,99203,99204','1','N,C,R');"
            ),
            (
                '"0d-11A":"NDQ674", "12A-17A":"NDQ675", "18A-29A":"NDQ676", "30A-59A":"NDQ677", "60A+":"NDQ678"',
                "dbo.AyudaTecn_EnRiesgo('fisico','97762,97703','2','N,C,R');"
            ),
            (
                '"0d-11A":"NDQ679", "12A-17A":"NDQ680", "18A-29A":"NDQ681", "30A-59A":"NDQ682", "60A+":"NDQ683"',
                "dbo.AyudaTecn_EnRiesgo('sensorial','97762,97703','2','N,C,R');"
            ),
            (
                '"0d-11A":"NDQ684", "12A-17A":"NDQ685", "18A-29A":"NDQ686", "30A-59A":"NDQ687", "60A+":"NDQ688"',
                "dbo.AyudaTecn_EnRiesgo('mental','97762,97703','2','N,C,R');"
            ),


        ],
        "FACT_DISC_SNAPSHOT_REHABFISIC_BL1": [
            (
                '"0d-11A":"NDQ689", "12A-17A":"NDQ690", "18A-29A":"NDQ691", "30A-59A":"NDQ692", "60A+":"NDQ693"',
                "dbo.Rehabilit_FSM_ConCert('A178,A1782,A800,B690,B91X,B941,C720,C721,D334,G041,G042,G048,G049,G050,G051,G052,G058,G114,G320,G35X,G360,G373,G820,G821,G822,G823,G824,G825,G834,G950,G951,G952,G958,G959,G971,M471,M480,M500,Q050,Q051,Q052,Q053,Q054,Q055,Q056,Q057,Q058,Q059,Q060,Q061,Q062,Q063,Q064,Q068,Q069,S140,S141,S240,S241,S340,S341,T093,T889', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ694", "12A-17A":"NDQ695", "18A-29A":"NDQ696", "30A-59A":"NDQ697", "60A+":"NDQ698"',
                "dbo.Rehabilit_FSM_ConCert('Q650,Q651,Q652,Q653,Q654,Q655,Q656,Q658,Q659,Q660,Q661,Q662,Q663,Q664,Q665,Q666,Q667,Q668,Q669,Q671,Q672,Q673,Q674,Q675,Q676,Q677,Q678,Q740,Q741,Q742,Q743,Q744,Q745,Q746,Q747,Q748,Q749,Q740,Q741,Q742,Q748,Q749,Q750,Q751,Q752,Q753,Q754,Q755,Q758,Q759,Q760,Q761,Q762,Q763,Q764,Q765,Q766,Q767,Q768,Q769,Q771,Q772,Q773,Q775,Q776,Q777,Q778,Q779,Q780,Q781,Q782,Q783,Q784,Q785,Q786,Q788,Q789,Q790,Q791,Q792,Q793,Q794,Q795,Q796,Q798,Q799', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ699", "12A-17A":"NDQ700", "18A-29A":"NDQ701", "30A-59A":"NDQ702", "60A+":"NDQ703"',
                "dbo.Rehabilit_FSM_ConCert('M150,M151,M152,M153,M154,M158,M159,M160,M161,M162,M163,M164,M165,M166,M167,M169,M170,M171,M172,M173,M174,M175,M179,M180,M181,M182,M183,M184,M185,M189,M190,M191,M192,M198,M199,M224,M235,M238,M239,M241,M470,M472,M478,M479', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ704", "12A-17A":"NDQ705", "18A-29A":"NDQ706", "30A-59A":"NDQ707", "60A+":"NDQ708"',
                "dbo.Rehabilit_FSM_ConCert('A321,B582,F83X,G000,G001,G002,G003,G008,G009,G000,G001,G002,G003,G008,G009,G010,G011,G012,G013,G014,G015,G016,G017,G018,G019,G020,G021,G022,G023,G024,G025,G026,G027,G028,G029,G030,G031,G032,G033,G034,G035,G036,G037,G038,G039,G040,G041,G042,G043,G044,G045,G046,G047,G048,G049,G042,G050,G051,G052,G053,G054,G055,G056,G057,G058,G059,G800,G801,G802,G803,G804,G808,G809,G820,G821,G822,G823,G824,G825,G826,G827,G828,G829,G910,G911,G912,G913,G914,G915,G916,G917,G918,G919,G910,G911,G912,G913,G918,G919,P900,P901,P902,P903,P904,P905,P906,P907,P908,P909,P940,P941,P942,P948,P949,Q000,Q001,Q002,Q003,Q004,Q005,Q006,Q007,Q008,Q009,Q010,Q011,Q012,Q013,Q014,Q015,Q016,Q017,Q018,Q019,Q020,Q021,Q022,Q023,Q024,Q025,Q026,Q027,Q028,Q029,Q030,Q031,Q032,Q033,Q034,Q035,Q036,Q037,Q038,Q039,Q040,Q041,Q042,Q043,Q044,Q045,Q046,Q047,Q048,Q049,Q070,Q071,Q072,Q073,Q074,Q075,Q076,Q077,Q078,Q079', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ709", "12A-17A":"NDQ710", "18A-29A":"NDQ711", "30A-59A":"NDQ712", "60A+":"NDQ713"',
                "dbo.Rehabilit_FSM_ConCert('Q900,Q901,Q902,Q909', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ714", "12A-17A":"NDQ715", "18A-29A":"NDQ716", "30A-59A":"NDQ717", "60A+":"NDQ718"',
                "dbo.Rehabilit_FSM_ConCert('S480,S481,S489,S580,S581,S589,S680,S681,S682,S683,S684,S688,S689,T050,T051,T052,T056,T058,T059,Z890,Z891,Z892,Z893,Z898', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ719", "12A-17A":"NDQ720", "18A-29A":"NDQ721", "30A-59A":"NDQ722", "60A+":"NDQ723"',
                "dbo.Rehabilit_FSM_ConCert('S780,S781,S789,S880,S881,S889,S980,S981,S982,S983,S984,T053,T054,T055,Z894,Z895,Z896,Z897', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ724", "12A-17A":"NDQ725", "18A-29A":"NDQ726", "30A-59A":"NDQ727", "60A+":"NDQ728"',
                "dbo.Rehabilit_FSM_ConCert('G733,G732,G731,G730,G729,G728,G724,G723,G721,G720,G719,G718,G713,G712,G711,G710,G709,G708,G702,G701,G700,G129,G121,G120', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ729", "12A-17A":"NDQ730", "18A-29A":"NDQ731", "30A-59A":"NDQ732", "60A+":"NDQ733"',
                "dbo.Rehabilit_FSM_ConCert('G500,G501,G508,G509,G510,G511,G512,G513,G514,G518,G519,G530,G531,G532,G533,G538,G540,G541,G542,G543,G544,G545,G546,G547,G548,G549,G550,G551,G552,G553,G558,G560,G561,G562,G563,G564,G568,G569,G570,G571,G572,G573,G574,G575,G576,G578,G579,G580,G587,G588,G589,G590,G598,G600,G601,G602,G603,G608,G609,G610,G611,G618,G619,G620,G621,G622,G628,G629,G630,G631,G632,G633,G634,G635,G636,G638,G64X,M501,M511,M541,M543,M544,M792,P140,P141,P142,P143,P148,P149,S142,S143,S242,S243,S342,S343,S344,S346,S440,S441,S442,S443,S444,S445,S447,S448,S449,S540,S541,S542,S543,S547,S548,S549,S640,S641,S642,S643,S644,S647,S648,S649,S840,S841,S842,S847,S848,S849,S940,S941,S942,S943,S947,S948,S949', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ734", "12A-17A":"NDQ735", "18A-29A":"NDQ736", "30A-59A":"NDQ737", "60A+":"NDQ738"',
                "dbo.Rehabilit_FSM_ConCert('G811,I600,I601,I602,I603,I604,I605,I606,I607,I608,I609,I610,I611,I612,I613,I614,I615,I616,I618,I619,I620,I621,I629,I630,I631,I632,I633,I634,I635,I636,I638,I639,I64X,I650,I651,I652,I653,I658,I659,I660,I661,I662,I663,I664,I668,I669,I670,I671,I672,I673,I674,I675,I676,I677,I678,I679,I680,I681,I682,I688,I694,I690,Q282', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ739", "12A-17A":"NDQ740", "18A-29A":"NDQ741", "30A-59A":"NDQ742", "60A+":"NDQ743"',
                "dbo.Rehabilit_FSM_ConCert('G20X,G210,G211,G212,G213,G214,G218,G219,G22X', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ744", "12A-17A":"NDQ745", "18A-29A":"NDQ746", "30A-59A":"NDQ747", "60A+":"NDQ748"',
                "dbo.Rehabilit_FSM_ConCert('M400,M401,M402,M403,M404,M405,M410,M411,M412,M413,M414,M415,M418,M419', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ749", "12A-17A":"NDQ750", "18A-29A":"NDQ751", "30A-59A":"NDQ752", "60A+":"NDQ753"',
                "dbo.Rehabilit_FSM_ConCert('M420,M421,M429,M45X,M491,M492,M493,M494,M495,M498', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ754", "12A-17A":"NDQ755", "18A-29A":"NDQ756", "30A-59A":"NDQ757", "60A+":"NDQ758"',
                "dbo.Rehabilit_FSM_ConCert('G992,M501,M502,M503,M508,M509,M510,M512,M513,M514,M518,M519,M530,M531,M532,M533,M538,M539', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ759", "12A-17A":"NDQ760", "18A-29A":"NDQ761", "30A-59A":"NDQ762", "60A+":"NDQ763"',
                "dbo.Rehabilit_FSM_ConCert('M542,M545,M546,M548,M549', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ764", "12A-17A":"NDQ765", "18A-29A":"NDQ766", "30A-59A":"NDQ767", "60A+":"NDQ768"',
                "dbo.Rehabilit_FSM_ConCert('M430,M431,M432', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ769", "12A-17A":"NDQ770", "18A-29A":"NDQ771", "30A-59A":"NDQ772", "60A+":"NDQ773"',
                "dbo.Rehabilit_FSM_ConCert('Q241,Q670,Q715,Q716,Q718,Q719,Q743,Q770,Q774', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ774", "12A-17A":"NDQ775", "18A-29A":"NDQ776", "30A-59A":"NDQ777", "60A+":"NDQ778"',
                "dbo.Rehabilit_FSM_ConCert('M910,M911,M912,M913,M918,M919,M920,M921,M922,M923,M924,M925,M926,M927,M928,M929,M930,M931,M932,M938,M939,Q720,Q721,Q722,Q723,Q724,Q725,Q726,Q727,Q728,Q729,Q730,Q731,Q738,Q710,Q711,Q712,Q713', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ779", "12A-17A":"NDQ780", "18A-29A":"NDQ781", "30A-59A":"NDQ782", "60A+":"NDQ783"',
                "dbo.Rehabilit_FSM_ConCert('M960,M961,M962,M963,M964,M968,M969', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ784", "12A-17A":"NDQ785", "18A-29A":"NDQ786", "30A-59A":"NDQ787", "60A+":"NDQ788"',
                "dbo.Rehabilit_FSM_ConCert('I090,I091,I092,I098,I099,I200,I201,I208,I209,I210,I211,I212,I213,I214,I219,I260,I269,I270,I271,I272,I278,I279,I280,I281,I288,I289,I430,I431,I432,I438,I500,I501,I509,I520,I521,I528,I690,I691,I692,I693,I694,I730,I731,I738,I739,I99X,Q200,Q201,Q202,Q203,Q204,Q205,Q206,Q208,Q209,Z950,Z951,Z952', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ789", "12A-17A":"NDQ790", "18A-29A":"NDQ791", "30A-59A":"NDQ792", "60A+":"NDQ793"',
                "dbo.Rehabilit_FSM_ConCert('J1281,J1289,J180,J181,J182,J188,J189,J1891,J1892,J208,J220,J221,J222,J223,J224,J225,J226,J227,J228,J229,J40X,J410,J411,J418,J42X,J430,J431,J432,J438,J439,J440,J441,J448,J449,J450,J451,J458,J459,J4591,J46X,J47X,J680,J681,J682,J683,J684,J688,J689,J700,J701,J702,J703,J704,J708,J709,J800,J801,J802,J803,J804,J805,J806,J807,J808,J809,J841,J848,J960,J961,J969,J988,J981,J990,J991,J998', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ794", "12A-17A":"NDQ795", "18A-29A":"NDQ796", "30A-59A":"NDQ797", "60A+":"NDQ798"',
                "dbo.Rehabilit_FSM_ConCert('N311,N312,N318,N319,N320,N941,N942,N948,R102,R309', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ799", "12A-17A":"NDQ800", "18A-29A":"NDQ801", "30A-59A":"NDQ802", "60A+":"NDQ803"',
                "dbo.Rehabilit_FSM_ConCert('N393,N394,R15X,R32X', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ804", "12A-17A":"NDQ805", "18A-29A":"NDQ806", "30A-59A":"NDQ807", "60A+":"NDQ808"',
                "dbo.Rehabilit_FSM_ConCert('N812,N814,N815,N816,N818,N819', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ809", "12A-17A":"NDQ810", "18A-29A":"NDQ811", "30A-59A":"NDQ812", "60A+":"NDQ813"',
                "dbo.Rehabilit_FSM_ConCert('S000,S090,S091,S092,S097,S098,S099,S100,S101,S107,S108,S109,S197,S198,S199,S200,S201,S202,S203,S204,S207,S208,S290,S297,S298,S299,S300,S301,S302,S307,S308,S309,S390,S396,S397,S398,S399,S400,S407,S408,S409,S497,S498,S499,S500,S501,S507,S508,S509,S597,S598,S599,S600,S601,S602,S607,S608,S609,S697,S698,S699,S700,S701,S707,S708,S709,S797,S798,S799,S800,S801,S807,S808,S809,S897,S898,S899,S900,S901,S902,S903,S907,S908,S909,S997,S998,S999,T000,T001,T002,T003,T006,T008,T009,T07X,T08X,T140,T141,T142,T143,T144,T145,T146,T147,T148,T149,T900,T901,T902,T903,T904,T905,T908,T909,T910,T911,T912,T913,T914,T915,T918,T919,T920,T921,T922,T923,T924,T925,T926,T928,T929,T930,T931,T932,T933,T934,T935,T936,T938,T939,T940,T941,T950,T951,T952,T953,T954,T958,T959,T96X,T97X,T980,T981,T982,T983', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ814", "12A-17A":"NDQ815", "18A-29A":"NDQ816", "30A-59A":"NDQ817", "60A+":"NDQ818"',
                "dbo.Rehabilit_FSM_ConCert('M000,M001,M002,M008,M009,M300,M301,M302,M303,M308,M310,M311,M312,M313,M314,M315,M316,M317,M318,M319,M320,M321,M328,M329,M330,M331,M332,M339,M340,M341,M342,M348,M349,M350,M351,M352,M353,M354,M355,M356,M357,M358,M359,M360,M361,M362,M363,M364,M368,M600,M601,M602,M608,M609,M610,M611,M612,M613,M614,M615,M619,M620,M621,M622,M623,M624,M625,M626,M628,M629,M630,M631,M632,M633,M638,M650,M651,M652,M653,M654,M658,M659,M660,M661,M662,M663,M664,M665,M670,M671,M672,M673,M674,M678,M679,M680,M688,M800,M801,M802,M803,M804,M805,M808,M809,M850,M851,M852,M853,M854,M855,M856,M858,M859', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ819", "12A-17A":"NDQ820", "18A-29A":"NDQ821", "30A-59A":"NDQ822", "60A+":"NDQ823"',
                "dbo.Rehabilit_FSM_ConCert('M200,M201,M202,M203,M204,M205,M206,M210,M211,M212,M213,M214,M215,M216,M217,M218,M219,M220,M221,M222,M223,M228,M229,M230,M231,M232,M233,M234,M236,M240,M242,M243,M244,M245,M246,M247,M248,M249,M250,M251,M252,M253,M254,M256,M257,M258,M259,M759', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ824", "12A-17A":"NDQ825", "18A-29A":"NDQ826", "30A-59A":"NDQ827", "60A+":"NDQ828"',
                "dbo.Rehabilit_FSM_ConCert('A239,M490,M491,M860,M861,M862,M863,M864,M865,M866,M868,M869,M890,M891,M892,M893,M894,M895,M896,M898,M899', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ829", "12A-17A":"NDQ830", "18A-29A":"NDQ831", "30A-59A":"NDQ832", "60A+":"NDQ833"',
                "dbo.Rehabilit_FSM_ConCert('M998,M999', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ834", "12A-17A":"NDQ835", "18A-29A":"NDQ836", "30A-59A":"NDQ837", "60A+":"NDQ838"',
                "dbo.Rehabilit_FSM_ConCert('I890,I891,I892,I893,I894,I895,I896,I897,I898,I899,I890,I891,I898,I899,I972,I978,I979', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ839", "12A-17A":"NDQ840", "18A-29A":"NDQ841", "30A-59A":"NDQ842", "60A+":"NDQ843"',
                "dbo.Rehabilit_FSM_ConCert('M6284', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ844", "12A-17A":"NDQ845", "18A-29A":"NDQ846", "30A-59A":"NDQ847", "60A+":"NDQ848"',
                "dbo.Rehabilit_FSM_ConCert('M255,M791,M797,R521,R522,R529', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ849", "12A-17A":"NDQ850", "18A-29A":"NDQ851", "30A-59A":"NDQ852", "60A+":"NDQ853"',
                "dbo.Rehabilit_FSM_ConCert('T200,T201,T202,T203,T204,T205,T206,T207,T208,T209,T200,T201,T202,T203,T204,T205,T206,T207,T210,T220,T230,T240,T250,T260,T270,T280,T290,T300,T310,T311,T312,T313,T314,T315,T316,T317,T318,T319,T310,T311,T312,T313,T314,T315,T316,T317,T318,T319,T320,T321,T322,T323,T324,T325,T326,T327,T328,T329,T320,T321,T322,T323,T324,T325,T326,T327,T328,T329,T330,T331,T332,T333,T334,T335,T336,T337,T338,T339,T330,T331,T332,T333,T334,T335,T336,T337,T338,T339,T340,T341,T342,T343,T344,T345,T346,T347,T348,T349,T340,T341,T342,T343,T344,T345,T346,T347,T348,T349,T350,T351,T352,T353,T354,T355,T356,T357,T358,T359,T350,T351,T352,T353,T354,T355,T356,T357', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ854", "12A-17A":"NDQ855", "18A-29A":"NDQ856", "30A-59A":"NDQ857", "60A+":"NDQ858"',
                "dbo.Rehabilit_FSM_Rehab_Alta('A178,A1782,A800,B690,B91X,B941,C720,C721,D334,G041,G042,G048,G049,G050,G051,G052,G058,G114,G320,G35X,G360,G373,G820,G821,G822,G823,G824,G825,G834,G950,G951,G952,G958,G959,G971,M471,M480,M500,Q050,Q051,Q052,Q053,Q054,Q055,Q056,Q057,Q058,Q059,Q060,Q061,Q062,Q063,Q064,Q068,Q069,S140,S141,S240,S241,S340,S341,T093,T889', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ859", "12A-17A":"NDQ860", "18A-29A":"NDQ861", "30A-59A":"NDQ862", "60A+":"NDQ863"',
                "dbo.Rehabilit_FSM_Rehab_Alta('Q650,Q651,Q652,Q653,Q654,Q655,Q656,Q658,Q659,Q660,Q661,Q662,Q663,Q664,Q665,Q666,Q667,Q668,Q669,Q671,Q672,Q673,Q674,Q675,Q676,Q677,Q678,Q740,Q741,Q742,Q743,Q744,Q745,Q746,Q747,Q748,Q749,Q740,Q741,Q742,Q748,Q749,Q750,Q751,Q752,Q753,Q754,Q755,Q758,Q759,Q760,Q761,Q762,Q763,Q764,Q765,Q766,Q767,Q768,Q769,Q771,Q772,Q773,Q775,Q776,Q777,Q778,Q779,Q780,Q781,Q782,Q783,Q784,Q785,Q786,Q788,Q789,Q790,Q791,Q792,Q793,Q794,Q795,Q796,Q798,Q799', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ864", "12A-17A":"NDQ865", "18A-29A":"NDQ866", "30A-59A":"NDQ867", "60A+":"NDQ868"',
                "dbo.Rehabilit_FSM_Rehab_Alta('M150,M151,M152,M153,M154,M158,M159,M160,M161,M162,M163,M164,M165,M166,M167,M169,M170,M171,M172,M173,M174,M175,M179,M180,M181,M182,M183,M184,M185,M189,M190,M191,M192,M198,M199,M224,M235,M238,M239,M241,M470,M472,M478,M479', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ869", "12A-17A":"NDQ870", "18A-29A":"NDQ871", "30A-59A":"NDQ872", "60A+":"NDQ873"',
                "dbo.Rehabilit_FSM_Rehab_Alta('A321,B582,F83X,G000,G001,G002,G003,G008,G009,G000,G001,G002,G003,G008,G009,G010,G011,G012,G013,G014,G015,G016,G017,G018,G019,G020,G021,G022,G023,G024,G025,G026,G027,G028,G029,G030,G031,G032,G033,G034,G035,G036,G037,G038,G039,G040,G041,G042,G043,G044,G045,G046,G047,G048,G049,G042,G050,G051,G052,G053,G054,G055,G056,G057,G058,G059,G800,G801,G802,G803,G804,G808,G809,G820,G821,G822,G823,G824,G825,G826,G827,G828,G829,G910,G911,G912,G913,G914,G915,G916,G917,G918,G919,G910,G911,G912,G913,G918,G919,P900,P901,P902,P903,P904,P905,P906,P907,P908,P909,P940,P941,P942,P948,P949,Q000,Q001,Q002,Q003,Q004,Q005,Q006,Q007,Q008,Q009,Q010,Q011,Q012,Q013,Q014,Q015,Q016,Q017,Q018,Q019,Q020,Q021,Q022,Q023,Q024,Q025,Q026,Q027,Q028,Q029,Q030,Q031,Q032,Q033,Q034,Q035,Q036,Q037,Q038,Q039,Q040,Q041,Q042,Q043,Q044,Q045,Q046,Q047,Q048,Q049,Q070,Q071,Q072,Q073,Q074,Q075,Q076,Q077,Q078,Q079', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ874", "12A-17A":"NDQ875", "18A-29A":"NDQ876", "30A-59A":"NDQ877", "60A+":"NDQ878"',
                "dbo.Rehabilit_FSM_Rehab_Alta('Q900,Q901,Q902,Q909', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ879", "12A-17A":"NDQ880", "18A-29A":"NDQ881", "30A-59A":"NDQ882", "60A+":"NDQ883"',
                "dbo.Rehabilit_FSM_Rehab_Alta('S480,S481,S489,S580,S581,S589,S680,S681,S682,S683,S684,S688,S689,T050,T051,T052,T056,T058,T059,Z890,Z891,Z892,Z893,Z898', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ884", "12A-17A":"NDQ885", "18A-29A":"NDQ886", "30A-59A":"NDQ887", "60A+":"NDQ888"',
                "dbo.Rehabilit_FSM_Rehab_Alta('S780,S781,S789,S880,S881,S889,S980,S981,S982,S983,S984,T053,T054,T055,Z894,Z895,Z896,Z897', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ889", "12A-17A":"NDQ890", "18A-29A":"NDQ891", "30A-59A":"NDQ892", "60A+":"NDQ893"',
                "dbo.Rehabilit_FSM_Rehab_Alta('G733,G732,G731,G730,G729,G728,G724,G723,G721,G720,G719,G718,G713,G712,G711,G710,G709,G708,G702,G701,G700,G129,G121,G120', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ894", "12A-17A":"NDQ895", "18A-29A":"NDQ896", "30A-59A":"NDQ897", "60A+":"NDQ898"',
                "dbo.Rehabilit_FSM_Rehab_Alta('G500,G501,G508,G509,G510,G511,G512,G513,G514,G518,G519,G530,G531,G532,G533,G538,G540,G541,G542,G543,G544,G545,G546,G547,G548,G549,G550,G551,G552,G553,G558,G560,G561,G562,G563,G564,G568,G569,G570,G571,G572,G573,G574,G575,G576,G578,G579,G580,G587,G588,G589,G590,G598,G600,G601,G602,G603,G608,G609,G610,G611,G618,G619,G620,G621,G622,G628,G629,G630,G631,G632,G633,G634,G635,G636,G638,G64X,M501,M511,M541,M543,M544,M792,P140,P141,P142,P143,P148,P149,S142,S143,S242,S243,S342,S343,S344,S346,S440,S441,S442,S443,S444,S445,S447,S448,S449,S540,S541,S542,S543,S547,S548,S549,S640,S641,S642,S643,S644,S647,S648,S649,S840,S841,S842,S847,S848,S849,S940,S941,S942,S943,S947,S948,S949', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ899", "12A-17A":"NDQ900", "18A-29A":"NDQ901", "30A-59A":"NDQ902", "60A+":"NDQ903"',
                "dbo.Rehabilit_FSM_Rehab_Alta('G811,I600,I601,I602,I603,I604,I605,I606,I607,I608,I609,I610,I611,I612,I613,I614,I615,I616,I618,I619,I620,I621,I629,I630,I631,I632,I633,I634,I635,I636,I638,I639,I64X,I650,I651,I652,I653,I658,I659,I660,I661,I662,I663,I664,I668,I669,I670,I671,I672,I673,I674,I675,I676,I677,I678,I679,I680,I681,I682,I688,I694,I690,Q282', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ904", "12A-17A":"NDQ905", "18A-29A":"NDQ906", "30A-59A":"NDQ907", "60A+":"NDQ908"',
                "dbo.Rehabilit_FSM_Rehab_Alta('G20X,G210,G211,G212,G213,G214,G218,G219,G22X', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ909", "12A-17A":"NDQ910", "18A-29A":"NDQ911", "30A-59A":"NDQ912", "60A+":"NDQ913"',
                "dbo.Rehabilit_FSM_Rehab_Alta('M400,M401,M402,M403,M404,M405,M410,M411,M412,M413,M414,M415,M418,M419', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ914", "12A-17A":"NDQ915", "18A-29A":"NDQ916", "30A-59A":"NDQ917", "60A+":"NDQ918"',
                "dbo.Rehabilit_FSM_Rehab_Alta('M420,M421,M429,M45X,M491,M492,M493,M494,M495,M498', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ919", "12A-17A":"NDQ920", "18A-29A":"NDQ921", "30A-59A":"NDQ922", "60A+":"NDQ923"',
                "dbo.Rehabilit_FSM_Rehab_Alta('G992,M501,M502,M503,M508,M509,M510,M512,M513,M514,M518,M519,M530,M531,M532,M533,M538,M539', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ924", "12A-17A":"NDQ925", "18A-29A":"NDQ926", "30A-59A":"NDQ927", "60A+":"NDQ928"',
                "dbo.Rehabilit_FSM_Rehab_Alta('M542,M545,M546,M548,M549', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ929", "12A-17A":"NDQ930", "18A-29A":"NDQ931", "30A-59A":"NDQ932", "60A+":"NDQ933"',
                "dbo.Rehabilit_FSM_Rehab_Alta('M430,M431,M432', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ934", "12A-17A":"NDQ935", "18A-29A":"NDQ936", "30A-59A":"NDQ937", "60A+":"NDQ938"',
                "dbo.Rehabilit_FSM_Rehab_Alta('Q241,Q670,Q715,Q716,Q718,Q719,Q743,Q770,Q774', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ939", "12A-17A":"NDQ940", "18A-29A":"NDQ941", "30A-59A":"NDQ942", "60A+":"NDQ943"',
                "dbo.Rehabilit_FSM_Rehab_Alta('M910,M911,M912,M913,M918,M919,M920,M921,M922,M923,M924,M925,M926,M927,M928,M929,M930,M931,M932,M938,M939,Q720,Q721,Q722,Q723,Q724,Q725,Q726,Q727,Q728,Q729,Q730,Q731,Q738,Q710,Q711,Q712,Q713', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ944", "12A-17A":"NDQ945", "18A-29A":"NDQ946", "30A-59A":"NDQ947", "60A+":"NDQ948"',
                "dbo.Rehabilit_FSM_Rehab_Alta('M960,M961,M962,M963,M964,M968,M969', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ949", "12A-17A":"NDQ950", "18A-29A":"NDQ951", "30A-59A":"NDQ952", "60A+":"NDQ953"',
                "dbo.Rehabilit_FSM_Rehab_Alta('I090,I091,I092,I098,I099,I200,I201,I208,I209,I210,I211,I212,I213,I214,I219,I260,I269,I270,I271,I272,I278,I279,I280,I281,I288,I289,I430,I431,I432,I438,I500,I501,I509,I520,I521,I528,I690,I691,I692,I693,I694,I730,I731,I738,I739,I99X,Q200,Q201,Q202,Q203,Q204,Q205,Q206,Q208,Q209,Z950,Z951,Z952', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ954", "12A-17A":"NDQ955", "18A-29A":"NDQ956", "30A-59A":"NDQ957", "60A+":"NDQ958"',
                "dbo.Rehabilit_FSM_Rehab_Alta('J1281,J1289,J180,J181,J182,J188,J189,J1891,J1892,J208,J220,J221,J222,J223,J224,J225,J226,J227,J228,J229,J40X,J410,J411,J418,J42X,J430,J431,J432,J438,J439,J440,J441,J448,J449,J450,J451,J458,J459,J4591,J46X,J47X,J680,J681,J682,J683,J684,J688,J689,J700,J701,J702,J703,J704,J708,J709,J800,J801,J802,J803,J804,J805,J806,J807,J808,J809,J841,J848,J960,J961,J969,J988,J981,J990,J991,J998', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ959", "12A-17A":"NDQ960", "18A-29A":"NDQ961", "30A-59A":"NDQ962", "60A+":"NDQ963"',
                "dbo.Rehabilit_FSM_Rehab_Alta('N311,N312,N318,N319,N320,N941,N942,N948,R102,R309', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ964", "12A-17A":"NDQ965", "18A-29A":"NDQ966", "30A-59A":"NDQ967", "60A+":"NDQ968"',
                "dbo.Rehabilit_FSM_Rehab_Alta('N393,N394,R15X,R32X', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ969", "12A-17A":"NDQ970", "18A-29A":"NDQ971", "30A-59A":"NDQ972", "60A+":"NDQ973"',
                "dbo.Rehabilit_FSM_Rehab_Alta('N812,N814,N815,N816,N818,N819', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ974", "12A-17A":"NDQ975", "18A-29A":"NDQ976", "30A-59A":"NDQ977", "60A+":"NDQ978"',
                "dbo.Rehabilit_FSM_Rehab_Alta('S000,S090,S091,S092,S097,S098,S099,S100,S101,S107,S108,S109,S197,S198,S199,S200,S201,S202,S203,S204,S207,S208,S290,S297,S298,S299,S300,S301,S302,S307,S308,S309,S390,S396,S397,S398,S399,S400,S407,S408,S409,S497,S498,S499,S500,S501,S507,S508,S509,S597,S598,S599,S600,S601,S602,S607,S608,S609,S697,S698,S699,S700,S701,S707,S708,S709,S797,S798,S799,S800,S801,S807,S808,S809,S897,S898,S899,S900,S901,S902,S903,S907,S908,S909,S997,S998,S999,T000,T001,T002,T003,T006,T008,T009,T07X,T08X,T140,T141,T142,T143,T144,T145,T146,T147,T148,T149,T900,T901,T902,T903,T904,T905,T908,T909,T910,T911,T912,T913,T914,T915,T918,T919,T920,T921,T922,T923,T924,T925,T926,T928,T929,T930,T931,T932,T933,T934,T935,T936,T938,T939,T940,T941,T950,T951,T952,T953,T954,T958,T959,T96X,T97X,T980,T981,T982,T983', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ979", "12A-17A":"NDQ980", "18A-29A":"NDQ981", "30A-59A":"NDQ982", "60A+":"NDQ983"',
                "dbo.Rehabilit_FSM_Rehab_Alta('M000,M001,M002,M008,M009,M300,M301,M302,M303,M308,M310,M311,M312,M313,M314,M315,M316,M317,M318,M319,M320,M321,M328,M329,M330,M331,M332,M339,M340,M341,M342,M348,M349,M350,M351,M352,M353,M354,M355,M356,M357,M358,M359,M360,M361,M362,M363,M364,M368,M600,M601,M602,M608,M609,M610,M611,M612,M613,M614,M615,M619,M620,M621,M622,M623,M624,M625,M626,M628,M629,M630,M631,M632,M633,M638,M650,M651,M652,M653,M654,M658,M659,M660,M661,M662,M663,M664,M665,M670,M671,M672,M673,M674,M678,M679,M680,M688,M800,M801,M802,M803,M804,M805,M808,M809,M850,M851,M852,M853,M854,M855,M856,M858,M859', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ984", "12A-17A":"NDQ985", "18A-29A":"NDQ986", "30A-59A":"NDQ987", "60A+":"NDQ988"',
                "dbo.Rehabilit_FSM_Rehab_Alta('M200,M201,M202,M203,M204,M205,M206,M210,M211,M212,M213,M214,M215,M216,M217,M218,M219,M220,M221,M222,M223,M228,M229,M230,M231,M232,M233,M234,M236,M240,M242,M243,M244,M245,M246,M247,M248,M249,M250,M251,M252,M253,M254,M256,M257,M258,M259,M759', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ989", "12A-17A":"NDQ990", "18A-29A":"NDQ991", "30A-59A":"NDQ992", "60A+":"NDQ993"',
                "dbo.Rehabilit_FSM_Rehab_Alta('A239,M490,M491,M860,M861,M862,M863,M864,M865,M866,M868,M869,M890,M891,M892,M893,M894,M895,M896,M898,M899', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ994", "12A-17A":"NDQ995", "18A-29A":"NDQ996", "30A-59A":"NDQ997", "60A+":"NDQ998"',
                "dbo.Rehabilit_FSM_Rehab_Alta('M998,M999', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ999", "12A-17A":"NDQ1000", "18A-29A":"NDQ1001", "30A-59A":"NDQ1002", "60A+":"NDQ1003"',
                "dbo.Rehabilit_FSM_Rehab_Alta('I890,I891,I892,I893,I894,I895,I896,I897,I898,I899,I890,I891,I898,I899,I972,I978,I979', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1004", "12A-17A":"NDQ1005", "18A-29A":"NDQ1006", "30A-59A":"NDQ1007", "60A+":"NDQ1008"',
                "dbo.Rehabilit_FSM_Rehab_Alta('M6284', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1009", "12A-17A":"NDQ1010", "18A-29A":"NDQ1011", "30A-59A":"NDQ1012", "60A+":"NDQ1013"',
                "dbo.Rehabilit_FSM_Rehab_Alta('M255,M791,M797,R521,R522,R529', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1014", "12A-17A":"NDQ1015", "18A-29A":"NDQ1016", "30A-59A":"NDQ1017", "60A+":"NDQ1018"',
                "dbo.Rehabilit_FSM_Rehab_Alta('T200,T201,T202,T203,T204,T205,T206,T207,T208,T209,T200,T201,T202,T203,T204,T205,T206,T207,T210,T220,T230,T240,T250,T260,T270,T280,T290,T300,T310,T311,T312,T313,T314,T315,T316,T317,T318,T319,T310,T311,T312,T313,T314,T315,T316,T317,T318,T319,T320,T321,T322,T323,T324,T325,T326,T327,T328,T329,T320,T321,T322,T323,T324,T325,T326,T327,T328,T329,T330,T331,T332,T333,T334,T335,T336,T337,T338,T339,T330,T331,T332,T333,T334,T335,T336,T337,T338,T339,T340,T341,T342,T343,T344,T345,T346,T347,T348,T349,T340,T341,T342,T343,T344,T345,T346,T347,T348,T349,T350,T351,T352,T353,T354,T355,T356,T357,T358,T359,T350,T351,T352,T353,T354,T355,T356,T357', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1019", "12A-17A":"NDQ1020", "18A-29A":"NDQ1021", "30A-59A":"NDQ1022", "60A+":"NDQ1023"',
                "dbo.Rehabilit_FSM_SinCert('A178,A1782,A800,B690,B91X,B941,C720,C721,D334,G041,G042,G048,G049,G050,G051,G052,G058,G114,G320,G35X,G360,G373,G820,G821,G822,G823,G824,G825,G834,G950,G951,G952,G958,G959,G971,M471,M480,M500,Q050,Q051,Q052,Q053,Q054,Q055,Q056,Q057,Q058,Q059,Q060,Q061,Q062,Q063,Q064,Q068,Q069,S140,S141,S240,S241,S340,S341,T093,T889', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1024", "12A-17A":"NDQ1025", "18A-29A":"NDQ1026", "30A-59A":"NDQ1027", "60A+":"NDQ1028"',
                "dbo.Rehabilit_FSM_SinCert('Q650,Q651,Q652,Q653,Q654,Q655,Q656,Q658,Q659,Q660,Q661,Q662,Q663,Q664,Q665,Q666,Q667,Q668,Q669,Q671,Q672,Q673,Q674,Q675,Q676,Q677,Q678,Q740,Q741,Q742,Q743,Q744,Q745,Q746,Q747,Q748,Q749,Q740,Q741,Q742,Q748,Q749,Q750,Q751,Q752,Q753,Q754,Q755,Q758,Q759,Q760,Q761,Q762,Q763,Q764,Q765,Q766,Q767,Q768,Q769,Q771,Q772,Q773,Q775,Q776,Q777,Q778,Q779,Q780,Q781,Q782,Q783,Q784,Q785,Q786,Q788,Q789,Q790,Q791,Q792,Q793,Q794,Q795,Q796,Q798,Q799', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1029", "12A-17A":"NDQ1030", "18A-29A":"NDQ1031", "30A-59A":"NDQ1032", "60A+":"NDQ1033"',
                "dbo.Rehabilit_FSM_SinCert('M150,M151,M152,M153,M154,M158,M159,M160,M161,M162,M163,M164,M165,M166,M167,M169,M170,M171,M172,M173,M174,M175,M179,M180,M181,M182,M183,M184,M185,M189,M190,M191,M192,M198,M199,M224,M235,M238,M239,M241,M470,M472,M478,M479', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1034", "12A-17A":"NDQ1035", "18A-29A":"NDQ1036", "30A-59A":"NDQ1037", "60A+":"NDQ1038"',
                "dbo.Rehabilit_FSM_SinCert('A321,B582,F83X,G000,G001,G002,G003,G008,G009,G000,G001,G002,G003,G008,G009,G010,G011,G012,G013,G014,G015,G016,G017,G018,G019,G020,G021,G022,G023,G024,G025,G026,G027,G028,G029,G030,G031,G032,G033,G034,G035,G036,G037,G038,G039,G040,G041,G042,G043,G044,G045,G046,G047,G048,G049,G042,G050,G051,G052,G053,G054,G055,G056,G057,G058,G059,G800,G801,G802,G803,G804,G808,G809,G820,G821,G822,G823,G824,G825,G826,G827,G828,G829,G910,G911,G912,G913,G914,G915,G916,G917,G918,G919,G910,G911,G912,G913,G918,G919,P900,P901,P902,P903,P904,P905,P906,P907,P908,P909,P940,P941,P942,P948,P949,Q000,Q001,Q002,Q003,Q004,Q005,Q006,Q007,Q008,Q009,Q010,Q011,Q012,Q013,Q014,Q015,Q016,Q017,Q018,Q019,Q020,Q021,Q022,Q023,Q024,Q025,Q026,Q027,Q028,Q029,Q030,Q031,Q032,Q033,Q034,Q035,Q036,Q037,Q038,Q039,Q040,Q041,Q042,Q043,Q044,Q045,Q046,Q047,Q048,Q049,Q070,Q071,Q072,Q073,Q074,Q075,Q076,Q077,Q078,Q079', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1039", "12A-17A":"NDQ1040", "18A-29A":"NDQ1041", "30A-59A":"NDQ1042", "60A+":"NDQ1043"',
                "dbo.Rehabilit_FSM_SinCert('Q900,Q901,Q902,Q909', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1044", "12A-17A":"NDQ1045", "18A-29A":"NDQ1046", "30A-59A":"NDQ1047", "60A+":"NDQ1048"',
                "dbo.Rehabilit_FSM_SinCert('S480,S481,S489,S580,S581,S589,S680,S681,S682,S683,S684,S688,S689,T050,T051,T052,T056,T058,T059,Z890,Z891,Z892,Z893,Z898', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1049", "12A-17A":"NDQ1050", "18A-29A":"NDQ1051", "30A-59A":"NDQ1052", "60A+":"NDQ1053"',
                "dbo.Rehabilit_FSM_SinCert('S780,S781,S789,S880,S881,S889,S980,S981,S982,S983,S984,T053,T054,T055,Z894,Z895,Z896,Z897', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1054", "12A-17A":"NDQ1055", "18A-29A":"NDQ1056", "30A-59A":"NDQ1057", "60A+":"NDQ1058"',
                "dbo.Rehabilit_FSM_SinCert('G733,G732,G731,G730,G729,G728,G724,G723,G721,G720,G719,G718,G713,G712,G711,G710,G709,G708,G702,G701,G700,G129,G121,G120', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1059", "12A-17A":"NDQ1060", "18A-29A":"NDQ1061", "30A-59A":"NDQ1062", "60A+":"NDQ1063"',
                "dbo.Rehabilit_FSM_SinCert('G500,G501,G508,G509,G510,G511,G512,G513,G514,G518,G519,G530,G531,G532,G533,G538,G540,G541,G542,G543,G544,G545,G546,G547,G548,G549,G550,G551,G552,G553,G558,G560,G561,G562,G563,G564,G568,G569,G570,G571,G572,G573,G574,G575,G576,G578,G579,G580,G587,G588,G589,G590,G598,G600,G601,G602,G603,G608,G609,G610,G611,G618,G619,G620,G621,G622,G628,G629,G630,G631,G632,G633,G634,G635,G636,G638,G64X,M501,M511,M541,M543,M544,M792,P140,P141,P142,P143,P148,P149,S142,S143,S242,S243,S342,S343,S344,S346,S440,S441,S442,S443,S444,S445,S447,S448,S449,S540,S541,S542,S543,S547,S548,S549,S640,S641,S642,S643,S644,S647,S648,S649,S840,S841,S842,S847,S848,S849,S940,S941,S942,S943,S947,S948,S949', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1064", "12A-17A":"NDQ1065", "18A-29A":"NDQ1066", "30A-59A":"NDQ1067", "60A+":"NDQ1068"',
                "dbo.Rehabilit_FSM_SinCert('G811,I600,I601,I602,I603,I604,I605,I606,I607,I608,I609,I610,I611,I612,I613,I614,I615,I616,I618,I619,I620,I621,I629,I630,I631,I632,I633,I634,I635,I636,I638,I639,I64X,I650,I651,I652,I653,I658,I659,I660,I661,I662,I663,I664,I668,I669,I670,I671,I672,I673,I674,I675,I676,I677,I678,I679,I680,I681,I682,I688,I694,I690,Q282', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1069", "12A-17A":"NDQ1070", "18A-29A":"NDQ1071", "30A-59A":"NDQ1072", "60A+":"NDQ1073"',
                "dbo.Rehabilit_FSM_SinCert('G20X,G210,G211,G212,G213,G214,G218,G219,G22X', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1074", "12A-17A":"NDQ1075", "18A-29A":"NDQ1076", "30A-59A":"NDQ1077", "60A+":"NDQ1078"',
                "dbo.Rehabilit_FSM_SinCert('M400,M401,M402,M403,M404,M405,M410,M411,M412,M413,M414,M415,M418,M419', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1079", "12A-17A":"NDQ1080", "18A-29A":"NDQ1081", "30A-59A":"NDQ1082", "60A+":"NDQ1083"',
                "dbo.Rehabilit_FSM_SinCert('M420,M421,M429,M45X,M491,M492,M493,M494,M495,M498', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1084", "12A-17A":"NDQ1085", "18A-29A":"NDQ1086", "30A-59A":"NDQ1087", "60A+":"NDQ1088"',
                "dbo.Rehabilit_FSM_SinCert('G992,M501,M502,M503,M508,M509,M510,M512,M513,M514,M518,M519,M530,M531,M532,M533,M538,M539', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1089", "12A-17A":"NDQ1090", "18A-29A":"NDQ1091", "30A-59A":"NDQ1092", "60A+":"NDQ1093"',
                "dbo.Rehabilit_FSM_SinCert('M542,M545,M546,M548,M549', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1094", "12A-17A":"NDQ1095", "18A-29A":"NDQ1096", "30A-59A":"NDQ1097", "60A+":"NDQ1098"',
                "dbo.Rehabilit_FSM_SinCert('M430,M431,M432', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1099", "12A-17A":"NDQ1100", "18A-29A":"NDQ1101", "30A-59A":"NDQ1102", "60A+":"NDQ1103"',
                "dbo.Rehabilit_FSM_SinCert('Q241,Q670,Q715,Q716,Q718,Q719,Q743,Q770,Q774', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1104", "12A-17A":"NDQ1105", "18A-29A":"NDQ1106", "30A-59A":"NDQ1107", "60A+":"NDQ1108"',
                "dbo.Rehabilit_FSM_SinCert('M910,M911,M912,M913,M918,M919,M920,M921,M922,M923,M924,M925,M926,M927,M928,M929,M930,M931,M932,M938,M939,Q720,Q721,Q722,Q723,Q724,Q725,Q726,Q727,Q728,Q729,Q730,Q731,Q738,Q710,Q711,Q712,Q713', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1109", "12A-17A":"NDQ1110", "18A-29A":"NDQ1111", "30A-59A":"NDQ1112", "60A+":"NDQ1113"',
                "dbo.Rehabilit_FSM_SinCert('M960,M961,M962,M963,M964,M968,M969', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1114", "12A-17A":"NDQ1115", "18A-29A":"NDQ1116", "30A-59A":"NDQ1117", "60A+":"NDQ1118"',
                "dbo.Rehabilit_FSM_SinCert('I090,I091,I092,I098,I099,I200,I201,I208,I209,I210,I211,I212,I213,I214,I219,I260,I269,I270,I271,I272,I278,I279,I280,I281,I288,I289,I430,I431,I432,I438,I500,I501,I509,I520,I521,I528,I690,I691,I692,I693,I694,I730,I731,I738,I739,I99X,Q200,Q201,Q202,Q203,Q204,Q205,Q206,Q208,Q209,Z950,Z951,Z952', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1119", "12A-17A":"NDQ1120", "18A-29A":"NDQ1121", "30A-59A":"NDQ1122", "60A+":"NDQ1123"',
                "dbo.Rehabilit_FSM_SinCert('J1281,J1289,J180,J181,J182,J188,J189,J1891,J1892,J208,J220,J221,J222,J223,J224,J225,J226,J227,J228,J229,J40X,J410,J411,J418,J42X,J430,J431,J432,J438,J439,J440,J441,J448,J449,J450,J451,J458,J459,J4591,J46X,J47X,J680,J681,J682,J683,J684,J688,J689,J700,J701,J702,J703,J704,J708,J709,J800,J801,J802,J803,J804,J805,J806,J807,J808,J809,J841,J848,J960,J961,J969,J988,J981,J990,J991,J998', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1124", "12A-17A":"NDQ1125", "18A-29A":"NDQ1126", "30A-59A":"NDQ1127", "60A+":"NDQ1128"',
                "dbo.Rehabilit_FSM_SinCert('N311,N312,N318,N319,N320,N941,N942,N948,R102,R309', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1129", "12A-17A":"NDQ1130", "18A-29A":"NDQ1131", "30A-59A":"NDQ1132", "60A+":"NDQ1133"',
                "dbo.Rehabilit_FSM_SinCert('N393,N394,R15X,R32X', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1134", "12A-17A":"NDQ1135", "18A-29A":"NDQ1136", "30A-59A":"NDQ1137", "60A+":"NDQ1138"',
                "dbo.Rehabilit_FSM_SinCert('N812,N814,N815,N816,N818,N819', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1139", "12A-17A":"NDQ1140", "18A-29A":"NDQ1141", "30A-59A":"NDQ1142", "60A+":"NDQ1143"',
                "dbo.Rehabilit_FSM_SinCert('S000,S090,S091,S092,S097,S098,S099,S100,S101,S107,S108,S109,S197,S198,S199,S200,S201,S202,S203,S204,S207,S208,S290,S297,S298,S299,S300,S301,S302,S307,S308,S309,S390,S396,S397,S398,S399,S400,S407,S408,S409,S497,S498,S499,S500,S501,S507,S508,S509,S597,S598,S599,S600,S601,S602,S607,S608,S609,S697,S698,S699,S700,S701,S707,S708,S709,S797,S798,S799,S800,S801,S807,S808,S809,S897,S898,S899,S900,S901,S902,S903,S907,S908,S909,S997,S998,S999,T000,T001,T002,T003,T006,T008,T009,T07X,T08X,T140,T141,T142,T143,T144,T145,T146,T147,T148,T149,T900,T901,T902,T903,T904,T905,T908,T909,T910,T911,T912,T913,T914,T915,T918,T919,T920,T921,T922,T923,T924,T925,T926,T928,T929,T930,T931,T932,T933,T934,T935,T936,T938,T939,T940,T941,T950,T951,T952,T953,T954,T958,T959,T96X,T97X,T980,T981,T982,T983', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1144", "12A-17A":"NDQ1145", "18A-29A":"NDQ1146", "30A-59A":"NDQ1147", "60A+":"NDQ1148"',
                "dbo.Rehabilit_FSM_SinCert('M000,M001,M002,M008,M009,M300,M301,M302,M303,M308,M310,M311,M312,M313,M314,M315,M316,M317,M318,M319,M320,M321,M328,M329,M330,M331,M332,M339,M340,M341,M342,M348,M349,M350,M351,M352,M353,M354,M355,M356,M357,M358,M359,M360,M361,M362,M363,M364,M368,M600,M601,M602,M608,M609,M610,M611,M612,M613,M614,M615,M619,M620,M621,M622,M623,M624,M625,M626,M628,M629,M630,M631,M632,M633,M638,M650,M651,M652,M653,M654,M658,M659,M660,M661,M662,M663,M664,M665,M670,M671,M672,M673,M674,M678,M679,M680,M688,M800,M801,M802,M803,M804,M805,M808,M809,M850,M851,M852,M853,M854,M855,M856,M858,M859', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1149", "12A-17A":"NDQ1150", "18A-29A":"NDQ1151", "30A-59A":"NDQ1152", "60A+":"NDQ1153"',
                "dbo.Rehabilit_FSM_SinCert('M200,M201,M202,M203,M204,M205,M206,M210,M211,M212,M213,M214,M215,M216,M217,M218,M219,M220,M221,M222,M223,M228,M229,M230,M231,M232,M233,M234,M236,M240,M242,M243,M244,M245,M246,M247,M248,M249,M250,M251,M252,M253,M254,M256,M257,M258,M259,M759', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1154", "12A-17A":"NDQ1155", "18A-29A":"NDQ1156", "30A-59A":"NDQ1157", "60A+":"NDQ1158"',
                "dbo.Rehabilit_FSM_SinCert('A239,M490,M491,M860,M861,M862,M863,M864,M865,M866,M868,M869,M890,M891,M892,M893,M894,M895,M896,M898,M899', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1159", "12A-17A":"NDQ1160", "18A-29A":"NDQ1161", "30A-59A":"NDQ1162", "60A+":"NDQ1163"',
                "dbo.Rehabilit_FSM_SinCert('M998,M999', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1164", "12A-17A":"NDQ1165", "18A-29A":"NDQ1166", "30A-59A":"NDQ1167", "60A+":"NDQ1168"',
                "dbo.Rehabilit_FSM_SinCert('I890,I891,I892,I893,I894,I895,I896,I897,I898,I899,I890,I891,I898,I899,I972,I978,I979', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1169", "12A-17A":"NDQ1170", "18A-29A":"NDQ1171", "30A-59A":"NDQ1172", "60A+":"NDQ1173"',
                "dbo.Rehabilit_FSM_SinCert('M6284', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1174", "12A-17A":"NDQ1175", "18A-29A":"NDQ1176", "30A-59A":"NDQ1177", "60A+":"NDQ1178"',
                "dbo.Rehabilit_FSM_SinCert('M255,M791,M797,R521,R522,R529', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1179", "12A-17A":"NDQ1180", "18A-29A":"NDQ1181", "30A-59A":"NDQ1182", "60A+":"NDQ1183"',
                "dbo.Rehabilit_FSM_SinCert('T200,T201,T202,T203,T204,T205,T206,T207,T208,T209,T200,T201,T202,T203,T204,T205,T206,T207,T210,T220,T230,T240,T250,T260,T270,T280,T290,T300,T310,T311,T312,T313,T314,T315,T316,T317,T318,T319,T310,T311,T312,T313,T314,T315,T316,T317,T318,T319,T320,T321,T322,T323,T324,T325,T326,T327,T328,T329,T320,T321,T322,T323,T324,T325,T326,T327,T328,T329,T330,T331,T332,T333,T334,T335,T336,T337,T338,T339,T330,T331,T332,T333,T334,T335,T336,T337,T338,T339,T340,T341,T342,T343,T344,T345,T346,T347,T348,T349,T340,T341,T342,T343,T344,T345,T346,T347,T348,T349,T350,T351,T352,T353,T354,T355,T356,T357,T358,T359,T350,T351,T352,T353,T354,T355,T356,T357', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1184", "12A-17A":"NDQ1185", "18A-29A":"NDQ1186", "30A-59A":"NDQ1187", "60A+":"NDQ1188"',
                "dbo.Rehabilit_FSM_ServEval('A178,A1782,A800,B690,B91X,B941,C720,C721,D334,G041,G042,G048,G049,G050,G051,G052,G058,G114,G320,G35X,G360,G373,G820,G821,G822,G823,G824,G825,G834,G950,G951,G952,G958,G959,G971,M471,M480,M500,Q050,Q051,Q052,Q053,Q054,Q055,Q056,Q057,Q058,Q059,Q060,Q061,Q062,Q063,Q064,Q068,Q069,S140,S141,S240,S241,S340,S341,T093,T889', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1189", "12A-17A":"NDQ1190", "18A-29A":"NDQ1191", "30A-59A":"NDQ1192", "60A+":"NDQ1193"',
                "dbo.Rehabilit_FSM_ServEval('Q650,Q651,Q652,Q653,Q654,Q655,Q656,Q658,Q659,Q660,Q661,Q662,Q663,Q664,Q665,Q666,Q667,Q668,Q669,Q671,Q672,Q673,Q674,Q675,Q676,Q677,Q678,Q740,Q741,Q742,Q743,Q744,Q745,Q746,Q747,Q748,Q749,Q740,Q741,Q742,Q748,Q749,Q750,Q751,Q752,Q753,Q754,Q755,Q758,Q759,Q760,Q761,Q762,Q763,Q764,Q765,Q766,Q767,Q768,Q769,Q771,Q772,Q773,Q775,Q776,Q777,Q778,Q779,Q780,Q781,Q782,Q783,Q784,Q785,Q786,Q788,Q789,Q790,Q791,Q792,Q793,Q794,Q795,Q796,Q798,Q799', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1194", "12A-17A":"NDQ1195", "18A-29A":"NDQ1196", "30A-59A":"NDQ1197", "60A+":"NDQ1198"',
                "dbo.Rehabilit_FSM_ServEval('M150,M151,M152,M153,M154,M158,M159,M160,M161,M162,M163,M164,M165,M166,M167,M169,M170,M171,M172,M173,M174,M175,M179,M180,M181,M182,M183,M184,M185,M189,M190,M191,M192,M198,M199,M224,M235,M238,M239,M241,M470,M472,M478,M479', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1199", "12A-17A":"NDQ1200", "18A-29A":"NDQ1201", "30A-59A":"NDQ1202", "60A+":"NDQ1203"',
                "dbo.Rehabilit_FSM_ServEval('A321,B582,F83X,G000,G001,G002,G003,G008,G009,G000,G001,G002,G003,G008,G009,G010,G011,G012,G013,G014,G015,G016,G017,G018,G019,G020,G021,G022,G023,G024,G025,G026,G027,G028,G029,G030,G031,G032,G033,G034,G035,G036,G037,G038,G039,G040,G041,G042,G043,G044,G045,G046,G047,G048,G049,G042,G050,G051,G052,G053,G054,G055,G056,G057,G058,G059,G800,G801,G802,G803,G804,G808,G809,G820,G821,G822,G823,G824,G825,G826,G827,G828,G829,G910,G911,G912,G913,G914,G915,G916,G917,G918,G919,G910,G911,G912,G913,G918,G919,P900,P901,P902,P903,P904,P905,P906,P907,P908,P909,P940,P941,P942,P948,P949,Q000,Q001,Q002,Q003,Q004,Q005,Q006,Q007,Q008,Q009,Q010,Q011,Q012,Q013,Q014,Q015,Q016,Q017,Q018,Q019,Q020,Q021,Q022,Q023,Q024,Q025,Q026,Q027,Q028,Q029,Q030,Q031,Q032,Q033,Q034,Q035,Q036,Q037,Q038,Q039,Q040,Q041,Q042,Q043,Q044,Q045,Q046,Q047,Q048,Q049,Q070,Q071,Q072,Q073,Q074,Q075,Q076,Q077,Q078,Q079', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1204", "12A-17A":"NDQ1205", "18A-29A":"NDQ1206", "30A-59A":"NDQ1207", "60A+":"NDQ1208"',
                "dbo.Rehabilit_FSM_ServEval('Q900,Q901,Q902,Q909', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1209", "12A-17A":"NDQ1210", "18A-29A":"NDQ1211", "30A-59A":"NDQ1212", "60A+":"NDQ1213"',
                "dbo.Rehabilit_FSM_ServEval('S480,S481,S489,S580,S581,S589,S680,S681,S682,S683,S684,S688,S689,T050,T051,T052,T056,T058,T059,Z890,Z891,Z892,Z893,Z898', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1214", "12A-17A":"NDQ1215", "18A-29A":"NDQ1216", "30A-59A":"NDQ1217", "60A+":"NDQ1218"',
                "dbo.Rehabilit_FSM_ServEval('S780,S781,S789,S880,S881,S889,S980,S981,S982,S983,S984,T053,T054,T055,Z894,Z895,Z896,Z897', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1219", "12A-17A":"NDQ1220", "18A-29A":"NDQ1221", "30A-59A":"NDQ1222", "60A+":"NDQ1223"',
                "dbo.Rehabilit_FSM_ServEval('G733,G732,G731,G730,G729,G728,G724,G723,G721,G720,G719,G718,G713,G712,G711,G710,G709,G708,G702,G701,G700,G129,G121,G120', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1224", "12A-17A":"NDQ1225", "18A-29A":"NDQ1226", "30A-59A":"NDQ1227", "60A+":"NDQ1228"',
                "dbo.Rehabilit_FSM_ServEval('G500,G501,G508,G509,G510,G511,G512,G513,G514,G518,G519,G530,G531,G532,G533,G538,G540,G541,G542,G543,G544,G545,G546,G547,G548,G549,G550,G551,G552,G553,G558,G560,G561,G562,G563,G564,G568,G569,G570,G571,G572,G573,G574,G575,G576,G578,G579,G580,G587,G588,G589,G590,G598,G600,G601,G602,G603,G608,G609,G610,G611,G618,G619,G620,G621,G622,G628,G629,G630,G631,G632,G633,G634,G635,G636,G638,G64X,M501,M511,M541,M543,M544,M792,P140,P141,P142,P143,P148,P149,S142,S143,S242,S243,S342,S343,S344,S346,S440,S441,S442,S443,S444,S445,S447,S448,S449,S540,S541,S542,S543,S547,S548,S549,S640,S641,S642,S643,S644,S647,S648,S649,S840,S841,S842,S847,S848,S849,S940,S941,S942,S943,S947,S948,S949', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1229", "12A-17A":"NDQ1230", "18A-29A":"NDQ1231", "30A-59A":"NDQ1232", "60A+":"NDQ1233"',
                "dbo.Rehabilit_FSM_ServEval('G811,I600,I601,I602,I603,I604,I605,I606,I607,I608,I609,I610,I611,I612,I613,I614,I615,I616,I618,I619,I620,I621,I629,I630,I631,I632,I633,I634,I635,I636,I638,I639,I64X,I650,I651,I652,I653,I658,I659,I660,I661,I662,I663,I664,I668,I669,I670,I671,I672,I673,I674,I675,I676,I677,I678,I679,I680,I681,I682,I688,I694,I690,Q282', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1234", "12A-17A":"NDQ1235", "18A-29A":"NDQ1236", "30A-59A":"NDQ1237", "60A+":"NDQ1238"',
                "dbo.Rehabilit_FSM_ServEval('G20X,G210,G211,G212,G213,G214,G218,G219,G22X', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1239", "12A-17A":"NDQ1240", "18A-29A":"NDQ1241", "30A-59A":"NDQ1242", "60A+":"NDQ1243"',
                "dbo.Rehabilit_FSM_ServEval('M400,M401,M402,M403,M404,M405,M410,M411,M412,M413,M414,M415,M418,M419', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1244", "12A-17A":"NDQ1245", "18A-29A":"NDQ1246", "30A-59A":"NDQ1247", "60A+":"NDQ1248"',
                "dbo.Rehabilit_FSM_ServEval('M420,M421,M429,M45X,M491,M492,M493,M494,M495,M498', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1249", "12A-17A":"NDQ1250", "18A-29A":"NDQ1251", "30A-59A":"NDQ1252", "60A+":"NDQ1253"',
                "dbo.Rehabilit_FSM_ServEval('G992,M501,M502,M503,M508,M509,M510,M512,M513,M514,M518,M519,M530,M531,M532,M533,M538,M539', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1254", "12A-17A":"NDQ1255", "18A-29A":"NDQ1256", "30A-59A":"NDQ1257", "60A+":"NDQ1258"',
                "dbo.Rehabilit_FSM_ServEval('M542,M545,M546,M548,M549', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1259", "12A-17A":"NDQ1260", "18A-29A":"NDQ1261", "30A-59A":"NDQ1262", "60A+":"NDQ1263"',
                "dbo.Rehabilit_FSM_ServEval('M430,M431,M432', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1264", "12A-17A":"NDQ1265", "18A-29A":"NDQ1266", "30A-59A":"NDQ1267", "60A+":"NDQ1268"',
                "dbo.Rehabilit_FSM_ServEval('Q241,Q670,Q715,Q716,Q718,Q719,Q743,Q770,Q774', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1269", "12A-17A":"NDQ1270", "18A-29A":"NDQ1271", "30A-59A":"NDQ1272", "60A+":"NDQ1273"',
                "dbo.Rehabilit_FSM_ServEval('M910,M911,M912,M913,M918,M919,M920,M921,M922,M923,M924,M925,M926,M927,M928,M929,M930,M931,M932,M938,M939,Q720,Q721,Q722,Q723,Q724,Q725,Q726,Q727,Q728,Q729,Q730,Q731,Q738,Q710,Q711,Q712,Q713', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1274", "12A-17A":"NDQ1275", "18A-29A":"NDQ1276", "30A-59A":"NDQ1277", "60A+":"NDQ1278"',
                "dbo.Rehabilit_FSM_ServEval('M960,M961,M962,M963,M964,M968,M969', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1279", "12A-17A":"NDQ1280", "18A-29A":"NDQ1281", "30A-59A":"NDQ1282", "60A+":"NDQ1283"',
                "dbo.Rehabilit_FSM_ServEval('I090,I091,I092,I098,I099,I200,I201,I208,I209,I210,I211,I212,I213,I214,I219,I260,I269,I270,I271,I272,I278,I279,I280,I281,I288,I289,I430,I431,I432,I438,I500,I501,I509,I520,I521,I528,I690,I691,I692,I693,I694,I730,I731,I738,I739,I99X,Q200,Q201,Q202,Q203,Q204,Q205,Q206,Q208,Q209,Z950,Z951,Z952', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1284", "12A-17A":"NDQ1285", "18A-29A":"NDQ1286", "30A-59A":"NDQ1287", "60A+":"NDQ1288"',
                "dbo.Rehabilit_FSM_ServEval('J1281,J1289,J180,J181,J182,J188,J189,J1891,J1892,J208,J220,J221,J222,J223,J224,J225,J226,J227,J228,J229,J40X,J410,J411,J418,J42X,J430,J431,J432,J438,J439,J440,J441,J448,J449,J450,J451,J458,J459,J4591,J46X,J47X,J680,J681,J682,J683,J684,J688,J689,J700,J701,J702,J703,J704,J708,J709,J800,J801,J802,J803,J804,J805,J806,J807,J808,J809,J841,J848,J960,J961,J969,J988,J981,J990,J991,J998', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1289", "12A-17A":"NDQ1290", "18A-29A":"NDQ1291", "30A-59A":"NDQ1292", "60A+":"NDQ1293"',
                "dbo.Rehabilit_FSM_ServEval('N311,N312,N318,N319,N320,N941,N942,N948,R102,R309', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1294", "12A-17A":"NDQ1295", "18A-29A":"NDQ1296", "30A-59A":"NDQ1297", "60A+":"NDQ1298"',
                "dbo.Rehabilit_FSM_ServEval('N393,N394,R15X,R32X', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1299", "12A-17A":"NDQ1300", "18A-29A":"NDQ1301", "30A-59A":"NDQ1302", "60A+":"NDQ1303"',
                "dbo.Rehabilit_FSM_ServEval('N812,N814,N815,N816,N818,N819', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1304", "12A-17A":"NDQ1305", "18A-29A":"NDQ1306", "30A-59A":"NDQ1307", "60A+":"NDQ1308"',
                "dbo.Rehabilit_FSM_ServEval('S000,S090,S091,S092,S097,S098,S099,S100,S101,S107,S108,S109,S197,S198,S199,S200,S201,S202,S203,S204,S207,S208,S290,S297,S298,S299,S300,S301,S302,S307,S308,S309,S390,S396,S397,S398,S399,S400,S407,S408,S409,S497,S498,S499,S500,S501,S507,S508,S509,S597,S598,S599,S600,S601,S602,S607,S608,S609,S697,S698,S699,S700,S701,S707,S708,S709,S797,S798,S799,S800,S801,S807,S808,S809,S897,S898,S899,S900,S901,S902,S903,S907,S908,S909,S997,S998,S999,T000,T001,T002,T003,T006,T008,T009,T07X,T08X,T140,T141,T142,T143,T144,T145,T146,T147,T148,T149,T900,T901,T902,T903,T904,T905,T908,T909,T910,T911,T912,T913,T914,T915,T918,T919,T920,T921,T922,T923,T924,T925,T926,T928,T929,T930,T931,T932,T933,T934,T935,T936,T938,T939,T940,T941,T950,T951,T952,T953,T954,T958,T959,T96X,T97X,T980,T981,T982,T983', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1309", "12A-17A":"NDQ1310", "18A-29A":"NDQ1311", "30A-59A":"NDQ1312", "60A+":"NDQ1313"',
                "dbo.Rehabilit_FSM_ServEval('M000,M001,M002,M008,M009,M300,M301,M302,M303,M308,M310,M311,M312,M313,M314,M315,M316,M317,M318,M319,M320,M321,M328,M329,M330,M331,M332,M339,M340,M341,M342,M348,M349,M350,M351,M352,M353,M354,M355,M356,M357,M358,M359,M360,M361,M362,M363,M364,M368,M600,M601,M602,M608,M609,M610,M611,M612,M613,M614,M615,M619,M620,M621,M622,M623,M624,M625,M626,M628,M629,M630,M631,M632,M633,M638,M650,M651,M652,M653,M654,M658,M659,M660,M661,M662,M663,M664,M665,M670,M671,M672,M673,M674,M678,M679,M680,M688,M800,M801,M802,M803,M804,M805,M808,M809,M850,M851,M852,M853,M854,M855,M856,M858,M859', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1314", "12A-17A":"NDQ1315", "18A-29A":"NDQ1316", "30A-59A":"NDQ1317", "60A+":"NDQ1318"',
                "dbo.Rehabilit_FSM_ServEval('M200,M201,M202,M203,M204,M205,M206,M210,M211,M212,M213,M214,M215,M216,M217,M218,M219,M220,M221,M222,M223,M228,M229,M230,M231,M232,M233,M234,M236,M240,M242,M243,M244,M245,M246,M247,M248,M249,M250,M251,M252,M253,M254,M256,M257,M258,M259,M759', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1319", "12A-17A":"NDQ1320", "18A-29A":"NDQ1321", "30A-59A":"NDQ1322", "60A+":"NDQ1323"',
                "dbo.Rehabilit_FSM_ServEval('A239,M490,M491,M860,M861,M862,M863,M864,M865,M866,M868,M869,M890,M891,M892,M893,M894,M895,M896,M898,M899', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1324", "12A-17A":"NDQ1325", "18A-29A":"NDQ1326", "30A-59A":"NDQ1327", "60A+":"NDQ1328"',
                "dbo.Rehabilit_FSM_ServEval('M998,M999', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1329", "12A-17A":"NDQ1330", "18A-29A":"NDQ1331", "30A-59A":"NDQ1332", "60A+":"NDQ1333"',
                "dbo.Rehabilit_FSM_ServEval('I890,I891,I892,I893,I894,I895,I896,I897,I898,I899,I890,I891,I898,I899,I972,I978,I979', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1334", "12A-17A":"NDQ1335", "18A-29A":"NDQ1336", "30A-59A":"NDQ1337", "60A+":"NDQ1338"',
                "dbo.Rehabilit_FSM_ServEval('M6284', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1339", "12A-17A":"NDQ1340", "18A-29A":"NDQ1341", "30A-59A":"NDQ1342", "60A+":"NDQ1343"',
                "dbo.Rehabilit_FSM_ServEval('M255,M791,M797,R521,R522,R529', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1344", "12A-17A":"NDQ1345", "18A-29A":"NDQ1346", "30A-59A":"NDQ1347", "60A+":"NDQ1348"',
                "dbo.Rehabilit_FSM_ServEval('T200,T201,T202,T203,T204,T205,T206,T207,T208,T209,T200,T201,T202,T203,T204,T205,T206,T207,T210,T220,T230,T240,T250,T260,T270,T280,T290,T300,T310,T311,T312,T313,T314,T315,T316,T317,T318,T319,T310,T311,T312,T313,T314,T315,T316,T317,T318,T319,T320,T321,T322,T323,T324,T325,T326,T327,T328,T329,T320,T321,T322,T323,T324,T325,T326,T327,T328,T329,T330,T331,T332,T333,T334,T335,T336,T337,T338,T339,T330,T331,T332,T333,T334,T335,T336,T337,T338,T339,T340,T341,T342,T343,T344,T345,T346,T347,T348,T349,T340,T341,T342,T343,T344,T345,T346,T347,T348,T349,T350,T351,T352,T353,T354,T355,T356,T357,T358,T359,T350,T351,T352,T353,T354,T355,T356,T357', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1349", "12A-17A":"NDQ1350", "18A-29A":"NDQ1351", "30A-59A":"NDQ1352", "60A+":"NDQ1353"',
                "dbo.Rehabilit_FSM_EnRiesgo('A178,A1782,A800,B690,B91X,B941,C720,C721,D334,G041,G042,G048,G049,G050,G051,G052,G058,G114,G320,G35X,G360,G373,G820,G821,G822,G823,G824,G825,G834,G950,G951,G952,G958,G959,G971,M471,M480,M500,Q050,Q051,Q052,Q053,Q054,Q055,Q056,Q057,Q058,Q059,Q060,Q061,Q062,Q063,Q064,Q068,Q069,S140,S141,S240,S241,S340,S341,T093,T889', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1354", "12A-17A":"NDQ1355", "18A-29A":"NDQ1356", "30A-59A":"NDQ1357", "60A+":"NDQ1358"',
                "dbo.Rehabilit_FSM_EnRiesgo('Q650,Q651,Q652,Q653,Q654,Q655,Q656,Q658,Q659,Q660,Q661,Q662,Q663,Q664,Q665,Q666,Q667,Q668,Q669,Q671,Q672,Q673,Q674,Q675,Q676,Q677,Q678,Q740,Q741,Q742,Q743,Q744,Q745,Q746,Q747,Q748,Q749,Q740,Q741,Q742,Q748,Q749,Q750,Q751,Q752,Q753,Q754,Q755,Q758,Q759,Q760,Q761,Q762,Q763,Q764,Q765,Q766,Q767,Q768,Q769,Q771,Q772,Q773,Q775,Q776,Q777,Q778,Q779,Q780,Q781,Q782,Q783,Q784,Q785,Q786,Q788,Q789,Q790,Q791,Q792,Q793,Q794,Q795,Q796,Q798,Q799', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1359", "12A-17A":"NDQ1360", "18A-29A":"NDQ1361", "30A-59A":"NDQ1362", "60A+":"NDQ1363"',
                "dbo.Rehabilit_FSM_EnRiesgo('M150,M151,M152,M153,M154,M158,M159,M160,M161,M162,M163,M164,M165,M166,M167,M169,M170,M171,M172,M173,M174,M175,M179,M180,M181,M182,M183,M184,M185,M189,M190,M191,M192,M198,M199,M224,M235,M238,M239,M241,M470,M472,M478,M479', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1364", "12A-17A":"NDQ1365", "18A-29A":"NDQ1366", "30A-59A":"NDQ1367", "60A+":"NDQ1368"',
                "dbo.Rehabilit_FSM_EnRiesgo('A321,B582,F83X,G000,G001,G002,G003,G008,G009,G000,G001,G002,G003,G008,G009,G010,G011,G012,G013,G014,G015,G016,G017,G018,G019,G020,G021,G022,G023,G024,G025,G026,G027,G028,G029,G030,G031,G032,G033,G034,G035,G036,G037,G038,G039,G040,G041,G042,G043,G044,G045,G046,G047,G048,G049,G042,G050,G051,G052,G053,G054,G055,G056,G057,G058,G059,G800,G801,G802,G803,G804,G808,G809,G820,G821,G822,G823,G824,G825,G826,G827,G828,G829,G910,G911,G912,G913,G914,G915,G916,G917,G918,G919,G910,G911,G912,G913,G918,G919,P900,P901,P902,P903,P904,P905,P906,P907,P908,P909,P940,P941,P942,P948,P949,Q000,Q001,Q002,Q003,Q004,Q005,Q006,Q007,Q008,Q009,Q010,Q011,Q012,Q013,Q014,Q015,Q016,Q017,Q018,Q019,Q020,Q021,Q022,Q023,Q024,Q025,Q026,Q027,Q028,Q029,Q030,Q031,Q032,Q033,Q034,Q035,Q036,Q037,Q038,Q039,Q040,Q041,Q042,Q043,Q044,Q045,Q046,Q047,Q048,Q049,Q070,Q071,Q072,Q073,Q074,Q075,Q076,Q077,Q078,Q079', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1369", "12A-17A":"NDQ1370", "18A-29A":"NDQ1371", "30A-59A":"NDQ1372", "60A+":"NDQ1373"',
                "dbo.Rehabilit_FSM_EnRiesgo('Q900,Q901,Q902,Q909', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1374", "12A-17A":"NDQ1375", "18A-29A":"NDQ1376", "30A-59A":"NDQ1377", "60A+":"NDQ1378"',
                "dbo.Rehabilit_FSM_EnRiesgo('S480,S481,S489,S580,S581,S589,S680,S681,S682,S683,S684,S688,S689,T050,T051,T052,T056,T058,T059,Z890,Z891,Z892,Z893,Z898', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1379", "12A-17A":"NDQ1380", "18A-29A":"NDQ1381", "30A-59A":"NDQ1382", "60A+":"NDQ1383"',
                "dbo.Rehabilit_FSM_EnRiesgo('S780,S781,S789,S880,S881,S889,S980,S981,S982,S983,S984,T053,T054,T055,Z894,Z895,Z896,Z897', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1384", "12A-17A":"NDQ1385", "18A-29A":"NDQ1386", "30A-59A":"NDQ1387", "60A+":"NDQ1388"',
                "dbo.Rehabilit_FSM_EnRiesgo('G733,G732,G731,G730,G729,G728,G724,G723,G721,G720,G719,G718,G713,G712,G711,G710,G709,G708,G702,G701,G700,G129,G121,G120', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1389", "12A-17A":"NDQ1390", "18A-29A":"NDQ1391", "30A-59A":"NDQ1392", "60A+":"NDQ1393"',
                "dbo.Rehabilit_FSM_EnRiesgo('G500,G501,G508,G509,G510,G511,G512,G513,G514,G518,G519,G530,G531,G532,G533,G538,G540,G541,G542,G543,G544,G545,G546,G547,G548,G549,G550,G551,G552,G553,G558,G560,G561,G562,G563,G564,G568,G569,G570,G571,G572,G573,G574,G575,G576,G578,G579,G580,G587,G588,G589,G590,G598,G600,G601,G602,G603,G608,G609,G610,G611,G618,G619,G620,G621,G622,G628,G629,G630,G631,G632,G633,G634,G635,G636,G638,G64X,M501,M511,M541,M543,M544,M792,P140,P141,P142,P143,P148,P149,S142,S143,S242,S243,S342,S343,S344,S346,S440,S441,S442,S443,S444,S445,S447,S448,S449,S540,S541,S542,S543,S547,S548,S549,S640,S641,S642,S643,S644,S647,S648,S649,S840,S841,S842,S847,S848,S849,S940,S941,S942,S943,S947,S948,S949', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1394", "12A-17A":"NDQ1395", "18A-29A":"NDQ1396", "30A-59A":"NDQ1397", "60A+":"NDQ1398"',
                "dbo.Rehabilit_FSM_EnRiesgo('G811,I600,I601,I602,I603,I604,I605,I606,I607,I608,I609,I610,I611,I612,I613,I614,I615,I616,I618,I619,I620,I621,I629,I630,I631,I632,I633,I634,I635,I636,I638,I639,I64X,I650,I651,I652,I653,I658,I659,I660,I661,I662,I663,I664,I668,I669,I670,I671,I672,I673,I674,I675,I676,I677,I678,I679,I680,I681,I682,I688,I694,I690,Q282', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1399", "12A-17A":"NDQ1400", "18A-29A":"NDQ1401", "30A-59A":"NDQ1402", "60A+":"NDQ1403"',
                "dbo.Rehabilit_FSM_EnRiesgo('G20X,G210,G211,G212,G213,G214,G218,G219,G22X', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1404", "12A-17A":"NDQ1405", "18A-29A":"NDQ1406", "30A-59A":"NDQ1407", "60A+":"NDQ1408"',
                "dbo.Rehabilit_FSM_EnRiesgo('M400,M401,M402,M403,M404,M405,M410,M411,M412,M413,M414,M415,M418,M419', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1409", "12A-17A":"NDQ1410", "18A-29A":"NDQ1411", "30A-59A":"NDQ1412", "60A+":"NDQ1413"',
                "dbo.Rehabilit_FSM_EnRiesgo('M420,M421,M429,M45X,M491,M492,M493,M494,M495,M498', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1414", "12A-17A":"NDQ1415", "18A-29A":"NDQ1416", "30A-59A":"NDQ1417", "60A+":"NDQ1418"',
                "dbo.Rehabilit_FSM_EnRiesgo('G992,M501,M502,M503,M508,M509,M510,M512,M513,M514,M518,M519,M530,M531,M532,M533,M538,M539', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1419", "12A-17A":"NDQ1420", "18A-29A":"NDQ1421", "30A-59A":"NDQ1422", "60A+":"NDQ1423"',
                "dbo.Rehabilit_FSM_EnRiesgo('M542,M545,M546,M548,M549', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1424", "12A-17A":"NDQ1425", "18A-29A":"NDQ1426", "30A-59A":"NDQ1427", "60A+":"NDQ1428"',
                "dbo.Rehabilit_FSM_EnRiesgo('M430,M431,M432', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1429", "12A-17A":"NDQ1430", "18A-29A":"NDQ1431", "30A-59A":"NDQ1432", "60A+":"NDQ1433"',
                "dbo.Rehabilit_FSM_EnRiesgo('Q241,Q670,Q715,Q716,Q718,Q719,Q743,Q770,Q774', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1434", "12A-17A":"NDQ1435", "18A-29A":"NDQ1436", "30A-59A":"NDQ1437", "60A+":"NDQ1438"',
                "dbo.Rehabilit_FSM_EnRiesgo('M910,M911,M912,M913,M918,M919,M920,M921,M922,M923,M924,M925,M926,M927,M928,M929,M930,M931,M932,M938,M939,Q720,Q721,Q722,Q723,Q724,Q725,Q726,Q727,Q728,Q729,Q730,Q731,Q738,Q710,Q711,Q712,Q713', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1439", "12A-17A":"NDQ1440", "18A-29A":"NDQ1441", "30A-59A":"NDQ1442", "60A+":"NDQ1443"',
                "dbo.Rehabilit_FSM_EnRiesgo('M960,M961,M962,M963,M964,M968,M969', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1444", "12A-17A":"NDQ1445", "18A-29A":"NDQ1446", "30A-59A":"NDQ1447", "60A+":"NDQ1448"',
                "dbo.Rehabilit_FSM_EnRiesgo('I090,I091,I092,I098,I099,I200,I201,I208,I209,I210,I211,I212,I213,I214,I219,I260,I269,I270,I271,I272,I278,I279,I280,I281,I288,I289,I430,I431,I432,I438,I500,I501,I509,I520,I521,I528,I690,I691,I692,I693,I694,I730,I731,I738,I739,I99X,Q200,Q201,Q202,Q203,Q204,Q205,Q206,Q208,Q209,Z950,Z951,Z952', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1449", "12A-17A":"NDQ1450", "18A-29A":"NDQ1451", "30A-59A":"NDQ1452", "60A+":"NDQ1453"',
                "dbo.Rehabilit_FSM_EnRiesgo('J1281,J1289,J180,J181,J182,J188,J189,J1891,J1892,J208,J220,J221,J222,J223,J224,J225,J226,J227,J228,J229,J40X,J410,J411,J418,J42X,J430,J431,J432,J438,J439,J440,J441,J448,J449,J450,J451,J458,J459,J4591,J46X,J47X,J680,J681,J682,J683,J684,J688,J689,J700,J701,J702,J703,J704,J708,J709,J800,J801,J802,J803,J804,J805,J806,J807,J808,J809,J841,J848,J960,J961,J969,J988,J981,J990,J991,J998', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1454", "12A-17A":"NDQ1455", "18A-29A":"NDQ1456", "30A-59A":"NDQ1457", "60A+":"NDQ1458"',
                "dbo.Rehabilit_FSM_EnRiesgo('N311,N312,N318,N319,N320,N941,N942,N948,R102,R309', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1459", "12A-17A":"NDQ1460", "18A-29A":"NDQ1461", "30A-59A":"NDQ1462", "60A+":"NDQ1463"',
                "dbo.Rehabilit_FSM_EnRiesgo('N393,N394,R15X,R32X', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1464", "12A-17A":"NDQ1465", "18A-29A":"NDQ1466", "30A-59A":"NDQ1467", "60A+":"NDQ1468"',
                "dbo.Rehabilit_FSM_EnRiesgo('N812,N814,N815,N816,N818,N819', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1469", "12A-17A":"NDQ1470", "18A-29A":"NDQ1471", "30A-59A":"NDQ1472", "60A+":"NDQ1473"',
                "dbo.Rehabilit_FSM_EnRiesgo('S000,S090,S091,S092,S097,S098,S099,S100,S101,S107,S108,S109,S197,S198,S199,S200,S201,S202,S203,S204,S207,S208,S290,S297,S298,S299,S300,S301,S302,S307,S308,S309,S390,S396,S397,S398,S399,S400,S407,S408,S409,S497,S498,S499,S500,S501,S507,S508,S509,S597,S598,S599,S600,S601,S602,S607,S608,S609,S697,S698,S699,S700,S701,S707,S708,S709,S797,S798,S799,S800,S801,S807,S808,S809,S897,S898,S899,S900,S901,S902,S903,S907,S908,S909,S997,S998,S999,T000,T001,T002,T003,T006,T008,T009,T07X,T08X,T140,T141,T142,T143,T144,T145,T146,T147,T148,T149,T900,T901,T902,T903,T904,T905,T908,T909,T910,T911,T912,T913,T914,T915,T918,T919,T920,T921,T922,T923,T924,T925,T926,T928,T929,T930,T931,T932,T933,T934,T935,T936,T938,T939,T940,T941,T950,T951,T952,T953,T954,T958,T959,T96X,T97X,T980,T981,T982,T983', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1474", "12A-17A":"NDQ1475", "18A-29A":"NDQ1476", "30A-59A":"NDQ1477", "60A+":"NDQ1478"',
                "dbo.Rehabilit_FSM_EnRiesgo('M000,M001,M002,M008,M009,M300,M301,M302,M303,M308,M310,M311,M312,M313,M314,M315,M316,M317,M318,M319,M320,M321,M328,M329,M330,M331,M332,M339,M340,M341,M342,M348,M349,M350,M351,M352,M353,M354,M355,M356,M357,M358,M359,M360,M361,M362,M363,M364,M368,M600,M601,M602,M608,M609,M610,M611,M612,M613,M614,M615,M619,M620,M621,M622,M623,M624,M625,M626,M628,M629,M630,M631,M632,M633,M638,M650,M651,M652,M653,M654,M658,M659,M660,M661,M662,M663,M664,M665,M670,M671,M672,M673,M674,M678,M679,M680,M688,M800,M801,M802,M803,M804,M805,M808,M809,M850,M851,M852,M853,M854,M855,M856,M858,M859', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1479", "12A-17A":"NDQ1480", "18A-29A":"NDQ1481", "30A-59A":"NDQ1482", "60A+":"NDQ1483"',
                "dbo.Rehabilit_FSM_EnRiesgo('M200,M201,M202,M203,M204,M205,M206,M210,M211,M212,M213,M214,M215,M216,M217,M218,M219,M220,M221,M222,M223,M228,M229,M230,M231,M232,M233,M234,M236,M240,M242,M243,M244,M245,M246,M247,M248,M249,M250,M251,M252,M253,M254,M256,M257,M258,M259,M759', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1484", "12A-17A":"NDQ1485", "18A-29A":"NDQ1486", "30A-59A":"NDQ1487", "60A+":"NDQ1488"',
                "dbo.Rehabilit_FSM_EnRiesgo('A239,M490,M491,M860,M861,M862,M863,M864,M865,M866,M868,M869,M890,M891,M892,M893,M894,M895,M896,M898,M899', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1489", "12A-17A":"NDQ1490", "18A-29A":"NDQ1491", "30A-59A":"NDQ1492", "60A+":"NDQ1493"',
                "dbo.Rehabilit_FSM_EnRiesgo('M998,M999', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1494", "12A-17A":"NDQ1495", "18A-29A":"NDQ1496", "30A-59A":"NDQ1497", "60A+":"NDQ1498"',
                "dbo.Rehabilit_FSM_EnRiesgo('I890,I891,I892,I893,I894,I895,I896,I897,I898,I899,I890,I891,I898,I899,I972,I978,I979', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1499", "12A-17A":"NDQ1500", "18A-29A":"NDQ1501", "30A-59A":"NDQ1502", "60A+":"NDQ1503"',
                "dbo.Rehabilit_FSM_EnRiesgo('M6284', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1504", "12A-17A":"NDQ1505", "18A-29A":"NDQ1506", "30A-59A":"NDQ1507", "60A+":"NDQ1508"',
                "dbo.Rehabilit_FSM_EnRiesgo('M255,M791,M797,R521,R522,R529', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1509", "12A-17A":"NDQ1510", "18A-29A":"NDQ1511", "30A-59A":"NDQ1512", "60A+":"NDQ1513"',
                "dbo.Rehabilit_FSM_EnRiesgo('T200,T201,T202,T203,T204,T205,T206,T207,T208,T209,T200,T201,T202,T203,T204,T205,T206,T207,T210,T220,T230,T240,T250,T260,T270,T280,T290,T300,T310,T311,T312,T313,T314,T315,T316,T317,T318,T319,T310,T311,T312,T313,T314,T315,T316,T317,T318,T319,T320,T321,T322,T323,T324,T325,T326,T327,T328,T329,T320,T321,T322,T323,T324,T325,T326,T327,T328,T329,T330,T331,T332,T333,T334,T335,T336,T337,T338,T339,T330,T331,T332,T333,T334,T335,T336,T337,T338,T339,T340,T341,T342,T343,T344,T345,T346,T347,T348,T349,T340,T341,T342,T343,T344,T345,T346,T347,T348,T349,T350,T351,T352,T353,T354,T355,T356,T357,T358,T359,T350,T351,T352,T353,T354,T355,T356,T357', 'N,R');"
            ),


        ],

        "FACT_DISC_SNAPSHOT_REHABFISIC_BL2": [
            (
                '"0d-11A":"NDQ1514", "12A-17A":"NDQ1515", "18A-29A":"NDQ1516", "30A-59A":"NDQ1517", "60A+":"NDQ1518"',
                "dbo.RehabFisica_RefContra_Sl('A178,A1782,A800,B690,B91X,B941,C720,C721,D334,G041,G042,G048,G049,G050,G051,G052,G058,G114,G320,G35X,G360,G373,G820,G821,G822,G823,G824,G825,G834,G950,G951,G952,G958,G959,G971,M471,M480,M500,Q050,Q051,Q052,Q053,Q054,Q055,Q056,Q057,Q058,Q059,Q060,Q061,Q062,Q063,Q064,Q068,Q069,S140,S141,S240,S241,S340,S341,T093,T889', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1519", "12A-17A":"NDQ1520", "18A-29A":"NDQ1521", "30A-59A":"NDQ1522", "60A+":"NDQ1523"',
                "dbo.Rehabilit_FSM_RefContraResto('Q650,Q651,Q652,Q653,Q654,Q655,Q656,Q658,Q659,Q660,Q661,Q662,Q663,Q664,Q665,Q666,Q667,Q668,Q669,Q671,Q672,Q673,Q674,Q675,Q676,Q677,Q678,Q740,Q741,Q742,Q743,Q744,Q745,Q746,Q747,Q748,Q749,Q740,Q741,Q742,Q748,Q749,Q750,Q751,Q752,Q753,Q754,Q755,Q758,Q759,Q760,Q761,Q762,Q763,Q764,Q765,Q766,Q767,Q768,Q769,Q771,Q772,Q773,Q775,Q776,Q777,Q778,Q779,Q780,Q781,Q782,Q783,Q784,Q785,Q786,Q788,Q789,Q790,Q791,Q792,Q793,Q794,Q795,Q796,Q798,Q799', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1524", "12A-17A":"NDQ1525", "18A-29A":"NDQ1526", "30A-59A":"NDQ1527", "60A+":"NDQ1528"',
                "dbo.Rehabilit_FSM_RefContraResto('M150,M151,M152,M153,M154,M158,M159,M160,M161,M162,M163,M164,M165,M166,M167,M169,M170,M171,M172,M173,M174,M175,M179,M180,M181,M182,M183,M184,M185,M189,M190,M191,M192,M198,M199,M224,M235,M238,M239,M241,M470,M472,M478,M479', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1529", "12A-17A":"NDQ1530", "18A-29A":"NDQ1531", "30A-59A":"NDQ1532", "60A+":"NDQ1533"',
                "dbo.Rehabilit_FSM_RefContraResto('A321,B582,F83X,G000,G001,G002,G003,G008,G009,G000,G001,G002,G003,G008,G009,G010,G011,G012,G013,G014,G015,G016,G017,G018,G019,G020,G021,G022,G023,G024,G025,G026,G027,G028,G029,G030,G031,G032,G033,G034,G035,G036,G037,G038,G039,G040,G041,G042,G043,G044,G045,G046,G047,G048,G049,G042,G050,G051,G052,G053,G054,G055,G056,G057,G058,G059,G800,G801,G802,G803,G804,G808,G809,G820,G821,G822,G823,G824,G825,G826,G827,G828,G829,G910,G911,G912,G913,G914,G915,G916,G917,G918,G919,G910,G911,G912,G913,G918,G919,P900,P901,P902,P903,P904,P905,P906,P907,P908,P909,P940,P941,P942,P948,P949,Q000,Q001,Q002,Q003,Q004,Q005,Q006,Q007,Q008,Q009,Q010,Q011,Q012,Q013,Q014,Q015,Q016,Q017,Q018,Q019,Q020,Q021,Q022,Q023,Q024,Q025,Q026,Q027,Q028,Q029,Q030,Q031,Q032,Q033,Q034,Q035,Q036,Q037,Q038,Q039,Q040,Q041,Q042,Q043,Q044,Q045,Q046,Q047,Q048,Q049,Q070,Q071,Q072,Q073,Q074,Q075,Q076,Q077,Q078,Q079', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1534", "12A-17A":"NDQ1535", "18A-29A":"NDQ1536", "30A-59A":"NDQ1537", "60A+":"NDQ1538"',
                "dbo.Rehabilit_FSM_RefContraResto('Q900,Q901,Q902,Q909', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1539", "12A-17A":"NDQ1540", "18A-29A":"NDQ1541", "30A-59A":"NDQ1542", "60A+":"NDQ1543"',
                "dbo.Rehabilit_FSM_RefContraResto('S480,S481,S489,S580,S581,S589,S680,S681,S682,S683,S684,S688,S689,T050,T051,T052,T056,T058,T059,Z890,Z891,Z892,Z893,Z898', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1544", "12A-17A":"NDQ1545", "18A-29A":"NDQ1546", "30A-59A":"NDQ1547", "60A+":"NDQ1548"',
                "dbo.Rehabilit_FSM_RefContraResto('S780,S781,S789,S880,S881,S889,S980,S981,S982,S983,S984,T053,T054,T055,Z894,Z895,Z896,Z897', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1549", "12A-17A":"NDQ1550", "18A-29A":"NDQ1551", "30A-59A":"NDQ1552", "60A+":"NDQ1553"',
                "dbo.Rehabilit_FSM_RefContraResto('G733,G732,G731,G730,G729,G728,G724,G723,G721,G720,G719,G718,G713,G712,G711,G710,G709,G708,G702,G701,G700,G129,G121,G120', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1554", "12A-17A":"NDQ1555", "18A-29A":"NDQ1556", "30A-59A":"NDQ1557", "60A+":"NDQ1558"',
                "dbo.Rehabilit_FSM_RefContraResto('G500,G501,G508,G509,G510,G511,G512,G513,G514,G518,G519,G530,G531,G532,G533,G538,G540,G541,G542,G543,G544,G545,G546,G547,G548,G549,G550,G551,G552,G553,G558,G560,G561,G562,G563,G564,G568,G569,G570,G571,G572,G573,G574,G575,G576,G578,G579,G580,G587,G588,G589,G590,G598,G600,G601,G602,G603,G608,G609,G610,G611,G618,G619,G620,G621,G622,G628,G629,G630,G631,G632,G633,G634,G635,G636,G638,G64X,M501,M511,M541,M543,M544,M792,P140,P141,P142,P143,P148,P149,S142,S143,S242,S243,S342,S343,S344,S346,S440,S441,S442,S443,S444,S445,S447,S448,S449,S540,S541,S542,S543,S547,S548,S549,S640,S641,S642,S643,S644,S647,S648,S649,S840,S841,S842,S847,S848,S849,S940,S941,S942,S943,S947,S948,S949', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1559", "12A-17A":"NDQ1560", "18A-29A":"NDQ1561", "30A-59A":"NDQ1562", "60A+":"NDQ1563"',
                "dbo.Rehabilit_FSM_RefContraResto('G811,I600,I601,I602,I603,I604,I605,I606,I607,I608,I609,I610,I611,I612,I613,I614,I615,I616,I618,I619,I620,I621,I629,I630,I631,I632,I633,I634,I635,I636,I638,I639,I64X,I650,I651,I652,I653,I658,I659,I660,I661,I662,I663,I664,I668,I669,I670,I671,I672,I673,I674,I675,I676,I677,I678,I679,I680,I681,I682,I688,I694,I690,Q282', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1564", "12A-17A":"NDQ1565", "18A-29A":"NDQ1566", "30A-59A":"NDQ1567", "60A+":"NDQ1568"',
                "dbo.Rehabilit_FSM_RefContraResto('G20X,G210,G211,G212,G213,G214,G218,G219,G22X', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1569", "12A-17A":"NDQ1570", "18A-29A":"NDQ1571", "30A-59A":"NDQ1572", "60A+":"NDQ1573"',
                "dbo.Rehabilit_FSM_RefContraResto('M400,M401,M402,M403,M404,M405,M410,M411,M412,M413,M414,M415,M418,M419', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1574", "12A-17A":"NDQ1575", "18A-29A":"NDQ1576", "30A-59A":"NDQ1577", "60A+":"NDQ1578"',
                "dbo.Rehabilit_FSM_RefContraResto('M420,M421,M429,M45X,M491,M492,M493,M494,M495,M498', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1579", "12A-17A":"NDQ1580", "18A-29A":"NDQ1581", "30A-59A":"NDQ1582", "60A+":"NDQ1583"',
                "dbo.Rehabilit_FSM_RefContraResto('G992,M501,M502,M503,M508,M509,M510,M512,M513,M514,M518,M519,M530,M531,M532,M533,M538,M539', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1584", "12A-17A":"NDQ1585", "18A-29A":"NDQ1586", "30A-59A":"NDQ1587", "60A+":"NDQ1588"',
                "dbo.Rehabilit_FSM_RefContraResto('M542,M545,M546,M548,M549', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1589", "12A-17A":"NDQ1590", "18A-29A":"NDQ1591", "30A-59A":"NDQ1592", "60A+":"NDQ1593"',
                "dbo.Rehabilit_FSM_RefContraResto('M430,M431,M432', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1594", "12A-17A":"NDQ1595", "18A-29A":"NDQ1596", "30A-59A":"NDQ1597", "60A+":"NDQ1598"',
                "dbo.Rehabilit_FSM_RefContraResto('Q241,Q670,Q715,Q716,Q718,Q719,Q743,Q770,Q774', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1599", "12A-17A":"NDQ1600", "18A-29A":"NDQ1601", "30A-59A":"NDQ1602", "60A+":"NDQ1603"',
                "dbo.Rehabilit_FSM_RefContraResto('M910,M911,M912,M913,M918,M919,M920,M921,M922,M923,M924,M925,M926,M927,M928,M929,M930,M931,M932,M938,M939,Q720,Q721,Q722,Q723,Q724,Q725,Q726,Q727,Q728,Q729,Q730,Q731,Q738,Q710,Q711,Q712,Q713', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1604", "12A-17A":"NDQ1605", "18A-29A":"NDQ1606", "30A-59A":"NDQ1607", "60A+":"NDQ1608"',
                "dbo.Rehabilit_FSM_RefContraResto('M960,M961,M962,M963,M964,M968,M969', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1609", "12A-17A":"NDQ1610", "18A-29A":"NDQ1611", "30A-59A":"NDQ1612", "60A+":"NDQ1613"',
                "dbo.Rehabilit_FSM_RefContraResto('I090,I091,I092,I098,I099,I200,I201,I208,I209,I210,I211,I212,I213,I214,I219,I260,I269,I270,I271,I272,I278,I279,I280,I281,I288,I289,I430,I431,I432,I438,I500,I501,I509,I520,I521,I528,I690,I691,I692,I693,I694,I730,I731,I738,I739,I99X,Q200,Q201,Q202,Q203,Q204,Q205,Q206,Q208,Q209,Z950,Z951,Z952', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1614", "12A-17A":"NDQ1615", "18A-29A":"NDQ1616", "30A-59A":"NDQ1617", "60A+":"NDQ1618"',
                "dbo.Rehabilit_FSM_RefContraResto('J1281,J1289,J180,J181,J182,J188,J189,J1891,J1892,J208,J220,J221,J222,J223,J224,J225,J226,J227,J228,J229,J40X,J410,J411,J418,J42X,J430,J431,J432,J438,J439,J440,J441,J448,J449,J450,J451,J458,J459,J4591,J46X,J47X,J680,J681,J682,J683,J684,J688,J689,J700,J701,J702,J703,J704,J708,J709,J800,J801,J802,J803,J804,J805,J806,J807,J808,J809,J841,J848,J960,J961,J969,J988,J981,J990,J991,J998', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1619", "12A-17A":"NDQ1620", "18A-29A":"NDQ1621", "30A-59A":"NDQ1622", "60A+":"NDQ1623"',
                "dbo.Rehabilit_FSM_RefContraResto('N311,N312,N318,N319,N320,N941,N942,N948,R102,R309', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1624", "12A-17A":"NDQ1625", "18A-29A":"NDQ1626", "30A-59A":"NDQ1627", "60A+":"NDQ1628"',
                "dbo.Rehabilit_FSM_RefContraResto('N393,N394,R15X,R32X', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1629", "12A-17A":"NDQ1630", "18A-29A":"NDQ1631", "30A-59A":"NDQ1632", "60A+":"NDQ1633"',
                "dbo.Rehabilit_FSM_RefContraResto('N812,N814,N815,N816,N818,N819', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1634", "12A-17A":"NDQ1635", "18A-29A":"NDQ1636", "30A-59A":"NDQ1637", "60A+":"NDQ1638"',
                "dbo.Rehabilit_FSM_RefContraResto('S000,S090,S091,S092,S097,S098,S099,S100,S101,S107,S108,S109,S197,S198,S199,S200,S201,S202,S203,S204,S207,S208,S290,S297,S298,S299,S300,S301,S302,S307,S308,S309,S390,S396,S397,S398,S399,S400,S407,S408,S409,S497,S498,S499,S500,S501,S507,S508,S509,S597,S598,S599,S600,S601,S602,S607,S608,S609,S697,S698,S699,S700,S701,S707,S708,S709,S797,S798,S799,S800,S801,S807,S808,S809,S897,S898,S899,S900,S901,S902,S903,S907,S908,S909,S997,S998,S999,T000,T001,T002,T003,T006,T008,T009,T07X,T08X,T140,T141,T142,T143,T144,T145,T146,T147,T148,T149,T900,T901,T902,T903,T904,T905,T908,T909,T910,T911,T912,T913,T914,T915,T918,T919,T920,T921,T922,T923,T924,T925,T926,T928,T929,T930,T931,T932,T933,T934,T935,T936,T938,T939,T940,T941,T950,T951,T952,T953,T954,T958,T959,T96X,T97X,T980,T981,T982,T983', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1639", "12A-17A":"NDQ1640", "18A-29A":"NDQ1641", "30A-59A":"NDQ1642", "60A+":"NDQ1643"',
                "dbo.Rehabilit_FSM_RefContraResto('M000,M001,M002,M008,M009,M300,M301,M302,M303,M308,M310,M311,M312,M313,M314,M315,M316,M317,M318,M319,M320,M321,M328,M329,M330,M331,M332,M339,M340,M341,M342,M348,M349,M350,M351,M352,M353,M354,M355,M356,M357,M358,M359,M360,M361,M362,M363,M364,M368,M600,M601,M602,M608,M609,M610,M611,M612,M613,M614,M615,M619,M620,M621,M622,M623,M624,M625,M626,M628,M629,M630,M631,M632,M633,M638,M650,M651,M652,M653,M654,M658,M659,M660,M661,M662,M663,M664,M665,M670,M671,M672,M673,M674,M678,M679,M680,M688,M800,M801,M802,M803,M804,M805,M808,M809,M850,M851,M852,M853,M854,M855,M856,M858,M859', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1644", "12A-17A":"NDQ1645", "18A-29A":"NDQ1646", "30A-59A":"NDQ1647", "60A+":"NDQ1648"',
                "dbo.Rehabilit_FSM_RefContraResto('M200,M201,M202,M203,M204,M205,M206,M210,M211,M212,M213,M214,M215,M216,M217,M218,M219,M220,M221,M222,M223,M228,M229,M230,M231,M232,M233,M234,M236,M240,M242,M243,M244,M245,M246,M247,M248,M249,M250,M251,M252,M253,M254,M256,M257,M258,M259,M759', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1649", "12A-17A":"NDQ1650", "18A-29A":"NDQ1651", "30A-59A":"NDQ1652", "60A+":"NDQ1653"',
                "dbo.Rehabilit_FSM_RefContraResto('A239,M490,M491,M860,M861,M862,M863,M864,M865,M866,M868,M869,M890,M891,M892,M893,M894,M895,M896,M898,M899', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1654", "12A-17A":"NDQ1655", "18A-29A":"NDQ1656", "30A-59A":"NDQ1657", "60A+":"NDQ1658"',
                "dbo.Rehabilit_FSM_RefContraResto('M998,M999', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1659", "12A-17A":"NDQ1660", "18A-29A":"NDQ1661", "30A-59A":"NDQ1662", "60A+":"NDQ1663"',
                "dbo.Rehabilit_FSM_RefContraResto('I890,I891,I892,I893,I894,I895,I896,I897,I898,I899,I890,I891,I898,I899,I972,I978,I979', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1664", "12A-17A":"NDQ1665", "18A-29A":"NDQ1666", "30A-59A":"NDQ1667", "60A+":"NDQ1668"',
                "dbo.Rehabilit_FSM_RefContraResto('M6284', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1669", "12A-17A":"NDQ1670", "18A-29A":"NDQ1671", "30A-59A":"NDQ1672", "60A+":"NDQ1673"',
                "dbo.Rehabilit_FSM_RefContraResto('M255,M791,M797,R521,R522,R529', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1674", "12A-17A":"NDQ1675", "18A-29A":"NDQ1676", "30A-59A":"NDQ1677", "60A+":"NDQ1678"',
                "dbo.Rehabilit_FSM_RefContraResto('T200,T201,T202,T203,T204,T205,T206,T207,T208,T209,T200,T201,T202,T203,T204,T205,T206,T207,T210,T220,T230,T240,T250,T260,T270,T280,T290,T300,T310,T311,T312,T313,T314,T315,T316,T317,T318,T319,T310,T311,T312,T313,T314,T315,T316,T317,T318,T319,T320,T321,T322,T323,T324,T325,T326,T327,T328,T329,T320,T321,T322,T323,T324,T325,T326,T327,T328,T329,T330,T331,T332,T333,T334,T335,T336,T337,T338,T339,T330,T331,T332,T333,T334,T335,T336,T337,T338,T339,T340,T341,T342,T343,T344,T345,T346,T347,T348,T349,T340,T341,T342,T343,T344,T345,T346,T347,T348,T349,T350,T351,T352,T353,T354,T355,T356,T357,T358,T359,T350,T351,T352,T353,T354,T355,T356,T357', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1679", "12A-17A":"NDQ1680", "18A-29A":"NDQ1681", "30A-59A":"NDQ1682", "60A+":"NDQ1683"',
                "dbo.Rehabilit_FSM_Telemed('A178,A1782,A800,B690,B91X,B941,C720,C721,D334,G041,G042,G048,G049,G050,G051,G052,G058,G114,G320,G35X,G360,G373,G820,G821,G822,G823,G824,G825,G834,G950,G951,G952,G958,G959,G971,M471,M480,M500,Q050,Q051,Q052,Q053,Q054,Q055,Q056,Q057,Q058,Q059,Q060,Q061,Q062,Q063,Q064,Q068,Q069,S140,S141,S240,S241,S340,S341,T093,T889', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1684", "12A-17A":"NDQ1685", "18A-29A":"NDQ1686", "30A-59A":"NDQ1687", "60A+":"NDQ1688"',
                "dbo.Rehabilit_FSM_Telemed('Q650,Q651,Q652,Q653,Q654,Q655,Q656,Q658,Q659,Q660,Q661,Q662,Q663,Q664,Q665,Q666,Q667,Q668,Q669,Q671,Q672,Q673,Q674,Q675,Q676,Q677,Q678,Q740,Q741,Q742,Q743,Q744,Q745,Q746,Q747,Q748,Q749,Q740,Q741,Q742,Q748,Q749,Q750,Q751,Q752,Q753,Q754,Q755,Q758,Q759,Q760,Q761,Q762,Q763,Q764,Q765,Q766,Q767,Q768,Q769,Q771,Q772,Q773,Q775,Q776,Q777,Q778,Q779,Q780,Q781,Q782,Q783,Q784,Q785,Q786,Q788,Q789,Q790,Q791,Q792,Q793,Q794,Q795,Q796,Q798,Q799', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1689", "12A-17A":"NDQ1690", "18A-29A":"NDQ1691", "30A-59A":"NDQ1692", "60A+":"NDQ1693"',
                "dbo.Rehabilit_FSM_Telemed('M150,M151,M152,M153,M154,M158,M159,M160,M161,M162,M163,M164,M165,M166,M167,M169,M170,M171,M172,M173,M174,M175,M179,M180,M181,M182,M183,M184,M185,M189,M190,M191,M192,M198,M199,M224,M235,M238,M239,M241,M470,M472,M478,M479', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1694", "12A-17A":"NDQ1695", "18A-29A":"NDQ1696", "30A-59A":"NDQ1697", "60A+":"NDQ1698"',
                "dbo.Rehabilit_FSM_Telemed('A321,B582,F83X,G000,G001,G002,G003,G008,G009,G000,G001,G002,G003,G008,G009,G010,G011,G012,G013,G014,G015,G016,G017,G018,G019,G020,G021,G022,G023,G024,G025,G026,G027,G028,G029,G030,G031,G032,G033,G034,G035,G036,G037,G038,G039,G040,G041,G042,G043,G044,G045,G046,G047,G048,G049,G042,G050,G051,G052,G053,G054,G055,G056,G057,G058,G059,G800,G801,G802,G803,G804,G808,G809,G820,G821,G822,G823,G824,G825,G826,G827,G828,G829,G910,G911,G912,G913,G914,G915,G916,G917,G918,G919,G910,G911,G912,G913,G918,G919,P900,P901,P902,P903,P904,P905,P906,P907,P908,P909,P940,P941,P942,P948,P949,Q000,Q001,Q002,Q003,Q004,Q005,Q006,Q007,Q008,Q009,Q010,Q011,Q012,Q013,Q014,Q015,Q016,Q017,Q018,Q019,Q020,Q021,Q022,Q023,Q024,Q025,Q026,Q027,Q028,Q029,Q030,Q031,Q032,Q033,Q034,Q035,Q036,Q037,Q038,Q039,Q040,Q041,Q042,Q043,Q044,Q045,Q046,Q047,Q048,Q049,Q070,Q071,Q072,Q073,Q074,Q075,Q076,Q077,Q078,Q079', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1699", "12A-17A":"NDQ1700", "18A-29A":"NDQ1701", "30A-59A":"NDQ1702", "60A+":"NDQ1703"',
                "dbo.Rehabilit_FSM_Telemed('Q900,Q901,Q902,Q909', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1704", "12A-17A":"NDQ1705", "18A-29A":"NDQ1706", "30A-59A":"NDQ1707", "60A+":"NDQ1708"',
                "dbo.Rehabilit_FSM_Telemed('S480,S481,S489,S580,S581,S589,S680,S681,S682,S683,S684,S688,S689,T050,T051,T052,T056,T058,T059,Z890,Z891,Z892,Z893,Z898', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1709", "12A-17A":"NDQ1710", "18A-29A":"NDQ1711", "30A-59A":"NDQ1712", "60A+":"NDQ1713"',
                "dbo.Rehabilit_FSM_Telemed('S780,S781,S789,S880,S881,S889,S980,S981,S982,S983,S984,T053,T054,T055,Z894,Z895,Z896,Z897', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1714", "12A-17A":"NDQ1715", "18A-29A":"NDQ1716", "30A-59A":"NDQ1717", "60A+":"NDQ1718"',
                "dbo.Rehabilit_FSM_Telemed('G733,G732,G731,G730,G729,G728,G724,G723,G721,G720,G719,G718,G713,G712,G711,G710,G709,G708,G702,G701,G700,G129,G121,G120', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1719", "12A-17A":"NDQ1720", "18A-29A":"NDQ1721", "30A-59A":"NDQ1722", "60A+":"NDQ1723"',
                "dbo.Rehabilit_FSM_Telemed('G500,G501,G508,G509,G510,G511,G512,G513,G514,G518,G519,G530,G531,G532,G533,G538,G540,G541,G542,G543,G544,G545,G546,G547,G548,G549,G550,G551,G552,G553,G558,G560,G561,G562,G563,G564,G568,G569,G570,G571,G572,G573,G574,G575,G576,G578,G579,G580,G587,G588,G589,G590,G598,G600,G601,G602,G603,G608,G609,G610,G611,G618,G619,G620,G621,G622,G628,G629,G630,G631,G632,G633,G634,G635,G636,G638,G64X,M501,M511,M541,M543,M544,M792,P140,P141,P142,P143,P148,P149,S142,S143,S242,S243,S342,S343,S344,S346,S440,S441,S442,S443,S444,S445,S447,S448,S449,S540,S541,S542,S543,S547,S548,S549,S640,S641,S642,S643,S644,S647,S648,S649,S840,S841,S842,S847,S848,S849,S940,S941,S942,S943,S947,S948,S949', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1724", "12A-17A":"NDQ1725", "18A-29A":"NDQ1726", "30A-59A":"NDQ1727", "60A+":"NDQ1728"',
                "dbo.Rehabilit_FSM_Telemed('G811,I600,I601,I602,I603,I604,I605,I606,I607,I608,I609,I610,I611,I612,I613,I614,I615,I616,I618,I619,I620,I621,I629,I630,I631,I632,I633,I634,I635,I636,I638,I639,I64X,I650,I651,I652,I653,I658,I659,I660,I661,I662,I663,I664,I668,I669,I670,I671,I672,I673,I674,I675,I676,I677,I678,I679,I680,I681,I682,I688,I694,I690,Q282', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1729", "12A-17A":"NDQ1730", "18A-29A":"NDQ1731", "30A-59A":"NDQ1732", "60A+":"NDQ1733"',
                "dbo.Rehabilit_FSM_Telemed('G20X,G210,G211,G212,G213,G214,G218,G219,G22X', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1734", "12A-17A":"NDQ1735", "18A-29A":"NDQ1736", "30A-59A":"NDQ1737", "60A+":"NDQ1738"',
                "dbo.Rehabilit_FSM_Telemed('M400,M401,M402,M403,M404,M405,M410,M411,M412,M413,M414,M415,M418,M419', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1739", "12A-17A":"NDQ1740", "18A-29A":"NDQ1741", "30A-59A":"NDQ1742", "60A+":"NDQ1743"',
                "dbo.Rehabilit_FSM_Telemed('M420,M421,M429,M45X,M491,M492,M493,M494,M495,M498', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1744", "12A-17A":"NDQ1745", "18A-29A":"NDQ1746", "30A-59A":"NDQ1747", "60A+":"NDQ1748"',
                "dbo.Rehabilit_FSM_Telemed('G992,M501,M502,M503,M508,M509,M510,M512,M513,M514,M518,M519,M530,M531,M532,M533,M538,M539', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1749", "12A-17A":"NDQ1750", "18A-29A":"NDQ1751", "30A-59A":"NDQ1752", "60A+":"NDQ1753"',
                "dbo.Rehabilit_FSM_Telemed('M542,M545,M546,M548,M549', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1754", "12A-17A":"NDQ1755", "18A-29A":"NDQ1756", "30A-59A":"NDQ1757", "60A+":"NDQ1758"',
                "dbo.Rehabilit_FSM_Telemed('M430,M431,M432', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1759", "12A-17A":"NDQ1760", "18A-29A":"NDQ1761", "30A-59A":"NDQ1762", "60A+":"NDQ1763"',
                "dbo.Rehabilit_FSM_Telemed('Q241,Q670,Q715,Q716,Q718,Q719,Q743,Q770,Q774', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1764", "12A-17A":"NDQ1765", "18A-29A":"NDQ1766", "30A-59A":"NDQ1767", "60A+":"NDQ1768"',
                "dbo.Rehabilit_FSM_Telemed('M910,M911,M912,M913,M918,M919,M920,M921,M922,M923,M924,M925,M926,M927,M928,M929,M930,M931,M932,M938,M939,Q720,Q721,Q722,Q723,Q724,Q725,Q726,Q727,Q728,Q729,Q730,Q731,Q738,Q710,Q711,Q712,Q713', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1769", "12A-17A":"NDQ1770", "18A-29A":"NDQ1771", "30A-59A":"NDQ1772", "60A+":"NDQ1773"',
                "dbo.Rehabilit_FSM_Telemed('M960,M961,M962,M963,M964,M968,M969', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1774", "12A-17A":"NDQ1775", "18A-29A":"NDQ1776", "30A-59A":"NDQ1777", "60A+":"NDQ1778"',
                "dbo.Rehabilit_FSM_Telemed('I090,I091,I092,I098,I099,I200,I201,I208,I209,I210,I211,I212,I213,I214,I219,I260,I269,I270,I271,I272,I278,I279,I280,I281,I288,I289,I430,I431,I432,I438,I500,I501,I509,I520,I521,I528,I690,I691,I692,I693,I694,I730,I731,I738,I739,I99X,Q200,Q201,Q202,Q203,Q204,Q205,Q206,Q208,Q209,Z950,Z951,Z952', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1779", "12A-17A":"NDQ1780", "18A-29A":"NDQ1781", "30A-59A":"NDQ1782", "60A+":"NDQ1783"',
                "dbo.Rehabilit_FSM_Telemed('J1281,J1289,J180,J181,J182,J188,J189,J1891,J1892,J208,J220,J221,J222,J223,J224,J225,J226,J227,J228,J229,J40X,J410,J411,J418,J42X,J430,J431,J432,J438,J439,J440,J441,J448,J449,J450,J451,J458,J459,J4591,J46X,J47X,J680,J681,J682,J683,J684,J688,J689,J700,J701,J702,J703,J704,J708,J709,J800,J801,J802,J803,J804,J805,J806,J807,J808,J809,J841,J848,J960,J961,J969,J988,J981,J990,J991,J998', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1784", "12A-17A":"NDQ1785", "18A-29A":"NDQ1786", "30A-59A":"NDQ1787", "60A+":"NDQ1788"',
                "dbo.Rehabilit_FSM_Telemed('N311,N312,N318,N319,N320,N941,N942,N948,R102,R309', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1789", "12A-17A":"NDQ1790", "18A-29A":"NDQ1791", "30A-59A":"NDQ1792", "60A+":"NDQ1793"',
                "dbo.Rehabilit_FSM_Telemed('N393,N394,R15X,R32X', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1794", "12A-17A":"NDQ1795", "18A-29A":"NDQ1796", "30A-59A":"NDQ1797", "60A+":"NDQ1798"',
                "dbo.Rehabilit_FSM_Telemed('N812,N814,N815,N816,N818,N819', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1799", "12A-17A":"NDQ1800", "18A-29A":"NDQ1801", "30A-59A":"NDQ1802", "60A+":"NDQ1803"',
                "dbo.Rehabilit_FSM_Telemed('S000,S090,S091,S092,S097,S098,S099,S100,S101,S107,S108,S109,S197,S198,S199,S200,S201,S202,S203,S204,S207,S208,S290,S297,S298,S299,S300,S301,S302,S307,S308,S309,S390,S396,S397,S398,S399,S400,S407,S408,S409,S497,S498,S499,S500,S501,S507,S508,S509,S597,S598,S599,S600,S601,S602,S607,S608,S609,S697,S698,S699,S700,S701,S707,S708,S709,S797,S798,S799,S800,S801,S807,S808,S809,S897,S898,S899,S900,S901,S902,S903,S907,S908,S909,S997,S998,S999,T000,T001,T002,T003,T006,T008,T009,T07X,T08X,T140,T141,T142,T143,T144,T145,T146,T147,T148,T149,T900,T901,T902,T903,T904,T905,T908,T909,T910,T911,T912,T913,T914,T915,T918,T919,T920,T921,T922,T923,T924,T925,T926,T928,T929,T930,T931,T932,T933,T934,T935,T936,T938,T939,T940,T941,T950,T951,T952,T953,T954,T958,T959,T96X,T97X,T980,T981,T982,T983', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1804", "12A-17A":"NDQ1805", "18A-29A":"NDQ1806", "30A-59A":"NDQ1807", "60A+":"NDQ1808"',
                "dbo.Rehabilit_FSM_Telemed('M000,M001,M002,M008,M009,M300,M301,M302,M303,M308,M310,M311,M312,M313,M314,M315,M316,M317,M318,M319,M320,M321,M328,M329,M330,M331,M332,M339,M340,M341,M342,M348,M349,M350,M351,M352,M353,M354,M355,M356,M357,M358,M359,M360,M361,M362,M363,M364,M368,M600,M601,M602,M608,M609,M610,M611,M612,M613,M614,M615,M619,M620,M621,M622,M623,M624,M625,M626,M628,M629,M630,M631,M632,M633,M638,M650,M651,M652,M653,M654,M658,M659,M660,M661,M662,M663,M664,M665,M670,M671,M672,M673,M674,M678,M679,M680,M688,M800,M801,M802,M803,M804,M805,M808,M809,M850,M851,M852,M853,M854,M855,M856,M858,M859', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1809", "12A-17A":"NDQ1810", "18A-29A":"NDQ1811", "30A-59A":"NDQ1812", "60A+":"NDQ1813"',
                "dbo.Rehabilit_FSM_Telemed('M200,M201,M202,M203,M204,M205,M206,M210,M211,M212,M213,M214,M215,M216,M217,M218,M219,M220,M221,M222,M223,M228,M229,M230,M231,M232,M233,M234,M236,M240,M242,M243,M244,M245,M246,M247,M248,M249,M250,M251,M252,M253,M254,M256,M257,M258,M259,M759', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1814", "12A-17A":"NDQ1815", "18A-29A":"NDQ1816", "30A-59A":"NDQ1817", "60A+":"NDQ1818"',
                "dbo.Rehabilit_FSM_Telemed('A239,M490,M491,M860,M861,M862,M863,M864,M865,M866,M868,M869,M890,M891,M892,M893,M894,M895,M896,M898,M899', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1819", "12A-17A":"NDQ1820", "18A-29A":"NDQ1821", "30A-59A":"NDQ1822", "60A+":"NDQ1823"',
                "dbo.Rehabilit_FSM_Telemed('M998,M999', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1824", "12A-17A":"NDQ1825", "18A-29A":"NDQ1826", "30A-59A":"NDQ1827", "60A+":"NDQ1828"',
                "dbo.Rehabilit_FSM_Telemed('I890,I891,I892,I893,I894,I895,I896,I897,I898,I899,I890,I891,I898,I899,I972,I978,I979', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1829", "12A-17A":"NDQ1830", "18A-29A":"NDQ1831", "30A-59A":"NDQ1832", "60A+":"NDQ1833"',
                "dbo.Rehabilit_FSM_Telemed('M6284', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1834", "12A-17A":"NDQ1835", "18A-29A":"NDQ1836", "30A-59A":"NDQ1837", "60A+":"NDQ1838"',
                "dbo.Rehabilit_FSM_Telemed('M255,M791,M797,R521,R522,R529', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1839", "12A-17A":"NDQ1840", "18A-29A":"NDQ1841", "30A-59A":"NDQ1842", "60A+":"NDQ1843"',
                "dbo.Rehabilit_FSM_Telemed('T200,T201,T202,T203,T204,T205,T206,T207,T208,T209,T200,T201,T202,T203,T204,T205,T206,T207,T210,T220,T230,T240,T250,T260,T270,T280,T290,T300,T310,T311,T312,T313,T314,T315,T316,T317,T318,T319,T310,T311,T312,T313,T314,T315,T316,T317,T318,T319,T320,T321,T322,T323,T324,T325,T326,T327,T328,T329,T320,T321,T322,T323,T324,T325,T326,T327,T328,T329,T330,T331,T332,T333,T334,T335,T336,T337,T338,T339,T330,T331,T332,T333,T334,T335,T336,T337,T338,T339,T340,T341,T342,T343,T344,T345,T346,T347,T348,T349,T340,T341,T342,T343,T344,T345,T346,T347,T348,T349,T350,T351,T352,T353,T354,T355,T356,T357,T358,T359,T350,T351,T352,T353,T354,T355,T356,T357', 'N,R');"
            ),
            (
                '"0d-11A":"NDQ1844", "12A-17A":"NDQ1845", "18A-29A":"NDQ1846", "30A-59A":"NDQ1847", "60A+":"NDQ1848"',
                "dbo.Rehabilit_FSM_ConCert('A178,A1782,A800,B690,B91X,B941,C720,C721,D334,G041,G042,G048,G049,G050,G051,G052,G058,G114,G320,G35X,G360,G373,G820,G821,G822,G823,G824,G825,G834,G950,G951,G952,G958,G959,G971,M471,M480,M500,Q050,Q051,Q052,Q053,Q054,Q055,Q056,Q057,Q058,Q059,Q060,Q061,Q062,Q063,Q064,Q068,Q069,S140,S141,S240,S241,S340,S341,T093,T889', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ1849", "12A-17A":"NDQ1850", "18A-29A":"NDQ1851", "30A-59A":"NDQ1852", "60A+":"NDQ1853"',
                "dbo.Rehabilit_FSM_ConCert('Q650,Q651,Q652,Q653,Q654,Q655,Q656,Q658,Q659,Q660,Q661,Q662,Q663,Q664,Q665,Q666,Q667,Q668,Q669,Q671,Q672,Q673,Q674,Q675,Q676,Q677,Q678,Q740,Q741,Q742,Q743,Q744,Q745,Q746,Q747,Q748,Q749,Q740,Q741,Q742,Q748,Q749,Q750,Q751,Q752,Q753,Q754,Q755,Q758,Q759,Q760,Q761,Q762,Q763,Q764,Q765,Q766,Q767,Q768,Q769,Q771,Q772,Q773,Q775,Q776,Q777,Q778,Q779,Q780,Q781,Q782,Q783,Q784,Q785,Q786,Q788,Q789,Q790,Q791,Q792,Q793,Q794,Q795,Q796,Q798,Q799', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ1854", "12A-17A":"NDQ1855", "18A-29A":"NDQ1856", "30A-59A":"NDQ1857", "60A+":"NDQ1858"',
                "dbo.Rehabilit_FSM_ConCert('M150,M151,M152,M153,M154,M158,M159,M160,M161,M162,M163,M164,M165,M166,M167,M169,M170,M171,M172,M173,M174,M175,M179,M180,M181,M182,M183,M184,M185,M189,M190,M191,M192,M198,M199,M224,M235,M238,M239,M241,M470,M472,M478,M479', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ1859", "12A-17A":"NDQ1860", "18A-29A":"NDQ1861", "30A-59A":"NDQ1862", "60A+":"NDQ1863"',
                "dbo.Rehabilit_FSM_ConCert('A321,B582,F83X,G000,G001,G002,G003,G008,G009,G000,G001,G002,G003,G008,G009,G010,G011,G012,G013,G014,G015,G016,G017,G018,G019,G020,G021,G022,G023,G024,G025,G026,G027,G028,G029,G030,G031,G032,G033,G034,G035,G036,G037,G038,G039,G040,G041,G042,G043,G044,G045,G046,G047,G048,G049,G042,G050,G051,G052,G053,G054,G055,G056,G057,G058,G059,G800,G801,G802,G803,G804,G808,G809,G820,G821,G822,G823,G824,G825,G826,G827,G828,G829,G910,G911,G912,G913,G914,G915,G916,G917,G918,G919,G910,G911,G912,G913,G918,G919,P900,P901,P902,P903,P904,P905,P906,P907,P908,P909,P940,P941,P942,P948,P949,Q000,Q001,Q002,Q003,Q004,Q005,Q006,Q007,Q008,Q009,Q010,Q011,Q012,Q013,Q014,Q015,Q016,Q017,Q018,Q019,Q020,Q021,Q022,Q023,Q024,Q025,Q026,Q027,Q028,Q029,Q030,Q031,Q032,Q033,Q034,Q035,Q036,Q037,Q038,Q039,Q040,Q041,Q042,Q043,Q044,Q045,Q046,Q047,Q048,Q049,Q070,Q071,Q072,Q073,Q074,Q075,Q076,Q077,Q078,Q079', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ1864", "12A-17A":"NDQ1865", "18A-29A":"NDQ1866", "30A-59A":"NDQ1867", "60A+":"NDQ1868"',
                "dbo.Rehabilit_FSM_ConCert('Q900,Q901,Q902,Q909', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ1869", "12A-17A":"NDQ1870", "18A-29A":"NDQ1871", "30A-59A":"NDQ1872", "60A+":"NDQ1873"',
                "dbo.Rehabilit_FSM_ConCert('S480,S481,S489,S580,S581,S589,S680,S681,S682,S683,S684,S688,S689,T050,T051,T052,T056,T058,T059,Z890,Z891,Z892,Z893,Z898', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ1874", "12A-17A":"NDQ1875", "18A-29A":"NDQ1876", "30A-59A":"NDQ1877", "60A+":"NDQ1878"',
                "dbo.Rehabilit_FSM_ConCert('S780,S781,S789,S880,S881,S889,S980,S981,S982,S983,S984,T053,T054,T055,Z894,Z895,Z896,Z897', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ1879", "12A-17A":"NDQ1880", "18A-29A":"NDQ1881", "30A-59A":"NDQ1882", "60A+":"NDQ1883"',
                "dbo.Rehabilit_FSM_ConCert('G733,G732,G731,G730,G729,G728,G724,G723,G721,G720,G719,G718,G713,G712,G711,G710,G709,G708,G702,G701,G700,G129,G121,G120', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ1884", "12A-17A":"NDQ1885", "18A-29A":"NDQ1886", "30A-59A":"NDQ1887", "60A+":"NDQ1888"',
                "dbo.Rehabilit_FSM_ConCert('G500,G501,G508,G509,G510,G511,G512,G513,G514,G518,G519,G530,G531,G532,G533,G538,G540,G541,G542,G543,G544,G545,G546,G547,G548,G549,G550,G551,G552,G553,G558,G560,G561,G562,G563,G564,G568,G569,G570,G571,G572,G573,G574,G575,G576,G578,G579,G580,G587,G588,G589,G590,G598,G600,G601,G602,G603,G608,G609,G610,G611,G618,G619,G620,G621,G622,G628,G629,G630,G631,G632,G633,G634,G635,G636,G638,G64X,M501,M511,M541,M543,M544,M792,P140,P141,P142,P143,P148,P149,S142,S143,S242,S243,S342,S343,S344,S346,S440,S441,S442,S443,S444,S445,S447,S448,S449,S540,S541,S542,S543,S547,S548,S549,S640,S641,S642,S643,S644,S647,S648,S649,S840,S841,S842,S847,S848,S849,S940,S941,S942,S943,S947,S948,S949', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ1889", "12A-17A":"NDQ1890", "18A-29A":"NDQ1891", "30A-59A":"NDQ1892", "60A+":"NDQ1893"',
                "dbo.Rehabilit_FSM_ConCert('G811,I600,I601,I602,I603,I604,I605,I606,I607,I608,I609,I610,I611,I612,I613,I614,I615,I616,I618,I619,I620,I621,I629,I630,I631,I632,I633,I634,I635,I636,I638,I639,I64X,I650,I651,I652,I653,I658,I659,I660,I661,I662,I663,I664,I668,I669,I670,I671,I672,I673,I674,I675,I676,I677,I678,I679,I680,I681,I682,I688,I694,I690,Q282', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ1894", "12A-17A":"NDQ1895", "18A-29A":"NDQ1896", "30A-59A":"NDQ1897", "60A+":"NDQ1898"',
                "dbo.Rehabilit_FSM_ConCert('G20X,G210,G211,G212,G213,G214,G218,G219,G22X', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ1899", "12A-17A":"NDQ1900", "18A-29A":"NDQ1901", "30A-59A":"NDQ1902", "60A+":"NDQ1903"',
                "dbo.Rehabilit_FSM_ConCert('M400,M401,M402,M403,M404,M405,M410,M411,M412,M413,M414,M415,M418,M419', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ1904", "12A-17A":"NDQ1905", "18A-29A":"NDQ1906", "30A-59A":"NDQ1907", "60A+":"NDQ1908"',
                "dbo.Rehabilit_FSM_ConCert('M420,M421,M429,M45X,M491,M492,M493,M494,M495,M498', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ1909", "12A-17A":"NDQ1910", "18A-29A":"NDQ1911", "30A-59A":"NDQ1912", "60A+":"NDQ1913"',
                "dbo.Rehabilit_FSM_ConCert('G992,M501,M502,M503,M508,M509,M510,M512,M513,M514,M518,M519,M530,M531,M532,M533,M538,M539', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ1914", "12A-17A":"NDQ1915", "18A-29A":"NDQ1916", "30A-59A":"NDQ1917", "60A+":"NDQ1918"',
                "dbo.Rehabilit_FSM_ConCert('M542,M545,M546,M548,M549', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ1919", "12A-17A":"NDQ1920", "18A-29A":"NDQ1921", "30A-59A":"NDQ1922", "60A+":"NDQ1923"',
                "dbo.Rehabilit_FSM_ConCert('M430,M431,M432', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ1924", "12A-17A":"NDQ1925", "18A-29A":"NDQ1926", "30A-59A":"NDQ1927", "60A+":"NDQ1928"',
                "dbo.Rehabilit_FSM_ConCert('Q241,Q670,Q715,Q716,Q718,Q719,Q743,Q770,Q774', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ1929", "12A-17A":"NDQ1930", "18A-29A":"NDQ1931", "30A-59A":"NDQ1932", "60A+":"NDQ1933"',
                "dbo.Rehabilit_FSM_ConCert('M910,M911,M912,M913,M918,M919,M920,M921,M922,M923,M924,M925,M926,M927,M928,M929,M930,M931,M932,M938,M939,Q720,Q721,Q722,Q723,Q724,Q725,Q726,Q727,Q728,Q729,Q730,Q731,Q738,Q710,Q711,Q712,Q713', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ1934", "12A-17A":"NDQ1935", "18A-29A":"NDQ1936", "30A-59A":"NDQ1937", "60A+":"NDQ1938"',
                "dbo.Rehabilit_FSM_ConCert('M960,M961,M962,M963,M964,M968,M969', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ1939", "12A-17A":"NDQ1940", "18A-29A":"NDQ1941", "30A-59A":"NDQ1942", "60A+":"NDQ1943"',
                "dbo.Rehabilit_FSM_ConCert('I090,I091,I092,I098,I099,I200,I201,I208,I209,I210,I211,I212,I213,I214,I219,I260,I269,I270,I271,I272,I278,I279,I280,I281,I288,I289,I430,I431,I432,I438,I500,I501,I509,I520,I521,I528,I690,I691,I692,I693,I694,I730,I731,I738,I739,I99X,Q200,Q201,Q202,Q203,Q204,Q205,Q206,Q208,Q209,Z950,Z951,Z952', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ1944", "12A-17A":"NDQ1945", "18A-29A":"NDQ1946", "30A-59A":"NDQ1947", "60A+":"NDQ1948"',
                "dbo.Rehabilit_FSM_ConCert('J1281,J1289,J180,J181,J182,J188,J189,J1891,J1892,J208,J220,J221,J222,J223,J224,J225,J226,J227,J228,J229,J40X,J410,J411,J418,J42X,J430,J431,J432,J438,J439,J440,J441,J448,J449,J450,J451,J458,J459,J4591,J46X,J47X,J680,J681,J682,J683,J684,J688,J689,J700,J701,J702,J703,J704,J708,J709,J800,J801,J802,J803,J804,J805,J806,J807,J808,J809,J841,J848,J960,J961,J969,J988,J981,J990,J991,J998', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ1949", "12A-17A":"NDQ1950", "18A-29A":"NDQ1951", "30A-59A":"NDQ1952", "60A+":"NDQ1953"',
                "dbo.Rehabilit_FSM_ConCert('N311,N312,N318,N319,N320,N941,N942,N948,R102,R309', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ1954", "12A-17A":"NDQ1955", "18A-29A":"NDQ1956", "30A-59A":"NDQ1957", "60A+":"NDQ1958"',
                "dbo.Rehabilit_FSM_ConCert('N393,N394,R15X,R32X', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ1959", "12A-17A":"NDQ1960", "18A-29A":"NDQ1961", "30A-59A":"NDQ1962", "60A+":"NDQ1963"',
                "dbo.Rehabilit_FSM_ConCert('N812,N814,N815,N816,N818,N819', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ1964", "12A-17A":"NDQ1965", "18A-29A":"NDQ1966", "30A-59A":"NDQ1967", "60A+":"NDQ1968"',
                "dbo.Rehabilit_FSM_ConCert('S000,S090,S091,S092,S097,S098,S099,S100,S101,S107,S108,S109,S197,S198,S199,S200,S201,S202,S203,S204,S207,S208,S290,S297,S298,S299,S300,S301,S302,S307,S308,S309,S390,S396,S397,S398,S399,S400,S407,S408,S409,S497,S498,S499,S500,S501,S507,S508,S509,S597,S598,S599,S600,S601,S602,S607,S608,S609,S697,S698,S699,S700,S701,S707,S708,S709,S797,S798,S799,S800,S801,S807,S808,S809,S897,S898,S899,S900,S901,S902,S903,S907,S908,S909,S997,S998,S999,T000,T001,T002,T003,T006,T008,T009,T07X,T08X,T140,T141,T142,T143,T144,T145,T146,T147,T148,T149,T900,T901,T902,T903,T904,T905,T908,T909,T910,T911,T912,T913,T914,T915,T918,T919,T920,T921,T922,T923,T924,T925,T926,T928,T929,T930,T931,T932,T933,T934,T935,T936,T938,T939,T940,T941,T950,T951,T952,T953,T954,T958,T959,T96X,T97X,T980,T981,T982,T983', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ1969", "12A-17A":"NDQ1970", "18A-29A":"NDQ1971", "30A-59A":"NDQ1972", "60A+":"NDQ1973"',
                "dbo.Rehabilit_FSM_ConCert('M000,M001,M002,M008,M009,M300,M301,M302,M303,M308,M310,M311,M312,M313,M314,M315,M316,M317,M318,M319,M320,M321,M328,M329,M330,M331,M332,M339,M340,M341,M342,M348,M349,M350,M351,M352,M353,M354,M355,M356,M357,M358,M359,M360,M361,M362,M363,M364,M368,M600,M601,M602,M608,M609,M610,M611,M612,M613,M614,M615,M619,M620,M621,M622,M623,M624,M625,M626,M628,M629,M630,M631,M632,M633,M638,M650,M651,M652,M653,M654,M658,M659,M660,M661,M662,M663,M664,M665,M670,M671,M672,M673,M674,M678,M679,M680,M688,M800,M801,M802,M803,M804,M805,M808,M809,M850,M851,M852,M853,M854,M855,M856,M858,M859', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ1974", "12A-17A":"NDQ1975", "18A-29A":"NDQ1976", "30A-59A":"NDQ1977", "60A+":"NDQ1978"',
                "dbo.Rehabilit_FSM_ConCert('M200,M201,M202,M203,M204,M205,M206,M210,M211,M212,M213,M214,M215,M216,M217,M218,M219,M220,M221,M222,M223,M228,M229,M230,M231,M232,M233,M234,M236,M240,M242,M243,M244,M245,M246,M247,M248,M249,M250,M251,M252,M253,M254,M256,M257,M258,M259,M759', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ1979", "12A-17A":"NDQ1980", "18A-29A":"NDQ1981", "30A-59A":"NDQ1982", "60A+":"NDQ1983"',
                "dbo.Rehabilit_FSM_ConCert('A239,M490,M491,M860,M861,M862,M863,M864,M865,M866,M868,M869,M890,M891,M892,M893,M894,M895,M896,M898,M899', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ1984", "12A-17A":"NDQ1985", "18A-29A":"NDQ1986", "30A-59A":"NDQ1987", "60A+":"NDQ1988"',
                "dbo.Rehabilit_FSM_ConCert('M998,M999', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ1989", "12A-17A":"NDQ1990", "18A-29A":"NDQ1991", "30A-59A":"NDQ1992", "60A+":"NDQ1993"',
                "dbo.Rehabilit_FSM_ConCert('I890,I891,I892,I893,I894,I895,I896,I897,I898,I899,I890,I891,I898,I899,I972,I978,I979', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ1994", "12A-17A":"NDQ1995", "18A-29A":"NDQ1996", "30A-59A":"NDQ1997", "60A+":"NDQ1998"',
                "dbo.Rehabilit_FSM_ConCert('M6284', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ1999", "12A-17A":"NDQ2000", "18A-29A":"NDQ2001", "30A-59A":"NDQ2002", "60A+":"NDQ2003"',
                "dbo.Rehabilit_FSM_ConCert('M255,M791,M797,R521,R522,R529', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2004", "12A-17A":"NDQ2005", "18A-29A":"NDQ2006", "30A-59A":"NDQ2007", "60A+":"NDQ2008"',
                "dbo.Rehabilit_FSM_ConCert('T200,T201,T202,T203,T204,T205,T206,T207,T208,T209,T200,T201,T202,T203,T204,T205,T206,T207,T210,T220,T230,T240,T250,T260,T270,T280,T290,T300,T310,T311,T312,T313,T314,T315,T316,T317,T318,T319,T310,T311,T312,T313,T314,T315,T316,T317,T318,T319,T320,T321,T322,T323,T324,T325,T326,T327,T328,T329,T320,T321,T322,T323,T324,T325,T326,T327,T328,T329,T330,T331,T332,T333,T334,T335,T336,T337,T338,T339,T330,T331,T332,T333,T334,T335,T336,T337,T338,T339,T340,T341,T342,T343,T344,T345,T346,T347,T348,T349,T340,T341,T342,T343,T344,T345,T346,T347,T348,T349,T350,T351,T352,T353,T354,T355,T356,T357,T358,T359,T350,T351,T352,T353,T354,T355,T356,T357', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2009", "12A-17A":"NDQ2010", "18A-29A":"NDQ2011", "30A-59A":"NDQ2012", "60A+":"NDQ2013"',
                "dbo.Rehabilit_FSM_Nml_NCR('A178,A1782,A800,B690,B91X,B941,C720,C721,D334,G041,G042,G048,G049,G050,G051,G052,G058,G114,G320,G35X,G360,G373,G820,G821,G822,G823,G824,G825,G834,G950,G951,G952,G958,G959,G971,M471,M480,M500,Q050,Q051,Q052,Q053,Q054,Q055,Q056,Q057,Q058,Q059,Q060,Q061,Q062,Q063,Q064,Q068,Q069,S140,S141,S240,S241,S340,S341,T093,T889', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2014", "12A-17A":"NDQ2015", "18A-29A":"NDQ2016", "30A-59A":"NDQ2017", "60A+":"NDQ2018"',
                "dbo.Rehabilit_FSM_Nml_NCR('Q650,Q651,Q652,Q653,Q654,Q655,Q656,Q658,Q659,Q660,Q661,Q662,Q663,Q664,Q665,Q666,Q667,Q668,Q669,Q671,Q672,Q673,Q674,Q675,Q676,Q677,Q678,Q740,Q741,Q742,Q743,Q744,Q745,Q746,Q747,Q748,Q749,Q740,Q741,Q742,Q748,Q749,Q750,Q751,Q752,Q753,Q754,Q755,Q758,Q759,Q760,Q761,Q762,Q763,Q764,Q765,Q766,Q767,Q768,Q769,Q771,Q772,Q773,Q775,Q776,Q777,Q778,Q779,Q780,Q781,Q782,Q783,Q784,Q785,Q786,Q788,Q789,Q790,Q791,Q792,Q793,Q794,Q795,Q796,Q798,Q799', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2019", "12A-17A":"NDQ2020", "18A-29A":"NDQ2021", "30A-59A":"NDQ2022", "60A+":"NDQ2023"',
                "dbo.Rehabilit_FSM_Nml_NCR('M150,M151,M152,M153,M154,M158,M159,M160,M161,M162,M163,M164,M165,M166,M167,M169,M170,M171,M172,M173,M174,M175,M179,M180,M181,M182,M183,M184,M185,M189,M190,M191,M192,M198,M199,M224,M235,M238,M239,M241,M470,M472,M478,M479', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2024", "12A-17A":"NDQ2025", "18A-29A":"NDQ2026", "30A-59A":"NDQ2027", "60A+":"NDQ2028"',
                "dbo.Rehabilit_FSM_Nml_NCR('A321,B582,F83X,G000,G001,G002,G003,G008,G009,G000,G001,G002,G003,G008,G009,G010,G011,G012,G013,G014,G015,G016,G017,G018,G019,G020,G021,G022,G023,G024,G025,G026,G027,G028,G029,G030,G031,G032,G033,G034,G035,G036,G037,G038,G039,G040,G041,G042,G043,G044,G045,G046,G047,G048,G049,G042,G050,G051,G052,G053,G054,G055,G056,G057,G058,G059,G800,G801,G802,G803,G804,G808,G809,G820,G821,G822,G823,G824,G825,G826,G827,G828,G829,G910,G911,G912,G913,G914,G915,G916,G917,G918,G919,G910,G911,G912,G913,G918,G919,P900,P901,P902,P903,P904,P905,P906,P907,P908,P909,P940,P941,P942,P948,P949,Q000,Q001,Q002,Q003,Q004,Q005,Q006,Q007,Q008,Q009,Q010,Q011,Q012,Q013,Q014,Q015,Q016,Q017,Q018,Q019,Q020,Q021,Q022,Q023,Q024,Q025,Q026,Q027,Q028,Q029,Q030,Q031,Q032,Q033,Q034,Q035,Q036,Q037,Q038,Q039,Q040,Q041,Q042,Q043,Q044,Q045,Q046,Q047,Q048,Q049,Q070,Q071,Q072,Q073,Q074,Q075,Q076,Q077,Q078,Q079', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2029", "12A-17A":"NDQ2030", "18A-29A":"NDQ2031", "30A-59A":"NDQ2032", "60A+":"NDQ2033"',
                "dbo.Rehabilit_FSM_Nml_NCR('Q900,Q901,Q902,Q909', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2034", "12A-17A":"NDQ2035", "18A-29A":"NDQ2036", "30A-59A":"NDQ2037", "60A+":"NDQ2038"',
                "dbo.Rehabilit_FSM_Nml_NCR('S480,S481,S489,S580,S581,S589,S680,S681,S682,S683,S684,S688,S689,T050,T051,T052,T056,T058,T059,Z890,Z891,Z892,Z893,Z898', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2039", "12A-17A":"NDQ2040", "18A-29A":"NDQ2041", "30A-59A":"NDQ2042", "60A+":"NDQ2043"',
                "dbo.Rehabilit_FSM_Nml_NCR('S780,S781,S789,S880,S881,S889,S980,S981,S982,S983,S984,T053,T054,T055,Z894,Z895,Z896,Z897', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2044", "12A-17A":"NDQ2045", "18A-29A":"NDQ2046", "30A-59A":"NDQ2047", "60A+":"NDQ2048"',
                "dbo.Rehabilit_FSM_Nml_NCR('G733,G732,G731,G730,G729,G728,G724,G723,G721,G720,G719,G718,G713,G712,G711,G710,G709,G708,G702,G701,G700,G129,G121,G120', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2049", "12A-17A":"NDQ2050", "18A-29A":"NDQ2051", "30A-59A":"NDQ2052", "60A+":"NDQ2053"',
                "dbo.Rehabilit_FSM_Nml_NCR('G500,G501,G508,G509,G510,G511,G512,G513,G514,G518,G519,G530,G531,G532,G533,G538,G540,G541,G542,G543,G544,G545,G546,G547,G548,G549,G550,G551,G552,G553,G558,G560,G561,G562,G563,G564,G568,G569,G570,G571,G572,G573,G574,G575,G576,G578,G579,G580,G587,G588,G589,G590,G598,G600,G601,G602,G603,G608,G609,G610,G611,G618,G619,G620,G621,G622,G628,G629,G630,G631,G632,G633,G634,G635,G636,G638,G64X,M501,M511,M541,M543,M544,M792,P140,P141,P142,P143,P148,P149,S142,S143,S242,S243,S342,S343,S344,S346,S440,S441,S442,S443,S444,S445,S447,S448,S449,S540,S541,S542,S543,S547,S548,S549,S640,S641,S642,S643,S644,S647,S648,S649,S840,S841,S842,S847,S848,S849,S940,S941,S942,S943,S947,S948,S949', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2054", "12A-17A":"NDQ2055", "18A-29A":"NDQ2056", "30A-59A":"NDQ2057", "60A+":"NDQ2058"',
                "dbo.Rehabilit_FSM_Nml_NCR('G811,I600,I601,I602,I603,I604,I605,I606,I607,I608,I609,I610,I611,I612,I613,I614,I615,I616,I618,I619,I620,I621,I629,I630,I631,I632,I633,I634,I635,I636,I638,I639,I64X,I650,I651,I652,I653,I658,I659,I660,I661,I662,I663,I664,I668,I669,I670,I671,I672,I673,I674,I675,I676,I677,I678,I679,I680,I681,I682,I688,I694,I690,Q282', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2059", "12A-17A":"NDQ2060", "18A-29A":"NDQ2061", "30A-59A":"NDQ2062", "60A+":"NDQ2063"',
                "dbo.Rehabilit_FSM_Nml_NCR('G20X,G210,G211,G212,G213,G214,G218,G219,G22X', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2064", "12A-17A":"NDQ2065", "18A-29A":"NDQ2066", "30A-59A":"NDQ2067", "60A+":"NDQ2068"',
                "dbo.Rehabilit_FSM_Nml_NCR('M400,M401,M402,M403,M404,M405,M410,M411,M412,M413,M414,M415,M418,M419', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2069", "12A-17A":"NDQ2070", "18A-29A":"NDQ2071", "30A-59A":"NDQ2072", "60A+":"NDQ2073"',
                "dbo.Rehabilit_FSM_Nml_NCR('M420,M421,M429,M45X,M491,M492,M493,M494,M495,M498', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2074", "12A-17A":"NDQ2075", "18A-29A":"NDQ2076", "30A-59A":"NDQ2077", "60A+":"NDQ2078"',
                "dbo.Rehabilit_FSM_Nml_NCR('G992,M501,M502,M503,M508,M509,M510,M512,M513,M514,M518,M519,M530,M531,M532,M533,M538,M539', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2079", "12A-17A":"NDQ2080", "18A-29A":"NDQ2081", "30A-59A":"NDQ2082", "60A+":"NDQ2083"',
                "dbo.Rehabilit_FSM_Nml_NCR('M542,M545,M546,M548,M549', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2084", "12A-17A":"NDQ2085", "18A-29A":"NDQ2086", "30A-59A":"NDQ2087", "60A+":"NDQ2088"',
                "dbo.Rehabilit_FSM_Nml_NCR('M430,M431,M432', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2089", "12A-17A":"NDQ2090", "18A-29A":"NDQ2091", "30A-59A":"NDQ2092", "60A+":"NDQ2093"',
                "dbo.Rehabilit_FSM_Nml_NCR('Q241,Q670,Q715,Q716,Q718,Q719,Q743,Q770,Q774', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2094", "12A-17A":"NDQ2095", "18A-29A":"NDQ2096", "30A-59A":"NDQ2097", "60A+":"NDQ2098"',
                "dbo.Rehabilit_FSM_Nml_NCR('M910,M911,M912,M913,M918,M919,M920,M921,M922,M923,M924,M925,M926,M927,M928,M929,M930,M931,M932,M938,M939,Q720,Q721,Q722,Q723,Q724,Q725,Q726,Q727,Q728,Q729,Q730,Q731,Q738,Q710,Q711,Q712,Q713', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2099", "12A-17A":"NDQ2100", "18A-29A":"NDQ2101", "30A-59A":"NDQ2102", "60A+":"NDQ2103"',
                "dbo.Rehabilit_FSM_Nml_NCR('M960,M961,M962,M963,M964,M968,M969', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2104", "12A-17A":"NDQ2105", "18A-29A":"NDQ2106", "30A-59A":"NDQ2107", "60A+":"NDQ2108"',
                "dbo.Rehabilit_FSM_Nml_NCR('I090,I091,I092,I098,I099,I200,I201,I208,I209,I210,I211,I212,I213,I214,I219,I260,I269,I270,I271,I272,I278,I279,I280,I281,I288,I289,I430,I431,I432,I438,I500,I501,I509,I520,I521,I528,I690,I691,I692,I693,I694,I730,I731,I738,I739,I99X,Q200,Q201,Q202,Q203,Q204,Q205,Q206,Q208,Q209,Z950,Z951,Z952', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2109", "12A-17A":"NDQ2110", "18A-29A":"NDQ2111", "30A-59A":"NDQ2112", "60A+":"NDQ2113"',
                "dbo.Rehabilit_FSM_Nml_NCR('J1281,J1289,J180,J181,J182,J188,J189,J1891,J1892,J208,J220,J221,J222,J223,J224,J225,J226,J227,J228,J229,J40X,J410,J411,J418,J42X,J430,J431,J432,J438,J439,J440,J441,J448,J449,J450,J451,J458,J459,J4591,J46X,J47X,J680,J681,J682,J683,J684,J688,J689,J700,J701,J702,J703,J704,J708,J709,J800,J801,J802,J803,J804,J805,J806,J807,J808,J809,J841,J848,J960,J961,J969,J988,J981,J990,J991,J998', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2114", "12A-17A":"NDQ2115", "18A-29A":"NDQ2116", "30A-59A":"NDQ2117", "60A+":"NDQ2118"',
                "dbo.Rehabilit_FSM_Nml_NCR('N311,N312,N318,N319,N320,N941,N942,N948,R102,R309', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2119", "12A-17A":"NDQ2120", "18A-29A":"NDQ2121", "30A-59A":"NDQ2122", "60A+":"NDQ2123"',
                "dbo.Rehabilit_FSM_Nml_NCR('N393,N394,R15X,R32X', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2124", "12A-17A":"NDQ2125", "18A-29A":"NDQ2126", "30A-59A":"NDQ2127", "60A+":"NDQ2128"',
                "dbo.Rehabilit_FSM_Nml_NCR('N812,N814,N815,N816,N818,N819', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2129", "12A-17A":"NDQ2130", "18A-29A":"NDQ2131", "30A-59A":"NDQ2132", "60A+":"NDQ2133"',
                "dbo.Rehabilit_FSM_Nml_NCR('S000,S090,S091,S092,S097,S098,S099,S100,S101,S107,S108,S109,S197,S198,S199,S200,S201,S202,S203,S204,S207,S208,S290,S297,S298,S299,S300,S301,S302,S307,S308,S309,S390,S396,S397,S398,S399,S400,S407,S408,S409,S497,S498,S499,S500,S501,S507,S508,S509,S597,S598,S599,S600,S601,S602,S607,S608,S609,S697,S698,S699,S700,S701,S707,S708,S709,S797,S798,S799,S800,S801,S807,S808,S809,S897,S898,S899,S900,S901,S902,S903,S907,S908,S909,S997,S998,S999,T000,T001,T002,T003,T006,T008,T009,T07X,T08X,T140,T141,T142,T143,T144,T145,T146,T147,T148,T149,T900,T901,T902,T903,T904,T905,T908,T909,T910,T911,T912,T913,T914,T915,T918,T919,T920,T921,T922,T923,T924,T925,T926,T928,T929,T930,T931,T932,T933,T934,T935,T936,T938,T939,T940,T941,T950,T951,T952,T953,T954,T958,T959,T96X,T97X,T980,T981,T982,T983', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2134", "12A-17A":"NDQ2135", "18A-29A":"NDQ2136", "30A-59A":"NDQ2137", "60A+":"NDQ2138"',
                "dbo.Rehabilit_FSM_Nml_NCR('M000,M001,M002,M008,M009,M300,M301,M302,M303,M308,M310,M311,M312,M313,M314,M315,M316,M317,M318,M319,M320,M321,M328,M329,M330,M331,M332,M339,M340,M341,M342,M348,M349,M350,M351,M352,M353,M354,M355,M356,M357,M358,M359,M360,M361,M362,M363,M364,M368,M600,M601,M602,M608,M609,M610,M611,M612,M613,M614,M615,M619,M620,M621,M622,M623,M624,M625,M626,M628,M629,M630,M631,M632,M633,M638,M650,M651,M652,M653,M654,M658,M659,M660,M661,M662,M663,M664,M665,M670,M671,M672,M673,M674,M678,M679,M680,M688,M800,M801,M802,M803,M804,M805,M808,M809,M850,M851,M852,M853,M854,M855,M856,M858,M859', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2139", "12A-17A":"NDQ2140", "18A-29A":"NDQ2141", "30A-59A":"NDQ2142", "60A+":"NDQ2143"',
                "dbo.Rehabilit_FSM_Nml_NCR('M200,M201,M202,M203,M204,M205,M206,M210,M211,M212,M213,M214,M215,M216,M217,M218,M219,M220,M221,M222,M223,M228,M229,M230,M231,M232,M233,M234,M236,M240,M242,M243,M244,M245,M246,M247,M248,M249,M250,M251,M252,M253,M254,M256,M257,M258,M259,M759', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2144", "12A-17A":"NDQ2145", "18A-29A":"NDQ2146", "30A-59A":"NDQ2147", "60A+":"NDQ2148"',
                "dbo.Rehabilit_FSM_Nml_NCR('A239,M490,M491,M860,M861,M862,M863,M864,M865,M866,M868,M869,M890,M891,M892,M893,M894,M895,M896,M898,M899', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2149", "12A-17A":"NDQ2150", "18A-29A":"NDQ2151", "30A-59A":"NDQ2152", "60A+":"NDQ2153"',
                "dbo.Rehabilit_FSM_Nml_NCR('M998,M999', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2154", "12A-17A":"NDQ2155", "18A-29A":"NDQ2156", "30A-59A":"NDQ2157", "60A+":"NDQ2158"',
                "dbo.Rehabilit_FSM_Nml_NCR('I890,I891,I892,I893,I894,I895,I896,I897,I898,I899,I890,I891,I898,I899,I972,I978,I979', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2159", "12A-17A":"NDQ2160", "18A-29A":"NDQ2161", "30A-59A":"NDQ2162", "60A+":"NDQ2163"',
                "dbo.Rehabilit_FSM_Nml_NCR('M6284', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2164", "12A-17A":"NDQ2165", "18A-29A":"NDQ2166", "30A-59A":"NDQ2167", "60A+":"NDQ2168"',
                "dbo.Rehabilit_FSM_Nml_NCR('M255,M791,M797,R521,R522,R529', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2169", "12A-17A":"NDQ2170", "18A-29A":"NDQ2171", "30A-59A":"NDQ2172", "60A+":"NDQ2173"',
                "dbo.Rehabilit_FSM_Nml_NCR('T200,T201,T202,T203,T204,T205,T206,T207,T208,T209,T200,T201,T202,T203,T204,T205,T206,T207,T210,T220,T230,T240,T250,T260,T270,T280,T290,T300,T310,T311,T312,T313,T314,T315,T316,T317,T318,T319,T310,T311,T312,T313,T314,T315,T316,T317,T318,T319,T320,T321,T322,T323,T324,T325,T326,T327,T328,T329,T320,T321,T322,T323,T324,T325,T326,T327,T328,T329,T330,T331,T332,T333,T334,T335,T336,T337,T338,T339,T330,T331,T332,T333,T334,T335,T336,T337,T338,T339,T340,T341,T342,T343,T344,T345,T346,T347,T348,T349,T340,T341,T342,T343,T344,T345,T346,T347,T348,T349,T350,T351,T352,T353,T354,T355,T356,T357,T358,T359,T350,T351,T352,T353,T354,T355,T356,T357', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2174", "12A-17A":"NDQ2175", "18A-29A":"NDQ2176", "30A-59A":"NDQ2177", "60A+":"NDQ2178"',
                "dbo.Rehabilit_FSM_SinCert('A178,A1782,A800,B690,B91X,B941,C720,C721,D334,G041,G042,G048,G049,G050,G051,G052,G058,G114,G320,G35X,G360,G373,G820,G821,G822,G823,G824,G825,G834,G950,G951,G952,G958,G959,G971,M471,M480,M500,Q050,Q051,Q052,Q053,Q054,Q055,Q056,Q057,Q058,Q059,Q060,Q061,Q062,Q063,Q064,Q068,Q069,S140,S141,S240,S241,S340,S341,T093,T889', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2179", "12A-17A":"NDQ2180", "18A-29A":"NDQ2181", "30A-59A":"NDQ2182", "60A+":"NDQ2183"',
                "dbo.Rehabilit_FSM_SinCert('Q650,Q651,Q652,Q653,Q654,Q655,Q656,Q658,Q659,Q660,Q661,Q662,Q663,Q664,Q665,Q666,Q667,Q668,Q669,Q671,Q672,Q673,Q674,Q675,Q676,Q677,Q678,Q740,Q741,Q742,Q743,Q744,Q745,Q746,Q747,Q748,Q749,Q740,Q741,Q742,Q748,Q749,Q750,Q751,Q752,Q753,Q754,Q755,Q758,Q759,Q760,Q761,Q762,Q763,Q764,Q765,Q766,Q767,Q768,Q769,Q771,Q772,Q773,Q775,Q776,Q777,Q778,Q779,Q780,Q781,Q782,Q783,Q784,Q785,Q786,Q788,Q789,Q790,Q791,Q792,Q793,Q794,Q795,Q796,Q798,Q799', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2184", "12A-17A":"NDQ2185", "18A-29A":"NDQ2186", "30A-59A":"NDQ2187", "60A+":"NDQ2188"',
                "dbo.Rehabilit_FSM_SinCert('M150,M151,M152,M153,M154,M158,M159,M160,M161,M162,M163,M164,M165,M166,M167,M169,M170,M171,M172,M173,M174,M175,M179,M180,M181,M182,M183,M184,M185,M189,M190,M191,M192,M198,M199,M224,M235,M238,M239,M241,M470,M472,M478,M479', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2189", "12A-17A":"NDQ2190", "18A-29A":"NDQ2191", "30A-59A":"NDQ2192", "60A+":"NDQ2193"',
                "dbo.Rehabilit_FSM_SinCert('A321,B582,F83X,G000,G001,G002,G003,G008,G009,G000,G001,G002,G003,G008,G009,G010,G011,G012,G013,G014,G015,G016,G017,G018,G019,G020,G021,G022,G023,G024,G025,G026,G027,G028,G029,G030,G031,G032,G033,G034,G035,G036,G037,G038,G039,G040,G041,G042,G043,G044,G045,G046,G047,G048,G049,G042,G050,G051,G052,G053,G054,G055,G056,G057,G058,G059,G800,G801,G802,G803,G804,G808,G809,G820,G821,G822,G823,G824,G825,G826,G827,G828,G829,G910,G911,G912,G913,G914,G915,G916,G917,G918,G919,G910,G911,G912,G913,G918,G919,P900,P901,P902,P903,P904,P905,P906,P907,P908,P909,P940,P941,P942,P948,P949,Q000,Q001,Q002,Q003,Q004,Q005,Q006,Q007,Q008,Q009,Q010,Q011,Q012,Q013,Q014,Q015,Q016,Q017,Q018,Q019,Q020,Q021,Q022,Q023,Q024,Q025,Q026,Q027,Q028,Q029,Q030,Q031,Q032,Q033,Q034,Q035,Q036,Q037,Q038,Q039,Q040,Q041,Q042,Q043,Q044,Q045,Q046,Q047,Q048,Q049,Q070,Q071,Q072,Q073,Q074,Q075,Q076,Q077,Q078,Q079', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2194", "12A-17A":"NDQ2195", "18A-29A":"NDQ2196", "30A-59A":"NDQ2197", "60A+":"NDQ2198"',
                "dbo.Rehabilit_FSM_SinCert('Q900,Q901,Q902,Q909', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2199", "12A-17A":"NDQ2200", "18A-29A":"NDQ2201", "30A-59A":"NDQ2202", "60A+":"NDQ2203"',
                "dbo.Rehabilit_FSM_SinCert('S480,S481,S489,S580,S581,S589,S680,S681,S682,S683,S684,S688,S689,T050,T051,T052,T056,T058,T059,Z890,Z891,Z892,Z893,Z898', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2204", "12A-17A":"NDQ2205", "18A-29A":"NDQ2206", "30A-59A":"NDQ2207", "60A+":"NDQ2208"',
                "dbo.Rehabilit_FSM_SinCert('S780,S781,S789,S880,S881,S889,S980,S981,S982,S983,S984,T053,T054,T055,Z894,Z895,Z896,Z897', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2209", "12A-17A":"NDQ2210", "18A-29A":"NDQ2211", "30A-59A":"NDQ2212", "60A+":"NDQ2213"',
                "dbo.Rehabilit_FSM_SinCert('G733,G732,G731,G730,G729,G728,G724,G723,G721,G720,G719,G718,G713,G712,G711,G710,G709,G708,G702,G701,G700,G129,G121,G120', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2214", "12A-17A":"NDQ2215", "18A-29A":"NDQ2216", "30A-59A":"NDQ2217", "60A+":"NDQ2218"',
                "dbo.Rehabilit_FSM_SinCert('G500,G501,G508,G509,G510,G511,G512,G513,G514,G518,G519,G530,G531,G532,G533,G538,G540,G541,G542,G543,G544,G545,G546,G547,G548,G549,G550,G551,G552,G553,G558,G560,G561,G562,G563,G564,G568,G569,G570,G571,G572,G573,G574,G575,G576,G578,G579,G580,G587,G588,G589,G590,G598,G600,G601,G602,G603,G608,G609,G610,G611,G618,G619,G620,G621,G622,G628,G629,G630,G631,G632,G633,G634,G635,G636,G638,G64X,M501,M511,M541,M543,M544,M792,P140,P141,P142,P143,P148,P149,S142,S143,S242,S243,S342,S343,S344,S346,S440,S441,S442,S443,S444,S445,S447,S448,S449,S540,S541,S542,S543,S547,S548,S549,S640,S641,S642,S643,S644,S647,S648,S649,S840,S841,S842,S847,S848,S849,S940,S941,S942,S943,S947,S948,S949', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2219", "12A-17A":"NDQ2220", "18A-29A":"NDQ2221", "30A-59A":"NDQ2222", "60A+":"NDQ2223"',
                "dbo.Rehabilit_FSM_SinCert('G811,I600,I601,I602,I603,I604,I605,I606,I607,I608,I609,I610,I611,I612,I613,I614,I615,I616,I618,I619,I620,I621,I629,I630,I631,I632,I633,I634,I635,I636,I638,I639,I64X,I650,I651,I652,I653,I658,I659,I660,I661,I662,I663,I664,I668,I669,I670,I671,I672,I673,I674,I675,I676,I677,I678,I679,I680,I681,I682,I688,I694,I690,Q282', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2224", "12A-17A":"NDQ2225", "18A-29A":"NDQ2226", "30A-59A":"NDQ2227", "60A+":"NDQ2228"',
                "dbo.Rehabilit_FSM_SinCert('G20X,G210,G211,G212,G213,G214,G218,G219,G22X', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2229", "12A-17A":"NDQ2230", "18A-29A":"NDQ2231", "30A-59A":"NDQ2232", "60A+":"NDQ2233"',
                "dbo.Rehabilit_FSM_SinCert('M400,M401,M402,M403,M404,M405,M410,M411,M412,M413,M414,M415,M418,M419', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2234", "12A-17A":"NDQ2235", "18A-29A":"NDQ2236", "30A-59A":"NDQ2237", "60A+":"NDQ2238"',
                "dbo.Rehabilit_FSM_SinCert('M420,M421,M429,M45X,M491,M492,M493,M494,M495,M498', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2239", "12A-17A":"NDQ2240", "18A-29A":"NDQ2241", "30A-59A":"NDQ2242", "60A+":"NDQ2243"',
                "dbo.Rehabilit_FSM_SinCert('G992,M501,M502,M503,M508,M509,M510,M512,M513,M514,M518,M519,M530,M531,M532,M533,M538,M539', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2244", "12A-17A":"NDQ2245", "18A-29A":"NDQ2246", "30A-59A":"NDQ2247", "60A+":"NDQ2248"',
                "dbo.Rehabilit_FSM_SinCert('M542,M545,M546,M548,M549', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2249", "12A-17A":"NDQ2250", "18A-29A":"NDQ2251", "30A-59A":"NDQ2252", "60A+":"NDQ2253"',
                "dbo.Rehabilit_FSM_SinCert('M430,M431,M432', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2254", "12A-17A":"NDQ2255", "18A-29A":"NDQ2256", "30A-59A":"NDQ2257", "60A+":"NDQ2258"',
                "dbo.Rehabilit_FSM_SinCert('Q241,Q670,Q715,Q716,Q718,Q719,Q743,Q770,Q774', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2259", "12A-17A":"NDQ2260", "18A-29A":"NDQ2261", "30A-59A":"NDQ2262", "60A+":"NDQ2263"',
                "dbo.Rehabilit_FSM_SinCert('M910,M911,M912,M913,M918,M919,M920,M921,M922,M923,M924,M925,M926,M927,M928,M929,M930,M931,M932,M938,M939,Q720,Q721,Q722,Q723,Q724,Q725,Q726,Q727,Q728,Q729,Q730,Q731,Q738,Q710,Q711,Q712,Q713', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2264", "12A-17A":"NDQ2265", "18A-29A":"NDQ2266", "30A-59A":"NDQ2267", "60A+":"NDQ2268"',
                "dbo.Rehabilit_FSM_SinCert('M960,M961,M962,M963,M964,M968,M969', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2269", "12A-17A":"NDQ2270", "18A-29A":"NDQ2271", "30A-59A":"NDQ2272", "60A+":"NDQ2273"',
                "dbo.Rehabilit_FSM_SinCert('I090,I091,I092,I098,I099,I200,I201,I208,I209,I210,I211,I212,I213,I214,I219,I260,I269,I270,I271,I272,I278,I279,I280,I281,I288,I289,I430,I431,I432,I438,I500,I501,I509,I520,I521,I528,I690,I691,I692,I693,I694,I730,I731,I738,I739,I99X,Q200,Q201,Q202,Q203,Q204,Q205,Q206,Q208,Q209,Z950,Z951,Z952', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2274", "12A-17A":"NDQ2275", "18A-29A":"NDQ2276", "30A-59A":"NDQ2277", "60A+":"NDQ2278"',
                "dbo.Rehabilit_FSM_SinCert('J1281,J1289,J180,J181,J182,J188,J189,J1891,J1892,J208,J220,J221,J222,J223,J224,J225,J226,J227,J228,J229,J40X,J410,J411,J418,J42X,J430,J431,J432,J438,J439,J440,J441,J448,J449,J450,J451,J458,J459,J4591,J46X,J47X,J680,J681,J682,J683,J684,J688,J689,J700,J701,J702,J703,J704,J708,J709,J800,J801,J802,J803,J804,J805,J806,J807,J808,J809,J841,J848,J960,J961,J969,J988,J981,J990,J991,J998', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2279", "12A-17A":"NDQ2280", "18A-29A":"NDQ2281", "30A-59A":"NDQ2282", "60A+":"NDQ2283"',
                "dbo.Rehabilit_FSM_SinCert('N311,N312,N318,N319,N320,N941,N942,N948,R102,R309', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2284", "12A-17A":"NDQ2285", "18A-29A":"NDQ2286", "30A-59A":"NDQ2287", "60A+":"NDQ2288"',
                "dbo.Rehabilit_FSM_SinCert('N393,N394,R15X,R32X', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2289", "12A-17A":"NDQ2290", "18A-29A":"NDQ2291", "30A-59A":"NDQ2292", "60A+":"NDQ2293"',
                "dbo.Rehabilit_FSM_SinCert('N812,N814,N815,N816,N818,N819', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2294", "12A-17A":"NDQ2295", "18A-29A":"NDQ2296", "30A-59A":"NDQ2297", "60A+":"NDQ2298"',
                "dbo.Rehabilit_FSM_SinCert('S000,S090,S091,S092,S097,S098,S099,S100,S101,S107,S108,S109,S197,S198,S199,S200,S201,S202,S203,S204,S207,S208,S290,S297,S298,S299,S300,S301,S302,S307,S308,S309,S390,S396,S397,S398,S399,S400,S407,S408,S409,S497,S498,S499,S500,S501,S507,S508,S509,S597,S598,S599,S600,S601,S602,S607,S608,S609,S697,S698,S699,S700,S701,S707,S708,S709,S797,S798,S799,S800,S801,S807,S808,S809,S897,S898,S899,S900,S901,S902,S903,S907,S908,S909,S997,S998,S999,T000,T001,T002,T003,T006,T008,T009,T07X,T08X,T140,T141,T142,T143,T144,T145,T146,T147,T148,T149,T900,T901,T902,T903,T904,T905,T908,T909,T910,T911,T912,T913,T914,T915,T918,T919,T920,T921,T922,T923,T924,T925,T926,T928,T929,T930,T931,T932,T933,T934,T935,T936,T938,T939,T940,T941,T950,T951,T952,T953,T954,T958,T959,T96X,T97X,T980,T981,T982,T983', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2299", "12A-17A":"NDQ2300", "18A-29A":"NDQ2301", "30A-59A":"NDQ2302", "60A+":"NDQ2303"',
                "dbo.Rehabilit_FSM_SinCert('M000,M001,M002,M008,M009,M300,M301,M302,M303,M308,M310,M311,M312,M313,M314,M315,M316,M317,M318,M319,M320,M321,M328,M329,M330,M331,M332,M339,M340,M341,M342,M348,M349,M350,M351,M352,M353,M354,M355,M356,M357,M358,M359,M360,M361,M362,M363,M364,M368,M600,M601,M602,M608,M609,M610,M611,M612,M613,M614,M615,M619,M620,M621,M622,M623,M624,M625,M626,M628,M629,M630,M631,M632,M633,M638,M650,M651,M652,M653,M654,M658,M659,M660,M661,M662,M663,M664,M665,M670,M671,M672,M673,M674,M678,M679,M680,M688,M800,M801,M802,M803,M804,M805,M808,M809,M850,M851,M852,M853,M854,M855,M856,M858,M859', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2304", "12A-17A":"NDQ2305", "18A-29A":"NDQ2306", "30A-59A":"NDQ2307", "60A+":"NDQ2308"',
                "dbo.Rehabilit_FSM_SinCert('M200,M201,M202,M203,M204,M205,M206,M210,M211,M212,M213,M214,M215,M216,M217,M218,M219,M220,M221,M222,M223,M228,M229,M230,M231,M232,M233,M234,M236,M240,M242,M243,M244,M245,M246,M247,M248,M249,M250,M251,M252,M253,M254,M256,M257,M258,M259,M759', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2309", "12A-17A":"NDQ2310", "18A-29A":"NDQ2311", "30A-59A":"NDQ2312", "60A+":"NDQ2313"',
                "dbo.Rehabilit_FSM_SinCert('A239,M490,M491,M860,M861,M862,M863,M864,M865,M866,M868,M869,M890,M891,M892,M893,M894,M895,M896,M898,M899', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2314", "12A-17A":"NDQ2315", "18A-29A":"NDQ2316", "30A-59A":"NDQ2317", "60A+":"NDQ2318"',
                "dbo.Rehabilit_FSM_SinCert('M998,M999', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2319", "12A-17A":"NDQ2320", "18A-29A":"NDQ2321", "30A-59A":"NDQ2322", "60A+":"NDQ2323"',
                "dbo.Rehabilit_FSM_SinCert('I890,I891,I892,I893,I894,I895,I896,I897,I898,I899,I890,I891,I898,I899,I972,I978,I979', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2324", "12A-17A":"NDQ2325", "18A-29A":"NDQ2326", "30A-59A":"NDQ2327", "60A+":"NDQ2328"',
                "dbo.Rehabilit_FSM_SinCert('M6284', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2329", "12A-17A":"NDQ2330", "18A-29A":"NDQ2331", "30A-59A":"NDQ2332", "60A+":"NDQ2333"',
                "dbo.Rehabilit_FSM_SinCert('M255,M791,M797,R521,R522,R529', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2334", "12A-17A":"NDQ2335", "18A-29A":"NDQ2336", "30A-59A":"NDQ2337", "60A+":"NDQ2338"',
                "dbo.Rehabilit_FSM_SinCert('T200,T201,T202,T203,T204,T205,T206,T207,T208,T209,T200,T201,T202,T203,T204,T205,T206,T207,T210,T220,T230,T240,T250,T260,T270,T280,T290,T300,T310,T311,T312,T313,T314,T315,T316,T317,T318,T319,T310,T311,T312,T313,T314,T315,T316,T317,T318,T319,T320,T321,T322,T323,T324,T325,T326,T327,T328,T329,T320,T321,T322,T323,T324,T325,T326,T327,T328,T329,T330,T331,T332,T333,T334,T335,T336,T337,T338,T339,T330,T331,T332,T333,T334,T335,T336,T337,T338,T339,T340,T341,T342,T343,T344,T345,T346,T347,T348,T349,T340,T341,T342,T343,T344,T345,T346,T347,T348,T349,T350,T351,T352,T353,T354,T355,T356,T357,T358,T359,T350,T351,T352,T353,T354,T355,T356,T357', 'N,C,R');"
            ),


        ],
        "FACT_DISC_SNAPSHOT_REHABFISIC_BL3": [
            (
                '"0d-11A":"NDQ2339", "12A-17A":"NDQ2340", "18A-29A":"NDQ2341", "30A-59A":"NDQ2342", "60A+":"NDQ2343"',
                "dbo.Rehabilit_FSM_ServEval_NCR('A178,A1782,A800,B690,B91X,B941,C720,C721,D334,G041,G042,G048,G049,G050,G051,G052,G058,G114,G320,G35X,G360,G373,G820,G821,G822,G823,G824,G825,G834,G950,G951,G952,G958,G959,G971,M471,M480,M500,Q050,Q051,Q052,Q053,Q054,Q055,Q056,Q057,Q058,Q059,Q060,Q061,Q062,Q063,Q064,Q068,Q069,S140,S141,S240,S241,S340,S341,T093,T889', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2344", "12A-17A":"NDQ2345", "18A-29A":"NDQ2346", "30A-59A":"NDQ2347", "60A+":"NDQ2348"',
                "dbo.Rehabilit_FSM_ServEval_NCR('Q650,Q651,Q652,Q653,Q654,Q655,Q656,Q658,Q659,Q660,Q661,Q662,Q663,Q664,Q665,Q666,Q667,Q668,Q669,Q671,Q672,Q673,Q674,Q675,Q676,Q677,Q678,Q740,Q741,Q742,Q743,Q744,Q745,Q746,Q747,Q748,Q749,Q740,Q741,Q742,Q748,Q749,Q750,Q751,Q752,Q753,Q754,Q755,Q758,Q759,Q760,Q761,Q762,Q763,Q764,Q765,Q766,Q767,Q768,Q769,Q771,Q772,Q773,Q775,Q776,Q777,Q778,Q779,Q780,Q781,Q782,Q783,Q784,Q785,Q786,Q788,Q789,Q790,Q791,Q792,Q793,Q794,Q795,Q796,Q798,Q799', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2349", "12A-17A":"NDQ2350", "18A-29A":"NDQ2351", "30A-59A":"NDQ2352", "60A+":"NDQ2353"',
                "dbo.Rehabilit_FSM_ServEval_NCR('M150,M151,M152,M153,M154,M158,M159,M160,M161,M162,M163,M164,M165,M166,M167,M169,M170,M171,M172,M173,M174,M175,M179,M180,M181,M182,M183,M184,M185,M189,M190,M191,M192,M198,M199,M224,M235,M238,M239,M241,M470,M472,M478,M479', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2354", "12A-17A":"NDQ2355", "18A-29A":"NDQ2356", "30A-59A":"NDQ2357", "60A+":"NDQ2358"',
                "dbo.Rehabilit_FSM_ServEval_NCR('A321,B582,F83X,G000,G001,G002,G003,G008,G009,G000,G001,G002,G003,G008,G009,G010,G011,G012,G013,G014,G015,G016,G017,G018,G019,G020,G021,G022,G023,G024,G025,G026,G027,G028,G029,G030,G031,G032,G033,G034,G035,G036,G037,G038,G039,G040,G041,G042,G043,G044,G045,G046,G047,G048,G049,G042,G050,G051,G052,G053,G054,G055,G056,G057,G058,G059,G800,G801,G802,G803,G804,G808,G809,G820,G821,G822,G823,G824,G825,G826,G827,G828,G829,G910,G911,G912,G913,G914,G915,G916,G917,G918,G919,G910,G911,G912,G913,G918,G919,P900,P901,P902,P903,P904,P905,P906,P907,P908,P909,P940,P941,P942,P948,P949,Q000,Q001,Q002,Q003,Q004,Q005,Q006,Q007,Q008,Q009,Q010,Q011,Q012,Q013,Q014,Q015,Q016,Q017,Q018,Q019,Q020,Q021,Q022,Q023,Q024,Q025,Q026,Q027,Q028,Q029,Q030,Q031,Q032,Q033,Q034,Q035,Q036,Q037,Q038,Q039,Q040,Q041,Q042,Q043,Q044,Q045,Q046,Q047,Q048,Q049,Q070,Q071,Q072,Q073,Q074,Q075,Q076,Q077,Q078,Q079', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2359", "12A-17A":"NDQ2360", "18A-29A":"NDQ2361", "30A-59A":"NDQ2362", "60A+":"NDQ2363"',
                "dbo.Rehabilit_FSM_ServEval_NCR('Q900,Q901,Q902,Q909', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2364", "12A-17A":"NDQ2365", "18A-29A":"NDQ2366", "30A-59A":"NDQ2367", "60A+":"NDQ2368"',
                "dbo.Rehabilit_FSM_ServEval_NCR('S480,S481,S489,S580,S581,S589,S680,S681,S682,S683,S684,S688,S689,T050,T051,T052,T056,T058,T059,Z890,Z891,Z892,Z893,Z898', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2369", "12A-17A":"NDQ2370", "18A-29A":"NDQ2371", "30A-59A":"NDQ2372", "60A+":"NDQ2373"',
                "dbo.Rehabilit_FSM_ServEval_NCR('S780,S781,S789,S880,S881,S889,S980,S981,S982,S983,S984,T053,T054,T055,Z894,Z895,Z896,Z897', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2374", "12A-17A":"NDQ2375", "18A-29A":"NDQ2376", "30A-59A":"NDQ2377", "60A+":"NDQ2378"',
                "dbo.Rehabilit_FSM_ServEval_NCR('G733,G732,G731,G730,G729,G728,G724,G723,G721,G720,G719,G718,G713,G712,G711,G710,G709,G708,G702,G701,G700,G129,G121,G120', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2379", "12A-17A":"NDQ2380", "18A-29A":"NDQ2381", "30A-59A":"NDQ2382", "60A+":"NDQ2383"',
                "dbo.Rehabilit_FSM_ServEval_NCR('G500,G501,G508,G509,G510,G511,G512,G513,G514,G518,G519,G530,G531,G532,G533,G538,G540,G541,G542,G543,G544,G545,G546,G547,G548,G549,G550,G551,G552,G553,G558,G560,G561,G562,G563,G564,G568,G569,G570,G571,G572,G573,G574,G575,G576,G578,G579,G580,G587,G588,G589,G590,G598,G600,G601,G602,G603,G608,G609,G610,G611,G618,G619,G620,G621,G622,G628,G629,G630,G631,G632,G633,G634,G635,G636,G638,G64X,M501,M511,M541,M543,M544,M792,P140,P141,P142,P143,P148,P149,S142,S143,S242,S243,S342,S343,S344,S346,S440,S441,S442,S443,S444,S445,S447,S448,S449,S540,S541,S542,S543,S547,S548,S549,S640,S641,S642,S643,S644,S647,S648,S649,S840,S841,S842,S847,S848,S849,S940,S941,S942,S943,S947,S948,S949', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2384", "12A-17A":"NDQ2385", "18A-29A":"NDQ2386", "30A-59A":"NDQ2387", "60A+":"NDQ2388"',
                "dbo.Rehabilit_FSM_ServEval_NCR('G811,I600,I601,I602,I603,I604,I605,I606,I607,I608,I609,I610,I611,I612,I613,I614,I615,I616,I618,I619,I620,I621,I629,I630,I631,I632,I633,I634,I635,I636,I638,I639,I64X,I650,I651,I652,I653,I658,I659,I660,I661,I662,I663,I664,I668,I669,I670,I671,I672,I673,I674,I675,I676,I677,I678,I679,I680,I681,I682,I688,I694,I690,Q282', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2389", "12A-17A":"NDQ2390", "18A-29A":"NDQ2391", "30A-59A":"NDQ2392", "60A+":"NDQ2393"',
                "dbo.Rehabilit_FSM_ServEval_NCR('G20X,G210,G211,G212,G213,G214,G218,G219,G22X', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2394", "12A-17A":"NDQ2395", "18A-29A":"NDQ2396", "30A-59A":"NDQ2397", "60A+":"NDQ2398"',
                "dbo.Rehabilit_FSM_ServEval_NCR('M400,M401,M402,M403,M404,M405,M410,M411,M412,M413,M414,M415,M418,M419', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2399", "12A-17A":"NDQ2400", "18A-29A":"NDQ2401", "30A-59A":"NDQ2402", "60A+":"NDQ2403"',
                "dbo.Rehabilit_FSM_ServEval_NCR('M420,M421,M429,M45X,M491,M492,M493,M494,M495,M498', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2404", "12A-17A":"NDQ2405", "18A-29A":"NDQ2406", "30A-59A":"NDQ2407", "60A+":"NDQ2408"',
                "dbo.Rehabilit_FSM_ServEval_NCR('G992,M501,M502,M503,M508,M509,M510,M512,M513,M514,M518,M519,M530,M531,M532,M533,M538,M539', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2409", "12A-17A":"NDQ2410", "18A-29A":"NDQ2411", "30A-59A":"NDQ2412", "60A+":"NDQ2413"',
                "dbo.Rehabilit_FSM_ServEval_NCR('M542,M545,M546,M548,M549', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2414", "12A-17A":"NDQ2415", "18A-29A":"NDQ2416", "30A-59A":"NDQ2417", "60A+":"NDQ2418"',
                "dbo.Rehabilit_FSM_ServEval_NCR('M430,M431,M432', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2419", "12A-17A":"NDQ2420", "18A-29A":"NDQ2421", "30A-59A":"NDQ2422", "60A+":"NDQ2423"',
                "dbo.Rehabilit_FSM_ServEval_NCR('Q241,Q670,Q715,Q716,Q718,Q719,Q743,Q770,Q774', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2424", "12A-17A":"NDQ2425", "18A-29A":"NDQ2426", "30A-59A":"NDQ2427", "60A+":"NDQ2428"',
                "dbo.Rehabilit_FSM_ServEval_NCR('M910,M911,M912,M913,M918,M919,M920,M921,M922,M923,M924,M925,M926,M927,M928,M929,M930,M931,M932,M938,M939,Q720,Q721,Q722,Q723,Q724,Q725,Q726,Q727,Q728,Q729,Q730,Q731,Q738,Q710,Q711,Q712,Q713', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2429", "12A-17A":"NDQ2430", "18A-29A":"NDQ2431", "30A-59A":"NDQ2432", "60A+":"NDQ2433"',
                "dbo.Rehabilit_FSM_ServEval_NCR('M960,M961,M962,M963,M964,M968,M969', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2434", "12A-17A":"NDQ2435", "18A-29A":"NDQ2436", "30A-59A":"NDQ2437", "60A+":"NDQ2438"',
                "dbo.Rehabilit_FSM_ServEval_NCR('I090,I091,I092,I098,I099,I200,I201,I208,I209,I210,I211,I212,I213,I214,I219,I260,I269,I270,I271,I272,I278,I279,I280,I281,I288,I289,I430,I431,I432,I438,I500,I501,I509,I520,I521,I528,I690,I691,I692,I693,I694,I730,I731,I738,I739,I99X,Q200,Q201,Q202,Q203,Q204,Q205,Q206,Q208,Q209,Z950,Z951,Z952', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2439", "12A-17A":"NDQ2440", "18A-29A":"NDQ2441", "30A-59A":"NDQ2442", "60A+":"NDQ2443"',
                "dbo.Rehabilit_FSM_ServEval_NCR('J1281,J1289,J180,J181,J182,J188,J189,J1891,J1892,J208,J220,J221,J222,J223,J224,J225,J226,J227,J228,J229,J40X,J410,J411,J418,J42X,J430,J431,J432,J438,J439,J440,J441,J448,J449,J450,J451,J458,J459,J4591,J46X,J47X,J680,J681,J682,J683,J684,J688,J689,J700,J701,J702,J703,J704,J708,J709,J800,J801,J802,J803,J804,J805,J806,J807,J808,J809,J841,J848,J960,J961,J969,J988,J981,J990,J991,J998', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2444", "12A-17A":"NDQ2445", "18A-29A":"NDQ2446", "30A-59A":"NDQ2447", "60A+":"NDQ2448"',
                "dbo.Rehabilit_FSM_ServEval_NCR('N311,N312,N318,N319,N320,N941,N942,N948,R102,R309', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2449", "12A-17A":"NDQ2450", "18A-29A":"NDQ2451", "30A-59A":"NDQ2452", "60A+":"NDQ2453"',
                "dbo.Rehabilit_FSM_ServEval_NCR('N393,N394,R15X,R32X', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2454", "12A-17A":"NDQ2455", "18A-29A":"NDQ2456", "30A-59A":"NDQ2457", "60A+":"NDQ2458"',
                "dbo.Rehabilit_FSM_ServEval_NCR('N812,N814,N815,N816,N818,N819', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2459", "12A-17A":"NDQ2460", "18A-29A":"NDQ2461", "30A-59A":"NDQ2462", "60A+":"NDQ2463"',
                "dbo.Rehabilit_FSM_ServEval_NCR('S000,S090,S091,S092,S097,S098,S099,S100,S101,S107,S108,S109,S197,S198,S199,S200,S201,S202,S203,S204,S207,S208,S290,S297,S298,S299,S300,S301,S302,S307,S308,S309,S390,S396,S397,S398,S399,S400,S407,S408,S409,S497,S498,S499,S500,S501,S507,S508,S509,S597,S598,S599,S600,S601,S602,S607,S608,S609,S697,S698,S699,S700,S701,S707,S708,S709,S797,S798,S799,S800,S801,S807,S808,S809,S897,S898,S899,S900,S901,S902,S903,S907,S908,S909,S997,S998,S999,T000,T001,T002,T003,T006,T008,T009,T07X,T08X,T140,T141,T142,T143,T144,T145,T146,T147,T148,T149,T900,T901,T902,T903,T904,T905,T908,T909,T910,T911,T912,T913,T914,T915,T918,T919,T920,T921,T922,T923,T924,T925,T926,T928,T929,T930,T931,T932,T933,T934,T935,T936,T938,T939,T940,T941,T950,T951,T952,T953,T954,T958,T959,T96X,T97X,T980,T981,T982,T983', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2464", "12A-17A":"NDQ2465", "18A-29A":"NDQ2466", "30A-59A":"NDQ2467", "60A+":"NDQ2468"',
                "dbo.Rehabilit_FSM_ServEval_NCR('M000,M001,M002,M008,M009,M300,M301,M302,M303,M308,M310,M311,M312,M313,M314,M315,M316,M317,M318,M319,M320,M321,M328,M329,M330,M331,M332,M339,M340,M341,M342,M348,M349,M350,M351,M352,M353,M354,M355,M356,M357,M358,M359,M360,M361,M362,M363,M364,M368,M600,M601,M602,M608,M609,M610,M611,M612,M613,M614,M615,M619,M620,M621,M622,M623,M624,M625,M626,M628,M629,M630,M631,M632,M633,M638,M650,M651,M652,M653,M654,M658,M659,M660,M661,M662,M663,M664,M665,M670,M671,M672,M673,M674,M678,M679,M680,M688,M800,M801,M802,M803,M804,M805,M808,M809,M850,M851,M852,M853,M854,M855,M856,M858,M859', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2469", "12A-17A":"NDQ2470", "18A-29A":"NDQ2471", "30A-59A":"NDQ2472", "60A+":"NDQ2473"',
                "dbo.Rehabilit_FSM_ServEval_NCR('M200,M201,M202,M203,M204,M205,M206,M210,M211,M212,M213,M214,M215,M216,M217,M218,M219,M220,M221,M222,M223,M228,M229,M230,M231,M232,M233,M234,M236,M240,M242,M243,M244,M245,M246,M247,M248,M249,M250,M251,M252,M253,M254,M256,M257,M258,M259,M759', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2474", "12A-17A":"NDQ2475", "18A-29A":"NDQ2476", "30A-59A":"NDQ2477", "60A+":"NDQ2478"',
                "dbo.Rehabilit_FSM_ServEval_NCR('A239,M490,M491,M860,M861,M862,M863,M864,M865,M866,M868,M869,M890,M891,M892,M893,M894,M895,M896,M898,M899', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2479", "12A-17A":"NDQ2480", "18A-29A":"NDQ2481", "30A-59A":"NDQ2482", "60A+":"NDQ2483"',
                "dbo.Rehabilit_FSM_ServEval_NCR('M998,M999', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2484", "12A-17A":"NDQ2485", "18A-29A":"NDQ2486", "30A-59A":"NDQ2487", "60A+":"NDQ2488"',
                "dbo.Rehabilit_FSM_ServEval_NCR('I890,I891,I892,I893,I894,I895,I896,I897,I898,I899,I890,I891,I898,I899,I972,I978,I979', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2489", "12A-17A":"NDQ2490", "18A-29A":"NDQ2491", "30A-59A":"NDQ2492", "60A+":"NDQ2493"',
                "dbo.Rehabilit_FSM_ServEval_NCR('M6284', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2494", "12A-17A":"NDQ2495", "18A-29A":"NDQ2496", "30A-59A":"NDQ2497", "60A+":"NDQ2498"',
                "dbo.Rehabilit_FSM_ServEval_NCR('M255,M791,M797,R521,R522,R529', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2499", "12A-17A":"NDQ2500", "18A-29A":"NDQ2501", "30A-59A":"NDQ2502", "60A+":"NDQ2503"',
                "dbo.Rehabilit_FSM_ServEval_NCR('T200,T201,T202,T203,T204,T205,T206,T207,T208,T209,T200,T201,T202,T203,T204,T205,T206,T207,T210,T220,T230,T240,T250,T260,T270,T280,T290,T300,T310,T311,T312,T313,T314,T315,T316,T317,T318,T319,T310,T311,T312,T313,T314,T315,T316,T317,T318,T319,T320,T321,T322,T323,T324,T325,T326,T327,T328,T329,T320,T321,T322,T323,T324,T325,T326,T327,T328,T329,T330,T331,T332,T333,T334,T335,T336,T337,T338,T339,T330,T331,T332,T333,T334,T335,T336,T337,T338,T339,T340,T341,T342,T343,T344,T345,T346,T347,T348,T349,T340,T341,T342,T343,T344,T345,T346,T347,T348,T349,T350,T351,T352,T353,T354,T355,T356,T357,T358,T359,T350,T351,T352,T353,T354,T355,T356,T357', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2504", "12A-17A":"NDQ2505", "18A-29A":"NDQ2506", "30A-59A":"NDQ2507", "60A+":"NDQ2508"',
                "dbo.Rehabilit_FSM_Ambulatoria_NCR('A178,A1782,A800,B690,B91X,B941,C720,C721,D334,G041,G042,G048,G049,G050,G051,G052,G058,G114,G320,G35X,G360,G373,G820,G821,G822,G823,G824,G825,G834,G950,G951,G952,G958,G959,G971,M471,M480,M500,Q050,Q051,Q052,Q053,Q054,Q055,Q056,Q057,Q058,Q059,Q060,Q061,Q062,Q063,Q064,Q068,Q069,S140,S141,S240,S241,S340,S341,T093,T889', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2509", "12A-17A":"NDQ2510", "18A-29A":"NDQ2511", "30A-59A":"NDQ2512", "60A+":"NDQ2513"',
                "dbo.Rehabilit_FSM_Ambulatoria_NCR('Q650,Q651,Q652,Q653,Q654,Q655,Q656,Q658,Q659,Q660,Q661,Q662,Q663,Q664,Q665,Q666,Q667,Q668,Q669,Q671,Q672,Q673,Q674,Q675,Q676,Q677,Q678,Q740,Q741,Q742,Q743,Q744,Q745,Q746,Q747,Q748,Q749,Q740,Q741,Q742,Q748,Q749,Q750,Q751,Q752,Q753,Q754,Q755,Q758,Q759,Q760,Q761,Q762,Q763,Q764,Q765,Q766,Q767,Q768,Q769,Q771,Q772,Q773,Q775,Q776,Q777,Q778,Q779,Q780,Q781,Q782,Q783,Q784,Q785,Q786,Q788,Q789,Q790,Q791,Q792,Q793,Q794,Q795,Q796,Q798,Q799', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2514", "12A-17A":"NDQ2515", "18A-29A":"NDQ2516", "30A-59A":"NDQ2517", "60A+":"NDQ2518"',
                "dbo.Rehabilit_FSM_Ambulatoria_NCR('M150,M151,M152,M153,M154,M158,M159,M160,M161,M162,M163,M164,M165,M166,M167,M169,M170,M171,M172,M173,M174,M175,M179,M180,M181,M182,M183,M184,M185,M189,M190,M191,M192,M198,M199,M224,M235,M238,M239,M241,M470,M472,M478,M479', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2519", "12A-17A":"NDQ2520", "18A-29A":"NDQ2521", "30A-59A":"NDQ2522", "60A+":"NDQ2523"',
                "dbo.Rehabilit_FSM_Ambulatoria_NCR('A321,B582,F83X,G000,G001,G002,G003,G008,G009,G000,G001,G002,G003,G008,G009,G010,G011,G012,G013,G014,G015,G016,G017,G018,G019,G020,G021,G022,G023,G024,G025,G026,G027,G028,G029,G030,G031,G032,G033,G034,G035,G036,G037,G038,G039,G040,G041,G042,G043,G044,G045,G046,G047,G048,G049,G042,G050,G051,G052,G053,G054,G055,G056,G057,G058,G059,G800,G801,G802,G803,G804,G808,G809,G820,G821,G822,G823,G824,G825,G826,G827,G828,G829,G910,G911,G912,G913,G914,G915,G916,G917,G918,G919,G910,G911,G912,G913,G918,G919,P900,P901,P902,P903,P904,P905,P906,P907,P908,P909,P940,P941,P942,P948,P949,Q000,Q001,Q002,Q003,Q004,Q005,Q006,Q007,Q008,Q009,Q010,Q011,Q012,Q013,Q014,Q015,Q016,Q017,Q018,Q019,Q020,Q021,Q022,Q023,Q024,Q025,Q026,Q027,Q028,Q029,Q030,Q031,Q032,Q033,Q034,Q035,Q036,Q037,Q038,Q039,Q040,Q041,Q042,Q043,Q044,Q045,Q046,Q047,Q048,Q049,Q070,Q071,Q072,Q073,Q074,Q075,Q076,Q077,Q078,Q079', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2524", "12A-17A":"NDQ2525", "18A-29A":"NDQ2526", "30A-59A":"NDQ2527", "60A+":"NDQ2528"',
                "dbo.Rehabilit_FSM_Ambulatoria_NCR('Q900,Q901,Q902,Q909', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2529", "12A-17A":"NDQ2530", "18A-29A":"NDQ2531", "30A-59A":"NDQ2532", "60A+":"NDQ2533"',
                "dbo.Rehabilit_FSM_Ambulatoria_NCR('S480,S481,S489,S580,S581,S589,S680,S681,S682,S683,S684,S688,S689,T050,T051,T052,T056,T058,T059,Z890,Z891,Z892,Z893,Z898', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2534", "12A-17A":"NDQ2535", "18A-29A":"NDQ2536", "30A-59A":"NDQ2537", "60A+":"NDQ2538"',
                "dbo.Rehabilit_FSM_Ambulatoria_NCR('S780,S781,S789,S880,S881,S889,S980,S981,S982,S983,S984,T053,T054,T055,Z894,Z895,Z896,Z897', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2539", "12A-17A":"NDQ2540", "18A-29A":"NDQ2541", "30A-59A":"NDQ2542", "60A+":"NDQ2543"',
                "dbo.Rehabilit_FSM_Ambulatoria_NCR('G733,G732,G731,G730,G729,G728,G724,G723,G721,G720,G719,G718,G713,G712,G711,G710,G709,G708,G702,G701,G700,G129,G121,G120', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2544", "12A-17A":"NDQ2545", "18A-29A":"NDQ2546", "30A-59A":"NDQ2547", "60A+":"NDQ2548"',
                "dbo.Rehabilit_FSM_Ambulatoria_NCR('G500,G501,G508,G509,G510,G511,G512,G513,G514,G518,G519,G530,G531,G532,G533,G538,G540,G541,G542,G543,G544,G545,G546,G547,G548,G549,G550,G551,G552,G553,G558,G560,G561,G562,G563,G564,G568,G569,G570,G571,G572,G573,G574,G575,G576,G578,G579,G580,G587,G588,G589,G590,G598,G600,G601,G602,G603,G608,G609,G610,G611,G618,G619,G620,G621,G622,G628,G629,G630,G631,G632,G633,G634,G635,G636,G638,G64X,M501,M511,M541,M543,M544,M792,P140,P141,P142,P143,P148,P149,S142,S143,S242,S243,S342,S343,S344,S346,S440,S441,S442,S443,S444,S445,S447,S448,S449,S540,S541,S542,S543,S547,S548,S549,S640,S641,S642,S643,S644,S647,S648,S649,S840,S841,S842,S847,S848,S849,S940,S941,S942,S943,S947,S948,S949', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2549", "12A-17A":"NDQ2550", "18A-29A":"NDQ2551", "30A-59A":"NDQ2552", "60A+":"NDQ2553"',
                "dbo.Rehabilit_FSM_Ambulatoria_NCR('G811,I600,I601,I602,I603,I604,I605,I606,I607,I608,I609,I610,I611,I612,I613,I614,I615,I616,I618,I619,I620,I621,I629,I630,I631,I632,I633,I634,I635,I636,I638,I639,I64X,I650,I651,I652,I653,I658,I659,I660,I661,I662,I663,I664,I668,I669,I670,I671,I672,I673,I674,I675,I676,I677,I678,I679,I680,I681,I682,I688,I694,I690,Q282', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2554", "12A-17A":"NDQ2555", "18A-29A":"NDQ2556", "30A-59A":"NDQ2557", "60A+":"NDQ2558"',
                "dbo.Rehabilit_FSM_Ambulatoria_NCR('G20X,G210,G211,G212,G213,G214,G218,G219,G22X', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2559", "12A-17A":"NDQ2560", "18A-29A":"NDQ2561", "30A-59A":"NDQ2562", "60A+":"NDQ2563"',
                "dbo.Rehabilit_FSM_Ambulatoria_NCR('M400,M401,M402,M403,M404,M405,M410,M411,M412,M413,M414,M415,M418,M419', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2564", "12A-17A":"NDQ2565", "18A-29A":"NDQ2566", "30A-59A":"NDQ2567", "60A+":"NDQ2568"',
                "dbo.Rehabilit_FSM_Ambulatoria_NCR('M420,M421,M429,M45X,M491,M492,M493,M494,M495,M498', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2569", "12A-17A":"NDQ2570", "18A-29A":"NDQ2571", "30A-59A":"NDQ2572", "60A+":"NDQ2573"',
                "dbo.Rehabilit_FSM_Ambulatoria_NCR('G992,M501,M502,M503,M508,M509,M510,M512,M513,M514,M518,M519,M530,M531,M532,M533,M538,M539', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2574", "12A-17A":"NDQ2575", "18A-29A":"NDQ2576", "30A-59A":"NDQ2577", "60A+":"NDQ2578"',
                "dbo.Rehabilit_FSM_Ambulatoria_NCR('M542,M545,M546,M548,M549', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2579", "12A-17A":"NDQ2580", "18A-29A":"NDQ2581", "30A-59A":"NDQ2582", "60A+":"NDQ2583"',
                "dbo.Rehabilit_FSM_Ambulatoria_NCR('M430,M431,M432', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2584", "12A-17A":"NDQ2585", "18A-29A":"NDQ2586", "30A-59A":"NDQ2587", "60A+":"NDQ2588"',
                "dbo.Rehabilit_FSM_Ambulatoria_NCR('Q241,Q670,Q715,Q716,Q718,Q719,Q743,Q770,Q774', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2589", "12A-17A":"NDQ2590", "18A-29A":"NDQ2591", "30A-59A":"NDQ2592", "60A+":"NDQ2593"',
                "dbo.Rehabilit_FSM_Ambulatoria_NCR('M910,M911,M912,M913,M918,M919,M920,M921,M922,M923,M924,M925,M926,M927,M928,M929,M930,M931,M932,M938,M939,Q720,Q721,Q722,Q723,Q724,Q725,Q726,Q727,Q728,Q729,Q730,Q731,Q738,Q710,Q711,Q712,Q713', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2594", "12A-17A":"NDQ2595", "18A-29A":"NDQ2596", "30A-59A":"NDQ2597", "60A+":"NDQ2598"',
                "dbo.Rehabilit_FSM_Ambulatoria_NCR('M960,M961,M962,M963,M964,M968,M969', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2599", "12A-17A":"NDQ2600", "18A-29A":"NDQ2601", "30A-59A":"NDQ2602", "60A+":"NDQ2603"',
                "dbo.Rehabilit_FSM_Ambulatoria_NCR('I090,I091,I092,I098,I099,I200,I201,I208,I209,I210,I211,I212,I213,I214,I219,I260,I269,I270,I271,I272,I278,I279,I280,I281,I288,I289,I430,I431,I432,I438,I500,I501,I509,I520,I521,I528,I690,I691,I692,I693,I694,I730,I731,I738,I739,I99X,Q200,Q201,Q202,Q203,Q204,Q205,Q206,Q208,Q209,Z950,Z951,Z952', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2604", "12A-17A":"NDQ2605", "18A-29A":"NDQ2606", "30A-59A":"NDQ2607", "60A+":"NDQ2608"',
                "dbo.Rehabilit_FSM_Ambulatoria_NCR('J1281,J1289,J180,J181,J182,J188,J189,J1891,J1892,J208,J220,J221,J222,J223,J224,J225,J226,J227,J228,J229,J40X,J410,J411,J418,J42X,J430,J431,J432,J438,J439,J440,J441,J448,J449,J450,J451,J458,J459,J4591,J46X,J47X,J680,J681,J682,J683,J684,J688,J689,J700,J701,J702,J703,J704,J708,J709,J800,J801,J802,J803,J804,J805,J806,J807,J808,J809,J841,J848,J960,J961,J969,J988,J981,J990,J991,J998', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2609", "12A-17A":"NDQ2610", "18A-29A":"NDQ2611", "30A-59A":"NDQ2612", "60A+":"NDQ2613"',
                "dbo.Rehabilit_FSM_Ambulatoria_NCR('N311,N312,N318,N319,N320,N941,N942,N948,R102,R309', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2614", "12A-17A":"NDQ2615", "18A-29A":"NDQ2616", "30A-59A":"NDQ2617", "60A+":"NDQ2618"',
                "dbo.Rehabilit_FSM_Ambulatoria_NCR('N393,N394,R15X,R32X', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2619", "12A-17A":"NDQ2620", "18A-29A":"NDQ2621", "30A-59A":"NDQ2622", "60A+":"NDQ2623"',
                "dbo.Rehabilit_FSM_Ambulatoria_NCR('N812,N814,N815,N816,N818,N819', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2624", "12A-17A":"NDQ2625", "18A-29A":"NDQ2626", "30A-59A":"NDQ2627", "60A+":"NDQ2628"',
                "dbo.Rehabilit_FSM_Ambulatoria_NCR('S000,S090,S091,S092,S097,S098,S099,S100,S101,S107,S108,S109,S197,S198,S199,S200,S201,S202,S203,S204,S207,S208,S290,S297,S298,S299,S300,S301,S302,S307,S308,S309,S390,S396,S397,S398,S399,S400,S407,S408,S409,S497,S498,S499,S500,S501,S507,S508,S509,S597,S598,S599,S600,S601,S602,S607,S608,S609,S697,S698,S699,S700,S701,S707,S708,S709,S797,S798,S799,S800,S801,S807,S808,S809,S897,S898,S899,S900,S901,S902,S903,S907,S908,S909,S997,S998,S999,T000,T001,T002,T003,T006,T008,T009,T07X,T08X,T140,T141,T142,T143,T144,T145,T146,T147,T148,T149,T900,T901,T902,T903,T904,T905,T908,T909,T910,T911,T912,T913,T914,T915,T918,T919,T920,T921,T922,T923,T924,T925,T926,T928,T929,T930,T931,T932,T933,T934,T935,T936,T938,T939,T940,T941,T950,T951,T952,T953,T954,T958,T959,T96X,T97X,T980,T981,T982,T983', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2629", "12A-17A":"NDQ2630", "18A-29A":"NDQ2631", "30A-59A":"NDQ2632", "60A+":"NDQ2633"',
                "dbo.Rehabilit_FSM_Ambulatoria_NCR('M000,M001,M002,M008,M009,M300,M301,M302,M303,M308,M310,M311,M312,M313,M314,M315,M316,M317,M318,M319,M320,M321,M328,M329,M330,M331,M332,M339,M340,M341,M342,M348,M349,M350,M351,M352,M353,M354,M355,M356,M357,M358,M359,M360,M361,M362,M363,M364,M368,M600,M601,M602,M608,M609,M610,M611,M612,M613,M614,M615,M619,M620,M621,M622,M623,M624,M625,M626,M628,M629,M630,M631,M632,M633,M638,M650,M651,M652,M653,M654,M658,M659,M660,M661,M662,M663,M664,M665,M670,M671,M672,M673,M674,M678,M679,M680,M688,M800,M801,M802,M803,M804,M805,M808,M809,M850,M851,M852,M853,M854,M855,M856,M858,M859', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2634", "12A-17A":"NDQ2635", "18A-29A":"NDQ2636", "30A-59A":"NDQ2637", "60A+":"NDQ2638"',
                "dbo.Rehabilit_FSM_Ambulatoria_NCR('M200,M201,M202,M203,M204,M205,M206,M210,M211,M212,M213,M214,M215,M216,M217,M218,M219,M220,M221,M222,M223,M228,M229,M230,M231,M232,M233,M234,M236,M240,M242,M243,M244,M245,M246,M247,M248,M249,M250,M251,M252,M253,M254,M256,M257,M258,M259,M759', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2639", "12A-17A":"NDQ2640", "18A-29A":"NDQ2641", "30A-59A":"NDQ2642", "60A+":"NDQ2643"',
                "dbo.Rehabilit_FSM_Ambulatoria_NCR('A239,M490,M491,M860,M861,M862,M863,M864,M865,M866,M868,M869,M890,M891,M892,M893,M894,M895,M896,M898,M899', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2644", "12A-17A":"NDQ2645", "18A-29A":"NDQ2646", "30A-59A":"NDQ2647", "60A+":"NDQ2648"',
                "dbo.Rehabilit_FSM_Ambulatoria_NCR('M998,M999', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2649", "12A-17A":"NDQ2650", "18A-29A":"NDQ2651", "30A-59A":"NDQ2652", "60A+":"NDQ2653"',
                "dbo.Rehabilit_FSM_Ambulatoria_NCR('I890,I891,I892,I893,I894,I895,I896,I897,I898,I899,I890,I891,I898,I899,I972,I978,I979', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2654", "12A-17A":"NDQ2655", "18A-29A":"NDQ2656", "30A-59A":"NDQ2657", "60A+":"NDQ2658"',
                "dbo.Rehabilit_FSM_Ambulatoria_NCR('M6284', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2659", "12A-17A":"NDQ2660", "18A-29A":"NDQ2661", "30A-59A":"NDQ2662", "60A+":"NDQ2663"',
                "dbo.Rehabilit_FSM_Ambulatoria_NCR('M255,M791,M797,R521,R522,R529', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2664", "12A-17A":"NDQ2665", "18A-29A":"NDQ2666", "30A-59A":"NDQ2667", "60A+":"NDQ2668"',
                "dbo.Rehabilit_FSM_Ambulatoria_NCR('T200,T201,T202,T203,T204,T205,T206,T207,T208,T209,T200,T201,T202,T203,T204,T205,T206,T207,T210,T220,T230,T240,T250,T260,T270,T280,T290,T300,T310,T311,T312,T313,T314,T315,T316,T317,T318,T319,T310,T311,T312,T313,T314,T315,T316,T317,T318,T319,T320,T321,T322,T323,T324,T325,T326,T327,T328,T329,T320,T321,T322,T323,T324,T325,T326,T327,T328,T329,T330,T331,T332,T333,T334,T335,T336,T337,T338,T339,T330,T331,T332,T333,T334,T335,T336,T337,T338,T339,T340,T341,T342,T343,T344,T345,T346,T347,T348,T349,T340,T341,T342,T343,T344,T345,T346,T347,T348,T349,T350,T351,T352,T353,T354,T355,T356,T357,T358,T359,T350,T351,T352,T353,T354,T355,T356,T357', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2669", "12A-17A":"NDQ2670", "18A-29A":"NDQ2671", "30A-59A":"NDQ2672", "60A+":"NDQ2673"',
                "dbo.RehabFisica_ReviFinal_NCR_Sl('A178,A1782,A800,B690,B91X,B941,C720,C721,D334,G041,G042,G048,G049,G050,G051,G052,G058,G114,G320,G35X,G360,G373,G820,G821,G822,G823,G824,G825,G834,G950,G951,G952,G958,G959,G971,M471,M480,M500,Q050,Q051,Q052,Q053,Q054,Q055,Q056,Q057,Q058,Q059,Q060,Q061,Q062,Q063,Q064,Q068,Q069,S140,S141,S240,S241,S340,S341,T093,T889', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2674", "12A-17A":"NDQ2675", "18A-29A":"NDQ2676", "30A-59A":"NDQ2677", "60A+":"NDQ2678"',
                "dbo.Rehabilit_FSM_ReviFinal_NCR('Q650,Q651,Q652,Q653,Q654,Q655,Q656,Q658,Q659,Q660,Q661,Q662,Q663,Q664,Q665,Q666,Q667,Q668,Q669,Q671,Q672,Q673,Q674,Q675,Q676,Q677,Q678,Q740,Q741,Q742,Q743,Q744,Q745,Q746,Q747,Q748,Q749,Q740,Q741,Q742,Q748,Q749,Q750,Q751,Q752,Q753,Q754,Q755,Q758,Q759,Q760,Q761,Q762,Q763,Q764,Q765,Q766,Q767,Q768,Q769,Q771,Q772,Q773,Q775,Q776,Q777,Q778,Q779,Q780,Q781,Q782,Q783,Q784,Q785,Q786,Q788,Q789,Q790,Q791,Q792,Q793,Q794,Q795,Q796,Q798,Q799', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2679", "12A-17A":"NDQ2680", "18A-29A":"NDQ2681", "30A-59A":"NDQ2682", "60A+":"NDQ2683"',
                "dbo.Rehabilit_FSM_ReviFinal_NCR('M150,M151,M152,M153,M154,M158,M159,M160,M161,M162,M163,M164,M165,M166,M167,M169,M170,M171,M172,M173,M174,M175,M179,M180,M181,M182,M183,M184,M185,M189,M190,M191,M192,M198,M199,M224,M235,M238,M239,M241,M470,M472,M478,M479', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2684", "12A-17A":"NDQ2685", "18A-29A":"NDQ2686", "30A-59A":"NDQ2687", "60A+":"NDQ2688"',
                "dbo.Rehabilit_FSM_ReviFinal_NCR('A321,B582,F83X,G000,G001,G002,G003,G008,G009,G000,G001,G002,G003,G008,G009,G010,G011,G012,G013,G014,G015,G016,G017,G018,G019,G020,G021,G022,G023,G024,G025,G026,G027,G028,G029,G030,G031,G032,G033,G034,G035,G036,G037,G038,G039,G040,G041,G042,G043,G044,G045,G046,G047,G048,G049,G042,G050,G051,G052,G053,G054,G055,G056,G057,G058,G059,G800,G801,G802,G803,G804,G808,G809,G820,G821,G822,G823,G824,G825,G826,G827,G828,G829,G910,G911,G912,G913,G914,G915,G916,G917,G918,G919,G910,G911,G912,G913,G918,G919,P900,P901,P902,P903,P904,P905,P906,P907,P908,P909,P940,P941,P942,P948,P949,Q000,Q001,Q002,Q003,Q004,Q005,Q006,Q007,Q008,Q009,Q010,Q011,Q012,Q013,Q014,Q015,Q016,Q017,Q018,Q019,Q020,Q021,Q022,Q023,Q024,Q025,Q026,Q027,Q028,Q029,Q030,Q031,Q032,Q033,Q034,Q035,Q036,Q037,Q038,Q039,Q040,Q041,Q042,Q043,Q044,Q045,Q046,Q047,Q048,Q049,Q070,Q071,Q072,Q073,Q074,Q075,Q076,Q077,Q078,Q079', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2689", "12A-17A":"NDQ2690", "18A-29A":"NDQ2691", "30A-59A":"NDQ2692", "60A+":"NDQ2693"',
                "dbo.Rehabilit_FSM_ReviFinal_NCR('Q900,Q901,Q902,Q909', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2694", "12A-17A":"NDQ2695", "18A-29A":"NDQ2696", "30A-59A":"NDQ2697", "60A+":"NDQ2698"',
                "dbo.Rehabilit_FSM_ReviFinal_NCR('S480,S481,S489,S580,S581,S589,S680,S681,S682,S683,S684,S688,S689,T050,T051,T052,T056,T058,T059,Z890,Z891,Z892,Z893,Z898', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2699", "12A-17A":"NDQ2700", "18A-29A":"NDQ2701", "30A-59A":"NDQ2702", "60A+":"NDQ2703"',
                "dbo.Rehabilit_FSM_ReviFinal_NCR('S780,S781,S789,S880,S881,S889,S980,S981,S982,S983,S984,T053,T054,T055,Z894,Z895,Z896,Z897', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2704", "12A-17A":"NDQ2705", "18A-29A":"NDQ2706", "30A-59A":"NDQ2707", "60A+":"NDQ2708"',
                "dbo.Rehabilit_FSM_ReviFinal_NCR('G733,G732,G731,G730,G729,G728,G724,G723,G721,G720,G719,G718,G713,G712,G711,G710,G709,G708,G702,G701,G700,G129,G121,G120', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2709", "12A-17A":"NDQ2710", "18A-29A":"NDQ2711", "30A-59A":"NDQ2712", "60A+":"NDQ2713"',
                "dbo.Rehabilit_FSM_ReviFinal_NCR('G500,G501,G508,G509,G510,G511,G512,G513,G514,G518,G519,G530,G531,G532,G533,G538,G540,G541,G542,G543,G544,G545,G546,G547,G548,G549,G550,G551,G552,G553,G558,G560,G561,G562,G563,G564,G568,G569,G570,G571,G572,G573,G574,G575,G576,G578,G579,G580,G587,G588,G589,G590,G598,G600,G601,G602,G603,G608,G609,G610,G611,G618,G619,G620,G621,G622,G628,G629,G630,G631,G632,G633,G634,G635,G636,G638,G64X,M501,M511,M541,M543,M544,M792,P140,P141,P142,P143,P148,P149,S142,S143,S242,S243,S342,S343,S344,S346,S440,S441,S442,S443,S444,S445,S447,S448,S449,S540,S541,S542,S543,S547,S548,S549,S640,S641,S642,S643,S644,S647,S648,S649,S840,S841,S842,S847,S848,S849,S940,S941,S942,S943,S947,S948,S949', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2714", "12A-17A":"NDQ2715", "18A-29A":"NDQ2716", "30A-59A":"NDQ2717", "60A+":"NDQ2718"',
                "dbo.Rehabilit_FSM_ReviFinal_NCR('G811,I600,I601,I602,I603,I604,I605,I606,I607,I608,I609,I610,I611,I612,I613,I614,I615,I616,I618,I619,I620,I621,I629,I630,I631,I632,I633,I634,I635,I636,I638,I639,I64X,I650,I651,I652,I653,I658,I659,I660,I661,I662,I663,I664,I668,I669,I670,I671,I672,I673,I674,I675,I676,I677,I678,I679,I680,I681,I682,I688,I694,I690,Q282', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2719", "12A-17A":"NDQ2720", "18A-29A":"NDQ2721", "30A-59A":"NDQ2722", "60A+":"NDQ2723"',
                "dbo.Rehabilit_FSM_ReviFinal_NCR('G20X,G210,G211,G212,G213,G214,G218,G219,G22X', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2724", "12A-17A":"NDQ2725", "18A-29A":"NDQ2726", "30A-59A":"NDQ2727", "60A+":"NDQ2728"',
                "dbo.Rehabilit_FSM_ReviFinal_NCR('M400,M401,M402,M403,M404,M405,M410,M411,M412,M413,M414,M415,M418,M419', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2729", "12A-17A":"NDQ2730", "18A-29A":"NDQ2731", "30A-59A":"NDQ2732", "60A+":"NDQ2733"',
                "dbo.Rehabilit_FSM_ReviFinal_NCR('M420,M421,M429,M45X,M491,M492,M493,M494,M495,M498', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2734", "12A-17A":"NDQ2735", "18A-29A":"NDQ2736", "30A-59A":"NDQ2737", "60A+":"NDQ2738"',
                "dbo.Rehabilit_FSM_ReviFinal_NCR('G992,M501,M502,M503,M508,M509,M510,M512,M513,M514,M518,M519,M530,M531,M532,M533,M538,M539', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2739", "12A-17A":"NDQ2740", "18A-29A":"NDQ2741", "30A-59A":"NDQ2742", "60A+":"NDQ2743"',
                "dbo.Rehabilit_FSM_ReviFinal_NCR('M542,M545,M546,M548,M549', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2744", "12A-17A":"NDQ2745", "18A-29A":"NDQ2746", "30A-59A":"NDQ2747", "60A+":"NDQ2748"',
                "dbo.Rehabilit_FSM_ReviFinal_NCR('M430,M431,M432', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2749", "12A-17A":"NDQ2750", "18A-29A":"NDQ2751", "30A-59A":"NDQ2752", "60A+":"NDQ2753"',
                "dbo.Rehabilit_FSM_ReviFinal_NCR('Q241,Q670,Q715,Q716,Q718,Q719,Q743,Q770,Q774', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2754", "12A-17A":"NDQ2755", "18A-29A":"NDQ2756", "30A-59A":"NDQ2757", "60A+":"NDQ2758"',
                "dbo.Rehabilit_FSM_ReviFinal_NCR('M910,M911,M912,M913,M918,M919,M920,M921,M922,M923,M924,M925,M926,M927,M928,M929,M930,M931,M932,M938,M939,Q720,Q721,Q722,Q723,Q724,Q725,Q726,Q727,Q728,Q729,Q730,Q731,Q738,Q710,Q711,Q712,Q713', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2759", "12A-17A":"NDQ2760", "18A-29A":"NDQ2761", "30A-59A":"NDQ2762", "60A+":"NDQ2763"',
                "dbo.Rehabilit_FSM_ReviFinal_NCR('M960,M961,M962,M963,M964,M968,M969', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2764", "12A-17A":"NDQ2765", "18A-29A":"NDQ2766", "30A-59A":"NDQ2767", "60A+":"NDQ2768"',
                "dbo.Rehabilit_FSM_ReviFinal_NCR('I090,I091,I092,I098,I099,I200,I201,I208,I209,I210,I211,I212,I213,I214,I219,I260,I269,I270,I271,I272,I278,I279,I280,I281,I288,I289,I430,I431,I432,I438,I500,I501,I509,I520,I521,I528,I690,I691,I692,I693,I694,I730,I731,I738,I739,I99X,Q200,Q201,Q202,Q203,Q204,Q205,Q206,Q208,Q209,Z950,Z951,Z952', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2769", "12A-17A":"NDQ2770", "18A-29A":"NDQ2771", "30A-59A":"NDQ2772", "60A+":"NDQ2773"',
                "dbo.Rehabilit_FSM_ReviFinal_NCR('J1281,J1289,J180,J181,J182,J188,J189,J1891,J1892,J208,J220,J221,J222,J223,J224,J225,J226,J227,J228,J229,J40X,J410,J411,J418,J42X,J430,J431,J432,J438,J439,J440,J441,J448,J449,J450,J451,J458,J459,J4591,J46X,J47X,J680,J681,J682,J683,J684,J688,J689,J700,J701,J702,J703,J704,J708,J709,J800,J801,J802,J803,J804,J805,J806,J807,J808,J809,J841,J848,J960,J961,J969,J988,J981,J990,J991,J998', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2774", "12A-17A":"NDQ2775", "18A-29A":"NDQ2776", "30A-59A":"NDQ2777", "60A+":"NDQ2778"',
                "dbo.Rehabilit_FSM_ReviFinal_NCR('N311,N312,N318,N319,N320,N941,N942,N948,R102,R309', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2779", "12A-17A":"NDQ2780", "18A-29A":"NDQ2781", "30A-59A":"NDQ2782", "60A+":"NDQ2783"',
                "dbo.Rehabilit_FSM_ReviFinal_NCR('N393,N394,R15X,R32X', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2784", "12A-17A":"NDQ2785", "18A-29A":"NDQ2786", "30A-59A":"NDQ2787", "60A+":"NDQ2788"',
                "dbo.Rehabilit_FSM_ReviFinal_NCR('N812,N814,N815,N816,N818,N819', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2789", "12A-17A":"NDQ2790", "18A-29A":"NDQ2791", "30A-59A":"NDQ2792", "60A+":"NDQ2793"',
                "dbo.Rehabilit_FSM_ReviFinal_NCR('S000,S090,S091,S092,S097,S098,S099,S100,S101,S107,S108,S109,S197,S198,S199,S200,S201,S202,S203,S204,S207,S208,S290,S297,S298,S299,S300,S301,S302,S307,S308,S309,S390,S396,S397,S398,S399,S400,S407,S408,S409,S497,S498,S499,S500,S501,S507,S508,S509,S597,S598,S599,S600,S601,S602,S607,S608,S609,S697,S698,S699,S700,S701,S707,S708,S709,S797,S798,S799,S800,S801,S807,S808,S809,S897,S898,S899,S900,S901,S902,S903,S907,S908,S909,S997,S998,S999,T000,T001,T002,T003,T006,T008,T009,T07X,T08X,T140,T141,T142,T143,T144,T145,T146,T147,T148,T149,T900,T901,T902,T903,T904,T905,T908,T909,T910,T911,T912,T913,T914,T915,T918,T919,T920,T921,T922,T923,T924,T925,T926,T928,T929,T930,T931,T932,T933,T934,T935,T936,T938,T939,T940,T941,T950,T951,T952,T953,T954,T958,T959,T96X,T97X,T980,T981,T982,T983', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2794", "12A-17A":"NDQ2795", "18A-29A":"NDQ2796", "30A-59A":"NDQ2797", "60A+":"NDQ2798"',
                "dbo.Rehabilit_FSM_ReviFinal_NCR('M000,M001,M002,M008,M009,M300,M301,M302,M303,M308,M310,M311,M312,M313,M314,M315,M316,M317,M318,M319,M320,M321,M328,M329,M330,M331,M332,M339,M340,M341,M342,M348,M349,M350,M351,M352,M353,M354,M355,M356,M357,M358,M359,M360,M361,M362,M363,M364,M368,M600,M601,M602,M608,M609,M610,M611,M612,M613,M614,M615,M619,M620,M621,M622,M623,M624,M625,M626,M628,M629,M630,M631,M632,M633,M638,M650,M651,M652,M653,M654,M658,M659,M660,M661,M662,M663,M664,M665,M670,M671,M672,M673,M674,M678,M679,M680,M688,M800,M801,M802,M803,M804,M805,M808,M809,M850,M851,M852,M853,M854,M855,M856,M858,M859', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2799", "12A-17A":"NDQ2800", "18A-29A":"NDQ2801", "30A-59A":"NDQ2802", "60A+":"NDQ2803"',
                "dbo.Rehabilit_FSM_ReviFinal_NCR('M200,M201,M202,M203,M204,M205,M206,M210,M211,M212,M213,M214,M215,M216,M217,M218,M219,M220,M221,M222,M223,M228,M229,M230,M231,M232,M233,M234,M236,M240,M242,M243,M244,M245,M246,M247,M248,M249,M250,M251,M252,M253,M254,M256,M257,M258,M259,M759', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2804", "12A-17A":"NDQ2805", "18A-29A":"NDQ2806", "30A-59A":"NDQ2807", "60A+":"NDQ2808"',
                "dbo.Rehabilit_FSM_ReviFinal_NCR('A239,M490,M491,M860,M861,M862,M863,M864,M865,M866,M868,M869,M890,M891,M892,M893,M894,M895,M896,M898,M899', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2809", "12A-17A":"NDQ2810", "18A-29A":"NDQ2811", "30A-59A":"NDQ2812", "60A+":"NDQ2813"',
                "dbo.Rehabilit_FSM_ReviFinal_NCR('M998,M999', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2814", "12A-17A":"NDQ2815", "18A-29A":"NDQ2816", "30A-59A":"NDQ2817", "60A+":"NDQ2818"',
                "dbo.Rehabilit_FSM_ReviFinal_NCR('I890,I891,I892,I893,I894,I895,I896,I897,I898,I899,I890,I891,I898,I899,I972,I978,I979', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2819", "12A-17A":"NDQ2820", "18A-29A":"NDQ2821", "30A-59A":"NDQ2822", "60A+":"NDQ2823"',
                "dbo.Rehabilit_FSM_ReviFinal_NCR('M6284', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2824", "12A-17A":"NDQ2825", "18A-29A":"NDQ2826", "30A-59A":"NDQ2827", "60A+":"NDQ2828"',
                "dbo.Rehabilit_FSM_ReviFinal_NCR('M255,M791,M797,R521,R522,R529', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2829", "12A-17A":"NDQ2830", "18A-29A":"NDQ2831", "30A-59A":"NDQ2832", "60A+":"NDQ2833"',
                "dbo.Rehabilit_FSM_ReviFinal_NCR('T200,T201,T202,T203,T204,T205,T206,T207,T208,T209,T200,T201,T202,T203,T204,T205,T206,T207,T210,T220,T230,T240,T250,T260,T270,T280,T290,T300,T310,T311,T312,T313,T314,T315,T316,T317,T318,T319,T310,T311,T312,T313,T314,T315,T316,T317,T318,T319,T320,T321,T322,T323,T324,T325,T326,T327,T328,T329,T320,T321,T322,T323,T324,T325,T326,T327,T328,T329,T330,T331,T332,T333,T334,T335,T336,T337,T338,T339,T330,T331,T332,T333,T334,T335,T336,T337,T338,T339,T340,T341,T342,T343,T344,T345,T346,T347,T348,T349,T340,T341,T342,T343,T344,T345,T346,T347,T348,T349,T350,T351,T352,T353,T354,T355,T356,T357,T358,T359,T350,T351,T352,T353,T354,T355,T356,T357', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2834", "12A-17A":"NDQ2835", "18A-29A":"NDQ2836", "30A-59A":"NDQ2837", "60A+":"NDQ2838"',
                "dbo.Rehabilit_FSM_Telemed('A178,A1782,A800,B690,B91X,B941,C720,C721,D334,G041,G042,G048,G049,G050,G051,G052,G058,G114,G320,G35X,G360,G373,G820,G821,G822,G823,G824,G825,G834,G950,G951,G952,G958,G959,G971,M471,M480,M500,Q050,Q051,Q052,Q053,Q054,Q055,Q056,Q057,Q058,Q059,Q060,Q061,Q062,Q063,Q064,Q068,Q069,S140,S141,S240,S241,S340,S341,T093,T889', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2839", "12A-17A":"NDQ2840", "18A-29A":"NDQ2841", "30A-59A":"NDQ2842", "60A+":"NDQ2843"',
                "dbo.Rehabilit_FSM_Telemed('Q650,Q651,Q652,Q653,Q654,Q655,Q656,Q658,Q659,Q660,Q661,Q662,Q663,Q664,Q665,Q666,Q667,Q668,Q669,Q671,Q672,Q673,Q674,Q675,Q676,Q677,Q678,Q740,Q741,Q742,Q743,Q744,Q745,Q746,Q747,Q748,Q749,Q740,Q741,Q742,Q748,Q749,Q750,Q751,Q752,Q753,Q754,Q755,Q758,Q759,Q760,Q761,Q762,Q763,Q764,Q765,Q766,Q767,Q768,Q769,Q771,Q772,Q773,Q775,Q776,Q777,Q778,Q779,Q780,Q781,Q782,Q783,Q784,Q785,Q786,Q788,Q789,Q790,Q791,Q792,Q793,Q794,Q795,Q796,Q798,Q799', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2844", "12A-17A":"NDQ2845", "18A-29A":"NDQ2846", "30A-59A":"NDQ2847", "60A+":"NDQ2848"',
                "dbo.Rehabilit_FSM_Telemed('M150,M151,M152,M153,M154,M158,M159,M160,M161,M162,M163,M164,M165,M166,M167,M169,M170,M171,M172,M173,M174,M175,M179,M180,M181,M182,M183,M184,M185,M189,M190,M191,M192,M198,M199,M224,M235,M238,M239,M241,M470,M472,M478,M479', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2849", "12A-17A":"NDQ2850", "18A-29A":"NDQ2851", "30A-59A":"NDQ2852", "60A+":"NDQ2853"',
                "dbo.Rehabilit_FSM_Telemed('A321,B582,F83X,G000,G001,G002,G003,G008,G009,G000,G001,G002,G003,G008,G009,G010,G011,G012,G013,G014,G015,G016,G017,G018,G019,G020,G021,G022,G023,G024,G025,G026,G027,G028,G029,G030,G031,G032,G033,G034,G035,G036,G037,G038,G039,G040,G041,G042,G043,G044,G045,G046,G047,G048,G049,G042,G050,G051,G052,G053,G054,G055,G056,G057,G058,G059,G800,G801,G802,G803,G804,G808,G809,G820,G821,G822,G823,G824,G825,G826,G827,G828,G829,G910,G911,G912,G913,G914,G915,G916,G917,G918,G919,G910,G911,G912,G913,G918,G919,P900,P901,P902,P903,P904,P905,P906,P907,P908,P909,P940,P941,P942,P948,P949,Q000,Q001,Q002,Q003,Q004,Q005,Q006,Q007,Q008,Q009,Q010,Q011,Q012,Q013,Q014,Q015,Q016,Q017,Q018,Q019,Q020,Q021,Q022,Q023,Q024,Q025,Q026,Q027,Q028,Q029,Q030,Q031,Q032,Q033,Q034,Q035,Q036,Q037,Q038,Q039,Q040,Q041,Q042,Q043,Q044,Q045,Q046,Q047,Q048,Q049,Q070,Q071,Q072,Q073,Q074,Q075,Q076,Q077,Q078,Q079', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2854", "12A-17A":"NDQ2855", "18A-29A":"NDQ2856", "30A-59A":"NDQ2857", "60A+":"NDQ2858"',
                "dbo.Rehabilit_FSM_Telemed('Q900,Q901,Q902,Q909', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2859", "12A-17A":"NDQ2860", "18A-29A":"NDQ2861", "30A-59A":"NDQ2862", "60A+":"NDQ2863"',
                "dbo.Rehabilit_FSM_Telemed('S480,S481,S489,S580,S581,S589,S680,S681,S682,S683,S684,S688,S689,T050,T051,T052,T056,T058,T059,Z890,Z891,Z892,Z893,Z898', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2864", "12A-17A":"NDQ2865", "18A-29A":"NDQ2866", "30A-59A":"NDQ2867", "60A+":"NDQ2868"',
                "dbo.Rehabilit_FSM_Telemed('S780,S781,S789,S880,S881,S889,S980,S981,S982,S983,S984,T053,T054,T055,Z894,Z895,Z896,Z897', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2869", "12A-17A":"NDQ2870", "18A-29A":"NDQ2871", "30A-59A":"NDQ2872", "60A+":"NDQ2873"',
                "dbo.Rehabilit_FSM_Telemed('G733,G732,G731,G730,G729,G728,G724,G723,G721,G720,G719,G718,G713,G712,G711,G710,G709,G708,G702,G701,G700,G129,G121,G120', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2874", "12A-17A":"NDQ2875", "18A-29A":"NDQ2876", "30A-59A":"NDQ2877", "60A+":"NDQ2878"',
                "dbo.Rehabilit_FSM_Telemed('G500,G501,G508,G509,G510,G511,G512,G513,G514,G518,G519,G530,G531,G532,G533,G538,G540,G541,G542,G543,G544,G545,G546,G547,G548,G549,G550,G551,G552,G553,G558,G560,G561,G562,G563,G564,G568,G569,G570,G571,G572,G573,G574,G575,G576,G578,G579,G580,G587,G588,G589,G590,G598,G600,G601,G602,G603,G608,G609,G610,G611,G618,G619,G620,G621,G622,G628,G629,G630,G631,G632,G633,G634,G635,G636,G638,G64X,M501,M511,M541,M543,M544,M792,P140,P141,P142,P143,P148,P149,S142,S143,S242,S243,S342,S343,S344,S346,S440,S441,S442,S443,S444,S445,S447,S448,S449,S540,S541,S542,S543,S547,S548,S549,S640,S641,S642,S643,S644,S647,S648,S649,S840,S841,S842,S847,S848,S849,S940,S941,S942,S943,S947,S948,S949', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2879", "12A-17A":"NDQ2880", "18A-29A":"NDQ2881", "30A-59A":"NDQ2882", "60A+":"NDQ2883"',
                "dbo.Rehabilit_FSM_Telemed('G811,I600,I601,I602,I603,I604,I605,I606,I607,I608,I609,I610,I611,I612,I613,I614,I615,I616,I618,I619,I620,I621,I629,I630,I631,I632,I633,I634,I635,I636,I638,I639,I64X,I650,I651,I652,I653,I658,I659,I660,I661,I662,I663,I664,I668,I669,I670,I671,I672,I673,I674,I675,I676,I677,I678,I679,I680,I681,I682,I688,I694,I690,Q282', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2884", "12A-17A":"NDQ2885", "18A-29A":"NDQ2886", "30A-59A":"NDQ2887", "60A+":"NDQ2888"',
                "dbo.Rehabilit_FSM_Telemed('G20X,G210,G211,G212,G213,G214,G218,G219,G22X', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2889", "12A-17A":"NDQ2890", "18A-29A":"NDQ2891", "30A-59A":"NDQ2892", "60A+":"NDQ2893"',
                "dbo.Rehabilit_FSM_Telemed('M400,M401,M402,M403,M404,M405,M410,M411,M412,M413,M414,M415,M418,M419', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2894", "12A-17A":"NDQ2895", "18A-29A":"NDQ2896", "30A-59A":"NDQ2897", "60A+":"NDQ2898"',
                "dbo.Rehabilit_FSM_Telemed('M420,M421,M429,M45X,M491,M492,M493,M494,M495,M498', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2899", "12A-17A":"NDQ2900", "18A-29A":"NDQ2901", "30A-59A":"NDQ2902", "60A+":"NDQ2903"',
                "dbo.Rehabilit_FSM_Telemed('G992,M501,M502,M503,M508,M509,M510,M512,M513,M514,M518,M519,M530,M531,M532,M533,M538,M539', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2904", "12A-17A":"NDQ2905", "18A-29A":"NDQ2906", "30A-59A":"NDQ2907", "60A+":"NDQ2908"',
                "dbo.Rehabilit_FSM_Telemed('M542,M545,M546,M548,M549', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2909", "12A-17A":"NDQ2910", "18A-29A":"NDQ2911", "30A-59A":"NDQ2912", "60A+":"NDQ2913"',
                "dbo.Rehabilit_FSM_Telemed('M430,M431,M432', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2914", "12A-17A":"NDQ2915", "18A-29A":"NDQ2916", "30A-59A":"NDQ2917", "60A+":"NDQ2918"',
                "dbo.Rehabilit_FSM_Telemed('Q241,Q670,Q715,Q716,Q718,Q719,Q743,Q770,Q774', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2919", "12A-17A":"NDQ2920", "18A-29A":"NDQ2921", "30A-59A":"NDQ2922", "60A+":"NDQ2923"',
                "dbo.Rehabilit_FSM_Telemed('M910,M911,M912,M913,M918,M919,M920,M921,M922,M923,M924,M925,M926,M927,M928,M929,M930,M931,M932,M938,M939,Q720,Q721,Q722,Q723,Q724,Q725,Q726,Q727,Q728,Q729,Q730,Q731,Q738,Q710,Q711,Q712,Q713', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2924", "12A-17A":"NDQ2925", "18A-29A":"NDQ2926", "30A-59A":"NDQ2927", "60A+":"NDQ2928"',
                "dbo.Rehabilit_FSM_Telemed('M960,M961,M962,M963,M964,M968,M969', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2929", "12A-17A":"NDQ2930", "18A-29A":"NDQ2931", "30A-59A":"NDQ2932", "60A+":"NDQ2933"',
                "dbo.Rehabilit_FSM_Telemed('I090,I091,I092,I098,I099,I200,I201,I208,I209,I210,I211,I212,I213,I214,I219,I260,I269,I270,I271,I272,I278,I279,I280,I281,I288,I289,I430,I431,I432,I438,I500,I501,I509,I520,I521,I528,I690,I691,I692,I693,I694,I730,I731,I738,I739,I99X,Q200,Q201,Q202,Q203,Q204,Q205,Q206,Q208,Q209,Z950,Z951,Z952', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2934", "12A-17A":"NDQ2935", "18A-29A":"NDQ2936", "30A-59A":"NDQ2937", "60A+":"NDQ2938"',
                "dbo.Rehabilit_FSM_Telemed('J1281,J1289,J180,J181,J182,J188,J189,J1891,J1892,J208,J220,J221,J222,J223,J224,J225,J226,J227,J228,J229,J40X,J410,J411,J418,J42X,J430,J431,J432,J438,J439,J440,J441,J448,J449,J450,J451,J458,J459,J4591,J46X,J47X,J680,J681,J682,J683,J684,J688,J689,J700,J701,J702,J703,J704,J708,J709,J800,J801,J802,J803,J804,J805,J806,J807,J808,J809,J841,J848,J960,J961,J969,J988,J981,J990,J991,J998', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2939", "12A-17A":"NDQ2940", "18A-29A":"NDQ2941", "30A-59A":"NDQ2942", "60A+":"NDQ2943"',
                "dbo.Rehabilit_FSM_Telemed('N311,N312,N318,N319,N320,N941,N942,N948,R102,R309', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2944", "12A-17A":"NDQ2945", "18A-29A":"NDQ2946", "30A-59A":"NDQ2947", "60A+":"NDQ2948"',
                "dbo.Rehabilit_FSM_Telemed('N393,N394,R15X,R32X', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2949", "12A-17A":"NDQ2950", "18A-29A":"NDQ2951", "30A-59A":"NDQ2952", "60A+":"NDQ2953"',
                "dbo.Rehabilit_FSM_Telemed('N812,N814,N815,N816,N818,N819', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2954", "12A-17A":"NDQ2955", "18A-29A":"NDQ2956", "30A-59A":"NDQ2957", "60A+":"NDQ2958"',
                "dbo.Rehabilit_FSM_Telemed('S000,S090,S091,S092,S097,S098,S099,S100,S101,S107,S108,S109,S197,S198,S199,S200,S201,S202,S203,S204,S207,S208,S290,S297,S298,S299,S300,S301,S302,S307,S308,S309,S390,S396,S397,S398,S399,S400,S407,S408,S409,S497,S498,S499,S500,S501,S507,S508,S509,S597,S598,S599,S600,S601,S602,S607,S608,S609,S697,S698,S699,S700,S701,S707,S708,S709,S797,S798,S799,S800,S801,S807,S808,S809,S897,S898,S899,S900,S901,S902,S903,S907,S908,S909,S997,S998,S999,T000,T001,T002,T003,T006,T008,T009,T07X,T08X,T140,T141,T142,T143,T144,T145,T146,T147,T148,T149,T900,T901,T902,T903,T904,T905,T908,T909,T910,T911,T912,T913,T914,T915,T918,T919,T920,T921,T922,T923,T924,T925,T926,T928,T929,T930,T931,T932,T933,T934,T935,T936,T938,T939,T940,T941,T950,T951,T952,T953,T954,T958,T959,T96X,T97X,T980,T981,T982,T983', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2959", "12A-17A":"NDQ2960", "18A-29A":"NDQ2961", "30A-59A":"NDQ2962", "60A+":"NDQ2963"',
                "dbo.Rehabilit_FSM_Telemed('M000,M001,M002,M008,M009,M300,M301,M302,M303,M308,M310,M311,M312,M313,M314,M315,M316,M317,M318,M319,M320,M321,M328,M329,M330,M331,M332,M339,M340,M341,M342,M348,M349,M350,M351,M352,M353,M354,M355,M356,M357,M358,M359,M360,M361,M362,M363,M364,M368,M600,M601,M602,M608,M609,M610,M611,M612,M613,M614,M615,M619,M620,M621,M622,M623,M624,M625,M626,M628,M629,M630,M631,M632,M633,M638,M650,M651,M652,M653,M654,M658,M659,M660,M661,M662,M663,M664,M665,M670,M671,M672,M673,M674,M678,M679,M680,M688,M800,M801,M802,M803,M804,M805,M808,M809,M850,M851,M852,M853,M854,M855,M856,M858,M859', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2964", "12A-17A":"NDQ2965", "18A-29A":"NDQ2966", "30A-59A":"NDQ2967", "60A+":"NDQ2968"',
                "dbo.Rehabilit_FSM_Telemed('M200,M201,M202,M203,M204,M205,M206,M210,M211,M212,M213,M214,M215,M216,M217,M218,M219,M220,M221,M222,M223,M228,M229,M230,M231,M232,M233,M234,M236,M240,M242,M243,M244,M245,M246,M247,M248,M249,M250,M251,M252,M253,M254,M256,M257,M258,M259,M759', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2969", "12A-17A":"NDQ2970", "18A-29A":"NDQ2971", "30A-59A":"NDQ2972", "60A+":"NDQ2973"',
                "dbo.Rehabilit_FSM_Telemed('A239,M490,M491,M860,M861,M862,M863,M864,M865,M866,M868,M869,M890,M891,M892,M893,M894,M895,M896,M898,M899', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2974", "12A-17A":"NDQ2975", "18A-29A":"NDQ2976", "30A-59A":"NDQ2977", "60A+":"NDQ2978"',
                "dbo.Rehabilit_FSM_Telemed('M998,M999', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2979", "12A-17A":"NDQ2980", "18A-29A":"NDQ2981", "30A-59A":"NDQ2982", "60A+":"NDQ2983"',
                "dbo.Rehabilit_FSM_Telemed('I890,I891,I892,I893,I894,I895,I896,I897,I898,I899,I890,I891,I898,I899,I972,I978,I979', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2984", "12A-17A":"NDQ2985", "18A-29A":"NDQ2986", "30A-59A":"NDQ2987", "60A+":"NDQ2988"',
                "dbo.Rehabilit_FSM_Telemed('M6284', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2989", "12A-17A":"NDQ2990", "18A-29A":"NDQ2991", "30A-59A":"NDQ2992", "60A+":"NDQ2993"',
                "dbo.Rehabilit_FSM_Telemed('M255,M791,M797,R521,R522,R529', 'N,C,R');"
            ),
            (
                '"0d-11A":"NDQ2994", "12A-17A":"NDQ2995", "18A-29A":"NDQ2996", "30A-59A":"NDQ2997", "60A+":"NDQ2998"',
                "dbo.Rehabilit_FSM_Telemed('T200,T201,T202,T203,T204,T205,T206,T207,T208,T209,T200,T201,T202,T203,T204,T205,T206,T207,T210,T220,T230,T240,T250,T260,T270,T280,T290,T300,T310,T311,T312,T313,T314,T315,T316,T317,T318,T319,T310,T311,T312,T313,T314,T315,T316,T317,T318,T319,T320,T321,T322,T323,T324,T325,T326,T327,T328,T329,T320,T321,T322,T323,T324,T325,T326,T327,T328,T329,T330,T331,T332,T333,T334,T335,T336,T337,T338,T339,T330,T331,T332,T333,T334,T335,T336,T337,T338,T339,T340,T341,T342,T343,T344,T345,T346,T347,T348,T349,T340,T341,T342,T343,T344,T345,T346,T347,T348,T349,T350,T351,T352,T353,T354,T355,T356,T357,T358,T359,T350,T351,T352,T353,T354,T355,T356,T357', 'N,C,R');"
            ),


        ],
        "FACT_DISC_SNAPSHOT_REHABSENSORIAL": [
            (
                '"0d-11A":"NDQ2999", "12A-17A":"NDQ3000", "18A-29A":"NDQ3001", "30A-59A":"NDQ3002", "60A+":"NDQ3003"',
                "Rehabilit_FSM_ConCert('H900,H901,H902,H903,H904,H905,H906,H907,H908,H909,H910,H911,H912,H918,H919','N,R')"
            ),
            (
                '"0d-11A":"NDQ3004", "12A-17A":"NDQ3005", "18A-29A":"NDQ3006", "30A-59A":"NDQ3007", "60A+":"NDQ3008"',
                "Rehabilit_FSM_ConCert('B940,H532,H534,H540,H541,H542,H543,H544,H545,H546,H547,H548,H549,R481','N,R')"
            ),
            (
                '"0d-11A":"NDQ3009", "12A-17A":"NDQ3010", "18A-29A":"NDQ3011", "30A-59A":"NDQ3012", "60A+":"NDQ3013"',
                "Rehabilit_FSM_ConCert('H913','N,R')"
            ),
            (
                '"0d-11A":"NDQ3014", "12A-17A":"NDQ3015", "18A-29A":"NDQ3016", "30A-59A":"NDQ3017", "60A+":"NDQ3018"',
                "Rehabilit_FSM_ConCert('R470,R481,R482','N,R')"
            ),
            (
                '"0d-11A":"NDQ3019", "12A-17A":"NDQ3020", "18A-29A":"NDQ3021", "30A-59A":"NDQ3022", "60A+":"NDQ3023"',
                "Rehabilit_FSM_ConCert('F800,F801,F802,F803,F804,F805,F806,F807,F808,F809,R480,R481,R482,R483,R484,R485,R486,R487,R488,R489','N,R')"
            ),
            (
                '"0d-11A":"NDQ3024", "12A-17A":"NDQ3025", "18A-29A":"NDQ3026", "30A-59A":"NDQ3027", "60A+":"NDQ3028"',
                "Rehabilit_FSM_ConCert('P050,P073,P229,P923,Z910','N,R')"
            ),
            (
                '"0d-11A":"NDQ3029", "12A-17A":"NDQ3030", "18A-29A":"NDQ3031", "30A-59A":"NDQ3032", "60A+":"NDQ3033"',
                "Rehabilit_FSM_ConCert('R471,R478','N,R')"
            ),
            (
                '"0d-11A":"NDQ3034", "12A-17A":"NDQ3035", "18A-29A":"NDQ3036", "30A-59A":"NDQ3037", "60A+":"NDQ3038"',
                "Rehabilit_FSM_ConCert('P920,P921,P922,P923,P924,P925,P926,P927,P928,P929,R13X,Z930','N,R')"
            ),
            (
                '"0d-11A":"NDQ3039", "12A-17A":"NDQ3040", "18A-29A":"NDQ3041", "30A-59A":"NDQ3042", "60A+":"NDQ3043"',
                "Rehabilit_FSM_Rehab_Alta('H900,H901,H902,H903,H904,H905,H906,H907,H908,H909,H910,H911,H912,H918,H919','N,R')"
            ),
            (
                '"0d-11A":"NDQ3044", "12A-17A":"NDQ3045", "18A-29A":"NDQ3046", "30A-59A":"NDQ3047", "60A+":"NDQ3048"',
                "Rehabilit_FSM_Rehab_Alta('B940,H532,H534,H540,H541,H542,H543,H544,H545,H546,H547,H548,H549,R481','N,R')"
            ),
            (
                '"0d-11A":"NDQ3049", "12A-17A":"NDQ3050", "18A-29A":"NDQ3051", "30A-59A":"NDQ3052", "60A+":"NDQ3053"',
                "Rehabilit_FSM_Rehab_Alta('H913','N,R')"
            ),
            (
                '"0d-11A":"NDQ3054", "12A-17A":"NDQ3055", "18A-29A":"NDQ3056", "30A-59A":"NDQ3057", "60A+":"NDQ3058"',
                "Rehabilit_FSM_Rehab_Alta('R470,R481,R482','N,R')"
            ),
            (
                '"0d-11A":"NDQ3059", "12A-17A":"NDQ3060", "18A-29A":"NDQ3061", "30A-59A":"NDQ3062", "60A+":"NDQ3063"',
                "Rehabilit_FSM_Rehab_Alta('F800,F801,F802,F803,F804,F805,F806,F807,F808,F809,R480,R481,R482,R483,R484,R485,R486,R487,R488,R489','N,R')"
            ),
            (
                '"0d-11A":"NDQ3064", "12A-17A":"NDQ3065", "18A-29A":"NDQ3066", "30A-59A":"NDQ3067", "60A+":"NDQ3068"',
                "Rehabilit_FSM_Rehab_Alta('P050,P073,P229,P923,Z910','N,R')"
            ),
            (
                '"0d-11A":"NDQ3069", "12A-17A":"NDQ3070", "18A-29A":"NDQ3071", "30A-59A":"NDQ3072", "60A+":"NDQ3073"',
                "Rehabilit_FSM_Rehab_Alta('R471,R478','N,R')"
            ),
            (
                '"0d-11A":"NDQ3074", "12A-17A":"NDQ3075", "18A-29A":"NDQ3076", "30A-59A":"NDQ3077", "60A+":"NDQ3078"',
                "Rehabilit_FSM_Rehab_Alta('P920,P921,P922,P923,P924,P925,P926,P927,P928,P929,R13X,Z930','N,R')"
            ),
            (
                '"0d-11A":"NDQ3079", "12A-17A":"NDQ3080", "18A-29A":"NDQ3081", "30A-59A":"NDQ3082", "60A+":"NDQ3083"',
                "Rehabilit_FSM_SinCert('H900,H901,H902,H903,H904,H905,H906,H907,H908,H909,H910,H911,H912,H918,H919','N,R')"
            ),
            (
                '"0d-11A":"NDQ3084", "12A-17A":"NDQ3085", "18A-29A":"NDQ3086", "30A-59A":"NDQ3087", "60A+":"NDQ3088"',
                "Rehabilit_FSM_SinCert('B940,H532,H534,H540,H541,H542,H543,H544,H545,H546,H547,H548,H549,R481','N,R')"
            ),
            (
                '"0d-11A":"NDQ3089", "12A-17A":"NDQ3090", "18A-29A":"NDQ3091", "30A-59A":"NDQ3092", "60A+":"NDQ3093"',
                "Rehabilit_FSM_SinCert('H913','N,R')"
            ),
            (
                '"0d-11A":"NDQ3094", "12A-17A":"NDQ3095", "18A-29A":"NDQ3096", "30A-59A":"NDQ3097", "60A+":"NDQ3098"',
                "Rehabilit_FSM_SinCert('R470,R481,R482','N,R')"
            ),
            (
                '"0d-11A":"NDQ3099", "12A-17A":"NDQ3100", "18A-29A":"NDQ3101", "30A-59A":"NDQ3102", "60A+":"NDQ3103"',
                "Rehabilit_FSM_SinCert('F800,F801,F802,F803,F804,F805,F806,F807,F808,F809,R480,R481,R482,R483,R484,R485,R486,R487,R488,R489','N,R')"
            ),
            (
                '"0d-11A":"NDQ3104", "12A-17A":"NDQ3105", "18A-29A":"NDQ3106", "30A-59A":"NDQ3107", "60A+":"NDQ3108"',
                "Rehabilit_FSM_SinCert('P050,P073,P229,P923,Z910','N,R')"
            ),
            (
                '"0d-11A":"NDQ3109", "12A-17A":"NDQ3110", "18A-29A":"NDQ3111", "30A-59A":"NDQ3112", "60A+":"NDQ3113"',
                "Rehabilit_FSM_SinCert('R471,R478','N,R')"
            ),
            (
                '"0d-11A":"NDQ3114", "12A-17A":"NDQ3115", "18A-29A":"NDQ3116", "30A-59A":"NDQ3117", "60A+":"NDQ3118"',
                "Rehabilit_FSM_SinCert('P920,P921,P922,P923,P924,P925,P926,P927,P928,P929,R13X,Z930','N,R')"
            ),
            (
                '"0d-11A":"NDQ3119", "12A-17A":"NDQ3120", "18A-29A":"NDQ3121", "30A-59A":"NDQ3122", "60A+":"NDQ3123"',
                "Rehabilit_FSM_ServEval('H900,H901,H902,H903,H904,H905,H906,H907,H908,H909,H910,H911,H912,H918,H919','N,R')"
            ),
            (
                '"0d-11A":"NDQ3124", "12A-17A":"NDQ3125", "18A-29A":"NDQ3126", "30A-59A":"NDQ3127", "60A+":"NDQ3128"',
                "Rehabilit_FSM_ServEval('B940,H532,H534,H540,H541,H542,H543,H544,H545,H546,H547,H548,H549,R481','N,R')"
            ),
            (
                '"0d-11A":"NDQ3129", "12A-17A":"NDQ3130", "18A-29A":"NDQ3131", "30A-59A":"NDQ3132", "60A+":"NDQ3133"',
                "Rehabilit_FSM_ServEval('H913','N,R')"
            ),
            (
                '"0d-11A":"NDQ3134", "12A-17A":"NDQ3135", "18A-29A":"NDQ3136", "30A-59A":"NDQ3137", "60A+":"NDQ3138"',
                "Rehabilit_FSM_ServEval('R470,R481,R482','N,R')"
            ),
            (
                '"0d-11A":"NDQ3139", "12A-17A":"NDQ3140", "18A-29A":"NDQ3141", "30A-59A":"NDQ3142", "60A+":"NDQ3143"',
                "Rehabilit_FSM_ServEval('F800,F801,F802,F803,F804,F805,F806,F807,F808,F809,R480,R481,R482,R483,R484,R485,R486,R487,R488,R489','N,R')"
            ),
            (
                '"0d-11A":"NDQ3144", "12A-17A":"NDQ3145", "18A-29A":"NDQ3146", "30A-59A":"NDQ3147", "60A+":"NDQ3148"',
                "Rehabilit_FSM_ServEval('P050,P073,P229,P923,Z910','N,R')"
            ),
            (
                '"0d-11A":"NDQ3149", "12A-17A":"NDQ3150", "18A-29A":"NDQ3151", "30A-59A":"NDQ3152", "60A+":"NDQ3153"',
                "Rehabilit_FSM_ServEval('R471,R478','N,R')"
            ),
            (
                '"0d-11A":"NDQ3154", "12A-17A":"NDQ3155", "18A-29A":"NDQ3156", "30A-59A":"NDQ3157", "60A+":"NDQ3158"',
                "Rehabilit_FSM_ServEval('P920,P921,P922,P923,P924,P925,P926,P927,P928,P929,R13X,Z930','N,R')"
            ),
            (
                '"0d-11A":"NDQ3159", "12A-17A":"NDQ3160", "18A-29A":"NDQ3161", "30A-59A":"NDQ3162", "60A+":"NDQ3163"',
                "Rehabilit_FSM_EnRiesgo('H900,H901,H902,H903,H904,H905,H906,H907,H908,H909,H910,H911,H912,H918,H919','N,R')"
            ),
            (
                '"0d-11A":"NDQ3164", "12A-17A":"NDQ3165", "18A-29A":"NDQ3166", "30A-59A":"NDQ3167", "60A+":"NDQ3168"',
                "Rehabilit_FSM_EnRiesgo('B940,H532,H534,H540,H541,H542,H543,H544,H545,H546,H547,H548,H549,R481','N,R')"
            ),
            (
                '"0d-11A":"NDQ3169", "12A-17A":"NDQ3170", "18A-29A":"NDQ3171", "30A-59A":"NDQ3172", "60A+":"NDQ3173"',
                "Rehabilit_FSM_EnRiesgo('H913','N,R')"
            ),
            (
                '"0d-11A":"NDQ3174", "12A-17A":"NDQ3175", "18A-29A":"NDQ3176", "30A-59A":"NDQ3177", "60A+":"NDQ3178"',
                "Rehabilit_FSM_EnRiesgo('R470,R481,R482','N,R')"
            ),
            (
                '"0d-11A":"NDQ3179", "12A-17A":"NDQ3180", "18A-29A":"NDQ3181", "30A-59A":"NDQ3182", "60A+":"NDQ3183"',
                "Rehabilit_FSM_EnRiesgo('F800,F801,F802,F803,F804,F805,F806,F807,F808,F809,R480,R481,R482,R483,R484,R485,R486,R487,R488,R489','N,R')"
            ),
            (
                '"0d-11A":"NDQ3184", "12A-17A":"NDQ3185", "18A-29A":"NDQ3186", "30A-59A":"NDQ3187", "60A+":"NDQ3188"',
                "Rehabilit_FSM_EnRiesgo('P050,P073,P229,P923,Z910','N,R')"
            ),
            (
                '"0d-11A":"NDQ3189", "12A-17A":"NDQ3190", "18A-29A":"NDQ3191", "30A-59A":"NDQ3192", "60A+":"NDQ3193"',
                "Rehabilit_FSM_EnRiesgo('R471,R478','N,R')"
            ),
            (
                '"0d-11A":"NDQ3194", "12A-17A":"NDQ3195", "18A-29A":"NDQ3196", "30A-59A":"NDQ3197", "60A+":"NDQ3198"',
                "Rehabilit_FSM_EnRiesgo('P920,P921,P922,P923,P924,P925,P926,P927,P928,P929,R13X,Z930','N,R')"
            ),
            (
                '"0d-11A":"NDQ3199", "12A-17A":"NDQ3200", "18A-29A":"NDQ3201", "30A-59A":"NDQ3202", "60A+":"NDQ3203"',
                "Rehabilit_FSM_RefContraResto('H900,H901,H902,H903,H904,H905,H906,H907,H908,H909,H910,H911,H912,H918,H919','N,R')"
            ),
            (
                '"0d-11A":"NDQ3204", "12A-17A":"NDQ3205", "18A-29A":"NDQ3206", "30A-59A":"NDQ3207", "60A+":"NDQ3208"',
                "Rehabilit_FSM_RefContraResto('B940,H532,H534,H540,H541,H542,H543,H544,H545,H546,H547,H548,H549,R481','N,R')"
            ),
            (
                '"0d-11A":"NDQ3209", "12A-17A":"NDQ3210", "18A-29A":"NDQ3211", "30A-59A":"NDQ3212", "60A+":"NDQ3213"',
                "Rehabilit_FSM_RefContraResto('H913','N,R')"
            ),
            (
                '"0d-11A":"NDQ3214", "12A-17A":"NDQ3215", "18A-29A":"NDQ3216", "30A-59A":"NDQ3217", "60A+":"NDQ3218"',
                "Rehabilit_FSM_RefContraResto('R470,R481,R482','N,R')"
            ),
            (
                '"0d-11A":"NDQ3219", "12A-17A":"NDQ3220", "18A-29A":"NDQ3221", "30A-59A":"NDQ3222", "60A+":"NDQ3223"',
                "Rehabilit_FSM_RefContraResto('F800,F801,F802,F803,F804,F805,F806,F807,F808,F809,R480,R481,R482,R483,R484,R485,R486,R487,R488,R489','N,R')"
            ),
            (
                '"0d-11A":"NDQ3224", "12A-17A":"NDQ3225", "18A-29A":"NDQ3226", "30A-59A":"NDQ3227", "60A+":"NDQ3228"',
                "Rehabilit_FSM_RefContraResto('P050,P073,P229,P923,Z910','N,R')"
            ),
            (
                '"0d-11A":"NDQ3229", "12A-17A":"NDQ3230", "18A-29A":"NDQ3231", "30A-59A":"NDQ3232", "60A+":"NDQ3233"',
                "Rehabilit_FSM_RefContraResto('R471,R478','N,R')"
            ),
            (
                '"0d-11A":"NDQ3234", "12A-17A":"NDQ3235", "18A-29A":"NDQ3236", "30A-59A":"NDQ3237", "60A+":"NDQ3238"',
                "Rehabilit_FSM_RefContraResto('P920,P921,P922,P923,P924,P925,P926,P927,P928,P929,R13X,Z930','N,R')"
            ),
            (
                '"0d-11A":"NDQ3239", "12A-17A":"NDQ3240", "18A-29A":"NDQ3241", "30A-59A":"NDQ3242", "60A+":"NDQ3243"',
                "Rehabilit_FSM_Telemed('H900,H901,H902,H903,H904,H905,H906,H907,H908,H909,H910,H911,H912,H918,H919','N,R')"
            ),
            (
                '"0d-11A":"NDQ3244", "12A-17A":"NDQ3245", "18A-29A":"NDQ3246", "30A-59A":"NDQ3247", "60A+":"NDQ3248"',
                "Rehabilit_FSM_Telemed('B940,H532,H534,H540,H541,H542,H543,H544,H545,H546,H547,H548,H549,R481','N,R')"
            ),
            (
                '"0d-11A":"NDQ3249", "12A-17A":"NDQ3250", "18A-29A":"NDQ3251", "30A-59A":"NDQ3252", "60A+":"NDQ3253"',
                "Rehabilit_FSM_Telemed('H913','N,R')"
            ),
            (
                '"0d-11A":"NDQ3254", "12A-17A":"NDQ3255", "18A-29A":"NDQ3256", "30A-59A":"NDQ3257", "60A+":"NDQ3258"',
                "Rehabilit_FSM_Telemed('R470,R481,R482','N,R')"
            ),
            (
                '"0d-11A":"NDQ3259", "12A-17A":"NDQ3260", "18A-29A":"NDQ3261", "30A-59A":"NDQ3262", "60A+":"NDQ3263"',
                "Rehabilit_FSM_Telemed('F800,F801,F802,F803,F804,F805,F806,F807,F808,F809,R480,R481,R482,R483,R484,R485,R486,R487,R488,R489','N,R')"
            ),
            (
                '"0d-11A":"NDQ3264", "12A-17A":"NDQ3265", "18A-29A":"NDQ3266", "30A-59A":"NDQ3267", "60A+":"NDQ3268"',
                "Rehabilit_FSM_Telemed('P050,P073,P229,P923,Z910','N,R')"
            ),
            (
                '"0d-11A":"NDQ3269", "12A-17A":"NDQ3270", "18A-29A":"NDQ3271", "30A-59A":"NDQ3272", "60A+":"NDQ3273"',
                "Rehabilit_FSM_Telemed('R471,R478','N,R')"
            ),
            (
                '"0d-11A":"NDQ3274", "12A-17A":"NDQ3275", "18A-29A":"NDQ3276", "30A-59A":"NDQ3277", "60A+":"NDQ3278"',
                "Rehabilit_FSM_Telemed('P920,P921,P922,P923,P924,P925,P926,P927,P928,P929,R13X,Z930','N,R')"
            ),
            (
                '"0d-11A":"NDQ3279", "12A-17A":"NDQ3280", "18A-29A":"NDQ3281", "30A-59A":"NDQ3282", "60A+":"NDQ3283"',
                "Rehabilit_FSM_ConCert('H900,H901,H902,H903,H904,H905,H906,H907,H908,H909,H910,H911,H912,H918,H919','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3284", "12A-17A":"NDQ3285", "18A-29A":"NDQ3286", "30A-59A":"NDQ3287", "60A+":"NDQ3288"',
                "Rehabilit_FSM_ConCert('B940,H532,H534,H540,H541,H542,H543,H544,H545,H546,H547,H548,H549,R481','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3289", "12A-17A":"NDQ3290", "18A-29A":"NDQ3291", "30A-59A":"NDQ3292", "60A+":"NDQ3293"',
                "Rehabilit_FSM_ConCert('H913','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3294", "12A-17A":"NDQ3295", "18A-29A":"NDQ3296", "30A-59A":"NDQ3297", "60A+":"NDQ3298"',
                "Rehabilit_FSM_ConCert('R470,R481,R482','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3299", "12A-17A":"NDQ3300", "18A-29A":"NDQ3301", "30A-59A":"NDQ3302", "60A+":"NDQ3303"',
                "Rehabilit_FSM_ConCert('F800,F801,F802,F803,F804,F805,F806,F807,F808,F809,R480,R481,R482,R483,R484,R485,R486,R487,R488,R489','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3304", "12A-17A":"NDQ3305", "18A-29A":"NDQ3306", "30A-59A":"NDQ3307", "60A+":"NDQ3308"',
                "Rehabilit_FSM_ConCert('P050,P073,P229,P923,Z910','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3309", "12A-17A":"NDQ3310", "18A-29A":"NDQ3311", "30A-59A":"NDQ3312", "60A+":"NDQ3313"',
                "Rehabilit_FSM_ConCert('R471,R478','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3314", "12A-17A":"NDQ3315", "18A-29A":"NDQ3316", "30A-59A":"NDQ3317", "60A+":"NDQ3318"',
                "Rehabilit_FSM_ConCert('P920,P921,P922,P923,P924,P925,P926,P927,P928,P929,R13X,Z930','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3319", "12A-17A":"NDQ3320", "18A-29A":"NDQ3321", "30A-59A":"NDQ3322", "60A+":"NDQ3323"',
                "Rehabilit_FSM_Nml_NCR('H900,H901,H902,H903,H904,H905,H906,H907,H908,H909,H910,H911,H912,H918,H919','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3324", "12A-17A":"NDQ3325", "18A-29A":"NDQ3326", "30A-59A":"NDQ3327", "60A+":"NDQ3328"',
                "Rehabilit_FSM_Nml_NCR('B940,H532,H534,H540,H541,H542,H543,H544,H545,H546,H547,H548,H549,R481','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3329", "12A-17A":"NDQ3330", "18A-29A":"NDQ3331", "30A-59A":"NDQ3332", "60A+":"NDQ3333"',
                "Rehabilit_FSM_Nml_NCR('H913','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3334", "12A-17A":"NDQ3335", "18A-29A":"NDQ3336", "30A-59A":"NDQ3337", "60A+":"NDQ3338"',
                "Rehabilit_FSM_Nml_NCR('R470,R481,R482','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3339", "12A-17A":"NDQ3340", "18A-29A":"NDQ3341", "30A-59A":"NDQ3342", "60A+":"NDQ3343"',
                "Rehabilit_FSM_Nml_NCR('F800,F801,F802,F803,F804,F805,F806,F807,F808,F809,R480,R481,R482,R483,R484,R485,R486,R487,R488,R489','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3344", "12A-17A":"NDQ3345", "18A-29A":"NDQ3346", "30A-59A":"NDQ3347", "60A+":"NDQ3348"',
                "Rehabilit_FSM_Nml_NCR('P050,P073,P229,P923,Z910','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3349", "12A-17A":"NDQ3350", "18A-29A":"NDQ3351", "30A-59A":"NDQ3352", "60A+":"NDQ3353"',
                "Rehabilit_FSM_Nml_NCR('R471,R478','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3354", "12A-17A":"NDQ3355", "18A-29A":"NDQ3356", "30A-59A":"NDQ3357", "60A+":"NDQ3358"',
                "Rehabilit_FSM_Nml_NCR('P920,P921,P922,P923,P924,P925,P926,P927,P928,P929,R13X,Z930','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3359", "12A-17A":"NDQ3360", "18A-29A":"NDQ3361", "30A-59A":"NDQ3362", "60A+":"NDQ3363"',
                "Rehabilit_FSM_SinCert('H900,H901,H902,H903,H904,H905,H906,H907,H908,H909,H910,H911,H912,H918,H919','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3364", "12A-17A":"NDQ3365", "18A-29A":"NDQ3366", "30A-59A":"NDQ3367", "60A+":"NDQ3368"',
                "Rehabilit_FSM_SinCert('B940,H532,H534,H540,H541,H542,H543,H544,H545,H546,H547,H548,H549,R481','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3369", "12A-17A":"NDQ3370", "18A-29A":"NDQ3371", "30A-59A":"NDQ3372", "60A+":"NDQ3373"',
                "Rehabilit_FSM_SinCert('H913','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3374", "12A-17A":"NDQ3375", "18A-29A":"NDQ3376", "30A-59A":"NDQ3377", "60A+":"NDQ3378"',
                "Rehabilit_FSM_SinCert('R470,R481,R482','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3379", "12A-17A":"NDQ3380", "18A-29A":"NDQ3381", "30A-59A":"NDQ3382", "60A+":"NDQ3383"',
                "Rehabilit_FSM_SinCert('F800,F801,F802,F803,F804,F805,F806,F807,F808,F809,R480,R481,R482,R483,R484,R485,R486,R487,R488,R489','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3384", "12A-17A":"NDQ3385", "18A-29A":"NDQ3386", "30A-59A":"NDQ3387", "60A+":"NDQ3388"',
                "Rehabilit_FSM_SinCert('P050,P073,P229,P923,Z910','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3389", "12A-17A":"NDQ3390", "18A-29A":"NDQ3391", "30A-59A":"NDQ3392", "60A+":"NDQ3393"',
                "Rehabilit_FSM_SinCert('R471,R478','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3394", "12A-17A":"NDQ3395", "18A-29A":"NDQ3396", "30A-59A":"NDQ3397", "60A+":"NDQ3398"',
                "Rehabilit_FSM_SinCert('P920,P921,P922,P923,P924,P925,P926,P927,P928,P929,R13X,Z930','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3399", "12A-17A":"NDQ3400", "18A-29A":"NDQ3401", "30A-59A":"NDQ3402", "60A+":"NDQ3403"',
                "Rehabilit_FSM_ServEval_NCR('H900,H901,H902,H903,H904,H905,H906,H907,H908,H909,H910,H911,H912,H918,H919','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3404", "12A-17A":"NDQ3405", "18A-29A":"NDQ3406", "30A-59A":"NDQ3407", "60A+":"NDQ3408"',
                "Rehabilit_FSM_ServEval_NCR('B940,H532,H534,H540,H541,H542,H543,H544,H545,H546,H547,H548,H549,R481','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3409", "12A-17A":"NDQ3410", "18A-29A":"NDQ3411", "30A-59A":"NDQ3412", "60A+":"NDQ3413"',
                "Rehabilit_FSM_ServEval_NCR('H913','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3414", "12A-17A":"NDQ3415", "18A-29A":"NDQ3416", "30A-59A":"NDQ3417", "60A+":"NDQ3418"',
                "Rehabilit_FSM_ServEval_NCR('R470,R481,R482','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3419", "12A-17A":"NDQ3420", "18A-29A":"NDQ3421", "30A-59A":"NDQ3422", "60A+":"NDQ3423"',
                "Rehabilit_FSM_ServEval_NCR('F800,F801,F802,F803,F804,F805,F806,F807,F808,F809,R480,R481,R482,R483,R484,R485,R486,R487,R488,R489','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3424", "12A-17A":"NDQ3425", "18A-29A":"NDQ3426", "30A-59A":"NDQ3427", "60A+":"NDQ3428"',
                "Rehabilit_FSM_ServEval_NCR('P050,P073,P229,P923,Z910','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3429", "12A-17A":"NDQ3430", "18A-29A":"NDQ3431", "30A-59A":"NDQ3432", "60A+":"NDQ3433"',
                "Rehabilit_FSM_ServEval_NCR('R471,R478','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3434", "12A-17A":"NDQ3435", "18A-29A":"NDQ3436", "30A-59A":"NDQ3437", "60A+":"NDQ3438"',
                "Rehabilit_FSM_ServEval_NCR('P920,P921,P922,P923,P924,P925,P926,P927,P928,P929,R13X,Z930','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3439", "12A-17A":"NDQ3440", "18A-29A":"NDQ3441", "30A-59A":"NDQ3442", "60A+":"NDQ3443"',
                "Rehabilit_FSM_Ambulatoria_NCR('H900,H901,H902,H903,H904,H905,H906,H907,H908,H909,H910,H911,H912,H918,H919','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3444", "12A-17A":"NDQ3445", "18A-29A":"NDQ3446", "30A-59A":"NDQ3447", "60A+":"NDQ3448"',
                "Rehabilit_FSM_Ambulatoria_NCR('B940,H532,H534,H540,H541,H542,H543,H544,H545,H546,H547,H548,H549,R481','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3449", "12A-17A":"NDQ3450", "18A-29A":"NDQ3451", "30A-59A":"NDQ3452", "60A+":"NDQ3453"',
                "Rehabilit_FSM_Ambulatoria_NCR('H913','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3454", "12A-17A":"NDQ3455", "18A-29A":"NDQ3456", "30A-59A":"NDQ3457", "60A+":"NDQ3458"',
                "Rehabilit_FSM_Ambulatoria_NCR('R470,R481,R482','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3459", "12A-17A":"NDQ3460", "18A-29A":"NDQ3461", "30A-59A":"NDQ3462", "60A+":"NDQ3463"',
                "Rehabilit_FSM_Ambulatoria_NCR('F800,F801,F802,F803,F804,F805,F806,F807,F808,F809,R480,R481,R482,R483,R484,R485,R486,R487,R488,R489','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3464", "12A-17A":"NDQ3465", "18A-29A":"NDQ3466", "30A-59A":"NDQ3467", "60A+":"NDQ3468"',
                "Rehabilit_FSM_Ambulatoria_NCR('P050,P073,P229,P923,Z910','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3469", "12A-17A":"NDQ3470", "18A-29A":"NDQ3471", "30A-59A":"NDQ3472", "60A+":"NDQ3473"',
                "Rehabilit_FSM_Ambulatoria_NCR('R471,R478','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3474", "12A-17A":"NDQ3475", "18A-29A":"NDQ3476", "30A-59A":"NDQ3477", "60A+":"NDQ3478"',
                "Rehabilit_FSM_Ambulatoria_NCR('P920,P921,P922,P923,P924,P925,P926,P927,P928,P929,R13X,Z930','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3479", "12A-17A":"NDQ3480", "18A-29A":"NDQ3481", "30A-59A":"NDQ3482", "60A+":"NDQ3483"',
                "Rehabilit_FSM_ReviFinal_NCR('H900,H901,H902,H903,H904,H905,H906,H907,H908,H909,H910,H911,H912,H918,H919','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3484", "12A-17A":"NDQ3485", "18A-29A":"NDQ3486", "30A-59A":"NDQ3487", "60A+":"NDQ3488"',
                "Rehabilit_FSM_ReviFinal_NCR('B940,H532,H534,H540,H541,H542,H543,H544,H545,H546,H547,H548,H549,R481','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3489", "12A-17A":"NDQ3490", "18A-29A":"NDQ3491", "30A-59A":"NDQ3492", "60A+":"NDQ3493"',
                "Rehabilit_FSM_ReviFinal_NCR('H913','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3494", "12A-17A":"NDQ3495", "18A-29A":"NDQ3496", "30A-59A":"NDQ3497", "60A+":"NDQ3498"',
                "Rehabilit_FSM_ReviFinal_NCR('R470,R481,R482','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3499", "12A-17A":"NDQ3500", "18A-29A":"NDQ3501", "30A-59A":"NDQ3502", "60A+":"NDQ3503"',
                "Rehabilit_FSM_ReviFinal_NCR('F800,F801,F802,F803,F804,F805,F806,F807,F808,F809,R480,R481,R482,R483,R484,R485,R486,R487,R488,R489','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3504", "12A-17A":"NDQ3505", "18A-29A":"NDQ3506", "30A-59A":"NDQ3507", "60A+":"NDQ3508"',
                "Rehabilit_FSM_ReviFinal_NCR('P050,P073,P229,P923,Z910','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3509", "12A-17A":"NDQ3510", "18A-29A":"NDQ3511", "30A-59A":"NDQ3512", "60A+":"NDQ3513"',
                "Rehabilit_FSM_ReviFinal_NCR('R471,R478','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3514", "12A-17A":"NDQ3515", "18A-29A":"NDQ3516", "30A-59A":"NDQ3517", "60A+":"NDQ3518"',
                "Rehabilit_FSM_ReviFinal_NCR('P920,P921,P922,P923,P924,P925,P926,P927,P928,P929,R13X,Z930','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3519", "12A-17A":"NDQ3520", "18A-29A":"NDQ3521", "30A-59A":"NDQ3522", "60A+":"NDQ3523"',
                "Rehabilit_FSM_Telemed('H900,H901,H902,H903,H904,H905,H906,H907,H908,H909,H910,H911,H912,H918,H919','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3524", "12A-17A":"NDQ3525", "18A-29A":"NDQ3526", "30A-59A":"NDQ3527", "60A+":"NDQ3528"',
                "Rehabilit_FSM_Telemed('B940,H532,H534,H540,H541,H542,H543,H544,H545,H546,H547,H548,H549,R481','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3529", "12A-17A":"NDQ3530", "18A-29A":"NDQ3531", "30A-59A":"NDQ3532", "60A+":"NDQ3533"',
                "Rehabilit_FSM_Telemed('H913','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3534", "12A-17A":"NDQ3535", "18A-29A":"NDQ3536", "30A-59A":"NDQ3537", "60A+":"NDQ3538"',
                "Rehabilit_FSM_Telemed('R470,R481,R482','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3539", "12A-17A":"NDQ3540", "18A-29A":"NDQ3541", "30A-59A":"NDQ3542", "60A+":"NDQ3543"',
                "Rehabilit_FSM_Telemed('F800,F801,F802,F803,F804,F805,F806,F807,F808,F809,R480,R481,R482,R483,R484,R485,R486,R487,R488,R489','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3544", "12A-17A":"NDQ3545", "18A-29A":"NDQ3546", "30A-59A":"NDQ3547", "60A+":"NDQ3548"',
                "Rehabilit_FSM_Telemed('P050,P073,P229,P923,Z910','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3549", "12A-17A":"NDQ3550", "18A-29A":"NDQ3551", "30A-59A":"NDQ3552", "60A+":"NDQ3553"',
                "Rehabilit_FSM_Telemed('R471,R478','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3554", "12A-17A":"NDQ3555", "18A-29A":"NDQ3556", "30A-59A":"NDQ3557", "60A+":"NDQ3558"',
                "Rehabilit_FSM_Telemed('P920,P921,P922,P923,P924,P925,P926,P927,P928,P929,R13X,Z930','N,C,R')"
            ),


        ],
        "FACT_DISC_SNAPSHOT_REHABMENTAL": [
            (
                '"0d-11A":"NDQ3559", "12A-17A":"NDQ3560", "18A-29A":"NDQ3561", "30A-59A":"NDQ3562", "60A+":"NDQ3563"',
                "Rehabilit_FSM_ConCert('F810, F811, F812, F813, F818, F819, F820, F821, F822, F823, F824, F825, F826, F827, F828, F829, Z558','N,R')"
            ),
            (
                '"0d-11A":"NDQ3564", "12A-17A":"NDQ3565", "18A-29A":"NDQ3566", "30A-59A":"NDQ3567", "60A+":"NDQ3568"',
                "Rehabilit_FSM_ConCert('F799, F798, F791, F790, F789, F788, F781, F780, F739, F738, F731, F730, F729, F728, F721, F720, F719, F718, F711, F710, F709, F708, F701, F700','N,R')"
            ),
            (
                '"0d-11A":"NDQ3569", "12A-17A":"NDQ3570", "18A-29A":"NDQ3571", "30A-59A":"NDQ3572", "60A+":"NDQ3573"',
                "Rehabilit_FSM_ConCert('F840, F841, F842, F843, F844, F845, F848, F849, F900, F901, F908, F909, F910, F911, F912, F9121, F9122, F913, F918, F919','N,R')"
            ),
            (
                '"0d-11A":"NDQ3574", "12A-17A":"NDQ3575", "18A-29A":"NDQ3576", "30A-59A":"NDQ3577", "60A+":"NDQ3578"',
                "Rehabilit_FSM_ConCert('F310, F311, F312, F313, F314, F315, F316, F317, F318, F319, F200, F201, F202, F203, F204, F205, F206, F207, F208, F209, F060, F061, F062, F063, F064, F065, F066, F067, F068, F069, F030, F031, F032, F033, F034, F035, F036, F037, F038, F039, F010, F011, F012, F013, F014, F015, F016, F017, F018, F019, G300, G301, G302, G303, G304, G305, G306, G307, G308, G309, G311, G319, F03X, F028','N,R')"
            ),
            (
                '"0d-11A":"NDQ3579", "12A-17A":"NDQ3580", "18A-29A":"NDQ3581", "30A-59A":"NDQ3582", "60A+":"NDQ3583"',
                "Rehabilit_FSM_Rehab_Alta('F810, F811, F812, F813, F818, F819, F820, F821, F822, F823, F824, F825, F826, F827, F828, F829, Z558','N,R')"
            ),
            (
                '"0d-11A":"NDQ3584", "12A-17A":"NDQ3585", "18A-29A":"NDQ3586", "30A-59A":"NDQ3587", "60A+":"NDQ3588"',
                "Rehabilit_FSM_Rehab_Alta('F799, F798, F791, F790, F789, F788, F781, F780, F739, F738, F731, F730, F729, F728, F721, F720, F719, F718, F711, F710, F709, F708, F701, F700','N,R')"
            ),
            (
                '"0d-11A":"NDQ3589", "12A-17A":"NDQ3590", "18A-29A":"NDQ3591", "30A-59A":"NDQ3592", "60A+":"NDQ3593"',
                "Rehabilit_FSM_Rehab_Alta('F840, F841, F842, F843, F844, F845, F848, F849, F900, F901, F908, F909, F910, F911, F912, F9121, F9122, F913, F918, F919','N,R')"
            ),
            (
                '"0d-11A":"NDQ3594", "12A-17A":"NDQ3595", "18A-29A":"NDQ3596", "30A-59A":"NDQ3597", "60A+":"NDQ3598"',
                "Rehabilit_FSM_Rehab_Alta('F310, F311, F312, F313, F314, F315, F316, F317, F318, F319, F200, F201, F202, F203, F204, F205, F206, F207, F208, F209, F060, F061, F062, F063, F064, F065, F066, F067, F068, F069, F030, F031, F032, F033, F034, F035, F036, F037, F038, F039, F010, F011, F012, F013, F014, F015, F016, F017, F018, F019, G300, G301, G302, G303, G304, G305, G306, G307, G308, G309, G311, G319, F03X, F028','N,R')"
            ),
            (
                '"0d-11A":"NDQ3599", "12A-17A":"NDQ3600", "18A-29A":"NDQ3601", "30A-59A":"NDQ3602", "60A+":"NDQ3603"',
                "Rehabilit_FSM_SinCert('F810, F811, F812, F813, F818, F819, F820, F821, F822, F823, F824, F825, F826, F827, F828, F829, Z558','N,R')"
            ),
            (
                '"0d-11A":"NDQ3604", "12A-17A":"NDQ3605", "18A-29A":"NDQ3606", "30A-59A":"NDQ3607", "60A+":"NDQ3608"',
                "Rehabilit_FSM_SinCert('F799, F798, F791, F790, F789, F788, F781, F780, F739, F738, F731, F730, F729, F728, F721, F720, F719, F718, F711, F710, F709, F708, F701, F700','N,R')"
            ),
            (
                '"0d-11A":"NDQ3609", "12A-17A":"NDQ3610", "18A-29A":"NDQ3611", "30A-59A":"NDQ3612", "60A+":"NDQ3613"',
                "Rehabilit_FSM_SinCert('F840, F841, F842, F843, F844, F845, F848, F849, F900, F901, F908, F909, F910, F911, F912, F9121, F9122, F913, F918, F919','N,R')"
            ),
            (
                '"0d-11A":"NDQ3614", "12A-17A":"NDQ3615", "18A-29A":"NDQ3616", "30A-59A":"NDQ3617", "60A+":"NDQ3618"',
                "Rehabilit_FSM_SinCert('F310, F311, F312, F313, F314, F315, F316, F317, F318, F319, F200, F201, F202, F203, F204, F205, F206, F207, F208, F209, F060, F061, F062, F063, F064, F065, F066, F067, F068, F069, F030, F031, F032, F033, F034, F035, F036, F037, F038, F039, F010, F011, F012, F013, F014, F015, F016, F017, F018, F019, G300, G301, G302, G303, G304, G305, G306, G307, G308, G309, G311, G319, F03X, F028','N,R')"
            ),
            (
                '"0d-11A":"NDQ3619", "12A-17A":"NDQ3620", "18A-29A":"NDQ3621", "30A-59A":"NDQ3622", "60A+":"NDQ3623"',
                "Rehabilit_FSM_ServEval('F810, F811, F812, F813, F818, F819, F820, F821, F822, F823, F824, F825, F826, F827, F828, F829, Z558','N,R')"
            ),
            (
                '"0d-11A":"NDQ3624", "12A-17A":"NDQ3625", "18A-29A":"NDQ3626", "30A-59A":"NDQ3627", "60A+":"NDQ3628"',
                "Rehabilit_FSM_ServEval('F799, F798, F791, F790, F789, F788, F781, F780, F739, F738, F731, F730, F729, F728, F721, F720, F719, F718, F711, F710, F709, F708, F701, F700','N,R')"
            ),
            (
                '"0d-11A":"NDQ3629", "12A-17A":"NDQ3630", "18A-29A":"NDQ3631", "30A-59A":"NDQ3632", "60A+":"NDQ3633"',
                "Rehabilit_FSM_ServEval('F840, F841, F842, F843, F844, F845, F848, F849, F900, F901, F908, F909, F910, F911, F912, F9121, F9122, F913, F918, F919','N,R')"
            ),
            (
                '"0d-11A":"NDQ3634", "12A-17A":"NDQ3635", "18A-29A":"NDQ3636", "30A-59A":"NDQ3637", "60A+":"NDQ3638"',
                "Rehabilit_FSM_ServEval('F310, F311, F312, F313, F314, F315, F316, F317, F318, F319, F200, F201, F202, F203, F204, F205, F206, F207, F208, F209, F060, F061, F062, F063, F064, F065, F066, F067, F068, F069, F030, F031, F032, F033, F034, F035, F036, F037, F038, F039, F010, F011, F012, F013, F014, F015, F016, F017, F018, F019, G300, G301, G302, G303, G304, G305, G306, G307, G308, G309, G311, G319, F03X, F028','N,R')"
            ),
            (
                '"0d-11A":"NDQ3639", "12A-17A":"NDQ3640", "18A-29A":"NDQ3641", "30A-59A":"NDQ3642", "60A+":"NDQ3643"',
                "Rehabilit_FSM_EnRiesgo('F810, F811, F812, F813, F818, F819, F820, F821, F822, F823, F824, F825, F826, F827, F828, F829, Z558','N,R')"
            ),
            (
                '"0d-11A":"NDQ3644", "12A-17A":"NDQ3645", "18A-29A":"NDQ3646", "30A-59A":"NDQ3647", "60A+":"NDQ3648"',
                "Rehabilit_FSM_EnRiesgo('F799, F798, F791, F790, F789, F788, F781, F780, F739, F738, F731, F730, F729, F728, F721, F720, F719, F718, F711, F710, F709, F708, F701, F700','N,R')"
            ),
            (
                '"0d-11A":"NDQ3649", "12A-17A":"NDQ3650", "18A-29A":"NDQ3651", "30A-59A":"NDQ3652", "60A+":"NDQ3653"',
                "Rehabilit_FSM_EnRiesgo('F840, F841, F842, F843, F844, F845, F848, F849, F900, F901, F908, F909, F910, F911, F912, F9121, F9122, F913, F918, F919','N,R')"
            ),
            (
                '"0d-11A":"NDQ3654", "12A-17A":"NDQ3655", "18A-29A":"NDQ3656", "30A-59A":"NDQ3657", "60A+":"NDQ3658"',
                "Rehabilit_FSM_EnRiesgo('F310, F311, F312, F313, F314, F315, F316, F317, F318, F319, F200, F201, F202, F203, F204, F205, F206, F207, F208, F209, F060, F061, F062, F063, F064, F065, F066, F067, F068, F069, F030, F031, F032, F033, F034, F035, F036, F037, F038, F039, F010, F011, F012, F013, F014, F015, F016, F017, F018, F019, G300, G301, G302, G303, G304, G305, G306, G307, G308, G309, G311, G319, F03X, F028','N,R')"
            ),
            (
                '"0d-11A":"NDQ3659", "12A-17A":"NDQ3660", "18A-29A":"NDQ3661", "30A-59A":"NDQ3662", "60A+":"NDQ3663"',
                "Rehabilit_FSM_RefContraResto('F810, F811, F812, F813, F818, F819, F820, F821, F822, F823, F824, F825, F826, F827, F828, F829, Z558','N,R')"
            ),
            (
                '"0d-11A":"NDQ3664", "12A-17A":"NDQ3665", "18A-29A":"NDQ3666", "30A-59A":"NDQ3667", "60A+":"NDQ3668"',
                "Rehabilit_FSM_RefContraResto('F799, F798, F791, F790, F789, F788, F781, F780, F739, F738, F731, F730, F729, F728, F721, F720, F719, F718, F711, F710, F709, F708, F701, F700','N,R')"
            ),
            (
                '"0d-11A":"NDQ3669", "12A-17A":"NDQ3670", "18A-29A":"NDQ3671", "30A-59A":"NDQ3672", "60A+":"NDQ3673"',
                "Rehabilit_FSM_RefContraResto('F840, F841, F842, F843, F844, F845, F848, F849, F900, F901, F908, F909, F910, F911, F912, F9121, F9122, F913, F918, F919','N,R')"
            ),
            (
                '"0d-11A":"NDQ3674", "12A-17A":"NDQ3675", "18A-29A":"NDQ3676", "30A-59A":"NDQ3677", "60A+":"NDQ3678"',
                "Rehabilit_FSM_RefContraResto('F310, F311, F312, F313, F314, F315, F316, F317, F318, F319, F200, F201, F202, F203, F204, F205, F206, F207, F208, F209, F060, F061, F062, F063, F064, F065, F066, F067, F068, F069, F030, F031, F032, F033, F034, F035, F036, F037, F038, F039, F010, F011, F012, F013, F014, F015, F016, F017, F018, F019, G300, G301, G302, G303, G304, G305, G306, G307, G308, G309, G311, G319, F03X, F028','N,R')"
            ),
            (
                '"0d-11A":"NDQ3679", "12A-17A":"NDQ3680", "18A-29A":"NDQ3681", "30A-59A":"NDQ3682", "60A+":"NDQ3683"',
                "Rehabilit_FSM_Telemed('F810, F811, F812, F813, F818, F819, F820, F821, F822, F823, F824, F825, F826, F827, F828, F829, Z558','N,R')"
            ),
            (
                '"0d-11A":"NDQ3684", "12A-17A":"NDQ3685", "18A-29A":"NDQ3686", "30A-59A":"NDQ3687", "60A+":"NDQ3688"',
                "Rehabilit_FSM_Telemed('F799, F798, F791, F790, F789, F788, F781, F780, F739, F738, F731, F730, F729, F728, F721, F720, F719, F718, F711, F710, F709, F708, F701, F700','N,R')"
            ),
            (
                '"0d-11A":"NDQ3689", "12A-17A":"NDQ3690", "18A-29A":"NDQ3691", "30A-59A":"NDQ3692", "60A+":"NDQ3693"',
                "Rehabilit_FSM_Telemed('F840, F841, F842, F843, F844, F845, F848, F849, F900, F901, F908, F909, F910, F911, F912, F9121, F9122, F913, F918, F919','N,R')"
            ),
            (
                '"0d-11A":"NDQ3694", "12A-17A":"NDQ3695", "18A-29A":"NDQ3696", "30A-59A":"NDQ3697", "60A+":"NDQ3698"',
                "Rehabilit_FSM_Telemed('F310, F311, F312, F313, F314, F315, F316, F317, F318, F319, F200, F201, F202, F203, F204, F205, F206, F207, F208, F209, F060, F061, F062, F063, F064, F065, F066, F067, F068, F069, F030, F031, F032, F033, F034, F035, F036, F037, F038, F039, F010, F011, F012, F013, F014, F015, F016, F017, F018, F019, G300, G301, G302, G303, G304, G305, G306, G307, G308, G309, G311, G319, F03X, F028','N,R')"
            ),
            (
                '"0d-11A":"NDQ3699", "12A-17A":"NDQ3700", "18A-29A":"NDQ3701", "30A-59A":"NDQ3702", "60A+":"NDQ3703"',
                "Rehabilit_FSM_ConCert('F810, F811, F812, F813, F818, F819, F820, F821, F822, F823, F824, F825, F826, F827, F828, F829, Z558','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3704", "12A-17A":"NDQ3705", "18A-29A":"NDQ3706", "30A-59A":"NDQ3707", "60A+":"NDQ3708"',
                "Rehabilit_FSM_ConCert('F799, F798, F791, F790, F789, F788, F781, F780, F739, F738, F731, F730, F729, F728, F721, F720, F719, F718, F711, F710, F709, F708, F701, F700','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3709", "12A-17A":"NDQ3710", "18A-29A":"NDQ3711", "30A-59A":"NDQ3712", "60A+":"NDQ3713"',
                "Rehabilit_FSM_ConCert('F840, F841, F842, F843, F844, F845, F848, F849, F900, F901, F908, F909, F910, F911, F912, F9121, F9122, F913, F918, F919','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3714", "12A-17A":"NDQ3715", "18A-29A":"NDQ3716", "30A-59A":"NDQ3717", "60A+":"NDQ3718"',
                "Rehabilit_FSM_ConCert('F310, F311, F312, F313, F314, F315, F316, F317, F318, F319, F200, F201, F202, F203, F204, F205, F206, F207, F208, F209, F060, F061, F062, F063, F064, F065, F066, F067, F068, F069, F030, F031, F032, F033, F034, F035, F036, F037, F038, F039, F010, F011, F012, F013, F014, F015, F016, F017, F018, F019, G300, G301, G302, G303, G304, G305, G306, G307, G308, G309, G311, G319, F03X, F028','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3719", "12A-17A":"NDQ3720", "18A-29A":"NDQ3721", "30A-59A":"NDQ3722", "60A+":"NDQ3723"',
                "Rehabilit_FSM_Nml_NCR('F810, F811, F812, F813, F818, F819, F820, F821, F822, F823, F824, F825, F826, F827, F828, F829, Z558','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3724", "12A-17A":"NDQ3725", "18A-29A":"NDQ3726", "30A-59A":"NDQ3727", "60A+":"NDQ3728"',
                "Rehabilit_FSM_Nml_NCR('F799, F798, F791, F790, F789, F788, F781, F780, F739, F738, F731, F730, F729, F728, F721, F720, F719, F718, F711, F710, F709, F708, F701, F700','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3729", "12A-17A":"NDQ3730", "18A-29A":"NDQ3731", "30A-59A":"NDQ3732", "60A+":"NDQ3733"',
                "Rehabilit_FSM_Nml_NCR('F840, F841, F842, F843, F844, F845, F848, F849, F900, F901, F908, F909, F910, F911, F912, F9121, F9122, F913, F918, F919','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3734", "12A-17A":"NDQ3735", "18A-29A":"NDQ3736", "30A-59A":"NDQ3737", "60A+":"NDQ3738"',
                "Rehabilit_FSM_Nml_NCR('F310, F311, F312, F313, F314, F315, F316, F317, F318, F319, F200, F201, F202, F203, F204, F205, F206, F207, F208, F209, F060, F061, F062, F063, F064, F065, F066, F067, F068, F069, F030, F031, F032, F033, F034, F035, F036, F037, F038, F039, F010, F011, F012, F013, F014, F015, F016, F017, F018, F019, G300, G301, G302, G303, G304, G305, G306, G307, G308, G309, G311, G319, F03X, F028','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3739", "12A-17A":"NDQ3740", "18A-29A":"NDQ3741", "30A-59A":"NDQ3742", "60A+":"NDQ3743"',
                "Rehabilit_FSM_SinCert('F810, F811, F812, F813, F818, F819, F820, F821, F822, F823, F824, F825, F826, F827, F828, F829, Z558','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3744", "12A-17A":"NDQ3745", "18A-29A":"NDQ3746", "30A-59A":"NDQ3747", "60A+":"NDQ3748"',
                "Rehabilit_FSM_SinCert('F799, F798, F791, F790, F789, F788, F781, F780, F739, F738, F731, F730, F729, F728, F721, F720, F719, F718, F711, F710, F709, F708, F701, F700','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3749", "12A-17A":"NDQ3750", "18A-29A":"NDQ3751", "30A-59A":"NDQ3752", "60A+":"NDQ3753"',
                "Rehabilit_FSM_SinCert('F840, F841, F842, F843, F844, F845, F848, F849, F900, F901, F908, F909, F910, F911, F912, F9121, F9122, F913, F918, F919','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3754", "12A-17A":"NDQ3755", "18A-29A":"NDQ3756", "30A-59A":"NDQ3757", "60A+":"NDQ3758"',
                "Rehabilit_FSM_SinCert('F310, F311, F312, F313, F314, F315, F316, F317, F318, F319, F200, F201, F202, F203, F204, F205, F206, F207, F208, F209, F060, F061, F062, F063, F064, F065, F066, F067, F068, F069, F030, F031, F032, F033, F034, F035, F036, F037, F038, F039, F010, F011, F012, F013, F014, F015, F016, F017, F018, F019, G300, G301, G302, G303, G304, G305, G306, G307, G308, G309, G311, G319, F03X, F028','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3759", "12A-17A":"NDQ3760", "18A-29A":"NDQ3761", "30A-59A":"NDQ3762", "60A+":"NDQ3763"',
                "Rehabilit_FSM_ServEval_NCR('F810, F811, F812, F813, F818, F819, F820, F821, F822, F823, F824, F825, F826, F827, F828, F829, Z558','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3764", "12A-17A":"NDQ3765", "18A-29A":"NDQ3766", "30A-59A":"NDQ3767", "60A+":"NDQ3768"',
                "Rehabilit_FSM_ServEval_NCR('F799, F798, F791, F790, F789, F788, F781, F780, F739, F738, F731, F730, F729, F728, F721, F720, F719, F718, F711, F710, F709, F708, F701, F700','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3769", "12A-17A":"NDQ3770", "18A-29A":"NDQ3771", "30A-59A":"NDQ3772", "60A+":"NDQ3773"',
                "Rehabilit_FSM_ServEval_NCR('F840, F841, F842, F843, F844, F845, F848, F849, F900, F901, F908, F909, F910, F911, F912, F9121, F9122, F913, F918, F919','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3774", "12A-17A":"NDQ3775", "18A-29A":"NDQ3776", "30A-59A":"NDQ3777", "60A+":"NDQ3778"',
                "Rehabilit_FSM_ServEval_NCR('F310, F311, F312, F313, F314, F315, F316, F317, F318, F319, F200, F201, F202, F203, F204, F205, F206, F207, F208, F209, F060, F061, F062, F063, F064, F065, F066, F067, F068, F069, F030, F031, F032, F033, F034, F035, F036, F037, F038, F039, F010, F011, F012, F013, F014, F015, F016, F017, F018, F019, G300, G301, G302, G303, G304, G305, G306, G307, G308, G309, G311, G319, F03X, F028','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3779", "12A-17A":"NDQ3780", "18A-29A":"NDQ3781", "30A-59A":"NDQ3782", "60A+":"NDQ3783"',
                "Rehabilit_FSM_Ambulatoria_NCR('F810, F811, F812, F813, F818, F819, F820, F821, F822, F823, F824, F825, F826, F827, F828, F829, Z558','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3784", "12A-17A":"NDQ3785", "18A-29A":"NDQ3786", "30A-59A":"NDQ3787", "60A+":"NDQ3788"',
                "Rehabilit_FSM_Ambulatoria_NCR('F799, F798, F791, F790, F789, F788, F781, F780, F739, F738, F731, F730, F729, F728, F721, F720, F719, F718, F711, F710, F709, F708, F701, F700','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3789", "12A-17A":"NDQ3790", "18A-29A":"NDQ3791", "30A-59A":"NDQ3792", "60A+":"NDQ3793"',
                "Rehabilit_FSM_Ambulatoria_NCR('F840, F841, F842, F843, F844, F845, F848, F849, F900, F901, F908, F909, F910, F911, F912, F9121, F9122, F913, F918, F919','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3794", "12A-17A":"NDQ3795", "18A-29A":"NDQ3796", "30A-59A":"NDQ3797", "60A+":"NDQ3798"',
                "Rehabilit_FSM_Ambulatoria_NCR('F310, F311, F312, F313, F314, F315, F316, F317, F318, F319, F200, F201, F202, F203, F204, F205, F206, F207, F208, F209, F060, F061, F062, F063, F064, F065, F066, F067, F068, F069, F030, F031, F032, F033, F034, F035, F036, F037, F038, F039, F010, F011, F012, F013, F014, F015, F016, F017, F018, F019, G300, G301, G302, G303, G304, G305, G306, G307, G308, G309, G311, G319, F03X, F028','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3799", "12A-17A":"NDQ3800", "18A-29A":"NDQ3801", "30A-59A":"NDQ3802", "60A+":"NDQ3803"',
                "Rehabilit_FSM_ReviFinal_NCR('F810, F811, F812, F813, F818, F819, F820, F821, F822, F823, F824, F825, F826, F827, F828, F829, Z558','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3804", "12A-17A":"NDQ3805", "18A-29A":"NDQ3806", "30A-59A":"NDQ3807", "60A+":"NDQ3808"',
                "Rehabilit_FSM_ReviFinal_NCR('F799, F798, F791, F790, F789, F788, F781, F780, F739, F738, F731, F730, F729, F728, F721, F720, F719, F718, F711, F710, F709, F708, F701, F700','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3809", "12A-17A":"NDQ3810", "18A-29A":"NDQ3811", "30A-59A":"NDQ3812", "60A+":"NDQ3813"',
                "Rehabilit_FSM_ReviFinal_NCR('F840, F841, F842, F843, F844, F845, F848, F849, F900, F901, F908, F909, F910, F911, F912, F9121, F9122, F913, F918, F919','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3814", "12A-17A":"NDQ3815", "18A-29A":"NDQ3816", "30A-59A":"NDQ3817", "60A+":"NDQ3818"',
                "Rehabilit_FSM_ReviFinal_NCR('F310, F311, F312, F313, F314, F315, F316, F317, F318, F319, F200, F201, F202, F203, F204, F205, F206, F207, F208, F209, F060, F061, F062, F063, F064, F065, F066, F067, F068, F069, F030, F031, F032, F033, F034, F035, F036, F037, F038, F039, F010, F011, F012, F013, F014, F015, F016, F017, F018, F019, G300, G301, G302, G303, G304, G305, G306, G307, G308, G309, G311, G319, F03X, F028','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3819", "12A-17A":"NDQ3820", "18A-29A":"NDQ3821", "30A-59A":"NDQ3822", "60A+":"NDQ3823"',
                "Rehabilit_FSM_Telemed('F810, F811, F812, F813, F818, F819, F820, F821, F822, F823, F824, F825, F826, F827, F828, F829, Z558','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3824", "12A-17A":"NDQ3825", "18A-29A":"NDQ3826", "30A-59A":"NDQ3827", "60A+":"NDQ3828"',
                "Rehabilit_FSM_Telemed('F799, F798, F791, F790, F789, F788, F781, F780, F739, F738, F731, F730, F729, F728, F721, F720, F719, F718, F711, F710, F709, F708, F701, F700','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3829", "12A-17A":"NDQ3830", "18A-29A":"NDQ3831", "30A-59A":"NDQ3832", "60A+":"NDQ3833"',
                "Rehabilit_FSM_Telemed('F840, F841, F842, F843, F844, F845, F848, F849, F900, F901, F908, F909, F910, F911, F912, F9121, F9122, F913, F918, F919','N,C,R')"
            ),
            (
                '"0d-11A":"NDQ3834", "12A-17A":"NDQ3835", "18A-29A":"NDQ3836", "30A-59A":"NDQ3837", "60A+":"NDQ3838"',
                "Rehabilit_FSM_Telemed('F310, F311, F312, F313, F314, F315, F316, F317, F318, F319, F200, F201, F202, F203, F204, F205, F206, F207, F208, F209, F060, F061, F062, F063, F064, F065, F066, F067, F068, F069, F030, F031, F032, F033, F034, F035, F036, F037, F038, F039, F010, F011, F012, F013, F014, F015, F016, F017, F018, F019, G300, G301, G302, G303, G304, G305, G306, G307, G308, G309, G311, G319, F03X, F028','N,C,R')"
            ),

        ],

        "FACT_DISC_SNAPSHOT_CERT_EESS": [
            (
                '"0d-11A":"NDQ3839", "12A-17A":"NDQ3840", "18A-29A":"NDQ3841", "30A-59A":"NDQ3842", "60A+":"NDQ3843"',
                "dbo.Certif_Eess_Eva();"
            ),
            (
                '"0d-11A":"NDQ3844", "12A-17A":"NDQ3845", "18A-29A":"NDQ3846", "30A-59A":"NDQ3847", "60A+":"NDQ3848"',
                "dbo.Certif_Eess_Cali();"
            ),
            (
                '"0d-11A":"NDQ3849", "12A-17A":"NDQ3850", "18A-29A":"NDQ3851", "30A-59A":"NDQ3852", "60A+":"NDQ3853"',
                "dbo.Certif_Eess_Cert();"
            ),
        ],

        "FACT_DISC_SNAPSHOT_COMUNID_FAMILIAR": [
            (
                '"0d-11A":"NDQ3869", "12A-17A":"NDQ3870", "18A-29A":"NDQ3871", "30A-59A":"NDQ3872", "60A+":"NDQ3873"',
                "dbo.Capa_Familia_ConCert('1')"
            ),
            (
                '"0d-11A":"NDQ3874", "12A-17A":"NDQ3875", "18A-29A":"NDQ3876", "30A-59A":"NDQ3877", "60A+":"NDQ3878"',
                "dbo.Capa_Familia_SinCert('1')"
            ),
            (
                '"0d-11A":"NDQ3879", "12A-17A":"NDQ3880", "18A-29A":"NDQ3881", "30A-59A":"NDQ3882", "60A+":"NDQ3883"',
                "dbo.Capa_Familia_ConCert('2')"
            ),
            (
                '"0d-11A":"NDQ3884", "12A-17A":"NDQ3885", "18A-29A":"NDQ3886", "30A-59A":"NDQ3887", "60A+":"NDQ3888"',
                "dbo.Capa_Familia_SinCert('2')"
            ),
            (
                '"0d-11A":"NDQ3889", "12A-17A":"NDQ3890", "18A-29A":"NDQ3891", "30A-59A":"NDQ3892", "60A+":"NDQ3893"',
                "dbo.Capa_Familia_ConCert('3')"
            ),
            (
                '"0d-11A":"NDQ3894", "12A-17A":"NDQ3895", "18A-29A":"NDQ3896", "30A-59A":"NDQ3897", "60A+":"NDQ3898"',
                "dbo.Capa_Familia_SinCert('3')"
            ),
        ]
        
    }
}
