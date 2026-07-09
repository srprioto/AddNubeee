# -*- coding: utf-8 -*-
"""
Autor: Yo!
Fecha: 2026
"""

NOMBRE_TABLA = "FACT_DISC_SNAPSHOT_CAP_MED_REHAB"

# ====================================================================================
# CONSTANTE: INDICADORES SOLO (Para SP_CargarFuncionAMatriz)
# ====================================================================================
# Formato: (NombreColumna, FuncionSQL)
INDICADORESSOLO = [
    ('NDQ1', "dbo.Capa_Med_Reh_1_N()"),
    ('NDQ2', "dbo.Capa_Med_Reh_1_S('1')"),
    ('NDQ3', "dbo.Capa_Med_Reh_1_S('2')"),
    ('NDQ4', "dbo.Capa_Med_Reh_1_S('3')"),
    ('NDQ5', "dbo.Capa_Med_Reh_1_S('4')"),
    ('NDQ6', "dbo.Capa_Med_Reh_1_S5()"),
    ('NDQ7', "dbo.Capa_Med_Reh_1_Sta()"),
    ('NDQ8', "dbo.Capa_Med_Reh_2_N('9945001', '2')"),
    ('NDQ9', "dbo.Capa_Med_Reh_2_S('9945001', '2', '1')"),
    ('NDQ10', "dbo.Capa_Med_Reh_2_S('9945001', '2', '2')"),
    ('NDQ11', "dbo.Capa_Med_Reh_2_S('9945001', '2', '3')"),
    ('NDQ12', "dbo.Capa_Med_Reh_2_S('9945001', '2', '4')"),
    ('NDQ13', "dbo.Capa_Med_Reh_2_S5('9945001', '2')"),
    ('NDQ14', "dbo.Capa_Med_Reh_2_Sta('9945001', '2')"),
    ('NDQ15', "dbo.Capa_Med_Reh_2_N('99201,99202,99203,99204,97762,97703', '3')"),
    ('NDQ16', "dbo.Capa_Med_Reh_2_S('99201,99202,99203,99204,97762,97703', '3', '1')"),
    ('NDQ17', "dbo.Capa_Med_Reh_2_S('99201,99202,99203,99204,97762,97703', '3', '2')"),
    ('NDQ18', "dbo.Capa_Med_Reh_2_S('99201,99202,99203,99204,97762,97703', '3', '3')"),
    ('NDQ19', "dbo.Capa_Med_Reh_2_S('99201,99202,99203,99204,97762,97703', '3', '4')"),
    ('NDQ20', "dbo.Capa_Med_Reh_2_S5('99201,99202,99203,99204,97762,97703', '3')"),
    ('NDQ21', "dbo.Capa_Med_Reh_2_Sta('99201,99202,99203,99204,97762,97703', '3')"),
    ('NDQ22', "dbo.Capa_Med_Reh_2_N('97799', '4')"),
    ('NDQ23', "dbo.Capa_Med_Reh_2_S('97799', '4', '1')"),
    ('NDQ24', "dbo.Capa_Med_Reh_2_S('97799', '4', '2')"),
    ('NDQ25', "dbo.Capa_Med_Reh_2_S('97799', '4', '3')"),
    ('NDQ26', "dbo.Capa_Med_Reh_2_S('97799', '4', '4')"),
    ('NDQ27', "dbo.Capa_Med_Reh_2_S5('97799', '4')"),
    ('NDQ28', "dbo.Capa_Med_Reh_2_Sta('97799', '4')")
]

# ====================================================================================
# CONSTANTE: INDICADORES MULTIPLE (Para SP_CargarFuncionAMatriz_Multi)
# ====================================================================================
# Formato: (MapeoColumnasJSON, FuncionSQL)

