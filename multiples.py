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


# EJECUCIÓN DEL SP (MODO MULTIPLE)

def ejecutar_sp_multiple(conn, mapeo_columnas: str, funcion_sql: str, nombre_tabla: str) -> Tuple[bool, str]:
    try:
        cursor = conn.cursor()
        sql = "EXEC dbo.SP_CargarFuncionAMatriz_Multi @MapeoColumnas = ?, @FuncionSQL = ?, @NombreTabla = ?"
        cursor.execute(sql, (mapeo_columnas, funcion_sql, nombre_tabla))
        cursor.commit()
        return True, "SUCCESS"
    except Exception as e:
        return False, str(e)


# PROCESAMIENTO DE UNA TABLA ESPECÍFICA (MODO MULTIPLE)

def procesar_multiple_tabla(conn, nombre_tabla: str) -> Tuple[int, int, int]:
    """
    Procesa los indicadores MULTIPLE para una tabla específica
    """
    # Obtener los indicadores de la tabla específica
    lista_indicadores = TODO.get("INDICADORESMULTIPLE", {}).get(nombre_tabla, [])
    nombre_sp = "dbo.SP_CargarFuncionAMatriz_Multi"

    print("\033[H\033[J", end="")
    print("=" * 80)
    print(f" INICIANDO PROCESO EN MODO: MULTIPLE")
    print(f" Tabla: {nombre_tabla}")
    print(f" SP Destino: {nombre_sp}")
    print(f" Total de indicadores a procesar: {len(lista_indicadores)}")
    print("=" * 80 + "\n")

    if not lista_indicadores:
        print(f"\033[1;33m La tabla {nombre_tabla} no tiene indicadores MULTIPLE definidos.\033[0m")
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
        for idx, (param_1, funcion_sql) in enumerate(lista_indicadores, 1):
            info_visual = param_1[:40] + "..."

            print(f"[{idx}/{total}] Ejecutando para: {info_visual} -> \033[1;33mCargando...\033[0m", end="", flush=True)

            # Normalizar formato JSON envolviendo con llaves {} si el catálogo no las trae escritas
            json_mapeo = f"{{{param_1}}}" if not (param_1.startswith('{') and param_1.endswith('}')) else param_1
            exito, mensaje = ejecutar_sp_multiple(conn, json_mapeo, funcion_sql, nombre_tabla)

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
def procesar_multiple(conn) -> Tuple[int, int, int]:
    """
    PROCESAMIENTO DE TODA LA LISTA (MODO MULTIPLE) - OBSOLETO
    Se mantiene por compatibilidad pero ya no se usa
    """
    print("\033[1;33mADVERTENCIA: Esta función está obsoleta. Use procesar_multiple_tabla() en su lugar.\033[0m")
    return 0, 0, 0