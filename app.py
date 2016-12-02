from flask import Flask, request, render_template
import random

app = Flask(__name__)
app.secret_key = "arbitrage"

@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == "POST":
		pass
	else:
		return render_template("index.html")
	
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")