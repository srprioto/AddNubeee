# -*- coding: utf-8 -*-
"""
Script principal para ejecutar SP_CargarFuncionAMatriz con múltiples indicadores
Autor: Sistema Automatizado
Fecha: 2026
"""

import pyodbc
import time
import logging
from typing import Dict, Tuple

# Importar configuración y datos
from config import DB_CONFIG, LOG_CONFIG, EXEC_CONFIG
from indicadores import INDICADORES

# ====================================================================================
# CONFIGURACIÓN DE LOGGING
# ====================================================================================
logging.basicConfig(
    level=getattr(logging, LOG_CONFIG['level']),
    format=LOG_CONFIG['format'],
    datefmt=LOG_CONFIG['datefmt']
)
logger = logging.getLogger(__name__)

# ====================================================================================
# FUNCIÓN PARA OBTENER CONEXIÓN
# ====================================================================================
def get_connection():
    """Establece conexión con SQL Server"""
    try:
        conn_str = (
            f"DRIVER={DB_CONFIG['driver']};"
            f"SERVER={DB_CONFIG['server']},{DB_CONFIG['port']};"
            f"DATABASE={DB_CONFIG['database']};"
            f"UID={DB_CONFIG['username']};"
            f"PWD={DB_CONFIG['password']};"
            f"TrustServerCertificate=yes;"
        )
        conn = pyodbc.connect(conn_str)
        logger.info("✅ Conexión exitosa a la base de datos")
        return conn
    except Exception as e:
        logger.error(f"❌ Error de conexión: {str(e)}")
        raise

# ====================================================================================
# FUNCIÓN PARA EJECUTAR EL SP
# ====================================================================================
def ejecutar_sp(conn, nombre_columna: str, funcion_sql: str) -> Tuple[bool, str]:
    """
    Ejecuta el SP_CargarFuncionAMatriz para un indicador específico
    
    Args:
        conn: Conexión a la base de datos
        nombre_columna: Nombre de la columna (ej: 'NDQ29')
        funcion_sql: Función SQL a ejecutar
    
    Returns:
        Tuple[bool, str]: (éxito, mensaje)
    """
    try:
        cursor = conn.cursor()
        
        # Construir el comando EXEC
        sql = f"""
        EXEC dbo.SP_CargarFuncionAMatriz 
            @NombreColumna = ?,
            @FuncionSQL = ?
        """
        
        logger.debug(f"🔄 Ejecutando: {nombre_columna} = {funcion_sql}")
        
        # Ejecutar el SP
        cursor.execute(sql, (nombre_columna, funcion_sql))
        cursor.commit()
        
        mensaje = f"✅ {nombre_columna} - SUCCESS: Función ejecutada correctamente"
        logger.info(mensaje)
        
        return True, mensaje
        
    except pyodbc.Error as e:
        # Error específico de ODBC
        error_msg = f"❌ {nombre_columna} - ERROR DB: {str(e)}"
        logger.error(error_msg)
        return False, error_msg
        
    except Exception as e:
        # Cualquier otro error
        error_msg = f"❌ {nombre_columna} - ERROR: {str(e)}"
        logger.error(error_msg)
        return False, error_msg

# ====================================================================================
# FUNCIÓN PARA VALIDAR QUE LA FUNCIÓN EXISTA (OPCIONAL)
# ====================================================================================
def validar_funcion(conn, funcion_sql: str) -> bool:
    """
    Valida que la función exista en la base de datos
    """
    if not EXEC_CONFIG['validate_functions']:
        return True
    
    try:
        # Extraer el nombre de la función (antes del paréntesis)
        nombre_funcion = funcion_sql.split('(')[0].strip()
        
        cursor = conn.cursor()
        sql = f"""
        SELECT COUNT(*) 
        FROM sys.objects 
        WHERE type IN ('FN', 'IF', 'TF', 'FS', 'FT') 
        AND name = '{nombre_funcion}'
        """
        
        cursor.execute(sql)
        count = cursor.fetchone()[0]
        
        if count > 0:
            return True
        else:
            logger.warning(f"⚠️ La función '{nombre_funcion}' no existe en la base de datos")
            return False
            
    except Exception as e:
        logger.warning(f"⚠️ No se pudo validar la función: {str(e)}")
        return True  # Continuamos aunque no se pueda validar

