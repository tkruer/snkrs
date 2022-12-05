import datetime

def log(message, taskNumber):
    now = datetime.now().time()
    print(f'[{now}] [SNKRS Bot] [Task-{taskNumber}] {message}')