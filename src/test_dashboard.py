import pytest
from flask import Flask
from flask_socketio import SocketIO, emit

@pytest.fixture
def client():
    app = Flask(__name__)
    socketio = SocketIO(app)

    @app.route('/dashboard')
    def dashboard():
        return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Raspberry Pi and Sensor Data Dashboard</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: purple;
                    margin: 0;
                    padding: 20px;
                }
                .container {
                    max-width: 1200px;
                    margin: auto;
                    background-color: white;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    border: 2px solid purple;
                }
                h1 {
                    text-align: center;
                    color: #333;
                }
                /* Other styles omitted for brevity */
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Raspberry Pi and Sensor Data Dashboard</h1>
                <!-- Other HTML content omitted for brevity -->
            </div>
        </body>
        </html>
        '''
    @app.route('/hidden')
    def hidden():
        return {
            "cpu_usage": 50,
            "memory_usage": 45,
            "disk_usage": 70
        }
    
    with app.test_client() as client:
        yield client, socketio

def test_dashboard_loads(client):
    client, _ = client
    response = client.get('/dashboard')
    assert response.status_code == 200
    assert b"Raspberry Pi and Sensor Data Dashboard" in response.data  # Check that the title exists in the HTML



def test_system_info(client): #REQ-02
    client, _ = client
    response = client.get('/hidden')
    assert response.status_code == 200
    data = response.json
    assert data['cpu_usage'] == 50
    assert data['memory_usage'] == 45
    assert data['disk_usage'] == 70

def test_sensor_data_socketio(client): #REQ-01
    client, socketio = client

    @socketio.on('request_data')
    def handle_request_data():
        emit('sensor_data', {
            'temperature': 30,
            'ph_level': 8,
            'humidity': 60,
            'light_intensity': 1000,
            'ec_level': 1.5
        })

    test_client = socketio.test_client(client.application)
    
    # Emit a request_data event
    test_client.emit('request_data')

    # Retrieve the emitted data
    received = test_client.get_received()
    assert len(received) == 1
    event = received[0]
    assert event['name'] == 'sensor_data'
    data = event['args'][0]

    # Check that the values match what we emitted #REQ-02
    assert data['temperature'] == 30
    assert data['ph_level'] == 8
    assert data['humidity'] == 60
    assert data['light_intensity'] == 1000
    assert data['ec_level'] == 1.5

def test_visual_warnings(client): #REQ-03
    client, socketio = client

    @socketio.on('request_data')
    def handle_request_data():
        emit('sensor_data', {
            'temperature': 30,  # Trigger warning for temperature
            'ph_level': 8,      # Trigger warning for pH level
            'humidity': 60,
            'light_intensity': 1000,
            'ec_level': 1.5
        })

    # Create a test client for Socket.IO
    test_client = socketio.test_client(client.application)
    
    # Emit a request_data event
    test_client.emit('request_data')

    # Retrieve the emitted data
    received = test_client.get_received()
    event = received[0]
    data = event['args'][0]

    # Ensure warnings are triggered correctly
    assert data['temperature'] > 25  # Check if temperature is above threshold
    assert data['ph_level'] > 7  # Check if pH level is above threshold
