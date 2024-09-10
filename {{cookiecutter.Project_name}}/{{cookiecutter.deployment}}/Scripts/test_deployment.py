# Tests_Despliegue.py
import requests

def probar_modelo():
    url = "http://localhost:5000/predict"  # URL del endpoint del modelo desplegado
    test_data = {"input": "example data"}  # Datos de prueba
    
    try:
        response = requests.post(url, json=test_data)
        response.raise_for_status()  # Lanza una excepción si la solicitud falla
        result = response.json()
        print("Prueba de modelo exitosa.")
        print("Resultado:", result)
    except requests.exceptions.RequestException as e:
        print("Error en la prueba de modelo:", e)

if __name__ == "__main__":
    probar_modelo()
