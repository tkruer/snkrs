import requests
from src import log
from config import config
import json
import time

class Snkrs():
    def __init__(self, taskJSON, taskNum):
        self.taskNum = taskNum
        self.email = taskJSON["email"]
        self.password = taskJSON["password"]
        self.size = taskJSON["size"]
        self.sku = taskJSON["sku"]


        def start(self):
            s = requests.Session()
            print("Starting task " + self.taskNum)
            return "task started"








