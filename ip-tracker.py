import geocoder
import folium

ip = input("Adress ip: ")
g = geocoder.ip(str(ip))

myAdress = g.latlng
print(myAdress)

my_map1 = folium.Map(location = myAdress,
                    zoom_start=12)

folium.CircleMarker(location=myAdress,
                    radius=50, popup="Yorkshire").add_to(my_map1)

folium.Marker(myAdress,
              popup="Yorkshire").add_to(my_map1)