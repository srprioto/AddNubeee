# -*- coding: utf-8 -*-
"""
Autor: Yo!
Fecha: 2026
"""

import pyodbc
import logging
import sys
import colorama
from colorama import Fore, Style

# Importar configuraciones
from config import DB_CONFIG, LOG_CONFIG

# Importar los módulos con la lógica de cada modo
import solo
import multiples
import todo
from indicadores import TODO

# CONFIGURACIÓN DE LOGGING (Hacia archivo o consola de fondo)

logging.basicConfig(
    level=getattr(logging, LOG_CONFIG['level']),
    format=LOG_CONFIG['format'],
    datefmt=LOG_CONFIG['datefmt']
)
logger = logging.getLogger(__name__)


# CONTROL DE TECLADO MULTIPLATAFORMA (Windows / Linux / Mac)

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


# INTERFAZ DE CONSOLA (MENÚ PRINCIPAL)

def seleccionar_modo() -> str:
    opciones = ["Solo", "Multiple", "Todo"]
    seleccionado = 0

    while True:
        print("\033[H\033[J", end="")
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


# SUBMENÚ PARA SELECCIONAR TABLA (DINÁMICO)

def seleccionar_tabla(tipo: str) -> str:
    """
    Muestra submenú con las tablas disponibles para SOLO o MULTIPLE
    tipo: 'solo' o 'multiple'
    Retorna: nombre de la tabla seleccionada
    """
    # Obtener las tablas según el tipo
    if tipo == "solo":
        tablas = list(TODO.get("INDICADORESSOLO", {}).keys())
        tipo_mostrar = "SOLO"
    else:  # multiple
        tablas = list(TODO.get("INDICADORESMULTIPLE", {}).keys())
        tipo_mostrar = "MULTIPLE"
    
    if not tablas:
        print(f"\n\033[1;31mNo hay tablas definidas para el modo {tipo_mostrar}\033[0m")
        input("\nPresiona ENTER para volver al menú principal...")
        return None
    
    seleccionado = 0
    
    while True:
        print("\033[H\033[J", end="")
        print("=" * 60)
        print(f"  SELECCIONE TABLA - MODO {tipo_mostrar} (Flechas)   ")
        print("=" * 60)
        for i, tabla in enumerate(tablas):
            if i == seleccionado:
                print(f" > \033[1;32m[{tabla}]\033[0m <")
            else:
                print(f"   {tabla}")
        print("=" * 60)
        print("Usa las ↑/↓ y ENTER para confirmar.")

        key = get_key()
        if key == KEY_UP:
            seleccionado = (seleccionado - 1) % len(tablas)
        elif key == KEY_DOWN:
            seleccionado = (seleccionado + 1) % len(tablas)
        elif key == KEY_ENTER or key == b' ':
            break
    
    return tablas[seleccionado]


# CONEXIÓN A BASE DE DATOS

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


# FLUJO PRINCIPAL

def main():
    modo = seleccionar_modo()
    
    # Si el modo es Solo o Multiple, mostrar submenú de tablas
    if modo in ["solo", "multiple"]:
        nombre_tabla = seleccionar_tabla(modo)
        if nombre_tabla is None:
            return  # Volver al menú principal (en realidad termina el programa)
        
        try:
            conn = get_connection()
        except Exception:
            return
        
        try:
            if modo == "solo":
                # Procesar SOLO para una tabla específica
                exitosos, fallidos, total = solo.procesar_solo_tabla(conn, nombre_tabla)
                
                # Reporte para modo solo
                print("\n" + "=" * 60)
                print(f"RESUMEN FINAL DE EJECUCIÓN - MODO SOLO")
                print(f"Tabla: {nombre_tabla}")
                print("=" * 60)
                print(f"   Registros Procesados: {exitosos + fallidos}/{total}")
                print(f"   ** OK ** Exitosos (SUCCESS): \033[1;32m{exitosos}\033[0m")
                print(f"   **ERROR* Fallidos  (ERROR):   \033[1;31m{fallidos}\033[0m")
                print("=" * 60 + "\n")
                
            else:  # multiple
                # Procesar MULTIPLE para una tabla específica
                exitosos, fallidos, total = multiples.procesar_multiple_tabla(conn, nombre_tabla)
                
                # Reporte para modo multiple
                print("\n" + "=" * 60)
                print(f"RESUMEN FINAL DE EJECUCIÓN - MODO MULTIPLE")
                print(f"Tabla: {nombre_tabla}")
                print("=" * 60)
                print(f"   Registros Procesados: {exitosos + fallidos}/{total}")
                print(f"   ** OK ** Exitosos (SUCCESS): \033[1;32m{exitosos}\033[0m")
                print(f"   **ERROR* Fallidos  (ERROR):   \033[1;31m{fallidos}\033[0m")
                print("=" * 60 + "\n")
                
        finally:
            if conn:
                conn.close()
    
    else:  # modo "todo"
        try:
            conn = get_connection()
        except Exception:
            return
        
        try:
            (total_tablas, total_exitosos_solo, total_fallidos_solo, 
             total_exitosos_multiple, total_fallidos_multiple, total_procesados) = todo.procesar_todo(conn)
            
            # Reporte para modo todo
            print("\n" + "=" * 60)
            print("RESUMEN FINAL DE EJECUCIÓN - MODO TODO (MASIVO)")
            print("=" * 60)
            print(f"   Tablas Procesadas: {total_tablas}")
            print(f"   Total Registros Procesados: {total_procesados}")
            print("-" * 60)
            print(f"   INDICADORES SOLO:")
            print(f"     ** OK ** Exitosos: \033[1;32m{total_exitosos_solo}\033[0m")
            print(f"     **ERROR* Fallidos:   \033[1;31m{total_fallidos_solo}\033[0m")
            print(f"   INDICADORES MULTIPLE:")
            print(f"     ** OK ** Exitosos: \033[1;32m{total_exitosos_multiple}\033[0m")
            print(f"     **ERROR* Fallidos:   \033[1;31m{total_fallidos_multiple}\033[0m")
            print("=" * 60 + "\n")
            
        finally:
            if conn:
                conn.close()

if __name__ == "__main__":
    main()