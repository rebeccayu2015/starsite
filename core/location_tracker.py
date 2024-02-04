from geopy.geocoders import Nominatim
import requests, json, pandas
import matplotlib.pyplot as plt
from skyfield.data import hipparcos
from skyfield.api import wgs84, load, Star
from skyfield.projections import build_stereographic_projection

# generate sky map given user input
# generates list of constellations viewable in each season from northern hemisphere
def convert_str(string_input):
    return string_input.replace(" ", "+")

user_input = "caracas venezuela" # change string to include user input location
input_loc = convert_str(user_input)
#print(input_loc)
geolocator = Nominatim(user_agent="geoapiExercises")

query = f"https://nominatim.openstreetmap.org/search?q={input_loc}&format=json&limit=1"
response = requests.get(query)
data = response.json()
data_str = json.dumps(data, indent = 4)
latitude = data[0]["lat"]
longitude = data[0]["lon"]
#print("latitude: " + latitude + "\nLongitude: " + longitude)

ts = load.timescale()
t = ts.now()
curr = t.utc_jpl()

eph = load('de421.bsp')
earth = eph['earth']

observer = wgs84.latlon(latitude_degrees = float(latitude), longitude_degrees = float(longitude))
observer = observer.at(t)
position = observer.from_altaz(alt_degrees = 90, az_degrees = 0)
ra, dec, distance = position.radec()
center_obs = Star(ra=ra, dec= dec)
center = earth.at(t).observe(center_obs)
projection = build_stereographic_projection(center)
with load.open(hipparcos.URL) as f:
    stars = hipparcos.load_dataframe(f)

star_positions = earth.at(t).observe(Star.from_dataframe(stars))
stars['x'], stars['y'] = projection(star_positions)

chart_size = 10
max_star_size = 100
limiting_magnitude = 10
bright_stars = (stars.magnitude <= limiting_magnitude)
magnitude = stars['magnitude'][bright_stars]

fig, ax = plt.subplots(figsize=(chart_size, chart_size))

border = plt.Circle((0, 0), 1, color='navy', fill = True)
ax.add_patch(border)
marker_size = max_star_size * 10 ** (magnitude / -2.5)

ax.scatter(stars['x'][bright_stars], stars["y"][bright_stars],
 s=marker_size, color='white', marker='.', linewidths=0,
 zorder=2)
horizon = plt.Circle((0, 0), radius=1, transform=ax.transData)
for col in ax.collections:
    col.set_clip_path(horizon)

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
plt.axis('off')
# plt.show() // may need to change this line to save plt to database and display on website

summer = []
winter = []
spring = []
fall = []
south = []

starDict = {}
with open('constellations.json') as json_star:
    constellations = json.load(json_star)
    for i in range(88):
        name = constellations[i]["latin_name_nom_latin"]
        season = constellations[i]["season_saison"]
        if "Summer" in season:
            summer.append(name)
        elif "Spring" in season:
            spring.append(name)
        elif "Winter" in season:
            winter.append(name)
        elif "Autumn" in season:
            fall.append(name)
        else:
            south.append(name)
        declination = constellations[i]["dec_declinaison"]
        r_ascension = constellations[i]["test"]
        image_url = ""
        found = 0
        starDict[name] = [r_ascension, declination]

winterMon = "JanFebDec"
springMon = "MarAprMay"
summerMon = "JunJulAug"
fallMon = "SepOctNov"

curr = curr.split("-")
if curr[1] in winterMon:
    print(winter)
elif curr in springMon:
    print(spring)
elif curr in summerMon:
    print(summer)
elif curr in fallMon:
    print(fall)