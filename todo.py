# -*- coding: utf-8 -*-
"""
Autor: Yo!
Fecha: 2026
"""

import time
from typing import Tuple, Dict, List

from config import EXEC_CONFIG
from indicadores import TODO
import solo
import multiples


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


# PROCESAMIENTO DE DATOS SOLO PARA UNA TABLA ESPECÍFICA

def procesar_solo_para_tabla(conn, nombre_tabla: str, lista_indicadores: List[tuple], 
                             idx_tabla: int, total_tablas_solo: int) -> Tuple[int, int, int]:
    """Procesa indicadores SOLO para una tabla específica"""
    total = len(lista_indicadores)
    exitosos = 0
    fallidos = 0
    
    if not lista_indicadores:
        print(f"\033[1;33m  No hay indicadores SOLO para {nombre_tabla}\033[0m")
        return 0, 0, 0
    
    print(f"\n  Procesando {total} indicadores SOLO para {nombre_tabla}...")
    
    # Usamos la función de solo.py pero modificando la tabla destino
    for idx, (nombre_columna, funcion_sql) in enumerate(lista_indicadores, 1):
        info_visual = nombre_columna
        
        print(f"    [{idx}/{total}] {info_visual} -> \033[1;33mCargando...\033[0m", end="", flush=True)
        
        # Llamamos a la función de solo pero con la tabla correcta
        try:
            cursor = conn.cursor()
            sql = "EXEC dbo.SP_CargarFuncionAMatriz @NombreColumna = ?, @FuncionSQL = ?, @NombreTabla = ?"
            cursor.execute(sql, (nombre_columna, funcion_sql, nombre_tabla))
            cursor.commit()
            exito = True
            mensaje = "SUCCESS"
        except Exception as e:
            exito = False
            mensaje = str(e)
        
        if exito:
            exitosos += 1
            print(f"\r    [SOLO/{idx_tabla}/{total_tablas_solo}] [{idx}/{total}] {info_visual} -> \033[1;32mSUCCESS\033[0m")
        else:
            fallidos += 1
            print(f"\r    [SOLO/{idx_tabla}/{total_tablas_solo}] [{idx}/{total}] {info_visual} -> \033[1;31mERROR\033[0m ({mensaje})")
        
        if EXEC_CONFIG['pause_seconds'] > 0:
            time.sleep(EXEC_CONFIG['pause_seconds'])
    
    return exitosos, fallidos, total


# PROCESAMIENTO DE DATOS MULTIPLE PARA UNA TABLA ESPECÍFICA

def procesar_multiple_para_tabla(conn, nombre_tabla: str, lista_indicadores: List[tuple],
                                 idx_tabla: int, total_tablas_multiple: int) -> Tuple[int, int, int]:
    """Procesa indicadores MULTIPLE para una tabla específica"""
    total = len(lista_indicadores)
    exitosos = 0
    fallidos = 0
    
    if not lista_indicadores:
        print(f"\033[1;33m  No hay indicadores MULTIPLE para {nombre_tabla}\033[0m")
        return 0, 0, 0
    
    print(f"\n  Procesando {total} indicadores MULTIPLE para {nombre_tabla}...")
    
    # Usamos la lógica de multiples.py pero con la tabla correcta
    for idx, (param_1, funcion_sql) in enumerate(lista_indicadores, 1):
        info_visual = param_1[:40] + "..."
        
        print(f"    [{idx}/{total}] {info_visual} -> \033[1;33mCargando...\033[0m", end="", flush=True)
        
        try:
            # Normalizar formato JSON
            json_mapeo = f"{{{param_1}}}" if not (param_1.startswith('{') and param_1.endswith('}')) else param_1
            
            cursor = conn.cursor()
            sql = "EXEC dbo.SP_CargarFuncionAMatriz_Multi @MapeoColumnas = ?, @FuncionSQL = ?, @NombreTabla = ?"
            cursor.execute(sql, (json_mapeo, funcion_sql, nombre_tabla))
            cursor.commit()
            exito = True
            mensaje = "SUCCESS"
        except Exception as e:
            exito = False
            mensaje = str(e)
        
        if exito:
            exitosos += 1
            print(f"\r    [MULTI/{idx_tabla}/{total_tablas_multiple}] [{idx}/{total}] {info_visual} -> \033[1;32mSUCCESS\033[0m")
        else:
            fallidos += 1
            print(f"\r    [MULTI/{idx_tabla}/{total_tablas_multiple}] [{idx}/{total}] {info_visual} -> \033[1;31mERROR\033[0m ({mensaje})")
        
        if EXEC_CONFIG['pause_seconds'] > 0:
            time.sleep(EXEC_CONFIG['pause_seconds'])
    
    return exitosos, fallidos, total


