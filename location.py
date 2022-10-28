import phonenumbers
import opencage
import folium
from test import number


from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "fr")
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "fr"))

from opencage.geocoder import OpenCageGeocode

key = "your api key"

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
print(results)

lat = results[0]["geometry"]["lat"]
lng = results[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat,lng], popup=location).add_to(myMap)

myMap.save("mylocation.html")