INDICADORESMULTIPLE = [
    (
        '"0d-11A":"NDQ2999", "12A-17A":"NDQ3000", "18A-29A":"NDQ3001", "30A-59A":"NDQ3002", "60A+":"NDQ3003"',
        "dbo.RehabSensorial_ConCert('H900,H901,H902,H903,H904,H905,H906,H907,H908,H909,H910,H911,H912,H918,H919', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3004", "12A-17A":"NDQ3005", "18A-29A":"NDQ3006", "30A-59A":"NDQ3007", "60A+":"NDQ3008"',
        "dbo.RehabSensorial_Rehab_Alta('H900,H901,H902,H903,H904,H905,H906,H907,H908,H909,H910,H911,H912,H918,H919', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3009", "12A-17A":"NDQ3010", "18A-29A":"NDQ3011", "30A-59A":"NDQ3012", "60A+":"NDQ3013"',
        "dbo.RehabSensorial_SinCert('H900,H901,H902,H903,H904,H905,H906,H907,H908,H909,H910,H911,H912,H918,H919', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3014", "12A-17A":"NDQ3015", "18A-29A":"NDQ3016", "30A-59A":"NDQ3017", "60A+":"NDQ3018"',
        "dbo.RehabSensorial_ServEval('H900,H901,H902,H903,H904,H905,H906,H907,H908,H909,H910,H911,H912,H918,H919', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3019", "12A-17A":"NDQ3020", "18A-29A":"NDQ3021", "30A-59A":"NDQ3022", "60A+":"NDQ3023"',
        "dbo.RehabSensorial_EnRiesgo('H900,H901,H902,H903,H904,H905,H906,H907,H908,H909,H910,H911,H912,H918,H919', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3024", "12A-17A":"NDQ3025", "18A-29A":"NDQ3026", "30A-59A":"NDQ3027", "60A+":"NDQ3028"',
        "dbo.RehabSensorial_RefContra('H900,H901,H902,H903,H904,H905,H906,H907,H908,H909,H910,H911,H912,H918,H919', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3029", "12A-17A":"NDQ3030", "18A-29A":"NDQ3031", "30A-59A":"NDQ3032", "60A+":"NDQ3033"',
        "dbo.RehabSensorial_Telemed('H900,H901,H902,H903,H904,H905,H906,H907,H908,H909,H910,H911,H912,H918,H919', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3034", "12A-17A":"NDQ3035", "18A-29A":"NDQ3036", "30A-59A":"NDQ3037", "60A+":"NDQ3038"',
        "dbo.RehabSensorial_ConCert('H900,H901,H902,H903,H904,H905,H906,H907,H908,H909,H910,H911,H912,H918,H919', 'N,C,R')"
    ),
    (
        '"0d-11A":"NDQ3039", "12A-17A":"NDQ3040", "18A-29A":"NDQ3041", "30A-59A":"NDQ3042", "60A+":"NDQ3043"',
        "dbo.RehabSensorial_Rehab_Nml_NCR('H900,H901,H902,H903,H904,H905,H906,H907,H908,H909,H910,H911,H912,H918,H919')"
    ),
    (
        '"0d-11A":"NDQ3044", "12A-17A":"NDQ3045", "18A-29A":"NDQ3046", "30A-59A":"NDQ3047", "60A+":"NDQ3048"',
        "dbo.RehabSensorial_SinCert('H900,H901,H902,H903,H904,H905,H906,H907,H908,H909,H910,H911,H912,H918,H919', 'N,C,R')"
    ),
    (
        '"0d-11A":"NDQ3049", "12A-17A":"NDQ3050", "18A-29A":"NDQ3051", "30A-59A":"NDQ3052", "60A+":"NDQ3053"',
        "dbo.RehabSensorial_ServEval_NCR('H900,H901,H902,H903,H904,H905,H906,H907,H908,H909,H910,H911,H912,H918,H919')"
    ),
    (
        '"0d-11A":"NDQ3054", "12A-17A":"NDQ3055", "18A-29A":"NDQ3056", "30A-59A":"NDQ3057", "60A+":"NDQ3058"',
        "dbo.RehabSensorial_Ambulatoria_NCR('H900,H901,H902,H903,H904,H905,H906,H907,H908,H909,H910,H911,H912,H918,H919')"
    ),
    (
        '"0d-11A":"NDQ3059", "12A-17A":"NDQ3060", "18A-29A":"NDQ3061", "30A-59A":"NDQ3062", "60A+":"NDQ3063"',
        "dbo.RehabSensorial_ReviFinal_NCR('H900,H901,H902,H903,H904,H905,H906,H907,H908,H909,H910,H911,H912,H918,H919')"
    ),
    (
        '"0d-11A":"NDQ3064", "12A-17A":"NDQ3065", "18A-29A":"NDQ3066", "30A-59A":"NDQ3067", "60A+":"NDQ3068"',
        "dbo.RehabSensorial_Telemed('H900,H901,H902,H903,H904,H905,H906,H907,H908,H909,H910,H911,H912,H918,H919', 'N,C,R')"
    ),
    (
        '"0d-11A":"NDQ3069", "12A-17A":"NDQ3070", "18A-29A":"NDQ3071", "30A-59A":"NDQ3072", "60A+":"NDQ3073"',
        "dbo.RehabSensorial_ConCert('B940,H532,H534,H540,H541,H542,H543,H544,H545,H546,H547,H548,H549,R481', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3074", "12A-17A":"NDQ3075", "18A-29A":"NDQ3076", "30A-59A":"NDQ3077", "60A+":"NDQ3078"',
        "dbo.RehabSensorial_Rehab_Alta('B940,H532,H534,H540,H541,H542,H543,H544,H545,H546,H547,H548,H549,R481', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3079", "12A-17A":"NDQ3080", "18A-29A":"NDQ3081", "30A-59A":"NDQ3082", "60A+":"NDQ3083"',
        "dbo.RehabSensorial_SinCert('B940,H532,H534,H540,H541,H542,H543,H544,H545,H546,H547,H548,H549,R481', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3084", "12A-17A":"NDQ3085", "18A-29A":"NDQ3086", "30A-59A":"NDQ3087", "60A+":"NDQ3088"',
        "dbo.RehabSensorial_ServEval('B940,H532,H534,H540,H541,H542,H543,H544,H545,H546,H547,H548,H549,R481', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3089", "12A-17A":"NDQ3090", "18A-29A":"NDQ3091", "30A-59A":"NDQ3092", "60A+":"NDQ3093"',
        "dbo.RehabSensorial_EnRiesgo('B940,H532,H534,H540,H541,H542,H543,H544,H545,H546,H547,H548,H549,R481', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3094", "12A-17A":"NDQ3095", "18A-29A":"NDQ3096", "30A-59A":"NDQ3097", "60A+":"NDQ3098"',
        "dbo.RehabSensorial_RefContra('B940,H532,H534,H540,H541,H542,H543,H544,H545,H546,H547,H548,H549,R481', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3099", "12A-17A":"NDQ3100", "18A-29A":"NDQ3101", "30A-59A":"NDQ3102", "60A+":"NDQ3103"',
        "dbo.RehabSensorial_Telemed('B940,H532,H534,H540,H541,H542,H543,H544,H545,H546,H547,H548,H549,R481', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3104", "12A-17A":"NDQ3105", "18A-29A":"NDQ3106", "30A-59A":"NDQ3107", "60A+":"NDQ3108"',
        "dbo.RehabSensorial_ConCert('B940,H532,H534,H540,H541,H542,H543,H544,H545,H546,H547,H548,H549,R481', 'N,C,R')"
    ),
    (
        '"0d-11A":"NDQ3109", "12A-17A":"NDQ3110", "18A-29A":"NDQ3111", "30A-59A":"NDQ3112", "60A+":"NDQ3113"',
        "dbo.RehabSensorial_Rehab_Nml_NCR('B940,H532,H534,H540,H541,H542,H543,H544,H545,H546,H547,H548,H549,R481')"
    ),
    (
        '"0d-11A":"NDQ3114", "12A-17A":"NDQ3115", "18A-29A":"NDQ3116", "30A-59A":"NDQ3117", "60A+":"NDQ3118"',
        "dbo.RehabSensorial_SinCert('B940,H532,H534,H540,H541,H542,H543,H544,H545,H546,H547,H548,H549,R481', 'N,C,R')"
    ),
    (
        '"0d-11A":"NDQ3119", "12A-17A":"NDQ3120", "18A-29A":"NDQ3121", "30A-59A":"NDQ3122", "60A+":"NDQ3123"',
        "dbo.RehabSensorial_ServEval_NCR('B940,H532,H534,H540,H541,H542,H543,H544,H545,H546,H547,H548,H549,R481')"
    ),
    (
        '"0d-11A":"NDQ3124", "12A-17A":"NDQ3125", "18A-29A":"NDQ3126", "30A-59A":"NDQ3127", "60A+":"NDQ3128"',
        "dbo.RehabSensorial_Ambulatoria_NCR('B940,H532,H534,H540,H541,H542,H543,H544,H545,H546,H547,H548,H549,R481')"
    ),
    (
        '"0d-11A":"NDQ3129", "12A-17A":"NDQ3130", "18A-29A":"NDQ3131", "30A-59A":"NDQ3132", "60A+":"NDQ3133"',
        "dbo.RehabSensorial_ReviFinal_NCR('B940,H532,H534,H540,H541,H542,H543,H544,H545,H546,H547,H548,H549,R481')"
    ),
    (
        '"0d-11A":"NDQ3134", "12A-17A":"NDQ3135", "18A-29A":"NDQ3136", "30A-59A":"NDQ3137", "60A+":"NDQ3138"',
        "dbo.RehabSensorial_Telemed('B940,H532,H534,H540,H541,H542,H543,H544,H545,H546,H547,H548,H549,R481', 'N,C,R')"
    ),
    (
        '"0d-11A":"NDQ3139", "12A-17A":"NDQ3140", "18A-29A":"NDQ3141", "30A-59A":"NDQ3142", "60A+":"NDQ3143"',
        "dbo.RehabSensorial_ConCert('H913', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3144", "12A-17A":"NDQ3145", "18A-29A":"NDQ3146", "30A-59A":"NDQ3147", "60A+":"NDQ3148"',
        "dbo.RehabSensorial_Rehab_Alta('H913', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3149", "12A-17A":"NDQ3150", "18A-29A":"NDQ3151", "30A-59A":"NDQ3152", "60A+":"NDQ3153"',
        "dbo.RehabSensorial_SinCert('H913', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3154", "12A-17A":"NDQ3155", "18A-29A":"NDQ3156", "30A-59A":"NDQ3157", "60A+":"NDQ3158"',
        "dbo.RehabSensorial_ServEval('H913', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3159", "12A-17A":"NDQ3160", "18A-29A":"NDQ3161", "30A-59A":"NDQ3162", "60A+":"NDQ3163"',
        "dbo.RehabSensorial_EnRiesgo('H913', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3164", "12A-17A":"NDQ3165", "18A-29A":"NDQ3166", "30A-59A":"NDQ3167", "60A+":"NDQ3168"',
        "dbo.RehabSensorial_RefContra('H913', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3169", "12A-17A":"NDQ3170", "18A-29A":"NDQ3171", "30A-59A":"NDQ3172", "60A+":"NDQ3173"',
        "dbo.RehabSensorial_Telemed('H913', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3174", "12A-17A":"NDQ3175", "18A-29A":"NDQ3176", "30A-59A":"NDQ3177", "60A+":"NDQ3178"',
        "dbo.RehabSensorial_ConCert('H913', 'N,C,R')"
    ),
    (
        '"0d-11A":"NDQ3179", "12A-17A":"NDQ3180", "18A-29A":"NDQ3181", "30A-59A":"NDQ3182", "60A+":"NDQ3183"',
        "dbo.RehabSensorial_Rehab_Nml_NCR('H913')"
    ),
    (
        '"0d-11A":"NDQ3184", "12A-17A":"NDQ3185", "18A-29A":"NDQ3186", "30A-59A":"NDQ3187", "60A+":"NDQ3188"',
        "dbo.RehabSensorial_SinCert('H913', 'N,C,R')"
    ),
    (
        '"0d-11A":"NDQ3189", "12A-17A":"NDQ3190", "18A-29A":"NDQ3191", "30A-59A":"NDQ3192", "60A+":"NDQ3193"',
        "dbo.RehabSensorial_ServEval_NCR('H913')"
    ),
    (
        '"0d-11A":"NDQ3194", "12A-17A":"NDQ3195", "18A-29A":"NDQ3196", "30A-59A":"NDQ3197", "60A+":"NDQ3198"',
        "dbo.RehabSensorial_Ambulatoria_NCR('H913')"
    ),
    (
        '"0d-11A":"NDQ3199", "12A-17A":"NDQ3200", "18A-29A":"NDQ3201", "30A-59A":"NDQ3202", "60A+":"NDQ3203"',
        "dbo.RehabSensorial_ReviFinal_NCR('H913')"
    ),
    (
        '"0d-11A":"NDQ3204", "12A-17A":"NDQ3205", "18A-29A":"NDQ3206", "30A-59A":"NDQ3207", "60A+":"NDQ3208"',
        "dbo.RehabSensorial_Telemed('H913', 'N,C,R')"
    ),
    (
        '"0d-11A":"NDQ3209", "12A-17A":"NDQ3210", "18A-29A":"NDQ3211", "30A-59A":"NDQ3212", "60A+":"NDQ3213"',
        "dbo.RehabSensorial_ConCert('R470,R481,R482', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3214", "12A-17A":"NDQ3215", "18A-29A":"NDQ3216", "30A-59A":"NDQ3217", "60A+":"NDQ3218"',
        "dbo.RehabSensorial_Rehab_Alta('R470,R481,R482', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3219", "12A-17A":"NDQ3220", "18A-29A":"NDQ3221", "30A-59A":"NDQ3222", "60A+":"NDQ3223"',
        "dbo.RehabSensorial_SinCert('R470,R481,R482', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3224", "12A-17A":"NDQ3225", "18A-29A":"NDQ3226", "30A-59A":"NDQ3227", "60A+":"NDQ3228"',
        "dbo.RehabSensorial_ServEval('R470,R481,R482', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3229", "12A-17A":"NDQ3230", "18A-29A":"NDQ3231", "30A-59A":"NDQ3232", "60A+":"NDQ3233"',
        "dbo.RehabSensorial_EnRiesgo('R470,R481,R482', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3234", "12A-17A":"NDQ3235", "18A-29A":"NDQ3236", "30A-59A":"NDQ3237", "60A+":"NDQ3238"',
        "dbo.RehabSensorial_RefContra('R470,R481,R482', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3239", "12A-17A":"NDQ3240", "18A-29A":"NDQ3241", "30A-59A":"NDQ3242", "60A+":"NDQ3243"',
        "dbo.RehabSensorial_Telemed('R470,R481,R482', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3244", "12A-17A":"NDQ3245", "18A-29A":"NDQ3246", "30A-59A":"NDQ3247", "60A+":"NDQ3248"',
        "dbo.RehabSensorial_ConCert('R470,R481,R482', 'N,C,R')"
    ),
    (
        '"0d-11A":"NDQ3249", "12A-17A":"NDQ3250", "18A-29A":"NDQ3251", "30A-59A":"NDQ3252", "60A+":"NDQ3253"',
        "dbo.RehabSensorial_Rehab_Nml_NCR('R470,R481,R482')"
    ),
    (
        '"0d-11A":"NDQ3254", "12A-17A":"NDQ3255", "18A-29A":"NDQ3256", "30A-59A":"NDQ3257", "60A+":"NDQ3258"',
        "dbo.RehabSensorial_SinCert('R470,R481,R482', 'N,C,R')"
    ),
    (
        '"0d-11A":"NDQ3259", "12A-17A":"NDQ3260", "18A-29A":"NDQ3261", "30A-59A":"NDQ3262", "60A+":"NDQ3263"',
        "dbo.RehabSensorial_ServEval_NCR('R470,R481,R482')"
    ),
    (
        '"0d-11A":"NDQ3264", "12A-17A":"NDQ3265", "18A-29A":"NDQ3266", "30A-59A":"NDQ3267", "60A+":"NDQ3268"',
        "dbo.RehabSensorial_Ambulatoria_NCR('R470,R481,R482')"
    ),
    (
        '"0d-11A":"NDQ3269", "12A-17A":"NDQ3270", "18A-29A":"NDQ3271", "30A-59A":"NDQ3272", "60A+":"NDQ3273"',
        "dbo.RehabSensorial_ReviFinal_NCR('R470,R481,R482')"
    ),
    (
        '"0d-11A":"NDQ3274", "12A-17A":"NDQ3275", "18A-29A":"NDQ3276", "30A-59A":"NDQ3277", "60A+":"NDQ3278"',
        "dbo.RehabSensorial_Telemed('R470,R481,R482', 'N,C,R')"
    ),
    (
        '"0d-11A":"NDQ3279", "12A-17A":"NDQ3280", "18A-29A":"NDQ3281", "30A-59A":"NDQ3282", "60A+":"NDQ3283"',
        "dbo.RehabSensorial_ConCert('F800,F801,F802,F803,F804,F805,F806,F807,F808,F809,R480,R481,R482,R483,R484,R485,R486,R487,R488,R489', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3284", "12A-17A":"NDQ3285", "18A-29A":"NDQ3286", "30A-59A":"NDQ3287", "60A+":"NDQ3288"',
        "dbo.RehabSensorial_Rehab_Alta('F800,F801,F802,F803,F804,F805,F806,F807,F808,F809,R480,R481,R482,R483,R484,R485,R486,R487,R488,R489', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3289", "12A-17A":"NDQ3290", "18A-29A":"NDQ3291", "30A-59A":"NDQ3292", "60A+":"NDQ3293"',
        "dbo.RehabSensorial_SinCert('F800,F801,F802,F803,F804,F805,F806,F807,F808,F809,R480,R481,R482,R483,R484,R485,R486,R487,R488,R489', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3294", "12A-17A":"NDQ3295", "18A-29A":"NDQ3296", "30A-59A":"NDQ3297", "60A+":"NDQ3298"',
        "dbo.RehabSensorial_ServEval('F800,F801,F802,F803,F804,F805,F806,F807,F808,F809,R480,R481,R482,R483,R484,R485,R486,R487,R488,R489', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3299", "12A-17A":"NDQ3300", "18A-29A":"NDQ3301", "30A-59A":"NDQ3302", "60A+":"NDQ3303"',
        "dbo.RehabSensorial_EnRiesgo('F800,F801,F802,F803,F804,F805,F806,F807,F808,F809,R480,R481,R482,R483,R484,R485,R486,R487,R488,R489', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3304", "12A-17A":"NDQ3305", "18A-29A":"NDQ3306", "30A-59A":"NDQ3307", "60A+":"NDQ3308"',
        "dbo.RehabSensorial_RefContra('F800,F801,F802,F803,F804,F805,F806,F807,F808,F809,R480,R481,R482,R483,R484,R485,R486,R487,R488,R489', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3309", "12A-17A":"NDQ3310", "18A-29A":"NDQ3311", "30A-59A":"NDQ3312", "60A+":"NDQ3313"',
        "dbo.RehabSensorial_Telemed('F800,F801,F802,F803,F804,F805,F806,F807,F808,F809,R480,R481,R482,R483,R484,R485,R486,R487,R488,R489', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3314", "12A-17A":"NDQ3315", "18A-29A":"NDQ3316", "30A-59A":"NDQ3317", "60A+":"NDQ3318"',
        "dbo.RehabSensorial_ConCert('F800,F801,F802,F803,F804,F805,F806,F807,F808,F809,R480,R481,R482,R483,R484,R485,R486,R487,R488,R489', 'N,C,R')"
    ),
    (
        '"0d-11A":"NDQ3319", "12A-17A":"NDQ3320", "18A-29A":"NDQ3321", "30A-59A":"NDQ3322", "60A+":"NDQ3323"',
        "dbo.RehabSensorial_Rehab_Nml_NCR('F800,F801,F802,F803,F804,F805,F806,F807,F808,F809,R480,R481,R482,R483,R484,R485,R486,R487,R488,R489')"
    ),
    (
        '"0d-11A":"NDQ3324", "12A-17A":"NDQ3325", "18A-29A":"NDQ3326", "30A-59A":"NDQ3327", "60A+":"NDQ3328"',
        "dbo.RehabSensorial_SinCert('F800,F801,F802,F803,F804,F805,F806,F807,F808,F809,R480,R481,R482,R483,R484,R485,R486,R487,R488,R489', 'N,C,R')"
    ),
    (
        '"0d-11A":"NDQ3329", "12A-17A":"NDQ3330", "18A-29A":"NDQ3331", "30A-59A":"NDQ3332", "60A+":"NDQ3333"',
        "dbo.RehabSensorial_ServEval_NCR('F800,F801,F802,F803,F804,F805,F806,F807,F808,F809,R480,R481,R482,R483,R484,R485,R486,R487,R488,R489')"
    ),
    (
        '"0d-11A":"NDQ3334", "12A-17A":"NDQ3335", "18A-29A":"NDQ3336", "30A-59A":"NDQ3337", "60A+":"NDQ3338"',
        "dbo.RehabSensorial_Ambulatoria_NCR('F800,F801,F802,F803,F804,F805,F806,F807,F808,F809,R480,R481,R482,R483,R484,R485,R486,R487,R488,R489')"
    ),
    (
        '"0d-11A":"NDQ3339", "12A-17A":"NDQ3340", "18A-29A":"NDQ3341", "30A-59A":"NDQ3342", "60A+":"NDQ3343"',
        "dbo.RehabSensorial_ReviFinal_NCR('F800,F801,F802,F803,F804,F805,F806,F807,F808,F809,R480,R481,R482,R483,R484,R485,R486,R487,R488,R489')"
    ),
    (
        '"0d-11A":"NDQ3344", "12A-17A":"NDQ3345", "18A-29A":"NDQ3346", "30A-59A":"NDQ3347", "60A+":"NDQ3348"',
        "dbo.RehabSensorial_Telemed('F800,F801,F802,F803,F804,F805,F806,F807,F808,F809,R480,R481,R482,R483,R484,R485,R486,R487,R488,R489', 'N,C,R')"
    ),
    (
        '"0d-11A":"NDQ3349", "12A-17A":"NDQ3350", "18A-29A":"NDQ3351", "30A-59A":"NDQ3352", "60A+":"NDQ3353"',
        "dbo.RehabSensorial_ConCert('P050,P073,P229,P923,Z910', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3354", "12A-17A":"NDQ3355", "18A-29A":"NDQ3356", "30A-59A":"NDQ3357", "60A+":"NDQ3358"',
        "dbo.RehabSensorial_Rehab_Alta('P050,P073,P229,P923,Z910', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3359", "12A-17A":"NDQ3360", "18A-29A":"NDQ3361", "30A-59A":"NDQ3362", "60A+":"NDQ3363"',
        "dbo.RehabSensorial_SinCert('P050,P073,P229,P923,Z910', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3364", "12A-17A":"NDQ3365", "18A-29A":"NDQ3366", "30A-59A":"NDQ3367", "60A+":"NDQ3368"',
        "dbo.RehabSensorial_ServEval('P050,P073,P229,P923,Z910', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3369", "12A-17A":"NDQ3370", "18A-29A":"NDQ3371", "30A-59A":"NDQ3372", "60A+":"NDQ3373"',
        "dbo.RehabSensorial_EnRiesgo('P050,P073,P229,P923,Z910', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3374", "12A-17A":"NDQ3375", "18A-29A":"NDQ3376", "30A-59A":"NDQ3377", "60A+":"NDQ3378"',
        "dbo.RehabSensorial_RefContra('P050,P073,P229,P923,Z910', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3379", "12A-17A":"NDQ3380", "18A-29A":"NDQ3381", "30A-59A":"NDQ3382", "60A+":"NDQ3383"',
        "dbo.RehabSensorial_Telemed('P050,P073,P229,P923,Z910', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3384", "12A-17A":"NDQ3385", "18A-29A":"NDQ3386", "30A-59A":"NDQ3387", "60A+":"NDQ3388"',
        "dbo.RehabSensorial_ConCert('P050,P073,P229,P923,Z910', 'N,C,R')"
    ),
    (
        '"0d-11A":"NDQ3389", "12A-17A":"NDQ3390", "18A-29A":"NDQ3391", "30A-59A":"NDQ3392", "60A+":"NDQ3393"',
        "dbo.RehabSensorial_Rehab_Nml_NCR('P050,P073,P229,P923,Z910')"
    ),
    (
        '"0d-11A":"NDQ3394", "12A-17A":"NDQ3395", "18A-29A":"NDQ3396", "30A-59A":"NDQ3397", "60A+":"NDQ3398"',
        "dbo.RehabSensorial_SinCert('P050,P073,P229,P923,Z910', 'N,C,R')"
    ),
    (
        '"0d-11A":"NDQ3399", "12A-17A":"NDQ3400", "18A-29A":"NDQ3401", "30A-59A":"NDQ3402", "60A+":"NDQ3403"',
        "dbo.RehabSensorial_ServEval_NCR('P050,P073,P229,P923,Z910')"
    ),
    (
        '"0d-11A":"NDQ3404", "12A-17A":"NDQ3405", "18A-29A":"NDQ3406", "30A-59A":"NDQ3407", "60A+":"NDQ3408"',
        "dbo.RehabSensorial_Ambulatoria_NCR('P050,P073,P229,P923,Z910')"
    ),
    (
        '"0d-11A":"NDQ3409", "12A-17A":"NDQ3410", "18A-29A":"NDQ3411", "30A-59A":"NDQ3412", "60A+":"NDQ3413"',
        "dbo.RehabSensorial_ReviFinal_NCR('P050,P073,P229,P923,Z910')"
    ),
    (
        '"0d-11A":"NDQ3414", "12A-17A":"NDQ3415", "18A-29A":"NDQ3416", "30A-59A":"NDQ3417", "60A+":"NDQ3418"',
        "dbo.RehabSensorial_Telemed('P050,P073,P229,P923,Z910', 'N,C,R')"
    ),
    (
        '"0d-11A":"NDQ3419", "12A-17A":"NDQ3420", "18A-29A":"NDQ3421", "30A-59A":"NDQ3422", "60A+":"NDQ3423"',
        "dbo.RehabSensorial_ConCert('R471,R478', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3424", "12A-17A":"NDQ3425", "18A-29A":"NDQ3426", "30A-59A":"NDQ3427", "60A+":"NDQ3428"',
        "dbo.RehabSensorial_Rehab_Alta('R471,R478', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3429", "12A-17A":"NDQ3430", "18A-29A":"NDQ3431", "30A-59A":"NDQ3432", "60A+":"NDQ3433"',
        "dbo.RehabSensorial_SinCert('R471,R478', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3434", "12A-17A":"NDQ3435", "18A-29A":"NDQ3436", "30A-59A":"NDQ3437", "60A+":"NDQ3438"',
        "dbo.RehabSensorial_ServEval('R471,R478', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3439", "12A-17A":"NDQ3440", "18A-29A":"NDQ3441", "30A-59A":"NDQ3442", "60A+":"NDQ3443"',
        "dbo.RehabSensorial_EnRiesgo('R471,R478', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3444", "12A-17A":"NDQ3445", "18A-29A":"NDQ3446", "30A-59A":"NDQ3447", "60A+":"NDQ3448"',
        "dbo.RehabSensorial_RefContra('R471,R478', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3449", "12A-17A":"NDQ3450", "18A-29A":"NDQ3451", "30A-59A":"NDQ3452", "60A+":"NDQ3453"',
        "dbo.RehabSensorial_Telemed('R471,R478', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3454", "12A-17A":"NDQ3455", "18A-29A":"NDQ3456", "30A-59A":"NDQ3457", "60A+":"NDQ3458"',
        "dbo.RehabSensorial_ConCert('R471,R478', 'N,C,R')"
    ),
    (
        '"0d-11A":"NDQ3459", "12A-17A":"NDQ3460", "18A-29A":"NDQ3461", "30A-59A":"NDQ3462", "60A+":"NDQ3463"',
        "dbo.RehabSensorial_Rehab_Nml_NCR('R471,R478')"
    ),
    (
        '"0d-11A":"NDQ3464", "12A-17A":"NDQ3465", "18A-29A":"NDQ3466", "30A-59A":"NDQ3467", "60A+":"NDQ3468"',
        "dbo.RehabSensorial_SinCert('R471,R478', 'N,C,R')"
    ),
    (
        '"0d-11A":"NDQ3469", "12A-17A":"NDQ3470", "18A-29A":"NDQ3471", "30A-59A":"NDQ3472", "60A+":"NDQ3473"',
        "dbo.RehabSensorial_ServEval_NCR('R471,R478')"
    ),
    (
        '"0d-11A":"NDQ3474", "12A-17A":"NDQ3475", "18A-29A":"NDQ3476", "30A-59A":"NDQ3477", "60A+":"NDQ3478"',
        "dbo.RehabSensorial_Ambulatoria_NCR('R471,R478')"
    ),
    (
        '"0d-11A":"NDQ3479", "12A-17A":"NDQ3480", "18A-29A":"NDQ3481", "30A-59A":"NDQ3482", "60A+":"NDQ3483"',
        "dbo.RehabSensorial_ReviFinal_NCR('R471,R478')"
    ),
    (
        '"0d-11A":"NDQ3484", "12A-17A":"NDQ3485", "18A-29A":"NDQ3486", "30A-59A":"NDQ3487", "60A+":"NDQ3488"',
        "dbo.RehabSensorial_Telemed('R471,R478', 'N,C,R')"
    ),
    (
        '"0d-11A":"NDQ3489", "12A-17A":"NDQ3490", "18A-29A":"NDQ3491", "30A-59A":"NDQ3492", "60A+":"NDQ3493"',
        "dbo.RehabSensorial_ConCert('P920,P921,P922,P923,P924,P925,P926,P927,P928,P929,R13X,Z930', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3494", "12A-17A":"NDQ3495", "18A-29A":"NDQ3496", "30A-59A":"NDQ3497", "60A+":"NDQ3498"',
        "dbo.RehabSensorial_Rehab_Alta('P920,P921,P922,P923,P924,P925,P926,P927,P928,P929,R13X,Z930', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3499", "12A-17A":"NDQ3500", "18A-29A":"NDQ3501", "30A-59A":"NDQ3502", "60A+":"NDQ3503"',
        "dbo.RehabSensorial_SinCert('P920,P921,P922,P923,P924,P925,P926,P927,P928,P929,R13X,Z930', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3504", "12A-17A":"NDQ3505", "18A-29A":"NDQ3506", "30A-59A":"NDQ3507", "60A+":"NDQ3508"',
        "dbo.RehabSensorial_ServEval('P920,P921,P922,P923,P924,P925,P926,P927,P928,P929,R13X,Z930', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3509", "12A-17A":"NDQ3510", "18A-29A":"NDQ3511", "30A-59A":"NDQ3512", "60A+":"NDQ3513"',
        "dbo.RehabSensorial_EnRiesgo('P920,P921,P922,P923,P924,P925,P926,P927,P928,P929,R13X,Z930', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3514", "12A-17A":"NDQ3515", "18A-29A":"NDQ3516", "30A-59A":"NDQ3517", "60A+":"NDQ3518"',
        "dbo.RehabSensorial_RefContra('P920,P921,P922,P923,P924,P925,P926,P927,P928,P929,R13X,Z930', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3519", "12A-17A":"NDQ3520", "18A-29A":"NDQ3521", "30A-59A":"NDQ3522", "60A+":"NDQ3523"',
        "dbo.RehabSensorial_Telemed('P920,P921,P922,P923,P924,P925,P926,P927,P928,P929,R13X,Z930', 'N,R')"
    ),
    (
        '"0d-11A":"NDQ3524", "12A-17A":"NDQ3525", "18A-29A":"NDQ3526", "30A-59A":"NDQ3527", "60A+":"NDQ3528"',
        "dbo.RehabSensorial_ConCert('P920,P921,P922,P923,P924,P925,P926,P927,P928,P929,R13X,Z930', 'N,C,R')"
    ),
    (
        '"0d-11A":"NDQ3529", "12A-17A":"NDQ3530", "18A-29A":"NDQ3531", "30A-59A":"NDQ3532", "60A+":"NDQ3533"',
        "dbo.RehabSensorial_Rehab_Nml_NCR('P920,P921,P922,P923,P924,P925,P926,P927,P928,P929,R13X,Z930')"
    ),
    (
        '"0d-11A":"NDQ3534", "12A-17A":"NDQ3535", "18A-29A":"NDQ3536", "30A-59A":"NDQ3537", "60A+":"NDQ3538"',
        "dbo.RehabSensorial_SinCert('P920,P921,P922,P923,P924,P925,P926,P927,P928,P929,R13X,Z930', 'N,C,R')"
    ),
    (
        '"0d-11A":"NDQ3539", "12A-17A":"NDQ3540", "18A-29A":"NDQ3541", "30A-59A":"NDQ3542", "60A+":"NDQ3543"',
        "dbo.RehabSensorial_ServEval_NCR('P920,P921,P922,P923,P924,P925,P926,P927,P928,P929,R13X,Z930')"
    ),
    (
        '"0d-11A":"NDQ3544", "12A-17A":"NDQ3545", "18A-29A":"NDQ3546", "30A-59A":"NDQ3547", "60A+":"NDQ3548"',
        "dbo.RehabSensorial_Ambulatoria_NCR('P920,P921,P922,P923,P924,P925,P926,P927,P928,P929,R13X,Z930')"
    ),
    (
        '"0d-11A":"NDQ3549", "12A-17A":"NDQ3550", "18A-29A":"NDQ3551", "30A-59A":"NDQ3552", "60A+":"NDQ3553"',
        "dbo.RehabSensorial_ReviFinal_NCR('P920,P921,P922,P923,P924,P925,P926,P927,P928,P929,R13X,Z930')"
    ),
    (
        '"0d-11A":"NDQ3554", "12A-17A":"NDQ3555", "18A-29A":"NDQ3556", "30A-59A":"NDQ3557", "60A+":"NDQ3558"',
        "dbo.RehabSensorial_Telemed('P920,P921,P922,P923,P924,P925,P926,P927,P928,P929,R13X,Z930', 'N,C,R')"
    ),
]