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


# INTERFAZ DE CONSOLA (MENÚ INTERACTIVO)

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

    try:
        conn = get_connection()
    except Exception:
        return

    try:
        if modo == "solo":
            exitosos, fallidos, total = solo.procesar_solo(conn)
        else:
            exitosos, fallidos, total = multiples.procesar_multiple(conn)
    finally:
        if conn:
            conn.close()

    # REPORTE FINAL EN CONSOLA

    print("\n" + "=" * 60)
    print(f"RESUMEN FINAL DE EJECUCIÓN - MODO {modo.upper()}")
    print("=" * 60)
    print(f"   Registros Procesados: {exitosos + fallidos}/{total}")
    print(f"   ** OK ** Exitosos (SUCCESS): \033[1;32m{exitosos}\033[0m")
    print(f"   **ERROR* Fallidos  (ERROR):   \033[1;31m{fallidos}\033[0m")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()
