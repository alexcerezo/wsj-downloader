import requests
import os
from datetime import datetime

url = 'https://customercenter.wsj.com/todaysPaper/'

# Hacer una petición GET a la URL modificada
response = requests.get(url, allow_redirects=True)
url = response.url
print(f"URL redirigida: {url}")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
        
response = requests.get(url, headers=headers)

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    # Descargar el archivo con el nombre de la fecha actual y sin la hora
    filename = f"{datetime.now().strftime('%Y-%m-%d')}.pdf"
    #Crear la capreta printed-editions si no existe
    if not os.path.exists('printed-editions'):
        os.makedirs('printed-editions')
    #Guardar el archivo en la carpeta printed-editions
    with open(f'printed-editions/{filename}', 'wb') as file:
        file.write(response.content)
else:
    print(f"Error al descargar el archivo: {response.status_code}")

        