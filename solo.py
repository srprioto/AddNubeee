# -*- coding: utf-8 -*-
"""
Autor: Yo!
Fecha: 2026
"""

import time
from typing import Tuple

from config import EXEC_CONFIG
from indicadores import INDICADORESSOLO, NOMBRE_TABLA


# EJECUCIÓN DEL SP (MODO SOLO)

def ejecutar_sp_solo(conn, nombre_columna: str, funcion_sql: str) -> Tuple[bool, str]:
    try:
        cursor = conn.cursor()
        sql = "EXEC dbo.SP_CargarFuncionAMatriz @NombreColumna = ?, @FuncionSQL = ?, @NombreTabla = ?"
        cursor.execute(sql, (nombre_columna, funcion_sql, NOMBRE_TABLA))
        cursor.commit()
        return True, "SUCCESS"
    except Exception as e:
        return False, str(e)


# PROCESAMIENTO DE TODA LA LISTA (MODO SOLO)

def procesar_solo(conn) -> Tuple[int, int, int]:
    lista_indicadores = INDICADORESSOLO
    nombre_sp = "dbo.SP_CargarFuncionAMatriz"

    print("\033[H\033[J", end="")
    print("=" * 80)
    print(f" INICIANDO PROCESO EN MODO: SOLO")
    print(f" SP Destino: {nombre_sp}")
    print(f" Total de registros a procesar: {len(lista_indicadores)}")
    print("=" * 80 + "\n")

    if not lista_indicadores:
        print("\033[1;33m La lista de indicadores seleccionada está vacía.\033[0m")
        return 0, 0, 0

    total = len(lista_indicadores)
    exitosos = 0
    fallidos = 0

    try:
        for idx, (nombre_columna, funcion_sql) in enumerate(lista_indicadores, 1):
            info_visual = nombre_columna

            print(f"[{idx}/{total}] Ejecutando para: {info_visual} -> \033[1;33mCargando...\033[0m", end="", flush=True)

            exito, mensaje = ejecutar_sp_solo(conn, nombre_columna, funcion_sql)

            if exito:
                exitosos += 1
                print(f"\r[{idx}/{total}] Ejecutando para: {info_visual} -> \033[1;32mSUCCESS\033[0m")
            else:
                fallidos += 1
                print(f"\r[{idx}/{total}] Ejecutando para: {info_visual} -> \033[1;31mERROR\033[0m ({mensaje})")

            if EXEC_CONFIG['pause_seconds'] > 0:
                time.sleep(EXEC_CONFIG['pause_seconds'])

    except KeyboardInterrupt:
        print("\n\n\033[1;33m!! Proceso interrumpido voluntariamente por el usuario.\033[0m")

    return exitosos, fallidos, total
