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
from logging.handlers import TimedRotatingFileHandler as TRFH


def main():

    printHeader()

    # setup log file and naming convention
    logFile = "counterLog.csv"
    dateTag = ""

    # setup rotating log handler
    logger = timeRotatingLogSetup(logFile)

    # begin "data acq" and logging
    writeLog(logger)


def printHeader():
    print("---------------------------------")
    print("    Rotating Log Test Script")
    print("   " + str(datetime.now()))
    print("---------------------------------")


def timeRotatingLogSetup(path):

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # when: s=sec, m=min, h=hour, d=day, W0-W6=weekday (0 = monday), midnight=midnight
    handler = TRFH(path, when="m", interval=1, backupCount=0, encoding="utf8", utc=True)
    logger.addHandler(handler)

    return logger


def writeLog(logger):

    # logger.handler[0].doRollover()
    # logger.doRollover()

    while(1):
        logger.info(str(datetime.now()) + ',' + "poop")
        time.sleep(6)


if __name__ == '__main__':
    main()
