# -*- coding: utf-8 -*-
"""
Autor: Yo!
Fecha: 2026
"""

import pyodbc
import time
import logging
import sys
from typing import Tuple, List
import colorama
from colorama import Fore, Style

# Importar configuraciones y catálogos
from config import DB_CONFIG, LOG_CONFIG, EXEC_CONFIG
from indicadores import INDICADORESSOLO, INDICADORESMULTIPLE, NOMBRE_TABLA

# ====================================================================================
# CONFIGURACIÓN DE LOGGING (Hacia archivo o consola de fondo)
# ====================================================================================
logging.basicConfig(
    level=getattr(logging, LOG_CONFIG['level']),
    format=LOG_CONFIG['format'],
    datefmt=LOG_CONFIG['datefmt']
)
logger = logging.getLogger(__name__)

# ====================================================================================
# CONTROL DE TECLADO MULTIPLATAFORMA (Windows / Linux / Mac)
# ====================================================================================
try:
    import msvcrt
    def get_key():
        ch = msvcrt.getch()
        if ch in (b'\x00', b'\xe0'):
            return msvcrt.getch()
        return ch
    KEY_UP = b'H'
    KEY_DOWN = b'P'
    KEY_ENTER = b'\r'
except ImportError:
    import tty
    import termios
    def get_key():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
            if ch == '\x1b':
                return sys.stdin.read(2)
            return ch.encode()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    KEY_UP = '[A'
    KEY_DOWN = '[B'
    KEY_ENTER = b'\n'

# ====================================================================================
# INTERFAZ DE CONSOLA (MENÚ INTERACTIVO)
# ====================================================================================
def seleccionar_modo() -> str:
    opciones = ["Solo", "Multiple"]
    seleccionado = 0
    
    while True:
        print("\033[H\033[J", end="")  # Limpia la pantalla
        print("==============================================")
        print("  SELECCIONE EL MODO DE EJECUCIÓN (Flechas)   ")
        print("==============================================")
        for i, opcion in enumerate(opciones):
            if i == seleccionado:
                print(f" > \033[1;32m[{opcion.upper()}]\033[0m <")
            else:
                print(f"   {opcion}")
        print("==============================================")
        print("Usa las ↑/↓ y ENTER para confirmar.")

        key = get_key()
        if key == KEY_UP:
            seleccionado = (seleccionado - 1) % len(opciones)
        elif key == KEY_DOWN:
            seleccionado = (seleccionado + 1) % len(opciones)
        elif key == KEY_ENTER or key == b' ':
            break
            
    return opciones[seleccionado].lower()

# ====================================================================================
# CONEXIÓN A BASE DE DATOS
# ====================================================================================
def get_connection():
    try:
        conn_str = (
            f"DRIVER={DB_CONFIG['driver']};"
            f"SERVER={DB_CONFIG['server']};"
            f"DATABASE={DB_CONFIG['database']};"
            f"UID={DB_CONFIG['username']};"
            f"PWD={DB_CONFIG['password']};"
            f"TrustServerCertificate=yes;"
        )
        return pyodbc.connect(conn_str)
    except Exception as e:
        print(f"\n\033[1;31m- ERROR DE CONEXIÓN -\033[0m No se pudo conectar a SQL Server: {str(e)}")
        raise

# ====================================================================================
# PROCEDIMIENTOS DE EJECUCIÓN SQL
# ====================================================================================
def ejecutar_sp_solo(conn, nombre_columna: str, funcion_sql: str) -> Tuple[bool, str]:
    try:
        cursor = conn.cursor()
        sql = "EXEC dbo.SP_CargarFuncionAMatriz @NombreColumna = ?, @FuncionSQL = ?"
        cursor.execute(sql, (nombre_columna, funcion_sql))
        cursor.commit()
        return True, "SUCCESS"
    except Exception as e:
        return False, str(e)

