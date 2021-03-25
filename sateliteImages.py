import requests
import ctypes
from geopy.geocoders import Nominatim


geolocator = Nominatim(user_agent="smolApp")

inputAddr = input("Address: ")

location = geolocator.geocode(inputAddr)
print(location.address)
lat = location.latitude 
lon = location.longitude


link =f"https://api.nasa.gov/planetary/earth/imagery?lon={lon}&lat=lat{lat}&api_key=9aUenJfd9glnuABx7O9iYIrNBl7FSUz6Ns3BrTBS"
out = requests.get(link)

imgName = f"sateliteImg.jpg"

with open(imgName, "wb") as f:
    f.write(requests.get(link).content)

