import requests
from geopy.geocoders import Nominatim


apiKey = "DEMO_KEY" #ENTER YOUR API KEY HERE | this one will work, but you'll get limited after some pulls
geolocator = Nominatim(user_agent="smolApp")

inputAddr = input("Address: ")
#loacting your addrs lat and lon
location = geolocator.geocode(inputAddr)
print(location.address)
lat = location.latitude 
lon = location.longitude

#formatted link w/ your info
link =f"https://api.nasa.gov/planetary/earth/imagery?lon={lon}&lat=lat{lat}&api_key={apiKey}"
out = requests.get(link)

imgName = f"sateliteImg.jpg"

#saving the img of the satelite img
with open(imgName, "wb") as f:
    f.write(requests.get(link).content)

