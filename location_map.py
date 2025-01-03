import folium
from geopy.geocoders import Nominatim
import webbrowser

# Demande d'entrée utilisateur
location_name = input("Enter a location: ")

# Localisation via geopy
geolocator = Nominatim(user_agent="geoapi")
location = geolocator.geocode(location_name)

if location:
    # Création de la carte centrée sur la localisation de l'utilisateur
    latitude = location.latitude
    longitude = location.longitude
    clcoding = folium.Map(location=[latitude, longitude], zoom_start=12)

    # Ajout d'un marqueur
    marker = folium.Marker([latitude, longitude], popup=location_name)
    marker.add_to(clcoding)

    # Sauvegarde dans un fichier temporaire
    temp_file = "map_temp.html"
    clcoding.save(temp_file)

    # Ouvrir le fichier dans le navigateur
    webbrowser.open(temp_file)
else:
    print("Location not found. Please try again.")
