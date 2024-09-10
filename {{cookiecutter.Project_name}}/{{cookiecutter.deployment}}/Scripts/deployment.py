# Despliegue.py
import os
import subprocess

def desplegar_modelo():
    # Comandos para desplegar el modelo en producción
    print("Iniciando el despliegue del modelo...")
    
    # Ejemplo: mover el archivo del modelo a un directorio específico
    subprocess.run(["mv", "ruta/del/modelo/Modelo_Final.pkl", "/ruta/de/destino/"], check=True)
    
    # Ejemplo: iniciar un servicio que utiliza el modelo
    # subprocess.run(["systemctl", "start", "nombre_del_servicio"], check=True)

    print("Despliegue completado con éxito.")

if __name__ == "__main__":
    desplegar_modelo()
