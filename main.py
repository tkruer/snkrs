from config import config
from src import snkrs
import json
import csv
from threading import Thread



def main():
    with open('config/config.json') as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()
        # finish logic here

    task_reader = csv.DictReader(open("config/accounts.csv", 'r'))
    for task in task_reader:
        if task_reader.line_num == 1:
            continue
        else:
            taskTotal = str(task_reader.line_num - 1)
            bot = Thread(target=snkrs.Snkrs(taskJSON=task, taskNum=taskTotal).start()).start()
            print(bot)

if __name__ == '__main__':
    main()
