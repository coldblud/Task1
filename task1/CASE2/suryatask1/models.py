'''
Created on May 8, 2018
@author: Surya Shankar Banerjee
'''

import json

class Device(object):

    def __init__(self, id, eth, wifi):
        self.id=id
        self.eth=eth
        self.wifi=wifi

    def to_dict(self):
        return self.__dict__
