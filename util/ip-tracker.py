import geocoder
import folium
import time

os.system('cls')
ip = input("put the ip adress here:")
g = geocoder.ip(str(ip))

myAdress = g.latlng
print(myAdress)

my_map1 = folium.Map(location = myAdress,
                    zoom_start=12)

folium.CircleMarker(location=myAdress,
                    radius=50, popup="The location").add_to(my_map1)

folium.Marker(myAdress,
              popup="The location").add_to(my_map1)


my_map1.save("location-map.html")

time.sleep(2)

exec(open('location-map.html').read())

