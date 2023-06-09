from datetime import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler


def tick():
    for i in range(10):
        print(f'{i} Tick! The time is: %s' % datetime.now())


def tac():
    for i in range(10):
        print(f'{i} Tac! The time is: %s' % datetime.now())


if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(tick, "interval", seconds=3)
    scheduler.add_job(tac, "interval", seconds=3)
    # scheduler.add_job(tac, 'cron', minute='*/1')
    print("Press CTRL + {0} to exit".format("Break" if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
