from flask import Flask
app = Flask(__name__)

@app.route('/arjun')
def hello():
	return "arjun pv --1  helm chart demo"


if __name__ == "__main__":
	app.run(host ='0.0.0.0', port = 5001, debug = True)
