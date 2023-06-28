import requests

object_id = '436535'  # Reemplaza con el ID de la obra de arte que deseas obtener

api_url = f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}'
response = requests.get(api_url)
data = response.json()

if response.ok and 'artistDisplayName' in data:
    artist_name = data['artistDisplayName']
    artist_nationality = data['artistNationality']
    artist_birth_year = data['artistBeginDate']
    artist_death_year = data['artistEndDate']
    object_url = data['objectURL']

    print(f"Nombre del artista: {artist_name}")
    print(f"Nacionalidad del artista: {artist_nationality}")
    print(f"Año de nacimiento del artista: {artist_birth_year}")
    print(f"Año de fallecimiento del artista: {artist_death_year}")
    print(f"Enlace a la obra: {object_url}")
else:
    print("No se encontró información del artista.")
