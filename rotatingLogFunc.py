#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

"""
This script will write a timestamp to a time rotating log file. The purpose is to use this as a test bed for
implementing the rotating log file handler in other projects.
"""

from datetime import datetime
import os
import logging
import time
from logging.handlers import TimedRotatingFileHandler


def main():

    printHeader()

    # setup log file and naming convention
    logFile = "counterLog.log"
    dateTag = ""

    # setup rotating log handler
    logger= timeRotatingLogSetup(logFile)

    # begin "data acq" and logging
    writeLog(logger)


def printHeader():
    print("---------------------------------")
    print("    Rotating Log Test Script")
    print("   " + str(datetime.now()))
    print("---------------------------------")


def timeRotatingLogSetup(path):

    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)

    handler = TimedRotatingFileHandler(path, "m", 1)
    logger.addHandler(handler)

    return logger


def writeLog(logger):

    logger.handler[0].doRollover()

    while(1):
        logger.info(str(datetime.now()))
        time.sleep(6)


if __name__ == '__main__':
    main()
