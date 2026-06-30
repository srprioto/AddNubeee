# -*- coding: utf-8 -*-
"""
Configuración de conexión a la base de datos
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
    'driver': '{ODBC Driver 17 for SQL Server}'  # Usar 'SQL Server' si no tienes el driver 17
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
    'pause_seconds': 0.5,  # Pausa entre ejecuciones
    'show_progress': True,  # Mostrar progreso en consola
    'validate_functions': False  # Validar funciones antes de ejecutar
}