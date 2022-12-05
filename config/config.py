import json
import csv
import string
import random

def getSettings():
    with open('config.json', 'r') as s:
        settings = json.load(s)
        webhook = settings['webhook']
        delay = settings['delay']
        akamaiAPIKEY = settings['akamaiAPIKEY']
        akamaiAPIURL = settings['akamaiAPIURL']
        return webhook, delay, akamaiAPIKEY, akamaiAPIURL

def getAccounts():
    with open('accounts.csv', 'r') as a:
        reader = csv.reader(a)
        accounts = list(reader)
        email = accounts[0]
        password = accounts[1]
        size = accounts[2]
        sku = accounts[3]
    return email, password, size, sku

def getProxies():
    with open('proxies.txt', 'r') as p:
        proxies = p.read().splitlines()
    return proxies

def createID(N: int):
    id_value =  ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
    return id_value

def createTask(email: str, password: str, sku: str, size: str, proxy: str, delay: int, webhook: str, akamaiAPIKEY: str, akamaiAPIURL: str, taskID: str):
    task_data = {
        "email": email,
        "sku": sku,
        "password": password,
        "size": size,
        "proxy": proxy,
        "delay": delay,
        "webhook": webhook,
        "akamaiAPIKEY": akamaiAPIKEY,
        "akamaiAPIURL": akamaiAPIURL,
        "taskID": taskID
    }
    return task_data

def buildTask():
    settings = getSettings()
    accounts = getAccounts()
    proxies = getProxies()
    taskID = createID(5)
    task = createTask(email=accounts[0], password=accounts[1], size=accounts[2], sku=accounts[3], proxy=proxies, delay=settings[1], webhook=settings[0], akamaiAPIKEY=settings[2], akamaiAPIURL=settings[3], taskID=taskID)
    return task

