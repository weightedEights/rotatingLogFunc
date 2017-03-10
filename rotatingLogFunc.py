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


def main():

    printHeader()

    # set the log file directory
    logFileDir = os.getcwd()

    logFile = logFileSetup(logFileDir)

    rotatingLog(logFile)



def printHeader():
    print("---------------------------------")
    print("    Rotating Log Test Script")
    print("   " + str(datetime.now()))
    print("---------------------------------")


def logFileSetup(fileDir):

    pass


def rotatingLog(logFile):

    pass


if __name__ == '__main__':
    main()
