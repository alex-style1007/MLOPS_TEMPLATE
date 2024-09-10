# Configuración_Entorno.py
import os

def configurar_entorno():
    print("Configurando el entorno...")
    
    # Establecer variables de entorno
    os.environ["MODEL_PATH"] = "/ruta/del/modelo/Modelo_Final.pkl"
    os.environ["ENVIRONMENT"] = "production"
    
    # Configurar otros aspectos necesarios
    # Por ejemplo, configurar acceso a bases de datos, servicios externos, etc.

    print("Entorno configurado.")

if __name__ == "__main__":
    configurar_entorno()
