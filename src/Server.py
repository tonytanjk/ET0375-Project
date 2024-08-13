from flask import Flask, render_template, jsonify
import psutil, time
from flask_socketio import SocketIO, emit
import threading
import time
import Light_intensity as LI
import EC_level as EC
import Relative_Humidity as RH
import Ambient_temperature as AT
import pH_level as PH

global var3
var3 = False
app = Flask(__name__)
socketio = SocketIO(app)

#Dashboard Routing
@app.route('/')
@app.route('/dashboard')
def index():
    return render_template('Dashboard.html')

@app.route('/ph_details')
def ph_board():
    return render_template('ph_details.html')

@app.route('/temperature_details')
def temp_board():
    return render_template('temperature_details.html')

@app.route('/humidity_details')
def humidity_board():
    return render_template('humidity_details.html')

@app.route('/light_intensity_details')
def light_intensity_board():
    return render_template('light_intensity_details.html')

@app.route('/ec_level_details')
def ec_board():
    return render_template('ec_level_details.html')

#Data Handling
@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

def background_thread():
    while True:
        AT.main(),        # Fixed temperature value
        PH.main(),   
        RH.main(),          # Fixed relative humidity value
        LI.main(),          # Extract light intensity value from the Light module
        EC.main(),           # Fixed EC level value

def init():
        global var3
        if var3 == False:
            AT.init()
            PH.init()
            RH.init()
            LI.init
            EC.init()
            var3=True

@socketio.on('request_data')
def handle_request_data():

    sensor_data = {
         'temperature': AT.Ambi_Temp(),       
         'ph_level': PH.process_key(),           #Read Data Functions
         'humidity': RH.Ambi_Humi(),                    
         'light_intensity':LI.read_light_intensity(),    
         'ec_level':EC.read_adc(),            
        #  'temperature': 25,        # Fixed temperature value
        # 'ph_level':6,           # Fixed pH level value
        # 'humidity': 0,           # Fixed relative humidity value
        # 'light_intensity':0,     # Extract light intensity value from the Light module
        # 'ec_level':1.5,            # Fixed EC level value
    }
    emit('sensor_data', sensor_data)

@app.route('/hidden') #RPI Stats
def system_info():
    # Get CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    
    # Get memory usage
    memory = psutil.virtual_memory()
    memory_usage = memory.percent

    # Get disk usage
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent

    # Get current timestamp
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

    return jsonify({
        'timestamp': timestamp,
        'cpu_usage': cpu_usage,
        'memory_usage': memory_usage,
        'disk_usage': disk_usage
    })

if __name__ == '__main__':
    init()
    # Start the background thread
    thread = threading.Thread(target=background_thread,daemon=True)
    thread.daemon = True
    thread.start()
    # Run the Flask-SocketIO app
    socketio.run(app, host="192.168.0.7", port = 5000, debug=True)
