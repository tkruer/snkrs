from config import config
from src import Snkrs
import csv
from threading import Thread



def main():
    snkrs = Snkrs()
    task_reader = csv.DictReader(open("travis.csv", 'r'))
    for task in task_reader:
        if task_reader.line_num == 1:
            continue
        else:
            taskNum = str(task_reader.line_num - 1)
            Thread(target=snkrs(task, taskNum).enter).start()


if __name__ == '__main__':
    main()
