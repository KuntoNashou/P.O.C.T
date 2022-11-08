import phonenumbers
import opencage
import folium



from phonenumbers import geocoder
os.system('cls')

number = input("put a number (dont forget toadd the country code):")

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "fr")
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "fr"))

from opencage.geocoder import OpenCageGeocode

key = "ae23b4856e6e48548db4ba0deff2297e"

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
print(results)

lat = results[0]["geometry"]["lat"]
lng = results[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat,lng], popup=location).add_to(myMap)

myMap.save("location.html")