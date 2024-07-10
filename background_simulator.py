import os
import time

from pddlgym.demo_planning import demo_planning
from server import PDDL_DOMAIN_PATH, PDDL_PROBLEM_PATH

FILES_TO_MONITOR = [PDDL_DOMAIN_PATH, PDDL_PROBLEM_PATH]

def main():
    last_timestamps = {}
    for filename in FILES_TO_MONITOR:
        last_timestamps[filename] = os.path.getmtime(filename)

    while True:
        change_found = False
        for filename in FILES_TO_MONITOR:
            time.sleep(0.1)
            if os.path.getmtime(filename) > last_timestamps[filename]:
                print('Change found')
                change_found = True
                last_timestamps[filename] = os.path.getmtime(filename)

        if change_found:
            demo_planning("sokoban", render=True, verbose=True)


if __name__ == '__main__':
    main()