def ejecutar_sp_multiple(conn, mapeo_columnas: str, funcion_sql: str) -> Tuple[bool, str]:
    try:
        cursor = conn.cursor()
        # pyodbc traduce strings de Python a NVARCHAR de forma automática y segura
        sql = "EXEC dbo.SP_CargarFuncionAMatriz_Multi @MapeoColumnas = ?, @FuncionSQL = ?, @NombreTabla = ?"
        cursor.execute(sql, (mapeo_columnas, funcion_sql, NOMBRE_TABLA))
        cursor.commit()
        return True, "SUCCESS"
    except Exception as e:
        return False, str(e)

# ====================================================================================
# FLUJO PRINCIPAL
# ====================================================================================
def main():
    modo = seleccionar_modo()
    
    # Asignar la lista correspondiente según el modo elegido
    if modo == "solo":
        lista_indicadores = INDICADORESSOLO
        nombre_sp = "dbo.SP_CargarFuncionAMatriz"
    else:
        lista_indicadores = INDICADORESMULTIPLE
        nombre_sp = "dbo.SP_CargarFuncionAMatriz_Multi"

    print("\033[H\033[J", end="")
    print("=" * 80)
    print(f" INICIANDO PROCESO EN MODO: {modo.upper()}")
    print(f" SP Destino: {nombre_sp}")
    print(f" Total de registros a procesar: {len(lista_indicadores)}")
    print("=" * 80 + "\n")

    if not lista_indicadores:
        print("\033[1;33m La lista de indicadores seleccionada está vacía.\033[0m")
        return

    try:
        conn = get_connection()
    except Exception:
        return

    total = len(lista_indicadores)
    exitosos = 0
    fallidos = 0

    try:
        for idx, (param_1, funcion_sql) in enumerate(lista_indicadores, 1):
            # Identificador visual corto para la consola
            info_visual = param_1 if modo == "solo" else (param_1[:40] + "...")
            
            # 1. Mostrar que el registro está cargando (sin salto de línea)
            print(f"[{idx}/{total}] Ejecutando para: {info_visual} -> \033[1;33mCargando...\033[0m", end="", flush=True)
            
            # Ejecución del procedimiento según el modo
            if modo == "solo":
                exito, mensaje = ejecutar_sp_solo(conn, param_1, funcion_sql)
            else:
                # Normalizar formato JSON envolviendo con llaves {} si el catálogo no las trae escritas
                json_mapeo = f"{{{param_1}}}" if not (param_1.startswith('{') and param_1.endswith('}')) else param_1
                exito, mensaje = ejecutar_sp_multiple(conn, json_mapeo, funcion_sql)
            
            # 2. Borrar el "Cargando..." de la línea actual y poner el resultado definitivo
            # Usamos '\r' para regresar al inicio de la línea e imprimir el estado real
            if exito:
                exitosos += 1
                print(f"\r[{idx}/{total}] Ejecutando para: {info_visual} -> \033[1;32mSUCCESS\033[0m")
            else:
                fallidos += 1
                print(f"\r[{idx}/{total}] Ejecutando para: {info_visual} -> \033[1;31mERROR\033[0m ({mensaje})")

            # Pausa opcional configurada
            if EXEC_CONFIG['pause_seconds'] > 0:
                time.sleep(EXEC_CONFIG['pause_seconds'])

    except KeyboardInterrupt:
        print("\n\n\033[1;33m!! Proceso interrumpido voluntariamente por el usuario.\033[0m")
    finally:
        if conn:
            conn.close()

    # ====================================================================================
    # REPORTE FINAL EN CONSOLA
    # ====================================================================================
    print("\n" + "=" * 60)
    print(f"RESUMEN FINAL DE EJECUCIÓN - MODO {modo.upper()}")
    print("=" * 60)
    print(f"   Registros Procesados: {exitosos + fallidos}/{total}")
    print(f"   ** OK ** Exitosos (SUCCESS): \033[1;32m{exitosos}\033[0m")
    print(f"   **ERROR* Fallidos  (ERROR):   \033[1;31m{fallidos}\033[0m")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()