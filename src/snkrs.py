import requests
from src import log
from config import config
import json
import time

class Snkrs(object):

    def __init__(self, taskNumber, taskData):
        self.taskNumber = taskNumber
        self.taskData = taskData
        self.email = taskData['email']
        self.password = taskData['password']
        self.sku = taskData['sku']
        self.size = taskData['size']
        self.proxy = taskData['proxy']
        self.delay = taskData['delay']
        self.webhook = taskData['webhook']
        self.akamaiAPIKEY = taskData['akamaiAPIKEY']
        self.akamaiAPIURL = taskData['akamaiAPIURL']
        self.taskID = taskData['taskID']

        def start(self):
            s = requests.Session()

            check_config = True

            while check_config == True:
                if self.email == '':
                    log.log(f'Email is not set in accounts.csv', self.taskNumber)
                    check_config = False
                elif self.password == '':
                    log.log(f'Password is not set in accounts.csv', self.taskNumber)
                    check_config = False
                elif self.sku == '':
                    log.log(f'SKU is not set in accounts.csv', self.taskNumber)
                    check_config = False
                elif self.size == '':
                    log.log(f'Size is not set in accounts.csv', self.taskNumber)
                    check_config = False
                elif self.proxy == '':
                    log.log(f'Proxy is not set in proxies.txt', self.taskNumber)
                    check_config = False
                elif self.delay == '':
                    log.log(f'Delay is not set in config.json', self.taskNumber)
                    check_config = False
                elif self.webhook == '':
                    log.log(f'Webhook is not set in config.json', self.taskNumber)
                    check_config = False
                elif self.akamaiAPIKEY == '':
                    log.log(f'Akamai API Key is not set in config.json', self.taskNumber)
                    check_config = False
                elif self.akamaiAPIURL == '':
                    log.log(f'Akamai API URL is not set in config.json', self.taskNumber)
                    check_config = False
                else:
                    check_config = False
                    log.log(f'All config values are set', self.taskNumber)

            start_task = True

            log.log(self.taskNumber, f'Starting Task...')

            while start_task == True:
                print('test')







