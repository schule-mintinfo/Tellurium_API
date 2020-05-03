from flask import Flask, jsonify
from subprocess import Popen as pop
import serial
app = Flask(__name__)
ser = serial.Serial('', baudrate=9600, timeout=1)

@app.route('/')
def index():
    return jsonify({"Nachricht": "API online",  "color": "alert-primary"})
@app.route('/turn/fast')
def TurnFast():
    ser.write("fast")
    return jsonify({"Nachricht": "Das Tellurium dreht sich schnell",  "color": "alert-primary"})
@app.route('/turn/normal')
def TurnSlow():
    ser.write("normal")
    return jsonify({"Nachricht": "Das Tellurium dreht sich normal",  "color": "alert-primary"})
@app.route('/reset')
def Zuruecksetzen():
    ser.write("reset")
    return jsonify({"Nachricht": "Das Tellurium hat sich automatisch zurueckgesetzt",  "color": "alert-primary"})
@app.route('/shutdown')
def shutdown():
    pop("shutdown -t 10", shell=False)
    return jsonify({"Nachricht": "Die API fährt herunter. Die Motoren bleiben im Standby",  "color": "alert-primary"})


if __name__ == "__main__":
    app.run()