# PROCESAMIENTO COMPLETO MODO TODO

def procesar_todo(conn) -> Tuple[int, int, int, int, int, int]:
    """
    Procesa TODOS los indicadores en modo masivo
    Retorna: (total_tablas, total_exitosos_solo, total_fallidos_solo, 
              total_exitosos_multiple, total_fallidos_multiple, total_procesados)
    """
    
    print("\033[H\033[J", end="")
    print("=" * 80)
    print(" INICIANDO PROCESO EN MODO: TODO (MASIVO)")
    print("=" * 80)
    
    # Contar tablas por separado
    total_tablas_solo = len(TODO.get("INDICADORESSOLO", {}))
    total_tablas_multiple = len(TODO.get("INDICADORESMULTIPLE", {}))
    total_tablas_general = total_tablas_solo + total_tablas_multiple
    
    idx_tabla_actual = 0
    
    total_exitosos_solo = 0
    total_fallidos_solo = 0
    total_exitosos_multiple = 0
    total_fallidos_multiple = 0
    total_procesados = 0
    
    try:
        # 1. PROCESAR INDICADORES SOLO
        print("\n" + "=" * 80)
        print(f" FASE 1: PROCESANDO INDICADORES SOLO ({total_tablas_solo} tablas)")
        print("=" * 80)
        
        if "INDICADORESSOLO" in TODO:
            idx_solo = 0
            for nombre_tabla, lista_indicadores in TODO["INDICADORESSOLO"].items():
                idx_solo += 1
                idx_tabla_actual += 1
                
                print(f"\n\033[1;36m>>> TABLA [{idx_tabla_actual}/{total_tablas_general}]: {nombre_tabla} [SOLO/{idx_solo}/{total_tablas_solo}]\033[0m")
                print("-" * 60)
                
                # Crear/limpiar tabla
                print(f"  Creando/limpiando tabla {nombre_tabla}...", end=" ", flush=True)
                exito, mensaje = ejecutar_crear_tabla(conn, nombre_tabla)
                if exito:
                    print("\033[1;32mOK\033[0m")
                else:
                    print(f"\033[1;31mERROR: {mensaje}\033[0m")
                    continue
                
                # Procesar indicadores SOLO
                exitosos, fallidos, total = procesar_solo_para_tabla(
                    conn, nombre_tabla, lista_indicadores, idx_solo, total_tablas_solo
                )
                total_exitosos_solo += exitosos
                total_fallidos_solo += fallidos
                total_procesados += total
        
        # 2. PROCESAR INDICADORES MULTIPLE
        print("\n" + "=" * 80)
        print(f" FASE 2: PROCESANDO INDICADORES MULTIPLE ({total_tablas_multiple} tablas)")
        print("=" * 80)
        
        if "INDICADORESMULTIPLE" in TODO:
            idx_multiple = 0
            for nombre_tabla, lista_indicadores in TODO["INDICADORESMULTIPLE"].items():
                idx_multiple += 1
                idx_tabla_actual += 1
                
                print(f"\n\033[1;36m>>> TABLA [{idx_tabla_actual}/{total_tablas_general}]: {nombre_tabla} [MULTI/{idx_multiple}/{total_tablas_multiple}]\033[0m")
                print("-" * 60)
                
                # Crear/limpiar tabla
                print(f"  Creando/limpiando tabla {nombre_tabla}...", end=" ", flush=True)
                exito, mensaje = ejecutar_crear_tabla(conn, nombre_tabla)
                if exito:
                    print("\033[1;32mOK\033[0m")
                else:
                    print(f"\033[1;31mERROR: {mensaje}\033[0m")
                    continue
                
                # Procesar indicadores MULTIPLE
                exitosos, fallidos, total = procesar_multiple_para_tabla(
                    conn, nombre_tabla, lista_indicadores, idx_multiple, total_tablas_multiple
                )
                total_exitosos_multiple += exitosos
                total_fallidos_multiple += fallidos
                total_procesados += total
                
    except KeyboardInterrupt:
        print("\n\n\033[1;33m!! Proceso interrumpido voluntariamente por el usuario.\033[0m")
    
    return (total_tablas_general, total_exitosos_solo, total_fallidos_solo, 
            total_exitosos_multiple, total_fallidos_multiple, total_procesados)