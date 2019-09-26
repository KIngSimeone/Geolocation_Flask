from flask import Flask, jsonify
from flask_simple_geoip import SimpleGeoIP


app = Flask(__name__)
app.config['GEOIPIFY_API_KEY'] = "AIzaSyDBsiPRXfcKausDDR1os1MtEIVCrdoABhE"

simple_geoip = SimpleGeoIP(app)


@app.route('/')
def test():
    
    geoip_data = simple_geoip.get_geoip_data()

    return jsonify(data=geoip_data)