import requests
from config import config
import json
import time

class Snkrs(object):

    def __init__(self):
        self.taskNumber = config.createTaskID()
        self.session = requests.Session()
        self.proxy = config.getProxies()
        self.webhook = config.getSettings()[0]
        self.delay = config.getSettings()[1]
        self.akamaiAPIKEY = config.getSettings()[2]
        self.akamaiAPIURL = config.getSettings()[3]
        self.email = config.getAccounts()[0]
        self.password = config.getAccounts()[1]
        self.size = config.getAccounts()[2]