# ====================================================================================
# FUNCIÓN PRINCIPAL
# ====================================================================================
def main():
    """Función principal que ejecuta todos los indicadores"""
    
    logger.info("=" * 80)
    logger.info("🚀 INICIANDO PROCESO DE CARGA DE INDICADORES")
    logger.info("=" * 80)
    logger.info(f"📋 Total de indicadores a procesar: {len(INDICADORES)}")
    logger.info("=" * 80)
    
    # Estadísticas
    total = len(INDICADORES)
    exitosos = 0
    fallidos = 0
    resultados = []
    
    # Conectar a la base de datos
    conn = None
    try:
        conn = get_connection()
    except Exception as e:
        logger.error(f"❌ No se pudo establecer conexión: {str(e)}")
        return
    
    try:
        # Procesar cada indicador
        for idx, (nombre_columna, funcion_sql) in enumerate(INDICADORES, 1):
            logger.info("-" * 80)
            logger.info(f"📌 Procesando [{idx}/{total}]: {nombre_columna}")
            
            # Validar función (opcional)
            if EXEC_CONFIG['validate_functions']:
                if not validar_funcion(conn, funcion_sql):
                    logger.warning(f"⚠️ Saltando {nombre_columna} - Función no válida")
                    fallidos += 1
                    resultados.append(f"❌ {nombre_columna} - Función no existe")
                    continue
            
            # Ejecutar el SP
            exito, mensaje = ejecutar_sp(conn, nombre_columna, funcion_sql)
            
            # Registrar resultado
            if exito:
                exitosos += 1
                resultados.append(f"✅ {nombre_columna}")
            else:
                fallidos += 1
                resultados.append(f"❌ {nombre_columna} - {mensaje}")
            
            # Pequeña pausa entre ejecuciones para no saturar
            if EXEC_CONFIG['pause_seconds'] > 0:
                time.sleep(EXEC_CONFIG['pause_seconds'])
            
            # Mostrar progreso en consola
            if EXEC_CONFIG['show_progress']:
                print(f"📊 Progreso: {idx}/{total} - {nombre_columna} - {'✅ ÉXITO' if exito else '❌ FALLÓ'}")
        
    except KeyboardInterrupt:
        logger.warning("⚠️ Proceso interrumpido por el usuario")
        
    except Exception as e:
        logger.error(f"❌ Error inesperado en el proceso: {str(e)}")
        
    finally:
        # Cerrar conexión
        if conn:
            conn.close()
            logger.info("🔒 Conexión cerrada")
    
    # ====================================================================================
    # REPORTE FINAL
    # ====================================================================================
    logger.info("=" * 80)
    logger.info("📊 REPORTE FINAL DE EJECUCIÓN")
    logger.info("=" * 80)
    logger.info(f"✅ Éxitos:  {exitosos}/{total}")
    logger.info(f"❌ Fallidos: {fallidos}/{total}")
    logger.info("=" * 80)
    
    # Mostrar detalles de los fallidos
    if fallidos > 0:
        logger.info("📋 Detalles de fallos:")
        for resultado in resultados:
            if resultado.startswith("❌"):
                logger.info(f"   {resultado}")
    
    logger.info("🏁 PROCESO FINALIZADO")
    logger.info("=" * 80)
    
    # Mostrar resumen en consola simple
    print("\n" + "=" * 60)
    print(f"📊 RESUMEN FINAL")
    print(f"   ✅ Exitosos: {exitosos}/{total}")
    print(f"   ❌ Fallidos: {fallidos}/{total}")
    print("=" * 60)

# ====================================================================================
# PUNTO DE ENTRADA
# ====================================================================================
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(f"❌ Error fatal: {str(e)}")
        print(f"\n❌ ERROR FATAL: {str(e)}")