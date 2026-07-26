# -*- coding: utf-8 -*-
"""
Autor: Yo!
Fecha: 2026
"""

import time
from typing import Tuple

from config import EXEC_CONFIG
from indicadores import TODO


# EJECUCIÓN DEL SP PARA CREAR TABLA

def ejecutar_crear_tabla(conn, nombre_tabla: str) -> Tuple[bool, str]:
    """Ejecuta SP para crear/limpiar la tabla"""
    try:
        cursor = conn.cursor()
        sql = "EXEC sp_Crear_Disc_Snapshot @NombreTabla = ?"
        cursor.execute(sql, (nombre_tabla,))
        cursor.commit()
        return True, "SUCCESS"
    except Exception as e:
        return False, str(e)


# EJECUCIÓN DEL SP (MODO SOLO)

def ejecutar_sp_solo(conn, nombre_columna: str, funcion_sql: str, nombre_tabla: str) -> Tuple[bool, str]:
    try:
        cursor = conn.cursor()
        sql = "EXEC dbo.SP_CargarFuncionAMatriz @NombreColumna = ?, @FuncionSQL = ?, @NombreTabla = ?"
        cursor.execute(sql, (nombre_columna, funcion_sql, nombre_tabla))
        cursor.commit()
        return True, "SUCCESS"
    except Exception as e:
        return False, str(e)


# PROCESAMIENTO DE UNA TABLA ESPECÍFICA (MODO SOLO)

def procesar_solo_tabla(conn, nombre_tabla: str) -> Tuple[int, int, int]:
    """
    Procesa los indicadores SOLO para una tabla específica
    """
    # Obtener los indicadores de la tabla específica
    lista_indicadores = TODO.get("INDICADORESSOLO", {}).get(nombre_tabla, [])
    nombre_sp = "dbo.SP_CargarFuncionAMatriz"

    print("\033[H\033[J", end="")
    print("=" * 80)
    print(f" INICIANDO PROCESO EN MODO: SOLO")
    print(f" Tabla: {nombre_tabla}")
    print(f" SP Destino: {nombre_sp}")
    print(f" Total de indicadores a procesar: {len(lista_indicadores)}")
    print("=" * 80 + "\n")

    if not lista_indicadores:
        print(f"\033[1;33m La tabla {nombre_tabla} no tiene indicadores SOLO definidos.\033[0m")
        return 0, 0, 0

    total = len(lista_indicadores)
    exitosos = 0
    fallidos = 0

    try:
        # 1. Crear/limpiar tabla
        print(f"  Creando/limpiando tabla {nombre_tabla}...", end=" ", flush=True)
        exito, mensaje = ejecutar_crear_tabla(conn, nombre_tabla)
        if exito:
            print("\033[1;32mOK\033[0m\n")
        else:
            print(f"\033[1;31mERROR: {mensaje}\033[0m\n")
            return 0, 0, 0

        # 2. Procesar indicadores
        for idx, (nombre_columna, funcion_sql) in enumerate(lista_indicadores, 1):
            info_visual = nombre_columna

            print(f"[{idx}/{total}] Ejecutando para: {info_visual} -> \033[1;33mCargando...\033[0m", end="", flush=True)

            exito, mensaje = ejecutar_sp_solo(conn, nombre_columna, funcion_sql, nombre_tabla)

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


# FUNCIÓN ANTIGUA (MANTENIDA POR COMPATIBILIDAD PERO OBSOLETA)
def procesar_solo(conn) -> Tuple[int, int, int]:
    """
    PROCESAMIENTO DE TODA LA LISTA (MODO SOLO) - OBSOLETO
    Se mantiene por compatibilidad pero ya no se usa
    """
    print("\033[1;33mADVERTENCIA: Esta función está obsoleta. Use procesar_solo_tabla() en su lugar.\033[0m")
    return 0, 0, 0