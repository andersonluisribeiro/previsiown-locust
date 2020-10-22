import json

class DeviceRepository:

    @staticmethod
    def all_devices():
        with open('devices.json') as json_file:
            devices = json.load(json_file)
            return devices