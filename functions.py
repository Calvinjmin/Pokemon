import sys
import time


def delay_print(string):
    """"
    Function that delays system printing
    """
    for character in string:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.025)