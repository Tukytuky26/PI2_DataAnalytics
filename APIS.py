import requests
#%%
url = "http://api.datosabiertos.enacom.gob.ar/api/v2/datastreams/TOTAL-NACIO-DE-ACCES-48866/data.csv/?auth_key=8PrQnuTl31gs3TOJAmAHLks2Se4hZz3QtkSoz9z4&limit=50&"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
with open("internet_tn_baf.csv", "w") as archivo:
    # Escribe la respuesta en el archivo
    archivo.write(response.text)

# %%
import requests

url = "http://api.datosabiertos.enacom.gob.ar/api/v2/datastreams/BANDA-ANCHA-Y-BANDA-ANGOS/data.csv/?auth_key=xogyMKih4T576U2y6op49KYRIFFgck8I8niCGluO&limit=850&"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
with open("internet_tn_baf_provincia.csv", "w") as archivo:
    # Escribe la respuesta en el archivo
    archivo.write(response.text)

#%%
import requests

url = "http://api.datosabiertos.enacom.gob.ar/api/v2/datastreams/ACCES-A-INTER-FIJO-23248/data.csv/?auth_key=xogyMKih4T576U2y6op49KYRIFFgck8I8niCGluO&limit=850"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
with open("accesos_velocidad_provincia.csv", "w") as archivo:
    # Escribe la respuesta en el archivo
    archivo.write(response.text)
# %%
import requests

url = "http://api.datosabiertos.enacom.gob.ar/api/v2/datastreams/ACCES-A-INTER-FIJO-16249/data.csv/?auth_key=xogyMKih4T576U2y6op49KYRIFFgck8I8niCGluO&limit=850"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
with open("accesos_velocidad_localidad.csv", "w") as archivo:
    # Escribe la respuesta en el archivo
    archivo.write(response.text)
# %%
import requests

url = "http://api.datosabiertos.enacom.gob.ar/api/v2/datastreams/LISTA-DE-LOCAL-CON-CONEC/data.csv/?auth_key=xogyMKih4T576U2y6op49KYRIFFgck8I8niCGluO&limit=4500"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
with open("localidad_conec_internet.csv", "w") as archivo:
    # Escribe la respuesta en el archivo
    archivo.write(response.text)
# %%
import requests

# URL de la API con el parámetro "output" establecido en "csv"
url = "http://api.datosabiertos.enacom.gob.ar/api/v2/visualizations/PENET-DE-INTER-FIJO-57760/?auth_key=YOUR_API_KEY&output=csv"

# Realizar la solicitud GET a la API
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Obtener el contenido de la respuesta en formato CSV
    data_csv = response.text

    # Guardar los datos en un archivo CSV local
    with open('penetracion_provincia.csv', 'w') as f:
        f.write(data_csv)

    print("Los datos se han guardado exitosamente en datos.csv")
else:
    print("Error al obtener los datos de la API")

# %%
