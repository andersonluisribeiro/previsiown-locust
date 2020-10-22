import time
from locust import HttpUser, task, constant, events
from device_repository import DeviceRepository

class QuickstartUser(HttpUser):
    wait_time = constant(1)
    devices = []
    id = 0
    ts = time.time()
    
    @task
    def publish(self):
        self.client.post("/eht/readings", json={
                "deviceId": self.device['id'],
                "readings": [{
                    "rpm": 22,
                    "actualTorque": 200,
                    "acceleratorPedal": 100,
                    "automaticPilot": "WAITING",
                    "secondaryBreakPedal": True,
                    "velocity": 100,
                    "batteryCharge": 50.0,
                    "fuelLevel": 40,
                    "engineOilTemperature": 50,
                    "clutchState": "SLIDING",
                    "engagedGear": 4,
                    "leverPosition": "P",
                    "airConditioningPressure": 200,
                    "gmvState": 30,
                    "atmPressure": 800,
                    "batteryVoltage": 10,
                    "consumption": 200,
                    "inletAirTemperature": 60,
                    "compressorClutch": False,
                    "odometer": 100000,
                    "externalAirTemperature": 33,
                    "airConditioningPower": 100,
                    "x208": "50D1031B7325B98800714",
                    "x38D": "50D1031B7325B98800714",
                    "x4F2": "50D1031B7325B98800714",
                    "x612": "50D1031B7325B98800714",
                    "x412": "50D1031B7325B98800714",
                    "x4F2": "50D1031B7325B98800714",
                    "x482": "50D1031B7325B98800714",
                    "x489": "50D1031B7325B98800714",
                    "x348": "50D1031B7325B98800714",
                    "x588": "50D1031B7325B98800714",
                    "x488": "50D1031B7325B98800714",
                    "x50E": "50D1031B7325B98800714",
                    "x552": "50D1031B7325B98800714",
                    "x5B2": "50D1031B7325B98800714",
                    "x592": "50D1031B7325B98800714",
                    "x50D": "50D1031B7325B98800714",
                    "location": "-22.4224564, -44.3433353",
                    "altitude": 100,
                    "id_usuario": 10,
                    "id_rodagem": 10,
                    "vin": "123",
                    "timestamp": QuickstartUser.ts
                }]
            })

    def on_start(self):
        for device in QuickstartUser.devices:
            if device['label'] == 'test_vehicle_{:03}'.format(self.id):
                self.device = device

        QuickstartUser.id = QuickstartUser.id + 1
        self.id = QuickstartUser.id


    @events.test_start.add_listener
    def on_test_start(**kwargs):
        QuickstartUser.devices = DeviceRepository.all_devices()