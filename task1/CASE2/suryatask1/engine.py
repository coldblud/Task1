'''
Created on May 8, 2018
@author: Surya Shankar Banerjee
'''

import json

from faker import Faker
fake = Faker()

from suryatask1.models import Device

class DeviceFaker(object):

    def fake_devices(number):
        device_list = []
        mac_addresses = set()
        while len(mac_addresses)<number:
            mac_addresses.add(fake.mac_address())

        wifi_addresses = set()
        while len(wifi_addresses)<number:
            wifi_addresses.add(fake.mac_address())
        
        for id in range(number):
            mac = mac_addresses.pop()
            wifi = wifi_addresses.pop()
            new_device = Device(id, mac, wifi)
            device_list.append(new_device.to_dict())
        return device_list

    def write_json_to_file(json_arr, filename):
        json_string = json.dumps(json_arr)
        with open(filename, "w") as json_file:
            json_file.write(json_string)
