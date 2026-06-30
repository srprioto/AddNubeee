# -*- coding: utf-8 -*-
"""
Configuración de conexión a la base de datos y ejecución
Autor: Sistema Automatizado
Fecha: 2026
"""

# ====================================================================================
# CONFIGURACIÓN DE CONEXIÓN A SQL SERVER
# ====================================================================================
DB_CONFIG = {
    'server': 'localhost',
    'port': 1433,
    'database': 'nubeee',
    'username': 'sa',
    'password': 'Clave-Sql-2026',
    'driver': '{ODBC Driver 17 for SQL Server}'
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