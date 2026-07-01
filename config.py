# -*- coding: utf-8 -*-
"""
Autor: Yo!
Fecha: 2026
"""

import os  # <-- ESTA LÍNEA FALTA
from dotenv import load_dotenv

# Carga las variables desde el archivo .env
load_dotenv()

# ====================================================================================
# CONFIGURACIÓN DE CONEXIÓN A SQL SERVER
# ====================================================================================
DB_CONFIG = {
    'server': os.environ.get('DB_SERVER'),
    # 'port': int(os.environ.get('DB_PORT', 1433)),  # El puerto se convierte a número entero
    'database': os.environ.get('DB_DATABASE'),
    'username': os.environ.get('DB_USERNAME'),
    'password': os.environ.get('DB_PASSWORD'),
    'driver': os.environ.get('DB_DRIVER')
}

# ====================================================================================
# CONFIGURACIÓN DE LOGGING
# ====================================================================================
LOG_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(levelname)s - %(message)s',
    'datefmt': '%Y-%m-%d %H:%M:%S'
}

# ====================================================================================
# CONFIGURACIÓN DE EJECUCIÓN
# ====================================================================================
EXEC_CONFIG = {
    'pause_seconds': 0.5,     # Pausa entre ejecuciones para no saturar el servidor
    'validate_functions': False
}