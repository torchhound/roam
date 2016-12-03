from flask import Flask, request, render_template
import random
import math

app = Flask(__name__)
app.config.from_object("app.cfg")
API_KEY = app.config["GMAPS_API"]

def mileConversion(miles):
	result = miles * 1.609344
	return result
	
def split(meters):
	multiplier = random.randrange(0,1)
	l = multiplier * meters
	r = meters - l
	return l, r

def randomize(lat, lon, offX, offY):
	lat0 = lat + (180 / math.pi) * (offY / 6378137)
	lon0 = lon + (180 / math.pi) * (offX / 6378137) / math.cos(lat)
	return lat0, lon0

@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == "POST":
		distance = request.form["distance"]
		meters = milesConversion(distance)
		#final = randomize(lat, lon, split(meters) #call in html with jinja
		return render_template("index.html", meters=meters, API_KEY=API_KEY)
	else:
		return render_template("distance.html")
	
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")