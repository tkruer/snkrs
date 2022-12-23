import requests
from src import log
from config import config
import json
import time

class Snkrs():
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

        while True:
            try:
                lines = open('proxies.txt').read().splitlines()
                proxy = random.choice(lines)
                split = proxy.split(':')
                good_format = (f'{split[2]}:{split[3]}@{split[0]}:{split[1]}')
                http_proxy = f"{good_format}"
                https_proxy = f"{good_format}"
                proxyDict = {
                    "http": f'http://{http_proxy}',
                    "https": f'http://{https_proxy}'}
            except Exception as e:
                print(e)
                log('Error getting proxies, you can only run with proxies, will be fixed soon', 196)
                time.sleep(10)
                exit()
            else:
                break


            while True:
                try:

                except Exception as e:
                    print(e)
                    time.sleep(delay)
                if response.status_code == 200:
                    log('Succesfully got raffle page', 3)
                    break

            while True:
                try:

                except Exception as e:
                    print(e)
                    time.sleep(delay)
                else:
                    try:

                    except Exception as e:
                        print(e)
                        time.sleep(delay)









